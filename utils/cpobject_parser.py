import json
import copy
import yaml
from pathlib import Path
from .file_ops import read_config_file, write_file
from .logger_main import log
from .cli_exporter import CLIExporter

FIELD_WHITELIST_PATH = './config/field_schemas/dynamic_valid_fields.json'


class ParseObjects:
    def __init__(self, client, formatted_cp_ansible_module_names):
        self.client = client
        self.config = read_config_file('./config/exporter_config.json')
        self.config_folder_name = self.config['config_folder_name']
        self.formatted_cp_ansible_module_names = formatted_cp_ansible_module_names
        self.field_whitelist = self._load_field_whitelist()
        self.cli_exporter = CLIExporter()
        self.db_objects = self.get_objects()

    def _load_field_whitelist(self):
        """Load the curated field whitelist for CLI commands."""
        try:
            with open(FIELD_WHITELIST_PATH, 'r', encoding='utf-8') as f:
                whitelist = json.load(f)
                log.info(f"Loaded field whitelist with {len(whitelist)} object types")
                return whitelist
        except Exception as e:
            log.warning(f"Could not load field whitelist: {e}. Using permissive mode.")
            return {}

    def filter_fields_for_cli(self, obj_type, db_object):
        """Filter object to only include fields valid for mgmt_cli add commands."""
        if obj_type not in self.field_whitelist:
            # No whitelist for this type - use existing logic
            return db_object
        
        valid_fields = set(self.field_whitelist[obj_type])
        # Always preserve 'type' for downstream processing (will be removed later)
        valid_fields.add('type')
        filtered = {}
        for key, value in db_object.items():
            if key in valid_fields:
                filtered[key] = value
        return filtered



    def get_objects(self):

        for cp_ansible_command in self.formatted_cp_ansible_module_names:
            db_objects = []
            done = False
            offset = 0
            while not done:
                get_objects = self.client.run_command(
                    "show-objects", payload={'type': cp_ansible_command, 'details-level': 'full', "limit": "500", "offset": offset})

                if 'total' not in get_objects:
                    # Check if this is an unsupported type on this server (expected, not an error)
                    err_code = get_objects.get('code', '')
                    if err_code == 'generic_err_invalid_api_type':
                        log.debug(f"Object type '{cp_ansible_command}' not available on this server, skipping.")
                    else:
                        log.warning(f"Failed to get objects for {cp_ansible_command}: {get_objects}")
                    break


                if get_objects['total'] == 0:
                    done = True
                    log.info(f"No {cp_ansible_command} objects found")
                    break
                if get_objects['total'] > get_objects['to']:

                    offset = int(get_objects['to'])
                    from_position = int(get_objects['from'])
                    total = get_objects['total']

                    log.info(
                        f"Parsing {cp_ansible_command} objects from {from_position} to {offset} out of {total}")

                else:
                    done = True

                for cp_object in get_objects['objects']:
                    if cp_object['type'] != cp_ansible_command:
                        log.error(
                            f" {cp_object['name']} with type: {cp_object['type']} found while parsing {cp_ansible_command} objects")
                    else:
                        db_objects.append(cp_object)

            # write_file('./objects/' + cp_ansible_command +'.json', mode = 'w', content=json.dumps(db_objects))
            self.parse_objects(db_objects, cp_ansible_command)

    def parse_objects(self, db_objects, cp_ansible_command):

        exported_objects = []
        cli_clean_objects = []  # Clean API data for CLI export
        
        # we need to match the fields from the DB and the fields from the API reference
        for db_object in db_objects:
            log.debug(db_object)
            if db_object['meta-info']['last-modifier'] != "System":

                # TODO create documentations (json export) for handling objects with API/Ansible limitations
                docs_objects = ['access-role', 'simple-gateway',
                                'simple-cluster', 'vpn-community-meshed', 'vpn-community-star']
                if db_object['type'] in docs_objects:
                    write_file(
                        './check_point_policy/docs/' + db_object['type'] + '.json', mode='a', content=json.dumps(db_object))

                # 0. Flatten references FIRST (before we delete UIDs)
                self.format_object_fields(db_object)

                # 1. Delete internal fields recursively
                self.remove_internal_fields(db_object)

                # 2. delete the fields that are not needed
                db_object_fields_deleted = self.delete_object_fields(db_object)

                # 3. Filter to only valid CLI input fields (using whitelist)
                db_object_fields_filtered = self.filter_fields_for_cli(
                    cp_ansible_command, db_object_fields_deleted)

                # >>> CLI PATH: Capture clean data BEFORE Ansible transformations <<<
                cli_clean_objects.append(copy.deepcopy(db_object_fields_filtered))

                # >>> ANSIBLE PATH: Ansible-specific transformations <<<
                # 4. Convert dashes to underscores ONLY at the end
                db_object_fields_converted = self.convert_dashes_in_keys(db_object_fields_filtered)

                # 5. add common fields for all objects
                db_object_fields_added = self.add_object_common_fields(
                    db_object_fields_converted)

                # create the Ansible playbook object
                command_module = self.create_ansible_module_object(
                    cp_ansible_command, db_object_fields_added)

                exported_objects.append(command_module)

        # Feed clean objects to CLI exporter (independent of Ansible)
        self.cli_exporter.add_objects(cp_ansible_command, cli_clean_objects)

        # we publish after creating 30 objects for better performance
        module_len = len(exported_objects)
        for item in range(30, module_len, 30):
            log.info(f"Inserting publisher at position {item}")
            exported_objects.insert(
                item, {'name': 'Publish Current Changes', 'cp_mgmt_publish': ''})

        # write the Ansible code to a file
        # write_file('./objects/' + cp_ansible_command +'.json', json.dumps(exported_objects))
        objects_folder = Path('check_point_policy/objects/')
        output_file_path = str(Path.joinpath(
            objects_folder, cp_ansible_command))
        if exported_objects:
            content = yaml.dump(exported_objects, sort_keys=False)
            write_file(output_file_path + '.yml', mode='w', content=content)

        else:
            log.info(f"No objects found for {cp_ansible_command}")

    # adding common fields for all objects

    def add_object_common_fields(self, db_object):

        db_object['state'] = "{{state}}"
        db_object['ignore_warnings'] = self.config.get('ignore_warnings')
        db_object['ignore_errors'] = self.config.get('ignore_errors')
        db_object['wait_for_task'] = self.config.get('wait_for_task')
        db_object['wait_for_task_timeout'] = self.config.get(
            'wait_for_task_timeout')

        if db_object['type'] == 'simple-gateway' or db_object['type'] == 'simple-cluster':
            del db_object['ignore_errors']
            
        # we need to use this option since we are exporing the cleanup rule from tbhe source machine  
        # This is not supported since the module uses a set-access-rule command   
        #if db_object['type'] == 'access-layer':
        #    db_object['add_default_rule'] = False

        return db_object

    # format the object fields

    def format_object_fields(self, db_object):

        # [REMOVED] Simple gateway short-circuit to allow full field export
        # if db_object['type'] == 'simple-gateway' or db_object['type'] == 'simple-cluster':
        #    return {"name": db_object['name'], "type": db_object['type'], "ipv4_address": db_object['ipv4-address']}

        # [REMOVED] VPN community short-circuit to allow full field export
        # if db_object['type'] == 'vpn-community-meshed' or db_object['type'] == 'vpn-community-star':
        #    return {"name": db_object['name'], "type": db_object['type']}

        # [MODIFIED] Generic recursive flattening of object references
        # This replaces specific handling for vpn-community, access-role, etc.
        # It converts any nested object (dict with 'uid') into its name.
        self.recursive_flatten_references(db_object)

        db_object['tags'] = [item['name'] for item in db_object.get('tags')]              
            

        if db_object.get('nat-settings'):
            db_object['nat_settings'] = {
                k.replace('-', '_'): v for k, v in db_object['nat-settings'].items()}

        if db_object.get('host-servers'):
            db_object["host_servers"] = {k.replace('-', '_'): (v if k != 'web-server-config' else {k2.replace('-', '_'): v2 for k2, v2 in db_object['host-servers']
                                                                                                   ['web-server-config'].items() if k2 != "standard-port-number"}) for k, v in db_object['host-servers'].items()}
        # format the interfaces field for host objects
        interfaces_ignored_fields = [
            'domain', 'uid', 'icon', 'type', 'tags', 'subnet-mask']
        if db_object.get('interfaces'):
            db_object['interfaces'] = [{k.replace('-', '_'): v for k, v in interface.items(
            ) if k not in interfaces_ignored_fields and v} for interface in db_object['interfaces']]

        # [MODIFIED] members field is now allowed for application-site
        if db_object.get('type') == 'application-site':
            pass
            # if db_object.get('members'):
            #    del db_object['members']
            #    log.info(
            #        f"members field is not supported in the Ansible module for {db_object['type']}")

        # format the group-with-exclusion objects
        format_fields = ['include', 'except']
        if db_object['type'] == 'group-with-exclusion':
            for key, value in db_object.items():
                if key in format_fields:
                    db_object[key] = value['name']

        # format access-roles
        # [REMOVED] Handled by recursive_flatten_references
        # if db_object.get('type') == 'access-role':
        #     fields = [ 'networks', 'users', 'machines', 'remote-access-client' ]
        #     for field in fields:
        #         self.flatten_reference_field(db_object, field)

        # format policy packages
        if db_object['type'] == 'package':
            db_object = self.parse_packages(db_object)

        # format group objects to replace members ids with names
        # [MODIFIED] Generic check for 'members' field instead of hardcoded types
        if 'members' in db_object:
             # specific check to avoid non-standard members fields if likely? 
             # actually standard groups always use members as list of UIDs.
             # but check if it's list first.
             if isinstance(db_object['members'], list) and len(db_object['members']) > 0:
                 # Check if first item is UID (string) to avoid re-converting if already names
                 if isinstance(db_object['members'][0], str):
                      # We might have already flattened it if it was list of objects?
                      # API 'members' for group is usually list of UIDs (strings), not objects.
                      # So recursive_flatten won't touch it.
                      # We need to resolve UIDs to Names.
                      db_object = self.convert_group_member_ids_to_names(db_object)


        # remove dashes from the object field names (MOVED TO parse_objects)
        # db_object = self.convert_dashes_in_keys(db_object)
        return db_object
        
    def convert_dashes_in_keys(self, obj):
        if obj is not None:
            if type(obj) in [str, int, bool]:
                return obj
            if type(obj) == list:
                return [self.convert_dashes_in_keys(v) for v in obj]
            if type(obj) == dict:
                return {k.replace('-', '_'): self.convert_dashes_in_keys(v) for k, v in obj.items()}
            raise ValueError(f"Unknown type: {obj}")
        return obj

    def parse_packages(self, package):

        db_object = {
            "name": package['name'],
            "type": package['type'],
            "access": package['access'],
            "threat_prevention": package['threat-prevention'],
            "desktop_security": package['desktop-security'],
            "qos": package['qos'],
            "color": package.get('color'),
            "comments": package.get('comments'),
            "installation_targets":  package['installation-targets'] if type(package['installation-targets']) == str else [item['name'] for item in package['installation-targets']],
            "qos_policy_type": package['qos-policy-type'],
            "tags": package['tags'],
            "vpn_traditional_mode": package['vpn-traditional-mode'],
        }

        return db_object

    # delete the fields that are not needed in the Ansible playbook

    def delete_object_fields(self, db_object):
        fields_to_delete = ["uid", "meta-info", "icon",
                            "parent-layer", "read-only", "domain", "mask-length4", 'ips-layer', 'application-id', 'risk', 'user-defined', 'available-actions', 'delayed-sync-value', 'enable-tcp-resource', 'use-delayed-sync', "primary-category-id"]
        
        # delete application-site members
        # [MODIFIED] Keep members for application-site
        # if db_object['type'] == 'application-site':
        #     fields_to_delete.append('members')
        
        # if use-default-timeout  is true, we cannot deine the timeout manually under agressive aging
        if db_object.get('type') == 'service-tcp':
            aa = db_object.get('aggressive-aging')
            if aa and aa.get('use-default-timeout'):
                if 'timeout' in aa:
                    del aa['timeout']
        
        return {k: v for k, v in db_object.items() if k not in fields_to_delete}

    # Object type is needed for processing but in the parser bbut must be removed before exporting the object
    def delete_object_type(self, db_object):
        del db_object['type']
        return db_object

    # convert grpup member ids into names:
    def convert_group_member_ids_to_names(self, db_object):
        member_names = []
        for member_uid in db_object['members']:
            member_name = self.client.run_command(
                "show-object", payload={"uid": member_uid})['object']['name']
            log.info(
                f"replacing group member id {member_uid} with name {member_name}")

            member_names.append(member_name)
        db_object['members'] = member_names
        return db_object

    # Helper to flatten valid object references (dict or list of dicts) to names
    def flatten_reference_field(self, db_object, field_name):
        if field_name not in db_object:
            return
            
        val = db_object[field_name]
        if isinstance(val, list):
            # If list of dicts with 'name', extract name. If string, keep.
            new_list = []
            for item in val:
                if isinstance(item, dict) and 'name' in item:
                    new_list.append(item['name'])
                else:
                    new_list.append(item)
            db_object[field_name] = new_list
        elif isinstance(val, dict) and 'name' in val:
            db_object[field_name] = val['name']

    # create the Ansible playbook object

    # Generic recursive flatten
    def recursive_flatten_references(self, obj):
        if isinstance(obj, dict):
            keys = list(obj.keys())
            for k in keys:
                val = obj[k]
                # Check if value is a Check Point object reference (has 'uid' and 'name')
                # AND it's not the top-level iteration (which is controlled by caller, but here we process values)
                if isinstance(val, dict) and 'uid' in val and 'name' in val:
                    # Replace dict with name string
                    obj[k] = val['name']
                else:
                    # Recurse
                    self.recursive_flatten_references(val)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                if isinstance(item, dict) and 'uid' in item and 'name' in item:
                    # Replace dict item with name string
                    obj[i] = item['name']
                else:
                    # Recurse
                    self.recursive_flatten_references(item)

    # Recursive delete internal keys
    # [MODIFIED] Added 'type' to deletion list to be safe for deep objects?
    # No, 'type' is useful context. Keep as is.
    def remove_internal_fields(self, obj):
        internal_keys = {
            'objId', 'domainId', 'folderPath', 'folder', 'is_owned', 'ownedName', 
            'meta-info', 'admin-modification-time', 'creation-time', 'last-modifier', 
            'creator', 'clpOverrideGlobalConfig', 'deviceSettingsModule',
            'uid', 'read-only', 'available-actions', 'icon', 'type',
            'base64-certificate', 'expiration-date', 'last-updated', 'sic-name', 'sic-identifier'
        }
        # Note: type is needed for logic but maybe removed at top level? 
        # delete_object_type removes it at top level. 
        # Nested objects (like gateways in vpn community) have type. mgmt_cli might not like it if it duplicates implied type?
        # Actually 'type' is useful for informational purposes. But let's check if 'type' is accepted in nested objects. 
        # Usually not. e.g. center-gateways.0.type? No.
        # But we FLATTENED reference fields!
        # center-gateways is now list of names. So nested type is gone there.
        # What about shared-secrets -> external-gateway?
        # That is a full object definition inside a list.
        # mgmt_cli might expect 'shared-secrets.0.external-gateway' to be name?
        # The YAML showed full object.
        # Check API spec for shared-secrets.
        # shared-secrets: List<VpnSharedSecret>
        # VpnSharedSecret has 'external-gateway' (CpmiGatewayPlain).
        # This implies reference?
        # If it is reference, I should flatten it!
        
        # Let's add 'type' to deletion just in case, except top level?
        # remove_internal_fields is called at top level.
        # We need 'type' at top level for the parser logic (lines 63, 115, etc)!
        # So we cannot delete 'type' recursively at the start!
        
        # Correct approach: Remove 'uid', 'read-only', 'available-actions', 'icon'.
        # Do NOT remove 'type'.
        internal_keys = {
            'objId', 'domainId', 'folderPath', 'folder', 'is_owned', 'ownedName', 
            'meta-info', 'admin-modification-time', 'creation-time', 'last-modifier', 
            'creator', 'clpOverrideGlobalConfig', 'deviceSettingsModule',
            'uid', 'read-only', 'available-actions', 'icon'
        }

        if isinstance(obj, dict):
            # iterating over copy of keys to allow deletion
            keys = list(obj.keys())
            for k in keys:
                if k in internal_keys:
                    del obj[k]
                else:
                    self.remove_internal_fields(obj[k])
        elif isinstance(obj, list):
            for item in obj:
                self.remove_internal_fields(item)

    def create_ansible_module_object(self, cp_ansible_command, db_object):
        try:
            log.info(f"Exporting object: {db_object['name']}, Type: {db_object['name']}")
            command_module = {}
            command_module['name'] = 'Task for ' + db_object['name']
            module_name = 'cp_mgmt_' + cp_ansible_command.replace('-', '_')

            # delete the object type
            self.delete_object_type(db_object)
            command_module[module_name] = db_object
            return command_module
        except Exception as e:
            log.error(f"Error exporting object {db_object['name']}")
            log.error(e)
