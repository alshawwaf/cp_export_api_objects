# API QA Performance Audit Report
Generated: 2026-02-09 23:37:36

## Summary Table
| Object Type | Variant | Status | Duration (s) |
| :--- | :--- | :--- | :--- |
| host | 1 | [PASSED] | 0.96 |
| host | 2 | [PASSED] | 1.01 |
| network | 1 | [PASSED] | 1.13 |
| network | 2 | [PASSED] | 1.15 |
| network | 3 | [PASSED] | 1.03 |
| network | 4 | [PASSED] | 1.18 |
| network | 5 | [PASSED] | 2.42 |
| group | 0 | [PASSED] | 0.40 |
| address-range | 1 | [PASSED] | 1.35 |
| address-range | 2 | [FAILED] | 0.39 |
| address-range | 3 | [PASSED] | 1.08 |
| address-range | 4 | [PASSED] | 1.04 |
| multicast-address-range | 1 | [PASSED] | 0.44 |
| multicast-address-range | 2 | [PASSED] | 0.37 |
| multicast-address-range | 3 | [PASSED] | 0.38 |
| multicast-address-range | 4 | [PASSED] | 0.32 |
| multicast-address-range | 5 | [PASSED] | 0.38 |
| multicast-address-range | 6 | [PASSED] | 0.35 |
| group-with-exclusion | 0 | [PASSED] | 0.71 |
| dns-domain | 0 | [PASSED] | 0.32 |
| wildcard | 0 | [PASSED] | 0.36 |

---
## host

<details>
<summary><b>[PASSED] Variant 1 (Total: 0.96s)</b></summary>

#### [PASSED] `add-host` ([0.46s])

**Payload:**
```json
{
  "interfaces": [
    {
      "name": "QA_5292",
      "subnet": "10.100.0.0",
      "mask-length": 24,
      "color": "slate blue",
      "comments": "QA Automated Test Object",
      "ignore-warnings": true,
      "ignore-errors": true
    }
  ],
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "host-servers": {
    "dns-server": false,
    "mail-server": false,
    "web-server": true,
    "web-server-config": {
      "additional-ports": [],
      "application-engines": [],
      "listen-standard-port": false,
      "operating-system": "windows"
    }
  },
  "name": "QA_HOST_1_977",
  "set-if-exists": true,
  "color": "black",
  "comments": "QA Automated Test Object",
  "details-level": "uid",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv4-address": "10.100.1.104"
}
```
**Response:**
```json
{
  "uid": "84533fb1-bba1-452b-9ad1-a33029261e35",
  "name": "QA_HOST_1_977",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.104",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "operating-system": "windows",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "b3f80f77-7ad5-488f-ad66-fe37d9312ab7",
      "name": "QA_5292",
      "type": "CpmiInterface",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "subnet4": "10.100.0.0",
      "mask-length4": 24,
      "subnet-mask": "255.255.255.0",
      "comments": "QA Automated Test Object",
      "color": "slate blue",
      "icon": "Unknown",
      "tags": []
    }
  ],
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "black",
  "icon": "Objects/host",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690053179,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690053179,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-host` ([0.13s])

**Payload:**
```json
{
  "name": "QA_HOST_1_977",
  "comments": "QA updated exhaustive variant 1",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "84533fb1-bba1-452b-9ad1-a33029261e35",
  "name": "QA_HOST_1_977",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.104",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "additional-ports": [],
      "operating-system": "windows",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "b3f80f77-7ad5-488f-ad66-fe37d9312ab7",
      "name": "QA_5292",
      "type": "CpmiInterface",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "subnet4": "10.100.0.0",
      "mask-length4": 24,
      "subnet-mask": "255.255.255.0",
      "comments": "QA Automated Test Object",
      "color": "slate blue",
      "icon": "Unknown",
      "tags": []
    }
  ],
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 1",
  "color": "orange",
  "icon": "Objects/host",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690053624,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690053179,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-host` ([0.10s])

**Payload:**
```json
{
  "name": "QA_HOST_1_977"
}
```
**Response:**
```json
{
  "uid": "84533fb1-bba1-452b-9ad1-a33029261e35",
  "name": "QA_HOST_1_977",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.104",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "additional-ports": [],
      "operating-system": "windows",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "b3f80f77-7ad5-488f-ad66-fe37d9312ab7",
      "name": "QA_5292",
      "type": "CpmiInterface",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "subnet4": "10.100.0.0",
      "mask-length4": 24,
      "subnet-mask": "255.255.255.0",
      "comments": "QA Automated Test Object",
      "color": "slate blue",
      "icon": "Unknown",
      "tags": []
    }
  ],
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 1",
  "color": "orange",
  "icon": "Objects/host",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690053624,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690053179,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-host` ([0.27s])

