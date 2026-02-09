
import argparse
import sys
import yaml
import json
import requests
from pathlib import Path
from itertools import chain
from utils.logger_main import log
from utils.api_client import API_client as api_client
from utils.cp_layer_rules_to_ansible import export_layer_rules_to_ansible
from utils.cpobject_exporter import cp_object_exporter
from utils.fetch_api_objects import fetch_api_objects
from utils.file_ops import read_config_file, create_required_folders, write_file

def filter_dynamic_modules(modules):
    """
    Filter out modules that are not objects (e.g. facts, commands)
    """
    clean_modules = []
    
    for mod in modules:
        name = mod
        
        # Exclude specific non-objects known to cause issues in show-objects
        # - Plurals (commands)
        # - Rules/Sections (handled via rulebase export)
        # - Layers (handled via specific show-*-layer commands usually, or separate logic)
        if name in ['vsx-provisioning-tool', 'ha-full-sync', 'access-layers', 'objects-batch', 'rules-batch']:
             continue
             
        if name.endswith('-rule') or name.endswith('-section') or name.endswith('-layer'):
            continue

        clean_modules.append(name)
        
    return clean_modules


def _add_rulebase_to_cli(client, cli_exporter, layer):
    """
    Generate CLI commands for access rules directly from the rulebase API response.
    
    Args:
        client: API client instance
        cli_exporter: CLIExporter instance to add commands to
        layer: Access layer name
    """
    try:
        response = client.run_command(
            "show-access-rulebase",
            payload={"name": layer, "use-object-dictionary": False})
    except Exception as e:
        log.warning(f"Failed to fetch rulebase for layer '{layer}': {e}")
        return
    
    if 'rulebase' not in response:
        return
    
    rule_objects = []
    section_objects = []
    
    def _process_rulebase(rulebase, current_layer):
        """Recursively process the rulebase entries."""
        for entry in rulebase:
            if entry.get('type') == 'access-section':
                # Section
                section_objects.append({
                    'layer': current_layer,
                    'name': entry['name'],
                    'position': entry.get('from', 'top'),
                })
                # Process rules inside the section
                if 'rulebase' in entry:
                    _process_rulebase(entry['rulebase'], current_layer)
                    
            elif entry.get('type') == 'access-rule':
                rule_name = entry.get('name') or f"rule # {entry.get('rule-number', 'unknown')}"
                
                # Skip cleanup rules
                if rule_name in ['Cleanup rule', 'Cleanup']:
                    continue
                
                rule_data = {
                    'layer': current_layer,
                    'name': rule_name,
                    'position': entry.get('rule-number'),
                    'source': [item['name'] for item in entry.get('source', [])],
                    'source-negate': entry.get('source-negate', False),
                    'destination': [item['name'] for item in entry.get('destination', [])],
                    'destination-negate': entry.get('destination-negate', False),
                    'service': [item['name'] for item in entry.get('service', [])],
                    'service-negate': entry.get('service-negate', False),
                    'action': entry['action']['name'] if isinstance(entry.get('action'), dict) else entry.get('action', ''),
                    'track': entry['track']['type']['name'] if isinstance(entry.get('track', {}).get('type'), dict) else '',
                    'enabled': entry.get('enabled', True),
                    'comments': entry.get('comments', ''),
                    'install-on': [item['name'] for item in entry.get('install-on', [])],
                }
                
                # Handle "Inner Layer" -> "Apply Layer"
                if rule_data['action'] == 'Inner Layer':
                    rule_data['action'] = 'Apply Layer'
                
                # Handle inline layer  
                if entry.get('inline-layer'):
                    rule_data['inline-layer'] = entry['inline-layer']['name']
                    
                # Simplify single-value "Any" lists
                for field in ['source', 'destination', 'service', 'install-on']:
                    if rule_data[field] == ['Any']:
                        rule_data[field] = 'Any'
                
                rule_objects.append(rule_data)
                
                # Recurse into inline layers
                if entry.get('inline-layer'):
                    inline_layer_name = entry['inline-layer']['name']
                    try:
                        inline_resp = client.run_command(
                            "show-access-rulebase",
                            payload={"name": inline_layer_name, "use-object-dictionary": False})
                        if 'rulebase' in inline_resp:
                            _process_rulebase(inline_resp['rulebase'], inline_layer_name)
                    except Exception as e:
                        log.warning(f"Failed to fetch inline layer '{inline_layer_name}': {e}")
    
    _process_rulebase(response['rulebase'], layer)
    
    # Add sections and rules to CLI exporter
    if section_objects:
        cli_exporter.add_objects('access-section', section_objects)
    if rule_objects:
        cli_exporter.add_objects('access-rule', rule_objects)


