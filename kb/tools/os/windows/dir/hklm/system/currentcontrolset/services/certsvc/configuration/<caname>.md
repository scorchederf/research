---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\CertSvc\Configuration\<CAName>'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - adcs
  - pki
aliases:
  - <CAName>
  - CertSvc Configuration
  - CA registry configuration
url:
  - https://learn.microsoft.com/windows-server/identity/ad-cs/migrate-certification-authority
  - https://learn.microsoft.com/windows-server/administration/windows-commands/certutil
  - https://learn.microsoft.com/windows-server/identity/ad-cs/configure-certificate-enrollment-web-service
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services\CertSvc\Configuration\<CAName>

# description

Per-CA configuration key of Active Directory Certificate Services (AD CS, service `CertSvc`); `<CAName>` is the name of the certification authority. It sits under `CertSvc\Configuration`, which holds the database locations, and is read and written by `certutil -getreg` / `-setreg` (alias `ca`) and the Certification Authority console.

## simple description

> ### 2026-11-21 Claude said
> On a Windows Certification Authority server, this key holds the settings for one CA: its server name, certificate file, CRL/AIA publishing URLs, policy and exit modules, and security flags. Admins usually change it with `certutil -setreg` rather than editing it directly. It is backed up and imported when a CA is migrated.
>
> **SOC NOTE**: Misconfigurations here enable AD CS abuse; e.g. the `EDITF_ATTRIBUTESUBJECTALTNAME2` flag in `PolicyModules\...\EditFlags` lets requesters specify arbitrary SANs (ESC6), leading to domain privilege escalation (MITRE ATT&CK T1649). Monitor changes to this key and CA audit events (4885-4899, e.g. 4890/4892 for setting changes) and service restarts of `certsvc` following `certutil -setreg`.
>

# purpose

Stores the configuration of a specific CA. During CA migration, the whole `HKLM\SYSTEM\CurrentControlSet\Services\CertSvc\Configuration` key is exported on the source CA and imported with `reg import` on the destination; if the server name changes, values under the CA-name key must be updated to the destination server name. Policy and exit module settings (e.g. `policy\EditFlags`) are changed with `certutil -setreg` and take effect after restarting the CA service (`net stop certsvc && net start certsvc`).

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `CAServerName` | string | Name of the CA server; replace with the destination server name when migrating to a server with a different name. |
| `CACertFileName` | string | CA certificate file name; created only with certain installation options; update the server name after migration. |

# subkeys

| subkey | description |
| --- | --- |
| `PolicyModules` | Policy module settings (certutil alias `Policy`), e.g. `EditFlags`, addressed by the module ProgID. |
| `ExitModules` | Exit module settings (certutil alias `Exit`). |
| `RestoreInProgress` | Restore state (certutil alias `Restore`). |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\CertSvc\Configuration\<CAName>"` | List the key's values. |
| `certutil -getreg ca` | Display the CA's registry values. |
| `certutil -getreg policy\EditFlags` | Display the policy module EditFlags value. |
| `certutil -config "<CAConfig>" -setreg policy\EditFlags +EDITF_ENABLERENEWONBEHALFOF` | Set a policy module flag (restart certsvc afterwards). |
| `certutil -setreg ca\KRAFlags +KRAF_ENABLEFOREIGN` | Allow the CA to import foreign certificates. |
