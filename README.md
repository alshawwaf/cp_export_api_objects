# Check Point Universal API Exporter

A Python tool that exports Check Point Security Policies, Rules, and Objects into **Ansible Playbooks** and **`mgmt_cli` commands** — generated directly from the Check Point API specification.

## Key Features

- **Dynamic Object Discovery** — Identifies 120+ exportable object types from the official API spec (`apis.json`)
- **Dual Export** — Generates both Ansible YAML playbooks and `mgmt_cli` CLI commands independently
  - **CLI export**: Supports all API-supported types, generated directly from clean API data
  - **Ansible export**: Generates `cp_mgmt_*` module tasks with proper field naming
- **Field-Aware Intelligence** — Recursively resolves API object inheritance to whitelist only valid input fields
- **Rulebase Export** — Full access control rulebase with sections, inline layers, and dependency ordering
- **Universal Compatibility** — Auto-detects server API version, works across R80.x, R81.x, and R82

## Installation

```bash
git clone <repo-url>
cd cp_export_api_objects
pip install -r requirements.txt
```

## Usage

```bash
python cp_exporter.py -m <MGMT_IP> -u <USERNAME> -p <PASSWORD>
```

### Options

| Flag | Description |
|------|-------------|
| `-m, --management` | Management Server IP or hostname (required) |
| `-u, --user` | Username (default: `admin`) |
| `-p, --password` | Password (prompted securely if omitted) |
| `-d, --domain` | Domain name for Multi-Domain (MDS) |
| `-v, --api-version` | API version override (default: auto-detect) |

## Output

All exported data is saved under `check_point_policy/`:

```
check_point_policy/
├── objects/           # Ansible YAML files per object type
├── docs/              # Expanded JSON for complex types (gateways, VPN)
├── cp_mgmt_playbook.yml    # Master Ansible playbook
└── import_mgmt_cli.txt     # Standalone mgmt_cli import script
```

### Architecture

```
Check Point API
      │
      ▼
  Fetch & Parse Objects ──► Whitelist Filter (API spec)
      │                            │
      │                     ┌──────┴──────┐
      │                     │             │
      │               CLI Path      Ansible Path
      │              (dash-keys)   (underscore-keys)
      ▼                     │             │
  Fetch Rulebase ──►   mgmt_cli     cp_mgmt_* YAML
      │                commands       playbook
      ▼                     │             │
  import_mgmt_cli.txt      ▼             ▼
                     Combined Output   Per-type .yml
```

## Utilities

| Script | Purpose |
|--------|---------|
| `utils/dynamic_field_extractor.py` | Refresh field whitelist from API spec |
| `utils/fetch_api_objects.py` | Discover exportable object types |
| `utils/cli_exporter.py` | Direct CLI command generation |

## Known Limitations

See [limitations.txt](limitations.txt) for Ansible-specific constraints (unsupported fields, cleanup rules, etc.).

## License

MIT License — see [LICENSE](LICENSE) for details.