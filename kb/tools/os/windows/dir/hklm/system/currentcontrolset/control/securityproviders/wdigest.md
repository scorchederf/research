---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - credential-access
aliases:
  - WDigest
  - Microsoft Digest SSP
  - wDigest
url:
  - https://learn.microsoft.com/azure/governance/policy/samples/guest-configuration-baseline-windows
  - https://learn.microsoft.com/azure/defender-for-cloud/alerts-windows-machines
  - https://learn.microsoft.com/windows-server/security/windows-authentication/security-support-provider-interface-architecture
  - https://learn.microsoft.com/windows/win32/secauthn/microsoft-digest-ssp
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest

# description

Configuration key for the Digest Security Support Provider (Wdigest.dll, `%Windir%\System32\Wdigest.dll`), which implements the Digest Access protocol for HTTP and SASL authentication (IE/IIS access, LDAP queries). Its `UseLogonCredential` value controls whether Lsass.exe keeps a plaintext copy of the user's password in memory. Microsoft is deprecating Microsoft Digest starting in Windows 11 22H2.

## simple description

> ### 2026-11-21 Claude said
> WDigest is an old authentication method. This key's UseLogonCredential setting decides whether Windows keeps users' passwords in clear text inside the LSASS process memory. On modern Windows it is off by default, and it should stay off.
>
> **SOC NOTE**: Attackers set `UseLogonCredential` to 1 so that tools like Mimikatz can dump cleartext passwords from LSASS after the next logon (MITRE ATT&CK T1112 Modify Registry, enabling T1003.001 LSASS Memory). Microsoft Defender for Cloud raises an alert on this change. Monitor registry writes to this key (Sysmon event 13, Security 4657).
>

# purpose

Holds WDigest settings. The Windows security baseline (AZ-WIN-73497, CIS 18.3.7) expects `UseLogonCredential` = 0; the setting is applied by the Group Policy `Computer Configuration\Policies\Administrative Templates\MS Security Guide\WDigest Authentication (disabling may require KB2871997)`.

# hive

| property | value |
| --- | --- |
| hive | HKLM (HKEY_LOCAL_MACHINE\System) |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\Config\System` (supporting files System, System.alt, System.log, System.sav) |

# values

| value name | type | description |
| --- | --- | --- |
| `UseLogonCredential` | REG_DWORD | When enabled, Lsass.exe retains a copy of the user's plaintext password in memory. If not configured, WDigest is disabled in Windows 8.1 / Server 2012 R2 and enabled by default in earlier versions. Recommended value: 0 (Disabled). |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest" /v UseLogonCredential` | Check whether plaintext credential caching is enabled. |
