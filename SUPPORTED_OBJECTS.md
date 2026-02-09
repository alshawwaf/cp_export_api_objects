# Check Point Object Export Support Guide
Based on API v2.0.1 (R82) and verified current tool configuration.

## Fully Supported Objects
The following objects are fully supported. The tool exports all available configuration fields defined in the API v2.1 specification, including complex nested objects and extended settings.

| Object Type | API Command | Notes |
|---|---|---|
| `access-layer` | `add-access-layer` | Full Field Export |
| `access-role` | `add-access-role` | Full Field Export |
| `address-range` | `add-address-range` | Full Field Export |
| `application-site` | `add-application-site` | Full Field Export |
| `application-site-category` | `add-application-site-category` | Full Field Export |
| `application-site-group` | `add-application-site-group` | Full Field Export |
| `dns-domain` | `add-dns-domain` | Full Field Export |
| `dynamic-object` | `add-dynamic-object` | Full Field Export |
| `group` | `add-group` | Full Field Export |
| `group-with-exclusion` | `add-group-with-exclusion` | Full Field Export |
| `host` | `add-host` | Full Field Export |
| `multicast-address-range` | `add-multicast-address-range` | Full Field Export |
| `network` | `add-network` | Full Field Export |
| `network-feed` | `add-network-feed` | Full Field Export |
| `opsec-application` | `add-opsec-application` | Full Field Export |
| `security-zone` | `add-security-zone` | Full Field Export |
| `service-dce-rpc` | `add-service-dce-rpc` | Full Field Export |
| `service-group` | `add-service-group` | Full Field Export |
| `service-icmp` | `add-service-icmp` | Full Field Export |
| `service-icmp6` | `add-service-icmp6` | Full Field Export |
| `service-other` | `add-service-other` | Full Field Export |
| `service-rpc` | `add-service-rpc` | Full Field Export |
| `service-sctp` | `add-service-sctp` | Full Field Export |
| `service-tcp` | `add-service-tcp` | Full Field Export |
| `service-udp` | `add-service-udp` | Full Field Export |
| `simple-cluster` | `add-simple-cluster` | Full Field Export |
| `simple-gateway` | `add-simple-gateway` | Full Field Export |
| `tag` | `add-tag` | Full Field Export |
| `time` | `add-time` | Full Field Export |
| `time-group` | `add-time-group` | Full Field Export |
| `vpn-community-meshed` | `add-vpn-community-meshed` | Full Field Export |
| `vpn-community-star` | `add-vpn-community-star` | Full Field Export |
| `wildcard` | `add-wildcard` | Full Field Export |

## Not Supported / Ignored Objects
The following objects are defined in the R82 API but are currently excluded from the export process. Some are operational commands (like `run-script`) or explicit ignore targets.

