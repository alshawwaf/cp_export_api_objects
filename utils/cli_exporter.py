"""
Direct CLI command generator from Check Point API data.
Generates mgmt_cli commands independently of Ansible modules.
"""
import json
import copy
from pathlib import Path
from .logger_main import log

OUTPUT_FILE = Path("check_point_policy/import_mgmt_cli.txt")

# Dependency ordering for mgmt_cli imports
# Lower number = earlier in import sequence
PRIORITY_MAP = {
    # Pass 1 - Basic objects (no dependencies)
    'tag': 1, 'host': 1, 'network': 1, 'network-feed': 1, 'wildcard': 1,
    'address-range': 1, 'multicast-address-range': 1,
    'service-tcp': 1, 'service-udp': 1, 'service-icmp': 1, 'service-icmp6': 1,
    'service-other': 1, 'service-dce-rpc': 1, 'service-rpc': 1, 'service-sctp': 1,
    'service-citrix-tcp': 1, 'service-compound-tcp': 1, 'service-gtp': 1,
    'time': 1, 'time-group': 1, 'dynamic-object': 1, 'dns-domain': 1,
    'security-zone': 1, 'trusted-client': 1, 'opsec-application': 1,
    'user': 1, 'user-group': 1, 'user-template': 1,
    'lsm-gateway': 1, 'lsm-cluster': 1,
    
    # Pass 2 - Groups and applications (depend on basic objects)
    'group': 2, 'group-with-exclusion': 2,
    'service-group': 2, 'application-site': 2,
    'application-site-category': 2, 'application-site-group': 2,
    
    # Pass 3 - Complex objects (depend on groups)
    'access-role': 3, 'access-layer': 3,
    'simple-gateway': 3, 'simple-cluster': 3, 'checkpoint-host': 3,
    'interoperable-device': 3,
    'vpn-community-meshed': 3, 'vpn-community-star': 3,
    'threat-profile': 3, 'threat-indicator': 3,
    'https-layer': 3, 'https-section': 3, 'nat-section': 3,
    
    # Pass 4 - Rules (depend on everything above)
    'access-rule': 100, 'nat-rule': 100, 'threat-rule': 100,
    'https-rule': 100, 'policy-rules': 100,
}

# Fields to exclude from CLI commands (Ansible-only or internal)
CLI_EXCLUDED_FIELDS = {
    'type',  # Implicit in the command itself
}


def _format_cli_value(value):
    """Format a value for mgmt_cli command line."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if value is None:
        return '""'
    
    s = str(value)
    # Quote if contains spaces, special chars, or is empty
    if s == "" or ' ' in s or any(c in s for c in '(){}[],;|&<>'):
        return f'"{s}"'
    return s


# Maximum nesting depth for CLI parameter flattening.
# The mgmt_cli API typically rejects parameters nested deeper than 2 levels
# (e.g. mep.default-priority-rule.satellite-gateways is invalid).
MAX_FLATTEN_DEPTH = 2


def _flatten_to_cli_params(data, parent_key='', depth=0):
    """Flatten a nested dict into dot-notation key-value pairs for mgmt_cli."""
    params = []
    
    if depth >= MAX_FLATTEN_DEPTH:
        return params
    
    if isinstance(data, dict):
        for k, v in data.items():
            if k in CLI_EXCLUDED_FIELDS:
                continue
            full_key = f"{parent_key}.{k}" if parent_key else k
            
            if isinstance(v, dict):
                params.extend(_flatten_to_cli_params(v, full_key, depth + 1))
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    if isinstance(item, (dict, list)):
                        params.extend(_flatten_to_cli_params(item, f"{full_key}.{i}", depth + 1))
                    else:
                        params.append((f"{full_key}.{i}", _format_cli_value(item)))
            else:
                params.append((full_key, _format_cli_value(v)))
    
    return params


def generate_cli_command(obj_type, obj_data, verb="add"):
    """
    Generate a single mgmt_cli command from clean API object data.
    """
    # Create a local copy to avoid modifying the original list/dict
    clean_data = copy.deepcopy(obj_data)
    
    # Strip internal markers before generating CLI
    clean_data.pop('is_cleanup', None)
    clean_data.pop('has_default_cleanup', None)
    
    params = _flatten_to_cli_params(clean_data)
    
    cmd_parts = [f"mgmt_cli -r true {verb} {obj_type}"]
    for key, value in params:
        cmd_parts.append(f"{key} {value}")
    cmd_parts.append("ignore-warnings true")
    
    return " ".join(cmd_parts)


class CLIExporter:
    """Collects CLI objects and writes them to import_mgmt_cli.txt."""
    
    def __init__(self):
        self.cli_objects = {}  # obj_type -> list of command strings
    
    def add_objects(self, obj_type, objects):
        """
        Add a batch of objects for a given type.
        
        Args:
            obj_type: The object type (e.g. 'host', 'network')
            objects: List of clean object dicts (dash-keyed, whitelist-filtered)
        """
        if not objects:
            return
            
        commands = []
        for obj_data in objects:
            try:
                # Use 'set' for objects that usually exist by default on target SMS
                verb = "add"
                if obj_type == 'access-layer':
                    verb = "set"
                
                # Special handling for Cleanup rules
                if obj_type == 'access-rule' and obj_data.get('is_cleanup'):
                    # Force track to Log for cleanup rules
                    obj_data['track'] = "Log"
                    if obj_data.get('has_default_cleanup'):
                        verb = "set"
                    else:
                        verb = "add"
                
                cmd = generate_cli_command(obj_type, obj_data, verb=verb)
                commands.append(cmd)
            except Exception as e:
                obj_name = obj_data.get('name', 'unknown')
                log.warning(f"Failed to generate CLI for {obj_type}/{obj_name}: {e}")
        
        if commands:
            self.cli_objects[obj_type] = commands
    
    def write(self):
        """Write all collected CLI commands to the output file, dependency-ordered."""
        if not self.cli_objects:
            log.warning("No CLI commands to write.")
            return
        
        # Sort by dependency priority
        def get_priority(obj_type):
            if obj_type in PRIORITY_MAP:
                return PRIORITY_MAP[obj_type]
            if 'rule' in obj_type or 'section' in obj_type:
                return 100
            return 2  # Default: group-level
        
        sorted_types = sorted(self.cli_objects.keys(), 
                              key=lambda t: (get_priority(t), t))
        
        all_lines = []
        total_commands = 0
        
        for obj_type in sorted_types:
            commands = self.cli_objects[obj_type]
            all_lines.append(f"\n# {obj_type} ({len(commands)} objects)")
            all_lines.extend(commands)
            total_commands += len(commands)
        
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write("\n".join(all_lines))
        
        log.info(f"CLI export complete: {total_commands} commands for "
                 f"{len(self.cli_objects)} object types written to {OUTPUT_FILE}")
