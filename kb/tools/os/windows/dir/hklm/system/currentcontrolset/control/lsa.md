---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Lsa'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Lsa
  - HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa
url:
  - https://learn.microsoft.com/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection
  - https://learn.microsoft.com/troubleshoot/windows-client/windows-security/enable-ntlm-2-authentication
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/audit-domain-controller-ntlmv1
  - https://learn.microsoft.com/azure/governance/policy/samples/guest-configuration-baseline-windows
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/0xc000035b-when-you-use-lmcompatibility
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\Lsa

# description

The Lsa key holds configuration for the Local Security Authority (LSASS), including LSA protection (`RunAsPPL`) and the LAN Manager authentication level (`LmCompatibilityLevel`). Settings are configured with Registry Editor, Group Policy (Security Options, "Configures LSASS to run as a protected process") or Intune (LocalSecurityAuthority CSP).

## simple description

> ### 2026-11-21 Claude said
> This registry key controls how LSASS, the process that handles Windows logons and credentials, behaves. It decides which NTLM/LM versions are allowed, whether LSASS runs as a protected process, which authentication and security packages load, and many anonymous-access restrictions. Changes usually require a reboot.
>
> **SOC NOTE**: High-value key for attackers: setting `RunAsPPL`=0 removes LSASS protection before Mimikatz (T1003.001); adding DLLs to `Security Packages`/`Authentication Packages`/`Notification Packages` gives persistence and password capture (T1547.002, T1547.005, T1556.002); `DisableRestrictedAdmin`=0 enables pass-the-hash RDP; lowering `LmCompatibilityLevel` enables NTLMv1 downgrade (T1562). Monitor Sysmon 13 / Event 4657 on this key.
>

# purpose

Stores LSA and authentication-protocol settings. `RunAsPPL` enables added LSA protection (LSASS as a protected process light); `LmCompatibilityLevel` sets the LAN Manager authentication level that decides whether clients send LM, NTLM or NTLMv2 and what DCs accept. The `MSV1_0` subkey holds minimum NTLM SSP session security settings.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `RunAsPPL` | REG_DWORD | 1 = LSA protection with a UEFI variable; 2 = without a UEFI variable (enforced on Windows 11 22H2 and later); 0 or deleted = disabled. Restart required. |
| `LmCompatibilityLevel` | REG_DWORD | 0 = send LM & NTLM; 1 = NTLMv2 session security if negotiated; 2 = NTLM only; 3 = NTLMv2 only; 4 = DCs refuse LM; 5 = DCs refuse LM & NTLM (baseline expects 5). Values below 3 force NTLMv1 and can break RDP 8.0 channel bindings (0xC000035B). |

# subkeys

| subkey | description |
| --- | --- |
| `MSV1_0` | Minimum security settings for programs using the NTLM Security Support Provider; values depend on `LmCompatibilityLevel`. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v RunAsPPL` | Check whether LSA protection is configured. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v LmCompatibilityLevel` | Show the LAN Manager authentication level. |
