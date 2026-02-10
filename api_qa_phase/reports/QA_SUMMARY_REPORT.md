# API QA Test Report
Generated: 2026-02-09 23:22:56

## Summary Table
| Object Type | Variant | Status | Attempts |
| :--- | :--- | :--- | :--- |
| host | 1 | [PASSED] | 1 |
| host | 2 | [PASSED] | 1 |
| network | 1 | [PASSED] | 2 |
| network | 2 | [PASSED] | 2 |
| network | 3 | [PASSED] | 1 |
| network | 4 | [PASSED] | 2 |
| network | 5 | [PASSED] | 2 |
| group | 0 | [PASSED] | 1 |
| address-range | 1 | [PASSED] | 1 |
| address-range | 2 | [PASSED] | 1 |
| address-range | 3 | [PASSED] | 1 |
| address-range | 4 | [FAILED] | 5 |
| multicast-address-range | 1 | [PASSED] | 2 |
| multicast-address-range | 2 | [PASSED] | 1 |
| multicast-address-range | 3 | [PASSED] | 2 |
| multicast-address-range | 4 | [PASSED] | 1 |
| multicast-address-range | 5 | [PASSED] | 2 |
| multicast-address-range | 6 | [PASSED] | 1 |
| group-with-exclusion | 0 | [PASSED] | 1 |
| dns-domain | 0 | [PASSED] | 1 |
| wildcard | 0 | [PASSED] | 1 |

---
## host

<details>
<summary><b>[PASSED] Variant 1</b></summary>

#### ✅ `add-host`

**Payload:**
```json
{
  "interfaces": [
    {
      "name": "QA_2569",
      "subnet": "10.100.0.0",
      "mask-length": 24,
      "color": "firebrick",
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
      "operating-system": "sparc solaris"
    }
  },
  "name": "QA_HOST_1_637",
  "set-if-exists": true,
  "color": "crete blue",
  "comments": "QA Automated Test Object",
  "details-level": "full",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv4-address": "10.100.1.95"
}
```
**Response:**
```json
{
  "uid": "4745c029-a1b5-42f0-b62b-0b28f6d7f2f0",
  "name": "QA_HOST_1_637",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.95",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "operating-system": "sparc solaris",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "083790c7-d212-4367-8de2-181d1df2eb12",
      "name": "QA_2569",
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
      "color": "firebrick",
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
  "color": "crete blue",
  "icon": "Objects/host",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689173876,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689173876,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-host`

**Payload:**
```json
{
  "name": "QA_HOST_1_637",
  "comments": "QA updated exhaustive variant 1",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "4745c029-a1b5-42f0-b62b-0b28f6d7f2f0",
  "name": "QA_HOST_1_637",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.95",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "additional-ports": [],
      "operating-system": "sparc solaris",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "083790c7-d212-4367-8de2-181d1df2eb12",
      "name": "QA_2569",
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
      "color": "firebrick",
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
      "posix": 1770689174215,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689173876,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-host`

**Payload:**
```json
{
  "name": "QA_HOST_1_637",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "4745c029-a1b5-42f0-b62b-0b28f6d7f2f0",
  "name": "QA_HOST_1_637",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.95",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "additional-ports": [],
      "operating-system": "sparc solaris",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "083790c7-d212-4367-8de2-181d1df2eb12",
      "name": "QA_2569",
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
      "color": "firebrick",
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
      "posix": 1770689174215,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689173876,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-host`