| Object Type | Status | API Command |
|---|---|---|
| `access-point-name` | Not Implemented | `add-access-point-name` |
| `access-rule` | Ignored | `add-access-rule` |
| `access-section` | Not Implemented | `add-access-section` |
| `administrator` | Ignored | `add-administrator` |
| `api-key` | Not Implemented | `add-api-key` |
| `azure-ad` | Not Implemented | `add-azure-ad` |
| `central-license` | Not Implemented | `add-central-license` |
| `checkpoint-host` | Not Implemented | `add-checkpoint-host` |
| `client-login-option` | Not Implemented | `add-client-login-option` |
| `custom-trusted-ca-certificate` | Not Implemented | `add-custom-trusted-ca-certificate` |
| `data-center-object` | Not Implemented | `add-data-center-object` |
| `data-center-query` | Not Implemented | `add-data-center-query` |
| `data-center-server` | Not Implemented | `add-data-center-server` |
| `data-type-compound-group` | Not Implemented | `add-data-type-compound-group` |
| `data-type-file-attributes` | Not Implemented | `add-data-type-file-attributes` |
| `data-type-group` | Not Implemented | `add-data-type-group` |
| `data-type-keywords` | Not Implemented | `add-data-type-keywords` |
| `data-type-patterns` | Not Implemented | `add-data-type-patterns` |
| `data-type-traditional-group` | Not Implemented | `add-data-type-traditional-group` |
| `data-type-weighted-keywords` | Not Implemented | `add-data-type-weighted-keywords` |
| `domain` | Not Implemented | `add-domain` |
| `domain-permissions-profile` | Not Implemented | `add-domain-permissions-profile` |
| `dynamic-global-network-object` | Not Implemented | `add-dynamic-global-network-object` |
| `exception-group` | Ignored | `add-exception-group` |
| `external-trusted-ca` | Not Implemented | `add-external-trusted-ca` |
| `gaia-best-practice` | Not Implemented | `add-gaia-best-practice` |
| `generic-object` | Not Implemented | `add-generic-object` |
| `global-assignment` | Ignored | `add-global-assignment` |
| `gsn-handover-group` | Not Implemented | `add-gsn-handover-group` |
| `https-layer` | Not Implemented | `add-https-layer` |
| `https-rule` | Not Implemented | `add-https-rule` |
| `https-section` | Not Implemented | `add-https-section` |
| `identity-provider` | Not Implemented | `add-identity-provider` |
| `identity-tag` | Ignored | `add-identity-tag` |
| `idp-administrator-group` | Not Implemented | `add-idp-administrator-group` |
| `if-map-server` | Not Implemented | `add-if-map-server` |
| `interface` | Not Implemented | `add-interface` |
| `interoperable-device` | Not Implemented | `add-interoperable-device` |
| `ldap-group` | Not Implemented | `add-ldap-group` |
| `limit` | Not Implemented | `add-limit` |
| `log-exporter` | Not Implemented | `add-log-exporter` |
| `logical-server` | Not Implemented | `add-logical-server` |
| `lsm-cluster` | Not Implemented | `add-lsm-cluster` |
| `lsm-gateway` | Not Implemented | `add-lsm-gateway` |
| `lsv-profile` | Not Implemented | `add-lsv-profile` |
| `md-permissions-profile` | Not Implemented | `add-md-permissions-profile` |
| `mds` | Ignored | `add-mds` |
| `mobile-access-profile-rule` | Not Implemented | `add-mobile-access-profile-rule` |
| `mobile-access-profile-section` | Not Implemented | `add-mobile-access-profile-section` |
| `mobile-access-rule` | Not Implemented | `add-mobile-access-rule` |
| `mobile-access-section` | Not Implemented | `add-mobile-access-section` |
| `mobile-profile` | Not Implemented | `add-mobile-profile` |
| `multiple-key-exchanges` | Not Implemented | `add-multiple-key-exchanges` |
| `nat-rule` | Not Implemented | `add-nat-rule` |
| `nat-section` | Not Implemented | `add-nat-section` |
| `network-probe` | Not Implemented | `add-network-probe` |
| `objects-batch` | Not Implemented | `add-objects-batch` |
| `opsec-trusted-ca` | Not Implemented | `add-opsec-trusted-ca` |
| `outbound-inspection-certificate` | Not Implemented | `add-outbound-inspection-certificate` |
| `override-categorization` | Not Implemented | `add-override-categorization` |
| `package` | Not Implemented | `add-package` |
| `passcode-profile` | Not Implemented | `add-passcode-profile` |
| `radius-group` | Not Implemented | `add-radius-group` |
| `radius-server` | Not Implemented | `add-radius-server` |
| `repository-package` | Not Implemented | `add-repository-package` |
| `repository-script` | Not Implemented | `add-repository-script` |
| `resource-cifs` | Not Implemented | `add-resource-cifs` |
| `resource-ftp` | Not Implemented | `add-resource-ftp` |
| `resource-mms` | Not Implemented | `add-resource-mms` |
| `resource-smtp` | Not Implemented | `add-resource-smtp` |
| `resource-tcp` | Not Implemented | `add-resource-tcp` |
| `resource-uri` | Not Implemented | `add-resource-uri` |
| `resource-uri-for-qos` | Not Implemented | `add-resource-uri-for-qos` |
| `rules-batch` | Not Implemented | `add-rules-batch` |
| `scada-application` | Not Implemented | `add-scada-application` |
| `securemote-dns-server` | Not Implemented | `add-securemote-dns-server` |
| `securid-server` | Not Implemented | `add-securid-server` |
| `server-certificate` | Not Implemented | `add-server-certificate` |
| `service-citrix-tcp` | Not Implemented | `add-service-citrix-tcp` |
| `service-compound-tcp` | Not Implemented | `add-service-compound-tcp` |
| `service-gtp` | Not Implemented | `add-service-gtp` |
| `smart-task` | Not Implemented | `add-smart-task` |
| `smtp-server` | Not Implemented | `add-smtp-server` |
| `subordinate-ca` | Not Implemented | `add-subordinate-ca` |
| `syslog-server` | Not Implemented | `add-syslog-server` |
| `tacacs-group` | Not Implemented | `add-tacacs-group` |
| `tacacs-server` | Not Implemented | `add-tacacs-server` |
| `threat-exception` | Ignored | `add-threat-exception` |
| `threat-indicator` | Ignored | `add-threat-indicator` |
| `threat-ioc-feed` | Not Implemented | `add-threat-ioc-feed` |
| `threat-layer` | Ignored | `add-threat-layer` |
| `threat-profile` | Ignored | `add-threat-profile` |
| `threat-protections` | Not Implemented | `add-threat-protections` |
| `threat-rule` | Ignored | `add-threat-rule` |
| `trusted-client` | Ignored | `add-trusted-client` |
| `updatable-object` | Not Implemented | `add-updatable-object` |
| `user` | Not Implemented | `add-user` |
| `user-group` | Not Implemented | `add-user-group` |
| `user-template` | Not Implemented | `add-user-template` |
| `voip-domain-h323-gatekeeper` | Not Implemented | `add-voip-domain-h323-gatekeeper` |
| `voip-domain-h323-gateway` | Not Implemented | `add-voip-domain-h323-gateway` |
| `voip-domain-mgcp-call-agent` | Not Implemented | `add-voip-domain-mgcp-call-agent` |
| `voip-domain-sccp-call-manager` | Not Implemented | `add-voip-domain-sccp-call-manager` |
| `voip-domain-sip-proxy` | Not Implemented | `add-voip-domain-sip-proxy` |
| `web-console-statistics` | Not Implemented | `add-web-console-statistics` |