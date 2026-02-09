import requests
import json
import os
import re

API_SPEC_URL = "https://sc1.checkpoint.com/documents/latest/APIs/data/v2.1/dynamic/apis.json"
OUTPUT_FILE = "config/api_supported_objects.json"


def _get_cmd_name(name_entry):
    """Extract the web command name from a command's name entry."""
    if isinstance(name_entry, dict):
        return name_entry.get('web', name_entry.get('cli', ''))
    elif isinstance(name_entry, str):
        return name_entry
    return ''


def fetch_api_objects(url=API_SPEC_URL):
    try:
        print(f"Fetching API spec from {url}...")
        response = requests.get(url, verify=False, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        commands = data.get('commands', [])
        print(f"Number of commands found: {len(commands)}")
        
        # Known non-policy objects to exclude
        EXCLUDED_TYPES = {
            'api-key', 'central-license', 'session', 'task', 'keepalive', 
            'login', 'logout', 'publish', 'discard', 'verify-policy', 'install-policy'
        }

        # Step 1: Build a set of ALL documented command names in the spec
        all_cmd_names = set()
        add_commands = {}  # cmd_name -> cmd object (for add commands only)
        
        for cmd in commands:
            # Only consider documented API commands
            if not cmd.get('documented', False):
                continue
                
            cmd_name = _get_cmd_name(cmd.get('name'))
            if cmd_name:
                all_cmd_names.add(cmd_name)
                if cmd_name.startswith('add-'):
                    add_commands[cmd_name] = cmd

        # Step 2: Find object types that have BOTH add-<type> AND show-<type>s (plural list command)
        add_pattern = re.compile(r"^add-(.+)$")
        object_types = set()

        for cmd_name in add_commands:
            match = add_pattern.match(cmd_name)
            if not match:
                continue
            
            obj_type = match.group(1)
            
            if obj_type in EXCLUDED_TYPES:
                continue
            
            # Verify this type has a corresponding show (list) command
            # Check Point uses show-<type>s (plural) for listing objects
            # e.g. add-host -> show-hosts, add-network -> show-networks
            has_show_plural = f"show-{obj_type}s" in all_cmd_names
            has_show_singular = f"show-{obj_type}" in all_cmd_names
            
            if has_show_plural or has_show_singular:
                object_types.add(obj_type)

        
        sorted_objects = sorted(list(object_types))
        print(f"Found {len(sorted_objects)} exportable object types (verified with show commands).")
        
        # Save to file
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(sorted_objects, f, indent=4)
            
        print(f"Saved to {OUTPUT_FILE}")
        return sorted_objects

    except Exception as e:
        print(f"Error fetching API spec: {e}")
        return []

if __name__ == "__main__":
    fetch_api_objects()