**Payload:**
```json
{
  "name": "QA_HOST_1_977"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 2 (Total: 1.01s)</b></summary>

#### [PASSED] `add-host` ([0.52s])

**Payload:**
```json
{
  "interfaces": [
    {
      "name": "QA_5292",
      "subnet": "10.100.0.0",
      "mask-length": 24,
      "color": "slate blue",
      "comments": "QA Automated Test Object",
      "ignore-warnings": true,
      "ignore-errors": true
    }
  ],
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "host-servers": {
    "dns-server": false,
    "mail-server": false,
    "web-server": true,
    "web-server-config": {
      "additional-ports": [],
      "application-engines": [],
      "listen-standard-port": false,
      "operating-system": "windows"
    }
  },
  "name": "QA_HOST_2_334",
  "set-if-exists": true,
  "color": "black",
  "comments": "QA Automated Test Object",
  "details-level": "uid",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv6-address": "2001:db8:85a3::1145"
}
```
**Response:**
```json
{
  "uid": "7e34caa2-31d2-42fe-af07-4090bff6958f",
  "name": "QA_HOST_2_334",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address": "2001:db8:85a3::1145",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "operating-system": "windows",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "4af3cb58-5977-4c0b-9193-7c6a19c034b4",
      "name": "QA_5292",
      "type": "CpmiInterface",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "subnet4": "10.100.0.0",
      "mask-length4": 24,
      "subnet-mask": "255.255.255.0",
      "comments": "QA Automated Test Object",
      "color": "slate blue",
      "icon": "Unknown",
      "tags": []
    }
  ],
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "black",
  "icon": "Objects/host",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690054178,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690054178,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-host` ([0.15s])

**Payload:**
```json
{
  "name": "QA_HOST_2_334",
  "comments": "QA updated exhaustive variant 2",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "7e34caa2-31d2-42fe-af07-4090bff6958f",
  "name": "QA_HOST_2_334",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address": "2001:db8:85a3::1145",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "additional-ports": [],
      "operating-system": "windows",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "4af3cb58-5977-4c0b-9193-7c6a19c034b4",
      "name": "QA_5292",
      "type": "CpmiInterface",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "subnet4": "10.100.0.0",
      "mask-length4": 24,
      "subnet-mask": "255.255.255.0",
      "comments": "QA Automated Test Object",
      "color": "slate blue",
      "icon": "Unknown",
      "tags": []
    }
  ],
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 2",
  "color": "orange",
  "icon": "Objects/host",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690054662,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690054178,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-host` ([0.09s])

**Payload:**
```json
{
  "name": "QA_HOST_2_334"
}
```
**Response:**
```json
{
  "uid": "7e34caa2-31d2-42fe-af07-4090bff6958f",
  "name": "QA_HOST_2_334",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address": "2001:db8:85a3::1145",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "additional-ports": [],
      "operating-system": "windows",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "4af3cb58-5977-4c0b-9193-7c6a19c034b4",
      "name": "QA_5292",
      "type": "CpmiInterface",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "subnet4": "10.100.0.0",
      "mask-length4": 24,
      "subnet-mask": "255.255.255.0",
      "comments": "QA Automated Test Object",
      "color": "slate blue",
      "icon": "Unknown",
      "tags": []
    }
  ],
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 2",
  "color": "orange",
  "icon": "Objects/host",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690054662,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690054178,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-host` ([0.25s])

**Payload:**
```json
{
  "name": "QA_HOST_2_334"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

---
## network

<details>
<summary><b>[PASSED] Variant 1 (Total: 1.13s)</b></summary>

#### [PASSED] `add-network` ([0.60s])

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "disallow",
  "name": "QA_NETWORK_1_988",
  "set-if-exists": true,
  "color": "burlywood",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "mask-length": 24,
  "subnet4": "10.100.0.0",
  "mask-length4": 24
}
```
**Response:**
```json
{
  "uid": "aab6e4b0-5c69-4707-952f-7716c2410876",
  "name": "QA_NETWORK_1_988",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 24,
  "subnet-mask": "255.255.255.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "burlywood",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690056450,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690056450,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-network` ([0.12s])

**Payload:**
```json
{
  "name": "QA_NETWORK_1_988",
  "comments": "QA updated exhaustive variant 1",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "aab6e4b0-5c69-4707-952f-7716c2410876",
  "name": "QA_NETWORK_1_988",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 24,
  "subnet-mask": "255.255.255.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 1",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690056973,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690056450,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-network` ([0.07s])

**Payload:**
```json
{
  "name": "QA_NETWORK_1_988"
}
```
**Response:**
```json
{
  "uid": "aab6e4b0-5c69-4707-952f-7716c2410876",
  "name": "QA_NETWORK_1_988",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 24,
  "subnet-mask": "255.255.255.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 1",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690056973,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690056450,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-network` ([0.33s])

**Payload:**
```json
{
  "name": "QA_NETWORK_1_988"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 2 (Total: 1.15s)</b></summary>

#### [PASSED] `add-network` ([0.64s])

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "disallow",
  "name": "QA_NETWORK_2_196",
  "set-if-exists": true,
  "color": "burlywood",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "mask-length": 24,
  "subnet6": "2001:db8:85a3::",
  "mask-length6": 64
}
```
**Response:**
```json
{
  "uid": "590abae2-cd73-42b9-bf17-e52c72e5f20b",
  "name": "QA_NETWORK_2_196",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet6": "2001:db8:85a3::",
  "mask-length6": 64,
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "burlywood",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690057781,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690057781,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-network` ([0.09s])

**Payload:**
```json
{
  "name": "QA_NETWORK_2_196",
  "comments": "QA updated exhaustive variant 2",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "590abae2-cd73-42b9-bf17-e52c72e5f20b",
  "name": "QA_NETWORK_2_196",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet6": "2001:db8:85a3::",
  "mask-length6": 64,
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 2",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690058195,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690057781,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-network` ([0.07s])

**Payload:**
```json
{
  "name": "QA_NETWORK_2_196"
}
```
**Response:**
```json
{
  "uid": "590abae2-cd73-42b9-bf17-e52c72e5f20b",
  "name": "QA_NETWORK_2_196",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet6": "2001:db8:85a3::",
  "mask-length6": 64,
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 2",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690058195,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690057781,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-network` ([0.35s])

**Payload:**
```json
{
  "name": "QA_NETWORK_2_196"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 3 (Total: 1.03s)</b></summary>

#### [PASSED] `add-network` ([0.47s])

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "disallow",
  "name": "QA_NETWORK_3_682",
  "set-if-exists": true,
  "color": "burlywood",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "subnet": "10.100.0.0",
  "mask-length4": 24
}
```
**Response:**
```json
{
  "uid": "6d6badf0-4f24-4b7c-b300-d1d0ea48161a",
  "name": "QA_NETWORK_3_682",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 24,
  "subnet-mask": "255.255.255.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "burlywood",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690058727,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690058727,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-network` ([0.10s])

**Payload:**
```json
{
  "name": "QA_NETWORK_3_682",
  "comments": "QA updated exhaustive variant 3",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "6d6badf0-4f24-4b7c-b300-d1d0ea48161a",
  "name": "QA_NETWORK_3_682",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 24,
  "subnet-mask": "255.255.255.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 3",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690059184,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690058727,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-network` ([0.07s])

**Payload:**
```json
{
  "name": "QA_NETWORK_3_682"
}
```
**Response:**
```json
{
  "uid": "6d6badf0-4f24-4b7c-b300-d1d0ea48161a",
  "name": "QA_NETWORK_3_682",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 24,
  "subnet-mask": "255.255.255.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 3",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690059184,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690058727,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-network` ([0.39s])

**Payload:**
```json
{
  "name": "QA_NETWORK_3_682"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 4 (Total: 1.18s)</b></summary>

#### [PASSED] `add-network` ([0.63s])

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "disallow",
  "name": "QA_NETWORK_4_446",
  "set-if-exists": true,
  "color": "burlywood",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "subnet": "10.100.0.0",
  "mask-length": 24
}
```
**Response:**
```json
{
  "uid": "6c614354-6091-4649-8411-9ed8fcec2b20",
  "name": "QA_NETWORK_4_446",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 24,
  "subnet-mask": "255.255.255.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "burlywood",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690059827,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690059827,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-network` ([0.12s])

**Payload:**
```json
{
  "name": "QA_NETWORK_4_446",
  "comments": "QA updated exhaustive variant 4",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "6c614354-6091-4649-8411-9ed8fcec2b20",
  "name": "QA_NETWORK_4_446",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 24,
  "subnet-mask": "255.255.255.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 4",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690060390,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690059827,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-network` ([0.07s])

**Payload:**
```json
{
  "name": "QA_NETWORK_4_446"
}
```
**Response:**
```json
{
  "uid": "6c614354-6091-4649-8411-9ed8fcec2b20",
  "name": "QA_NETWORK_4_446",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 24,
  "subnet-mask": "255.255.255.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 4",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690060390,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690059827,
      "iso-8601": "2026-02-09T21:20-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-network` ([0.36s])

**Payload:**
```json
{
  "name": "QA_NETWORK_4_446"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 5 (Total: 2.42s)</b></summary>

#### [PASSED] `add-network` ([1.74s])

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "disallow",
  "name": "QA_NETWORK_5_839",
  "set-if-exists": true,
  "color": "burlywood",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "subnet": "10.100.0.0",
  "subnet-mask": "255.255.0.0"
}
```
**Response:**
```json
{
  "uid": "1355509e-9d78-4f0c-9a49-988774534f7a",
  "name": "QA_NETWORK_5_839",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 16,
  "subnet-mask": "255.255.0.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "burlywood",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690061040,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690061040,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-network` ([0.10s])

**Payload:**
```json
{
  "name": "QA_NETWORK_5_839",
  "comments": "QA updated exhaustive variant 5",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "1355509e-9d78-4f0c-9a49-988774534f7a",
  "name": "QA_NETWORK_5_839",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 16,
  "subnet-mask": "255.255.0.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 5",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690062725,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690061040,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-network` ([0.08s])

**Payload:**
```json
{
  "name": "QA_NETWORK_5_839"
}
```
**Response:**
```json
{
  "uid": "1355509e-9d78-4f0c-9a49-988774534f7a",
  "name": "QA_NETWORK_5_839",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "disallow",
  "subnet4": "10.100.0.0",
  "mask-length4": 16,
  "subnet-mask": "255.255.0.0",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 5",
  "color": "orange",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690062725,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690061040,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-network` ([0.50s])

**Payload:**
```json
{
  "name": "QA_NETWORK_5_839"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

---
## group

<details>
<summary><b>[PASSED] Variant 0 (Total: 0.40s)</b></summary>

#### [PASSED] `add-group` ([0.09s])

**Payload:**
```json
{
  "members": [],
  "name": "QA_GROUP_0_480",
  "color": "firebrick",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true
}
```
**Response:**
```json
{
  "uid": "e921082c-bdf4-4e96-945c-3f5b17df1ba0",
  "name": "QA_GROUP_0_480",
  "type": "group",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "members": [],
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "firebrick",
  "icon": "General/group",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690063408,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690063408,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-group` ([0.13s])

**Payload:**
```json
{
  "name": "QA_GROUP_0_480",
  "comments": "QA updated exhaustive variant 0",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "e921082c-bdf4-4e96-945c-3f5b17df1ba0",
  "name": "QA_GROUP_0_480",
  "type": "group",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "members": [],
  "groups": [],
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "General/group",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690063535,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690063408,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-group` ([0.07s])

**Payload:**
```json
{
  "name": "QA_GROUP_0_480"
}
```
**Response:**
```json
{
  "uid": "e921082c-bdf4-4e96-945c-3f5b17df1ba0",
  "name": "QA_GROUP_0_480",
  "type": "group",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "members": [],
  "groups": [],
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "General/group",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690063535,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690063408,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-group` ([0.11s])

**Payload:**
```json
{
  "name": "QA_GROUP_0_480"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

---
## address-range

<details>
<summary><b>[PASSED] Variant 1 (Total: 1.35s)</b></summary>

#### [PASSED] `add-address-range` ([0.65s])

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "name": "QA_ADDRESS-RANGE_1_279",
  "set-if-exists": true,
  "color": "navy blue",
  "comments": "QA Automated Test Object",
  "details-level": "full",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv4-address-first": "10.100.1.10",
  "ipv4-address-last": "10.100.1.30"
}
```
**Response:**
```json
{
  "uid": "bd92bcca-5c9d-45d1-9b91-e5a9e3d5808b",
  "name": "QA_ADDRESS-RANGE_1_279",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "10.100.1.10",
  "ipv4-address-last": "10.100.1.30",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "navy blue",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690065247,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690065247,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-address-range` ([0.13s])

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_1_279",
  "comments": "QA updated exhaustive variant 1",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "bd92bcca-5c9d-45d1-9b91-e5a9e3d5808b",
  "name": "QA_ADDRESS-RANGE_1_279",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "10.100.1.10",
  "ipv4-address-last": "10.100.1.30",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 1",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690065897,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690065247,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-address-range` ([0.07s])

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_1_279"
}
```
**Response:**
```json
{
  "uid": "bd92bcca-5c9d-45d1-9b91-e5a9e3d5808b",
  "name": "QA_ADDRESS-RANGE_1_279",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "10.100.1.10",
  "ipv4-address-last": "10.100.1.30",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 1",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690065897,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690065247,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-address-range` ([0.49s])

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_1_279"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[FAILED] Variant 2 (Total: 0.39s)</b></summary>

#### [FAILED] `add-address-range` ([0.39s])

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "name": "QA_ADDRESS-RANGE_2_700",
  "groups": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv6-address-first": "2001:db8:85a3::27cd",
  "ipv6-address-last": "2001:db8:85a3::1f88"
}
```
**Response:**
```json
{
  "code": "err_validation_failed",
  "message": "Validation failed with 1 blocking-error",
  "blocking-errors": [
    {
      "message": "Address range is not valid"
    }
  ]
}
```
**Errors found:**
- Address range is not valid

</details>

<details>
<summary><b>[PASSED] Variant 3 (Total: 1.08s)</b></summary>

#### [PASSED] `add-address-range` ([0.47s])

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "name": "QA_ADDRESS-RANGE_3_151",
  "set-if-exists": true,
  "color": "navy blue",
  "comments": "QA Automated Test Object",
  "details-level": "full",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv4-address-last": "10.100.1.30",
  "ipv4-address-first": "10.100.1.10"
}
```
**Response:**
```json
{
  "uid": "cc1a1a0f-eee9-473d-a212-02c13c2159b7",
  "name": "QA_ADDRESS-RANGE_3_151",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "10.100.1.10",
  "ipv4-address-last": "10.100.1.30",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "navy blue",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690066971,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690066971,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-address-range` ([0.13s])

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_3_151",
  "comments": "QA updated exhaustive variant 3",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "cc1a1a0f-eee9-473d-a212-02c13c2159b7",
  "name": "QA_ADDRESS-RANGE_3_151",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "10.100.1.10",
  "ipv4-address-last": "10.100.1.30",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 3",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690067449,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690066971,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_3_151"
}
```
**Response:**
```json
{
  "uid": "cc1a1a0f-eee9-473d-a212-02c13c2159b7",
  "name": "QA_ADDRESS-RANGE_3_151",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "10.100.1.10",
  "ipv4-address-last": "10.100.1.30",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 3",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690067449,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690066971,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-address-range` ([0.41s])

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_3_151"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 4 (Total: 1.04s)</b></summary>

#### [PASSED] `add-address-range` ([0.43s])

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "name": "QA_ADDRESS-RANGE_4_902",
  "set-if-exists": true,
  "color": "navy blue",
  "comments": "QA Automated Test Object",
  "details-level": "full",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv6-address-last": "2001:db8:85a3::17a8",
  "ipv6-address-first": "2001:db8:85a3::13fc"
}
```
**Response:**
```json
{
  "uid": "c94d7c4c-0ec1-4715-84f9-a416285586ae",
  "name": "QA_ADDRESS-RANGE_4_902",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address-first": "2001:db8:85a3::13fc",
  "ipv6-address-last": "2001:db8:85a3::17a8",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "navy blue",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690068066,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690068066,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-address-range` ([0.10s])

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_4_902",
  "comments": "QA updated exhaustive variant 4",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "c94d7c4c-0ec1-4715-84f9-a416285586ae",
  "name": "QA_ADDRESS-RANGE_4_902",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address-first": "2001:db8:85a3::13fc",
  "ipv6-address-last": "2001:db8:85a3::17a8",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 4",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690068506,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690068066,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-address-range` ([0.07s])

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_4_902"
}
```
**Response:**
```json
{
  "uid": "c94d7c4c-0ec1-4715-84f9-a416285586ae",
  "name": "QA_ADDRESS-RANGE_4_902",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address-first": "2001:db8:85a3::13fc",
  "ipv6-address-last": "2001:db8:85a3::17a8",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 4",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690068506,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690068066,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-address-range` ([0.43s])

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_4_902"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

---
## multicast-address-range

<details>
<summary><b>[PASSED] Variant 1 (Total: 0.44s)</b></summary>

#### [PASSED] `add-multicast-address-range` ([0.18s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_173",
  "set-if-exists": true,
  "color": "dark green",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv4-address": "224.0.1.20"
}
```
**Response:**
```json
{
  "uid": "ea40864f-72b8-4ed4-9b97-503c31fb0cc9",
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_173",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.20",
  "ipv4-address-last": "224.0.1.20",
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "dark green",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690069643,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690069643,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_173",
  "comments": "QA updated exhaustive variant 1",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "ea40864f-72b8-4ed4-9b97-503c31fb0cc9",
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_173",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.20",
  "ipv4-address-last": "224.0.1.20",
  "groups": [],
  "comments": "QA updated exhaustive variant 1",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690069819,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690069643,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_173"
}
```
**Response:**
```json
{
  "uid": "ea40864f-72b8-4ed4-9b97-503c31fb0cc9",
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_173",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.20",
  "ipv4-address-last": "224.0.1.20",
  "groups": [],
  "comments": "QA updated exhaustive variant 1",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690069819,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690069643,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-multicast-address-range` ([0.10s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_173"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 2 (Total: 0.37s)</b></summary>

#### [PASSED] `add-multicast-address-range` ([0.10s])

**Payload:**
```json
{
  "ip-address-first": "224.0.1.10",
  "ip-address-last": "224.0.1.30",
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_201",
  "set-if-exists": true,
  "color": "dark green",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv6-address": "ff05::1:10"
}
```
**Response:**
```json
{
  "uid": "907dd0e0-2e67-435b-8bf1-6bba72019156",
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_201",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.10",
  "ipv6-address-first": "ff05::1:10",
  "ipv4-address-last": "224.0.1.30",
  "ipv6-address-last": "ff05::1:10",
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "dark green",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690070158,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690070158,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_201",
  "comments": "QA updated exhaustive variant 2",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "907dd0e0-2e67-435b-8bf1-6bba72019156",
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_201",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.10",
  "ipv6-address-first": "ff05::1:10",
  "ipv4-address-last": "224.0.1.30",
  "ipv6-address-last": "ff05::1:10",
  "groups": [],
  "comments": "QA updated exhaustive variant 2",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690070253,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690070158,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-multicast-address-range` ([0.07s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_201"
}
```
**Response:**
```json
{
  "uid": "907dd0e0-2e67-435b-8bf1-6bba72019156",
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_201",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.10",
  "ipv6-address-first": "ff05::1:10",
  "ipv4-address-last": "224.0.1.30",
  "ipv6-address-last": "ff05::1:10",
  "groups": [],
  "comments": "QA updated exhaustive variant 2",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690070253,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690070158,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-multicast-address-range` ([0.12s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_201"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 3 (Total: 0.38s)</b></summary>

#### [PASSED] `add-multicast-address-range` ([0.14s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_282",
  "set-if-exists": true,
  "color": "dark green",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv4-address-first": "224.0.1.10",
  "ipv4-address-last": "224.0.1.30"
}
```
**Response:**
```json
{
  "uid": "c15e9bd6-9abb-41c5-aa9a-088534663da7",
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_282",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.10",
  "ipv4-address-last": "224.0.1.30",
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "dark green",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690070588,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690070588,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-multicast-address-range` ([0.09s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_282",
  "comments": "QA updated exhaustive variant 3",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "c15e9bd6-9abb-41c5-aa9a-088534663da7",
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_282",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.10",
  "ipv4-address-last": "224.0.1.30",
  "groups": [],
  "comments": "QA updated exhaustive variant 3",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690070669,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690070588,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-multicast-address-range` ([0.07s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_282"
}
```
**Response:**
```json
{
  "uid": "c15e9bd6-9abb-41c5-aa9a-088534663da7",
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_282",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.10",
  "ipv4-address-last": "224.0.1.30",
  "groups": [],
  "comments": "QA updated exhaustive variant 3",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690070669,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690070588,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_282"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 4 (Total: 0.32s)</b></summary>

#### [PASSED] `add-multicast-address-range` ([0.09s])

**Payload:**
```json
{
  "ip-address": "224.0.1.20",
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_966",
  "set-if-exists": true,
  "color": "dark green",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv6-address-first": "ff05::1:1",
  "ipv6-address-last": "ff05::1:30"
}
```
**Response:**
```json
{
  "uid": "ac1ad699-124d-4493-9e68-4696dc500ab0",
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_966",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.20",
  "ipv6-address-first": "ff05::1:1",
  "ipv4-address-last": "224.0.1.20",
  "ipv6-address-last": "ff05::1:30",
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "dark green",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690070927,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690070927,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_966",
  "comments": "QA updated exhaustive variant 4",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "ac1ad699-124d-4493-9e68-4696dc500ab0",
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_966",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.20",
  "ipv6-address-first": "ff05::1:1",
  "ipv4-address-last": "224.0.1.20",
  "ipv6-address-last": "ff05::1:30",
  "groups": [],
  "comments": "QA updated exhaustive variant 4",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690071005,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690070927,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-multicast-address-range` ([0.07s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_966"
}
```
**Response:**
```json
{
  "uid": "ac1ad699-124d-4493-9e68-4696dc500ab0",
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_966",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.20",
  "ipv6-address-first": "ff05::1:1",
  "ipv4-address-last": "224.0.1.20",
  "ipv6-address-last": "ff05::1:30",
  "groups": [],
  "comments": "QA updated exhaustive variant 4",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690071005,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690070927,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-multicast-address-range` ([0.09s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_966"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 5 (Total: 0.38s)</b></summary>

#### [PASSED] `add-multicast-address-range` ([0.14s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_494",
  "set-if-exists": true,
  "color": "dark green",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv4-address-last": "224.0.1.30",
  "ipv4-address-first": "224.0.1.10"
}
```
**Response:**
```json
{
  "uid": "41d9234a-b19a-4ec1-9855-a046857f4c34",
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_494",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.10",
  "ipv4-address-last": "224.0.1.30",
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "dark green",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690071318,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690071318,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_494",
  "comments": "QA updated exhaustive variant 5",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "41d9234a-b19a-4ec1-9855-a046857f4c34",
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_494",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.10",
  "ipv4-address-last": "224.0.1.30",
  "groups": [],
  "comments": "QA updated exhaustive variant 5",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690071395,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690071318,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_494"
}
```
**Response:**
```json
{
  "uid": "41d9234a-b19a-4ec1-9855-a046857f4c34",
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_494",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.10",
  "ipv4-address-last": "224.0.1.30",
  "groups": [],
  "comments": "QA updated exhaustive variant 5",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690071395,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690071318,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_494"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

<details>
<summary><b>[PASSED] Variant 6 (Total: 0.35s)</b></summary>

#### [PASSED] `add-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "ip-address": "224.0.1.20",
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_977",
  "set-if-exists": true,
  "color": "dark green",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv6-address-last": "ff05::1:30",
  "ipv6-address-first": "ff05::1:1"
}
```
**Response:**
```json
{
  "uid": "5d796c56-2851-4444-b0cc-bd7eed1ead5d",
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_977",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.20",
  "ipv6-address-first": "ff05::1:1",
  "ipv4-address-last": "224.0.1.20",
  "ipv6-address-last": "ff05::1:30",
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "dark green",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690071647,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690071647,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-multicast-address-range` ([0.08s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_977",
  "comments": "QA updated exhaustive variant 6",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "5d796c56-2851-4444-b0cc-bd7eed1ead5d",
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_977",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.20",
  "ipv6-address-first": "ff05::1:1",
  "ipv4-address-last": "224.0.1.20",
  "ipv6-address-last": "ff05::1:30",
  "groups": [],
  "comments": "QA updated exhaustive variant 6",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690071728,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690071647,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-multicast-address-range` ([0.07s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_977"
}
```
**Response:**
```json
{
  "uid": "5d796c56-2851-4444-b0cc-bd7eed1ead5d",
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_977",
  "type": "multicast-address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address-first": "224.0.1.20",
  "ipv6-address-first": "ff05::1:1",
  "ipv4-address-last": "224.0.1.20",
  "ipv6-address-last": "ff05::1:30",
  "groups": [],
  "comments": "QA updated exhaustive variant 6",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690071728,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690071647,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-multicast-address-range` ([0.11s])

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_977"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

---
## group-with-exclusion

<details>
<summary><b>[PASSED] Variant 0 (Total: 0.71s)</b></summary>

#### [PASSED] `add-group-with-exclusion` ([0.30s])

**Payload:**
```json
{
  "name": "QA_GROUP-WITH-EXCLUSION_0_375",
  "except": "QA_HELPER_EXCEPT_3294",
  "include": "QA_HELPER_INCLUDE_7777",
  "color": "dark orange",
  "comments": "QA Automated Test Object",
  "details-level": "uid",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true
}
```
**Response:**
```json
{
  "uid": "8ded5b36-a781-4371-b2b8-5416532314a3",
  "name": "QA_GROUP-WITH-EXCLUSION_0_375",
  "type": "group-with-exclusion",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "include": "5edd2a8a-e10e-49e7-ba54-6a688351e98c",
  "except": "a6fdf16e-d3d2-4318-90df-ccbb57de84b6",
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "dark orange",
  "icon": "General/group",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690073484,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690073484,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-group-with-exclusion` ([0.10s])

**Payload:**
```json
{
  "name": "QA_GROUP-WITH-EXCLUSION_0_375",
  "comments": "QA updated exhaustive variant 0",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "8ded5b36-a781-4371-b2b8-5416532314a3",
  "name": "QA_GROUP-WITH-EXCLUSION_0_375",
  "type": "group-with-exclusion",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "include": {
    "uid": "5edd2a8a-e10e-49e7-ba54-6a688351e98c",
    "name": "QA_HELPER_INCLUDE_7777",
    "type": "group",
    "domain": {
      "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
      "name": "SMC User",
      "domain-type": "domain"
    },
    "icon": "General/group",
    "color": "black"
  },
  "except": {
    "uid": "a6fdf16e-d3d2-4318-90df-ccbb57de84b6",
    "name": "QA_HELPER_EXCEPT_3294",
    "type": "group",
    "domain": {
      "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
      "name": "SMC User",
      "domain-type": "domain"
    },
    "icon": "General/group",
    "color": "black"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "General/group",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690073677,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690073484,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-group-with-exclusion` ([0.16s])

**Payload:**
```json
{
  "name": "QA_GROUP-WITH-EXCLUSION_0_375"
}
```
**Response:**
```json
{
  "uid": "8ded5b36-a781-4371-b2b8-5416532314a3",
  "name": "QA_GROUP-WITH-EXCLUSION_0_375",
  "type": "group-with-exclusion",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "include": {
    "uid": "5edd2a8a-e10e-49e7-ba54-6a688351e98c",
    "name": "QA_HELPER_INCLUDE_7777",
    "type": "group",
    "domain": {
      "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
      "name": "SMC User",
      "domain-type": "domain"
    },
    "members": [],
    "groups": [],
    "comments": "",
    "color": "black",
    "icon": "General/group",
    "tags": [],
    "meta-info": {
      "lock": "locked by current session",
      "validation-state": "ok",
      "last-modify-time": {
        "posix": 1770690071993,
        "iso-8601": "2026-02-09T21:21-0500"
      },
      "last-modifier": "admin",
      "creation-time": {
        "posix": 1770690071993,
        "iso-8601": "2026-02-09T21:21-0500"
      },
      "creator": "admin"
    },
    "read-only": false,
    "available-actions": {
      "edit": "true",
      "delete": "true",
      "clone": "true"
    }
  },
  "except": {
    "uid": "a6fdf16e-d3d2-4318-90df-ccbb57de84b6",
    "name": "QA_HELPER_EXCEPT_3294",
    "type": "group",
    "domain": {
      "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
      "name": "SMC User",
      "domain-type": "domain"
    },
    "members": [],
    "groups": [],
    "comments": "",
    "color": "black",
    "icon": "General/group",
    "tags": [],
    "meta-info": {
      "lock": "locked by current session",
      "validation-state": "ok",
      "last-modify-time": {
        "posix": 1770690073267,
        "iso-8601": "2026-02-09T21:21-0500"
      },
      "last-modifier": "admin",
      "creation-time": {
        "posix": 1770690073267,
        "iso-8601": "2026-02-09T21:21-0500"
      },
      "creator": "admin"
    },
    "read-only": false,
    "available-actions": {
      "edit": "true",
      "delete": "true",
      "clone": "true"
    }
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "General/group",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690073677,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690073484,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-group-with-exclusion` ([0.15s])

**Payload:**
```json
{
  "name": "QA_GROUP-WITH-EXCLUSION_0_375"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

---
## dns-domain

<details>
<summary><b>[PASSED] Variant 0 (Total: 0.32s)</b></summary>

#### [PASSED] `add-dns-domain` ([0.07s])

**Payload:**
```json
{
  "name": ".qa-domain-0-353.example.com",
  "is-sub-domain": false,
  "color": "forest green",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true
}
```
**Response:**
```json
{
  "uid": "de686179-8a30-4719-a16f-ba479bda62db",
  "name": ".qa-domain-0-353.example.com",
  "type": "dns-domain",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "is-sub-domain": false,
  "comments": "QA Automated Test Object",
  "color": "forest green",
  "icon": "Objects/domain",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690074296,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690074296,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-dns-domain` ([0.09s])

**Payload:**
```json
{
  "name": ".qa-domain-0-353.example.com",
  "comments": "QA updated exhaustive variant 0",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "de686179-8a30-4719-a16f-ba479bda62db",
  "name": ".qa-domain-0-353.example.com",
  "type": "dns-domain",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "is-sub-domain": false,
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "Objects/domain",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690074387,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690074296,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-dns-domain` ([0.07s])

**Payload:**
```json
{
  "name": ".qa-domain-0-353.example.com"
}
```
**Response:**
```json
{
  "uid": "de686179-8a30-4719-a16f-ba479bda62db",
  "name": ".qa-domain-0-353.example.com",
  "type": "dns-domain",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "is-sub-domain": false,
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "Objects/domain",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690074387,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690074296,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-dns-domain` ([0.09s])

**Payload:**
```json
{
  "name": ".qa-domain-0-353.example.com"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>

---
## wildcard

<details>
<summary><b>[PASSED] Variant 0 (Total: 0.36s)</b></summary>

#### [PASSED] `add-wildcard` ([0.09s])

**Payload:**
```json
{
  "ipv4-address": "10.100.1.80",
  "ipv4-mask-wildcard": "10.100.1.115",
  "ipv6-address": "2001:db8:85a3::2de2",
  "ipv6-mask-wildcard": "2001:db8:85a3::1d87",
  "name": "QA_WILDCARD_0_949",
  "color": "magenta",
  "comments": "QA Automated Test Object",
  "details-level": "uid",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true
}
```
**Response:**
```json
{
  "uid": "edf9e584-bbf8-44e8-a464-7afa157e6b62",
  "name": "QA_WILDCARD_0_949",
  "type": "wildcard",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.80",
  "ipv6-address": "2001:db8:85a3::2de2",
  "ipv4-mask-wildcard": "10.100.1.115",
  "ipv6-mask-wildcard": "2001:db8:85a3::1d87",
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "magenta",
  "icon": "NetworkObjects/WildcardObject",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690074637,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690074637,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `set-wildcard` ([0.11s])

**Payload:**
```json
{
  "name": "QA_WILDCARD_0_949",
  "comments": "QA updated exhaustive variant 0",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "edf9e584-bbf8-44e8-a464-7afa157e6b62",
  "name": "QA_WILDCARD_0_949",
  "type": "wildcard",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.80",
  "ipv6-address": "2001:db8:85a3::2de2",
  "ipv4-mask-wildcard": "10.100.1.115",
  "ipv6-mask-wildcard": "2001:db8:85a3::1d87",
  "groups": [],
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "NetworkObjects/WildcardObject",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690074736,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690074637,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### [PASSED] `show-wildcard` ([0.07s])

**Payload:**
```json
{
  "name": "QA_WILDCARD_0_949"
}
```
**Response:**
```json
{
  "uid": "edf9e584-bbf8-44e8-a464-7afa157e6b62",
  "name": "QA_WILDCARD_0_949",
  "type": "wildcard",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.80",
  "ipv6-address": "2001:db8:85a3::2de2",
  "ipv4-mask-wildcard": "10.100.1.115",
  "ipv6-mask-wildcard": "2001:db8:85a3::1d87",
  "groups": [],
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "NetworkObjects/WildcardObject",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770690074736,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770690074637,
      "iso-8601": "2026-02-09T21:21-0500"
    },
    "creator": "admin"
  },
  "read-only": false,
  "available-actions": {
    "edit": "true",
    "delete": "true",
    "clone": "true"
  }
}
```

#### [PASSED] `delete-wildcard` ([0.09s])

**Payload:**
```json
{
  "name": "QA_WILDCARD_0_949"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>