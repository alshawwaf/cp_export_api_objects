"""
Dynamic Field Extractor for Check Point API Specification (v2)

This script extracts all valid input fields for each 'add-<type>' command by:
1. Following the inheritance chain in the API specification
2. Adding known universal/common fields that apply to most objects
3. Handling special cases for different object categories

The result is a complete, documentation-driven field whitelist.
"""

import json
import requests
import os
import re

API_SPEC_URL = "https://sc1.checkpoint.com/documents/latest/APIs/data/v2.1/dynamic/apis.json"
OUTPUT_FILE = "config/field_schemas/dynamic_valid_fields.json"

# Universal fields accepted by virtually ALL add/set commands
# These are defined at the API level, not in individual object schemas
UNIVERSAL_FIELDS = {
    "name",             # Object name (required for most)
    "color",            # Object color
    "comments",         # Object comments
    "tags",             # Object tags
    "ignore-warnings",  # API control
    "ignore-errors",    # API control  
    "details-level",    # Response detail control
    "new-name",         # For set commands (rename)
}

# Category-specific common fields
NETWORK_OBJECT_FIELDS = {
    "ipv4-address",
    "ipv6-address", 
    "subnet4",
    "subnet-mask",
    "mask-length4",
    "subnet6",
    "mask-length6",
}

RULE_COMMON_FIELDS = {
    "layer",
    "position",
    "name",
    "enabled",
    "comments",
    "ignore-warnings",
    "ignore-errors",
}

# Fields that are ALWAYS output-only (never valid for add/set)
ALWAYS_OUTPUT_ONLY = {
    "uid", "type", "domain", "meta-info", "icon", "read-only", 
    "available-actions", "groups", "creation-time", "last-modify-time",
    "creator", "last-modifier", "parent-layer", "objId", "domainId",
    "folder", "folderPath", "ownedName", "is_owned"
}

# Object type categories for smart field assignment
NETWORK_OBJECTS = {'host', 'network', 'address-range', 'multicast-address-range'}
RULE_OBJECTS = {'access-rule', 'nat-rule', 'threat-rule', 'https-rule'}
GATEWAY_OBJECTS = {'simple-gateway', 'simple-cluster', 'checkpoint-host', 'interoperable-device'}


class DynamicFieldExtractor:
    def __init__(self):
        self.spec = None
        self.objects_by_name = {}
        self.field_cache = {}
    
    def fetch_spec(self):
        """Fetch the API specification."""
        try:
            print(f"Fetching API spec from {API_SPEC_URL}...")
            r = requests.get(API_SPEC_URL, verify=False, timeout=30)
            self.spec = r.json()
            
            for obj in self.spec.get('objects', []):
                self.objects_by_name[obj.get('name', '')] = obj
            
            print(f"Loaded {len(self.objects_by_name)} object definitions")
            return True
        except Exception as e:
            print(f"Error fetching spec: {e}")
            return False
    
    def get_all_fields(self, object_name, visited=None):
        """Recursively get all fields for an object, including inherited fields."""
        if visited is None:
            visited = set()
        
        if object_name in visited:
            return set()
        visited.add(object_name)
        
        if object_name in self.field_cache:
            return self.field_cache[object_name].copy()
        
        obj_def = self.objects_by_name.get(object_name)
        if not obj_def:
            return set()
        
        fields = set()
        for field in obj_def.get('fields', []):
            field_name = field.get('name', '')
            if field_name and field_name not in ALWAYS_OUTPUT_ONLY:
                fields.add(field_name)
        
        # Get parent fields (inheritance)
        parent = obj_def.get('parent')
        if parent:
            parent_fields = self.get_all_fields(parent, visited)
            fields.update(parent_fields)
        
        self.field_cache[object_name] = fields
        return fields.copy()
    
    def get_category_fields(self, obj_type):
        """Get additional fields based on object category."""
        extra = set()
        
        if obj_type in NETWORK_OBJECTS:
            extra.update(NETWORK_OBJECT_FIELDS)
        
        if obj_type in RULE_OBJECTS:
            extra.update(RULE_COMMON_FIELDS)
        
        if obj_type in GATEWAY_OBJECTS:
            extra.update(NETWORK_OBJECT_FIELDS)
            extra.add('one-time-password')
            extra.add('version')
            extra.add('os-name')
        
        return extra
    
    def get_cmd_name(self, name_entry):
        if isinstance(name_entry, dict):
            return name_entry.get('web', '')
        elif isinstance(name_entry, str):
            return name_entry
        return ''
    
    def extract_all_add_command_fields(self):
        """Extract valid input fields for all 'add-<type>' commands."""
        result = {}
        
        for cmd in self.spec.get('commands', []):
            cmd_name = self.get_cmd_name(cmd.get('name'))
            
            if not cmd_name.startswith('add-'):
                continue
            
            obj_type = cmd_name[4:]  # Remove 'add-'
            request_type = cmd.get('request')
            
            # Start with universal fields
            all_fields = UNIVERSAL_FIELDS.copy()
            
            # Add category-specific fields
            all_fields.update(self.get_category_fields(obj_type))
            
            # Add spec-derived fields (with inheritance)
            if request_type:
                spec_fields = self.get_all_fields(request_type)
                all_fields.update(spec_fields)
            
            # Remove output-only fields
            all_fields -= ALWAYS_OUTPUT_ONLY
            
            if all_fields:
                result[obj_type] = sorted(list(all_fields))
        
        return result
    
    def save_result(self, result):
        """Save the extracted fields to JSON file."""
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        print(f"\nSaved valid fields for {len(result)} object types to {OUTPUT_FILE}")


def main():
    extractor = DynamicFieldExtractor()
    
    if not extractor.fetch_spec():
        return
    
    print("\nExtracting fields with inheritance + universal fields...")
    result = extractor.extract_all_add_command_fields()
    
    # Print sample results
    print("\n--- Sample: host ---")
    host_fields = result.get('host', [])
    print(f"  Fields ({len(host_fields)}): {host_fields}")
    
    print("\n--- Sample: network ---")
    net_fields = result.get('network', [])
    print(f"  Fields ({len(net_fields)}): {net_fields}")
    
    print("\n--- Sample: vpn-community-star ---")
    vpn_fields = result.get('vpn-community-star', [])
    print(f"  Fields ({len(vpn_fields)}): {vpn_fields}")
    
    print("\n--- Sample: access-rule ---")
    rule_fields = result.get('access-rule', [])
    print(f"  Fields ({len(rule_fields)}): {rule_fields}")
    
    extractor.save_result(result)
    
    # Summary
    total_fields = sum(len(fields) for fields in result.values())
    avg_fields = total_fields / len(result) if result else 0
    print(f"\nSummary:")
    print(f"  Object types: {len(result)}")
    print(f"  Total fields: {total_fields}")
    print(f"  Avg fields per type: {avg_fields:.1f}")


if __name__ == "__main__":
    main()