def main():

    parser = argparse.ArgumentParser(description="Check Point Universal API Exporter")
    parser.add_argument("-u", "--user", default="admin", help="Management Server username")
    parser.add_argument("-p", "--password", help="Management Server password")
    parser.add_argument("-m", "--management", required=True, help="Management Server IP or Hostname")
    parser.add_argument("-d", "--domain", default="", help="Domain name (for Multi-Domain)")
    parser.add_argument("-v", "--api-version", dest="api_version", default="latest", help="API version (e.g. 1.9, 2.0)")

    parsed_args = parser.parse_args()

    if not parsed_args.password:
        import getpass
        parsed_args.password = getpass.getpass(f"Password for {parsed_args.user}@{parsed_args.management}: ")

    client = api_client(parsed_args.management, parsed_args.user,
                        parsed_args.password, parsed_args.domain if parsed_args.domain else None)

    # Load configuration
    config = read_config_file('./config/exporter_config.json')
    create_required_folders(config['required_folders'])

    # Determine API Version
    if parsed_args.api_version == "latest":
        try:
            sid, server_version = client.login()
            log.info(f"Detected Server API Version: {server_version}")
            
            # Parse version (e.g. 2.0.1 -> 2.0)
            major_ver = ".".join(server_version.split('.')[0:2])
            
            schema_url = f"https://sc1.checkpoint.com/documents/latest/APIs/data/v{major_ver}/dynamic/apis.json"
            
            try:
                r = requests.head(schema_url, verify=False, timeout=5)
                if r.status_code == 200:
                    api_version = major_ver
                    log.info(f"Using detected API version: {api_version}")
                else:
                    log.warning(f"Schema for version {major_ver} not found. Falling back to default (v2.1).")
                    api_version = "2.1" # Using v2.1 as base for documentation fetching
            except Exception as e:
                log.warning(f"Failed to check schema availability: {e}. Falling back to v2.1.")
                api_version = "2.1"
                
        except Exception as e:
             log.error(f"Failed to login or detect version: {e}")
             sys.exit(1)
    else:
        api_version = parsed_args.api_version
        client.login()

    # Fetch dynamic objects from API Spec
    log.info("Fetching supported API objects from Check Point API Spec...")
    dynamic_objects = fetch_api_objects()
    
    if dynamic_objects:
        log.info(f"Found {len(dynamic_objects)} object types in API spec.")
        formatted_cp_ansible_module_names = filter_dynamic_modules(dynamic_objects)
        log.info(f"Using {len(formatted_cp_ansible_module_names)} exportable object types after filtering.")
    else:
        log.warning("Failed to fetch API objects. Falling back to static list.")
        try:
            with open('config/supported_ansible_modules.json', 'r') as f:
                cp_ansible_module_names = json.load(f)
                formatted_cp_ansible_module_names = [x.replace('cp_mgmt_', '').replace('_', '-') for x in cp_ansible_module_names]
        except FileNotFoundError:
            log.error("Could not find config/supported_ansible_modules.json")
            sys.exit(1)

    cli_exporter = None

    try:
        # Export Objects
        parser = cp_object_exporter(client, formatted_cp_ansible_module_names)
        if parser:
            cli_exporter = parser.cli_exporter
        log.info('Objects exported successfully')
    except Exception as exc:
        log.exception(exc)
        sys.exit(1)

    try:
        # Export Access Rules
        access_layers_resp = client.run_command("show-access-layers", payload={})
        if 'access-layers' in access_layers_resp:
            for layer_obj in access_layers_resp['access-layers']:
                layer = layer_obj['name']
                export_layer_rules_to_ansible(client, layer)
                log.info(f'Exporting {layer} Layer')
                
                # Also generate CLI commands for rules in this layer
                if cli_exporter:
                    _add_rulebase_to_cli(client, cli_exporter, layer)
                    
            log.info('Rulebase exported successfully')
        else:
            log.warning("No access layers found or failed to fetch them.")
            
    except Exception as exc:
        log.exception(exc)
        sys.exit(1)

    # Write CLI file (objects + rules combined)
    if cli_exporter:
        cli_exporter.write()

    # Generate Ansible Playbook
    log.info("Generating Ansible Playbook...")
    cwd = Path(__file__).parent.relative_to(Path.cwd())
    objects_folder = cwd / config['output_folder_name'] / config['objects_folder_name']
    playbook_file = cwd / config['playbook_file_name']
    
    exported_modules = [path.relative_to(cwd / config['output_folder_name']).as_posix()
                        for path in objects_folder.iterdir() if path.suffix == '.yml']

    # Define order for inclusion in playbook
    object_priority = {
        'access-layer': 1, 'access-role': 1, 'threat-layer': 1, 'group': 1, 
        "application-site-group": 2, "group-with-exclusion": 2, 
        'application-site-category': -1,  "simple-gateway": -1, 
        "policy-rules": 3, "policy-rules-sections": 4 
    }
    priority_list = {(Path(config['objects_folder_name']) / (k + ".yml")).as_posix(): v for k, v in object_priority.items()}

    ordered_list = sorted(exported_modules, key=lambda k: priority_list.get(k, 0))
    
    playbook = [{
        "name": "Playbook for rules and objects exported to Ansible from the Check Point API",
        "connection": "httpapi",
        "hosts": "checkpoint_mgmt",
        "gather_facts": False,
        "collections": ['check_point.mgmt'],
        "vars": {"state":"present"},
        "tasks": [{"include_tasks": "{{item}}", "loop": ordered_list}]
    }]
    
    write_file(playbook_file, mode='w', content=yaml.dump(playbook, sort_keys=False))
    log.info('Playbook created successfully')

    client.logout()
    log.info("Logout successful")


if __name__ == "__main__":
    main()

