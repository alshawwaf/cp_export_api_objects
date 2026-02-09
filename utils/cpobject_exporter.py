
import sys
import json
from pathlib import Path
from utils.logger_main import log
from utils.cpobject_parser import ParseObjects
from utils.file_ops import read_file, read_config_file

def cp_object_exporter(client, module_list):
    """
    Main exporter function for Check Point objects.
    
    Args:
        client: API client instance
        module_list (list): List of object types to export (e.g. ['host', 'network'])
    """
    # read the config file and create the required folders
    config = read_config_file('./config/exporter_config.json')

    config_folder_path = Path(config['config_folder_name'])
    ignored_ansible_modules_file_name = config['ignored_ansible_modules_file_name']
    ignored_ansible_modules_file = Path.joinpath(
        config_folder_path, ignored_ansible_modules_file_name)

    # Get the list of ignored modules from the config file ./config/ignore_modules.json
    log.info(f'Reading ignored ansible modules from file: {ignored_ansible_modules_file}')
    try:
        ignored_modules_list = json.loads(read_file(ignored_ansible_modules_file))
    except FileNotFoundError:
        log.warning(f"Ignored modules file {ignored_ansible_modules_file} not found. Skipping filtering.")
        ignored_modules_list = []

    # Clean and filter the module list
    def clean_name(n):
        return n.replace('cp_mgmt_', '').replace('_', '-')

    ignored_clean = [clean_name(x) for x in ignored_modules_list]
    
    formatted_cp_ansible_module_names = []
    for mod in module_list:
        clean_mod = clean_name(mod)
        if clean_mod not in ignored_clean:
            formatted_cp_ansible_module_names.append(clean_mod)

    try:
        # Create the parser and process objects
        log.info(f'Parsing {len(formatted_cp_ansible_module_names)} object types')
        parser = ParseObjects(client, formatted_cp_ansible_module_names)
        return parser
    except TimeoutError as exc:
        log.fatal(f"Timeout error: {exc}")    
    except Exception as exc:
        log.exception(exc)
        sys.exit(1)