**Payload:**
```json
{
  "name": "QA_HOST_1_637"
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
<summary><b>[PASSED] Variant 2</b></summary>

#### ✅ `add-host`

**Payload:**
```json
{
  "interfaces": [
    {
      "name": "QA_2569",
      "subnet": "10.100.0.0",
      "mask-length": 24,
      "color": "firebrick",
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
      "operating-system": "sparc solaris"
    }
  },
  "name": "QA_HOST_2_384",
  "set-if-exists": true,
  "color": "crete blue",
  "comments": "QA Automated Test Object",
  "details-level": "full",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv6-address": "2001:db8:85a3::30a5"
}
```
**Response:**
```json
{
  "uid": "ff81b50e-8b4e-4371-8819-4b2a2429df84",
  "name": "QA_HOST_2_384",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address": "2001:db8:85a3::30a5",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "operating-system": "sparc solaris",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "efcb21a5-e31e-4934-a3e3-2ae228fdb0bc",
      "name": "QA_2569",
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
      "color": "firebrick",
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
  "color": "crete blue",
  "icon": "Objects/host",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689174803,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689174803,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-host`

**Payload:**
```json
{
  "name": "QA_HOST_2_384",
  "comments": "QA updated exhaustive variant 2",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "ff81b50e-8b4e-4371-8819-4b2a2429df84",
  "name": "QA_HOST_2_384",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address": "2001:db8:85a3::30a5",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "additional-ports": [],
      "operating-system": "sparc solaris",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "efcb21a5-e31e-4934-a3e3-2ae228fdb0bc",
      "name": "QA_2569",
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
      "color": "firebrick",
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
      "posix": 1770689175155,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689174803,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-host`

**Payload:**
```json
{
  "name": "QA_HOST_2_384",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "ff81b50e-8b4e-4371-8819-4b2a2429df84",
  "name": "QA_HOST_2_384",
  "type": "host",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address": "2001:db8:85a3::30a5",
  "host-servers": {
    "web-server": true,
    "mail-server": false,
    "dns-server": false,
    "web-server-config": {
      "application-engines": [],
      "listen-standard-port": false,
      "additional-ports": [],
      "operating-system": "sparc solaris",
      "protected-by": "97aeb368-9aea-11d5-bd16-0090272ccb30"
    }
  },
  "interfaces": [
    {
      "uid": "efcb21a5-e31e-4934-a3e3-2ae228fdb0bc",
      "name": "QA_2569",
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
      "color": "firebrick",
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
      "posix": 1770689175155,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689174803,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-host`

**Payload:**
```json
{
  "name": "QA_HOST_2_384"
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
<summary><b>[PASSED] Variant 1 (Self-Healed in 2 attempts)</b></summary>

#### ✅ `add-network`

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "allow",
  "name": "QA_NETWORK_1_721",
  "set-if-exists": true,
  "color": "dark gold",
  "comments": "QA Automated Test Object",
  "details-level": "uid",
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
  "uid": "9df2ea3a-9830-46ed-965e-1cf5bc6d31c6",
  "name": "QA_NETWORK_1_721",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
  "color": "dark gold",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689177012,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689177012,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_1_721",
  "comments": "QA updated exhaustive variant 1",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "9df2ea3a-9830-46ed-965e-1cf5bc6d31c6",
  "name": "QA_NETWORK_1_721",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689177434,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689177012,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_1_721",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "9df2ea3a-9830-46ed-965e-1cf5bc6d31c6",
  "name": "QA_NETWORK_1_721",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689177434,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689177012,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_1_721"
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
<summary><b>[PASSED] Variant 2 (Self-Healed in 2 attempts)</b></summary>

#### ✅ `add-network`

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "allow",
  "name": "QA_NETWORK_2_134",
  "set-if-exists": true,
  "color": "dark gold",
  "comments": "QA Automated Test Object",
  "details-level": "uid",
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
  "uid": "2c63f557-b754-47ff-bad6-aaa7a8783d54",
  "name": "QA_NETWORK_2_134",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
  "color": "dark gold",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689178175,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689178175,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_2_134",
  "comments": "QA updated exhaustive variant 2",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "2c63f557-b754-47ff-bad6-aaa7a8783d54",
  "name": "QA_NETWORK_2_134",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689178580,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689178175,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_2_134",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "2c63f557-b754-47ff-bad6-aaa7a8783d54",
  "name": "QA_NETWORK_2_134",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689178580,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689178175,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_2_134"
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
<summary><b>[PASSED] Variant 3</b></summary>

#### ✅ `add-network`

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "allow",
  "name": "QA_NETWORK_3_450",
  "set-if-exists": true,
  "color": "dark gold",
  "comments": "QA Automated Test Object",
  "details-level": "uid",
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
  "uid": "f02a0280-549c-4e88-a1ed-7ef830e92f2f",
  "name": "QA_NETWORK_3_450",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
  "color": "dark gold",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689179113,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689179113,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_3_450",
  "comments": "QA updated exhaustive variant 3",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "f02a0280-549c-4e88-a1ed-7ef830e92f2f",
  "name": "QA_NETWORK_3_450",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689179616,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689179113,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_3_450",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "f02a0280-549c-4e88-a1ed-7ef830e92f2f",
  "name": "QA_NETWORK_3_450",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689179616,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689179113,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_3_450"
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
<summary><b>[PASSED] Variant 4 (Self-Healed in 2 attempts)</b></summary>

#### ✅ `add-network`

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "allow",
  "name": "QA_NETWORK_4_910",
  "set-if-exists": true,
  "color": "dark gold",
  "comments": "QA Automated Test Object",
  "details-level": "uid",
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
  "uid": "126a1f69-1839-45c1-8336-52c8c98ad03f",
  "name": "QA_NETWORK_4_910",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
  "color": "dark gold",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689181543,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689181543,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_4_910",
  "comments": "QA updated exhaustive variant 4",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "126a1f69-1839-45c1-8336-52c8c98ad03f",
  "name": "QA_NETWORK_4_910",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689182151,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689181543,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_4_910",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "126a1f69-1839-45c1-8336-52c8c98ad03f",
  "name": "QA_NETWORK_4_910",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689182151,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689181543,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_4_910"
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
<summary><b>[PASSED] Variant 5 (Self-Healed in 2 attempts)</b></summary>

#### ✅ `add-network`

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "broadcast": "allow",
  "name": "QA_NETWORK_5_561",
  "set-if-exists": true,
  "color": "dark gold",
  "comments": "QA Automated Test Object",
  "details-level": "uid",
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
  "uid": "54353714-fcbf-4bb3-a969-62f346903d60",
  "name": "QA_NETWORK_5_561",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
  "color": "dark gold",
  "icon": "NetworkObjects/network",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689182898,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689182898,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_5_561",
  "comments": "QA updated exhaustive variant 5",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "54353714-fcbf-4bb3-a969-62f346903d60",
  "name": "QA_NETWORK_5_561",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689183384,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689182898,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_5_561",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "54353714-fcbf-4bb3-a969-62f346903d60",
  "name": "QA_NETWORK_5_561",
  "type": "network",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "broadcast": "allow",
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
      "posix": 1770689183384,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689182898,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-network`

**Payload:**
```json
{
  "name": "QA_NETWORK_5_561"
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
<summary><b>[PASSED] Variant 0</b></summary>

#### ✅ `add-group`

**Payload:**
```json
{
  "members": [],
  "name": "QA_GROUP_0_752",
  "color": "gold",
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
  "uid": "1167c17d-a278-4afc-a1fc-e9511c3b4ac1",
  "name": "QA_GROUP_0_752",
  "type": "group",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "members": [],
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "gold",
  "icon": "General/group",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689183968,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689183968,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-group`

**Payload:**
```json
{
  "name": "QA_GROUP_0_752",
  "comments": "QA updated exhaustive variant 0",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "1167c17d-a278-4afc-a1fc-e9511c3b4ac1",
  "name": "QA_GROUP_0_752",
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
      "posix": 1770689184051,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689183968,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-group`

**Payload:**
```json
{
  "name": "QA_GROUP_0_752",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "1167c17d-a278-4afc-a1fc-e9511c3b4ac1",
  "name": "QA_GROUP_0_752",
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
      "posix": 1770689184051,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689183968,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-group`

**Payload:**
```json
{
  "name": "QA_GROUP_0_752"
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
<summary><b>[PASSED] Variant 1</b></summary>

#### ✅ `add-address-range`

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "name": "QA_ADDRESS-RANGE_1_341",
  "set-if-exists": true,
  "color": "orchid",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
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
  "uid": "34d80e56-4b2d-4c38-b275-eb10bdad03c9",
  "name": "QA_ADDRESS-RANGE_1_341",
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
  "color": "orchid",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689185545,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689185545,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-address-range`

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_1_341",
  "comments": "QA updated exhaustive variant 1",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "34d80e56-4b2d-4c38-b275-eb10bdad03c9",
  "name": "QA_ADDRESS-RANGE_1_341",
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
      "posix": 1770689186003,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689185545,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-address-range`

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_1_341",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "34d80e56-4b2d-4c38-b275-eb10bdad03c9",
  "name": "QA_ADDRESS-RANGE_1_341",
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
      "posix": 1770689186003,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689185545,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-address-range`

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_1_341"
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
<summary><b>[PASSED] Variant 2</b></summary>

#### ✅ `add-address-range`

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "name": "QA_ADDRESS-RANGE_2_882",
  "set-if-exists": true,
  "color": "orchid",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv6-address-first": "2001:db8:85a3::1214",
  "ipv6-address-last": "2001:db8:85a3::265e"
}
```
**Response:**
```json
{
  "uid": "eced9d5f-4353-4d35-9002-f901237a2f39",
  "name": "QA_ADDRESS-RANGE_2_882",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address-first": "2001:db8:85a3::1214",
  "ipv6-address-last": "2001:db8:85a3::265e",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "orchid",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689186536,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689186536,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-address-range`

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_2_882",
  "comments": "QA updated exhaustive variant 2",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "eced9d5f-4353-4d35-9002-f901237a2f39",
  "name": "QA_ADDRESS-RANGE_2_882",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address-first": "2001:db8:85a3::1214",
  "ipv6-address-last": "2001:db8:85a3::265e",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 2",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689186982,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689186536,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-address-range`

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_2_882",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "eced9d5f-4353-4d35-9002-f901237a2f39",
  "name": "QA_ADDRESS-RANGE_2_882",
  "type": "address-range",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv6-address-first": "2001:db8:85a3::1214",
  "ipv6-address-last": "2001:db8:85a3::265e",
  "nat-settings": {
    "auto-rule": true,
    "hide-behind": "gateway",
    "install-on": "All",
    "method": "hide"
  },
  "groups": [],
  "comments": "QA updated exhaustive variant 2",
  "color": "orange",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689186982,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689186536,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-address-range`

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_2_882"
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
<summary><b>[PASSED] Variant 3</b></summary>

#### ✅ `add-address-range`

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "name": "QA_ADDRESS-RANGE_3_882",
  "set-if-exists": true,
  "color": "orchid",
  "comments": "QA Automated Test Object",
  "details-level": "standard",
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
  "uid": "98597320-6180-41f4-bb42-d8ca332ea3d9",
  "name": "QA_ADDRESS-RANGE_3_882",
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
  "color": "orchid",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689187626,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689187626,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-address-range`

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_3_882",
  "comments": "QA updated exhaustive variant 3",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "98597320-6180-41f4-bb42-d8ca332ea3d9",
  "name": "QA_ADDRESS-RANGE_3_882",
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
      "posix": 1770689188184,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689187626,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-address-range`

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_3_882",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "98597320-6180-41f4-bb42-d8ca332ea3d9",
  "name": "QA_ADDRESS-RANGE_3_882",
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
      "posix": 1770689188184,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689187626,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-address-range`

**Payload:**
```json
{
  "name": "QA_ADDRESS-RANGE_3_882"
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
<summary><b>[FAILED] Variant 4 (Self-Healed in 5 attempts)</b></summary>

#### ❌ `add-address-range`

**Payload:**
```json
{
  "nat-settings": {
    "auto-rule": "true",
    "method": "hide",
    "hide-behind": "gateway"
  },
  "name": "QA_ADDRESS-RANGE_4_331",
  "groups": [],
  "ignore-warnings": true,
  "ignore-errors": true,
  "ipv6-address-last": "2001:db8:85a3::1ea7",
  "ipv6-address-first": "2001:db8:85a3::2dc9"
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

---
## multicast-address-range

<details>
<summary><b>[PASSED] Variant 1 (Self-Healed in 2 attempts)</b></summary>

#### ✅ `add-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_124",
  "set-if-exists": true,
  "color": "magenta",
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
  "uid": "a4a330b4-2f8d-4955-8b1c-f925401ac89d",
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_124",
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
  "color": "magenta",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689189659,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689189659,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_124",
  "comments": "QA updated exhaustive variant 1",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "a4a330b4-2f8d-4955-8b1c-f925401ac89d",
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_124",
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
      "posix": 1770689189767,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689189659,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_124",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "a4a330b4-2f8d-4955-8b1c-f925401ac89d",
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_124",
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
      "posix": 1770689189767,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689189659,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_1_124"
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
<summary><b>[PASSED] Variant 2</b></summary>

#### ✅ `add-multicast-address-range`

**Payload:**
```json
{
  "ip-address-first": "224.0.1.10",
  "ip-address-last": "224.0.1.30",
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_263",
  "set-if-exists": true,
  "color": "magenta",
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
  "uid": "48a97a84-c494-41e3-9c1a-4770762e78ef",
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_263",
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
  "color": "magenta",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689190005,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689190005,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_263",
  "comments": "QA updated exhaustive variant 2",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "48a97a84-c494-41e3-9c1a-4770762e78ef",
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_263",
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
      "posix": 1770689190093,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689190005,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_263",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "48a97a84-c494-41e3-9c1a-4770762e78ef",
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_263",
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
      "posix": 1770689190093,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689190005,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_2_263"
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
<summary><b>[PASSED] Variant 3 (Self-Healed in 2 attempts)</b></summary>

#### ✅ `add-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_956",
  "set-if-exists": true,
  "color": "magenta",
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
  "uid": "8793a806-db41-4513-98fb-552e48d18dba",
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_956",
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
  "color": "magenta",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689192187,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689192187,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_956",
  "comments": "QA updated exhaustive variant 3",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "8793a806-db41-4513-98fb-552e48d18dba",
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_956",
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
      "posix": 1770689192289,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689192187,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_956",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "8793a806-db41-4513-98fb-552e48d18dba",
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_956",
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
      "posix": 1770689192289,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689192187,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_3_956"
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
<summary><b>[PASSED] Variant 4</b></summary>

#### ✅ `add-multicast-address-range`

**Payload:**
```json
{
  "ip-address": "224.0.1.20",
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_913",
  "set-if-exists": true,
  "color": "magenta",
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
  "uid": "d857e15a-191f-4f42-b4ad-75c5fc12735e",
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_913",
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
  "color": "magenta",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689192530,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689192530,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_913",
  "comments": "QA updated exhaustive variant 4",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "d857e15a-191f-4f42-b4ad-75c5fc12735e",
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_913",
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
      "posix": 1770689192617,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689192530,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_913",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "d857e15a-191f-4f42-b4ad-75c5fc12735e",
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_913",
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
      "posix": 1770689192617,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689192530,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_4_913"
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
<summary><b>[PASSED] Variant 5 (Self-Healed in 2 attempts)</b></summary>

#### ✅ `add-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_442",
  "set-if-exists": true,
  "color": "magenta",
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
  "uid": "5831a973-e487-4a33-8785-f058f9246306",
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_442",
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
  "color": "magenta",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689192978,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689192978,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_442",
  "comments": "QA updated exhaustive variant 5",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "5831a973-e487-4a33-8785-f058f9246306",
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_442",
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
      "posix": 1770689193063,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689192978,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_442",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "5831a973-e487-4a33-8785-f058f9246306",
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_442",
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
      "posix": 1770689193063,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689192978,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_5_442"
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
<summary><b>[PASSED] Variant 6</b></summary>

#### ✅ `add-multicast-address-range`

**Payload:**
```json
{
  "ip-address": "224.0.1.20",
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_995",
  "set-if-exists": true,
  "color": "magenta",
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
  "uid": "0e658354-a7b1-4492-baf6-6b61a9250c67",
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_995",
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
  "color": "magenta",
  "icon": "Objects/ip",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689193323,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689193323,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_995",
  "comments": "QA updated exhaustive variant 6",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "0e658354-a7b1-4492-baf6-6b61a9250c67",
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_995",
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
      "posix": 1770689193408,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689193323,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_995",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "0e658354-a7b1-4492-baf6-6b61a9250c67",
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_995",
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
      "posix": 1770689193408,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689193323,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-multicast-address-range`

**Payload:**
```json
{
  "name": "QA_MULTICAST-ADDRESS-RANGE_6_995"
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
<summary><b>[PASSED] Variant 0</b></summary>

#### ✅ `add-group-with-exclusion`

**Payload:**
```json
{
  "name": "QA_GROUP-WITH-EXCLUSION_0_519",
  "except": "QA_HELPER_EXCEPT_2980",
  "include": "QA_HELPER_INCLUDE_6038",
  "color": "magenta",
  "comments": "QA Automated Test Object",
  "details-level": "full",
  "groups": [],
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true
}
```
**Response:**
```json
{
  "uid": "684319f8-5b69-485b-a060-39a4f47d4657",
  "name": "QA_GROUP-WITH-EXCLUSION_0_519",
  "type": "group-with-exclusion",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "include": {
    "uid": "8084acc8-a47b-4c84-a976-db9e636c8cfe",
    "name": "QA_HELPER_INCLUDE_6038",
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
        "posix": 1770689193668,
        "iso-8601": "2026-02-09T21:06-0500"
      },
      "last-modifier": "admin",
      "creation-time": {
        "posix": 1770689193668,
        "iso-8601": "2026-02-09T21:06-0500"
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
    "uid": "cd6a9fef-3e6a-4a87-bc2d-db15c41c3f0e",
    "name": "QA_HELPER_EXCEPT_2980",
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
        "posix": 1770689193758,
        "iso-8601": "2026-02-09T21:06-0500"
      },
      "last-modifier": "admin",
      "creation-time": {
        "posix": 1770689193758,
        "iso-8601": "2026-02-09T21:06-0500"
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
  "comments": "QA Automated Test Object",
  "color": "magenta",
  "icon": "General/group",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689193957,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689193957,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-group-with-exclusion`

**Payload:**
```json
{
  "name": "QA_GROUP-WITH-EXCLUSION_0_519",
  "comments": "QA updated exhaustive variant 0",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "684319f8-5b69-485b-a060-39a4f47d4657",
  "name": "QA_GROUP-WITH-EXCLUSION_0_519",
  "type": "group-with-exclusion",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "include": {
    "uid": "8084acc8-a47b-4c84-a976-db9e636c8cfe",
    "name": "QA_HELPER_INCLUDE_6038",
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
    "uid": "cd6a9fef-3e6a-4a87-bc2d-db15c41c3f0e",
    "name": "QA_HELPER_EXCEPT_2980",
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
      "posix": 1770689194250,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689193957,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-group-with-exclusion`

**Payload:**
```json
{
  "name": "QA_GROUP-WITH-EXCLUSION_0_519",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "684319f8-5b69-485b-a060-39a4f47d4657",
  "name": "QA_GROUP-WITH-EXCLUSION_0_519",
  "type": "group-with-exclusion",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "include": {
    "uid": "8084acc8-a47b-4c84-a976-db9e636c8cfe",
    "name": "QA_HELPER_INCLUDE_6038",
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
        "posix": 1770689193668,
        "iso-8601": "2026-02-09T21:06-0500"
      },
      "last-modifier": "admin",
      "creation-time": {
        "posix": 1770689193668,
        "iso-8601": "2026-02-09T21:06-0500"
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
    "uid": "cd6a9fef-3e6a-4a87-bc2d-db15c41c3f0e",
    "name": "QA_HELPER_EXCEPT_2980",
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
        "posix": 1770689193758,
        "iso-8601": "2026-02-09T21:06-0500"
      },
      "last-modifier": "admin",
      "creation-time": {
        "posix": 1770689193758,
        "iso-8601": "2026-02-09T21:06-0500"
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
      "posix": 1770689194250,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689193957,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-group-with-exclusion`

**Payload:**
```json
{
  "name": "QA_GROUP-WITH-EXCLUSION_0_519"
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
<summary><b>[PASSED] Variant 0</b></summary>

#### ✅ `add-dns-domain`

**Payload:**
```json
{
  "name": ".qa-domain-0-502.example.com",
  "is-sub-domain": false,
  "color": "light green",
  "comments": "QA Automated Test Object",
  "details-level": "full",
  "tags": [],
  "ignore-warnings": true,
  "ignore-errors": true
}
```
**Response:**
```json
{
  "uid": "a0e38137-e9e7-428d-a94b-201497c57d0c",
  "name": ".qa-domain-0-502.example.com",
  "type": "dns-domain",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "is-sub-domain": false,
  "comments": "QA Automated Test Object",
  "color": "light green",
  "icon": "Objects/domain",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689194848,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689194848,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-dns-domain`

**Payload:**
```json
{
  "name": ".qa-domain-0-502.example.com",
  "comments": "QA updated exhaustive variant 0",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "a0e38137-e9e7-428d-a94b-201497c57d0c",
  "name": ".qa-domain-0-502.example.com",
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
      "posix": 1770689194935,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689194848,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-dns-domain`

**Payload:**
```json
{
  "name": ".qa-domain-0-502.example.com",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "a0e38137-e9e7-428d-a94b-201497c57d0c",
  "name": ".qa-domain-0-502.example.com",
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
      "posix": 1770689194935,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689194848,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-dns-domain`

**Payload:**
```json
{
  "name": ".qa-domain-0-502.example.com"
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
<summary><b>[PASSED] Variant 0</b></summary>

#### ✅ `add-wildcard`

**Payload:**
```json
{
  "ipv4-address": "10.100.1.35",
  "ipv4-mask-wildcard": "10.100.1.61",
  "ipv6-address": "2001:db8:85a3::3df7",
  "ipv6-mask-wildcard": "2001:db8:85a3::389c",
  "name": "QA_WILDCARD_0_338",
  "color": "cyan",
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
  "uid": "41b64793-2d1d-457f-ac70-356ec1da4c14",
  "name": "QA_WILDCARD_0_338",
  "type": "wildcard",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.35",
  "ipv6-address": "2001:db8:85a3::3df7",
  "ipv4-mask-wildcard": "10.100.1.61",
  "ipv6-mask-wildcard": "2001:db8:85a3::389c",
  "groups": [],
  "comments": "QA Automated Test Object",
  "color": "cyan",
  "icon": "NetworkObjects/WildcardObject",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689195220,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689195220,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `set-wildcard`

**Payload:**
```json
{
  "name": "QA_WILDCARD_0_338",
  "comments": "QA updated exhaustive variant 0",
  "color": "orange"
}
```
**Response:**
```json
{
  "uid": "41b64793-2d1d-457f-ac70-356ec1da4c14",
  "name": "QA_WILDCARD_0_338",
  "type": "wildcard",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.35",
  "ipv6-address": "2001:db8:85a3::3df7",
  "ipv4-mask-wildcard": "10.100.1.61",
  "ipv6-mask-wildcard": "2001:db8:85a3::389c",
  "groups": [],
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "NetworkObjects/WildcardObject",
  "tags": [],
  "meta-info": {
    "lock": "unlocked",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689195336,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689195220,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "creator": "admin"
  },
  "read-only": true,
  "available-actions": {}
}
```

#### ✅ `show-wildcard`

**Payload:**
```json
{
  "name": "QA_WILDCARD_0_338",
  "details-level": "full"
}
```
**Response:**
```json
{
  "uid": "41b64793-2d1d-457f-ac70-356ec1da4c14",
  "name": "QA_WILDCARD_0_338",
  "type": "wildcard",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "ipv4-address": "10.100.1.35",
  "ipv6-address": "2001:db8:85a3::3df7",
  "ipv4-mask-wildcard": "10.100.1.61",
  "ipv6-mask-wildcard": "2001:db8:85a3::389c",
  "groups": [],
  "comments": "QA updated exhaustive variant 0",
  "color": "orange",
  "icon": "NetworkObjects/WildcardObject",
  "tags": [],
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1770689195336,
      "iso-8601": "2026-02-09T21:06-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1770689195220,
      "iso-8601": "2026-02-09T21:06-0500"
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

#### ✅ `delete-wildcard`

**Payload:**
```json
{
  "name": "QA_WILDCARD_0_338"
}
```
**Response:**
```json
{
  "message": "OK"
}
```

</details>