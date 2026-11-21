---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - tls
  - schannel
  - crypto
aliases:
  - 'SCHANNEL'
  - 'Schannel SSP settings'
  - 'TLS registry settings'
url:
  - https://learn.microsoft.com/windows-server/security/tls/tls-registry-settings
  - https://learn.microsoft.com/windows-server/identity/ad-fs/operations/manage-ssl-protocols-in-ad-fs
  - https://learn.microsoft.com/windows-server/security/tls/manage-tls
---

**fullpath**: HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL

# description

Registry key holding configuration for the Schannel Security Support Provider, Windows' TLS/DTLS/SSL implementation. It controls protocol versions (under `Protocols`), certificate mapping, session caching and OCSP stapling. Cipher suites, hashes and key exchange should be managed through Group Policy, MDM or the TLS PowerShell module rather than the registry.

## simple description

> ### 2026-11-21 Claude said
> SCHANNEL is where Windows stores its TLS/SSL settings - which protocol versions (SSL 3.0, TLS 1.0-1.3) are enabled for clients and servers, and related options. Admins edit it to disable old, weak protocols. Changes usually need a service or system restart to take effect. These settings apply to everything using the Windows TLS stack (IIS, RDP, LDAPS, etc.).
>
> **SOC NOTE**: Attackers can re-enable weak protocols (SSL 3.0/TLS 1.0) or modify CertificateMappingMethods to weaken authentication (T1562 Impair Defenses, T1556); the latter relates to AD CS certificate mapping abuse (ESC10). Monitor changes to this key (Sysmon 13, 4657) and Schannel events in the System log (event 36871, 36874, 36888).
>

# purpose

Configures Schannel SSP behavior: TLS/DTLS/SSL protocol versions, client certificate mapping, session cache lifetimes and OCSP stapling.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

| value name | type | description |
| --- | --- | --- |
| `CertificateMappingMethods` | REG_DWORD | Certificate mapping methods: 0x1 Subject/Issuer, 0x2 Issuer, 0x4 UPN, 0x8 S4U2Self (default), 0x10 S4U2Self Explicit (default). |
| `ClientCacheTime` | REG_DWORD | Client TLS session cache item lifetime in milliseconds; default 10 hours; 0 turns off client session caching. |
| `EnableOcspStaplingForSni` | REG_DWORD | 1 enables OCSP stapling for SNI/CCS bindings; 0 disables. May impact performance. |

# subkeys

| subkey | description |
| --- | --- |
| `Protocols` | Version-specific subkeys (for example `TLS 1.2\Server`, `TLS 1.2\Client`) with `Enabled` and `DisabledByDefault` DWORD values to enable or disable protocol versions. |
| `Ciphers` | Ciphers should be controlled through cipher suite order rather than registry. |
| `CipherSuites` | Configure via Group Policy, MDM or PowerShell instead of registry. |
| `Hashes` | Hash algorithms should be controlled through cipher suite order. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols" /s` | List protocol version settings. |
| `reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server" /v Enabled /t REG_DWORD /d 0` | Disable TLS 1.2 server side (not recommended; reboot required). |
