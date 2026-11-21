---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Policies\Microsoft\Windows Defender'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - defender
  - policy
aliases:
  - Windows Defender policy key
  - Microsoft Defender Antivirus policies
url:
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-microsoftdefenderantivirus
  - https://learn.microsoft.com/defender-endpoint/troubleshoot-microsoft-defender-antivirus-when-migrating
  - https://learn.microsoft.com/defender-endpoint/troubleshoot-onboarding
  - https://learn.microsoft.com/defender-endpoint/migrating-asr-rules
  - https://learn.microsoft.com/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-disableantispyware
---

**fullpath**:HKLM\SOFTWARE\Policies\Microsoft\Windows Defender

# description

This key holds Group Policy settings for Microsoft Defender Antivirus, written by the WindowsDefender.admx template ("Windows Components > Microsoft Defender Antivirus"), Group Policy preferences, MDM ADMX-backed policies, or direct registry edits. Changes to settings here are blocked when tamper protection is enabled.

## simple description

> ### 2026-11-21 Claude said
> This is where Windows stores administrator-enforced policy for Microsoft Defender Antivirus. Values here override local user choices, for example turning off real-time protection or adding scan exclusions. Domain Group Policy, Intune or local policy tools normally write to it. Subkeys such as `Real-Time Protection`, `Exclusions` and `Spynet` hold groups of related settings.
>
> **SOC NOTE**: Attackers write to this key to impair defenses (MITRE ATT&CK T1562.001), for example setting `DisableAntiSpyware`, `DisableRealtimeMonitoring` or adding paths under `Exclusions\Paths`. Defender logs Event ID 5007 (configuration changed) in Microsoft-Windows-Windows Defender/Operational when these change. Any write to this key from a non-GPO process on a workstation is suspicious; check whether tamper protection is on.

# purpose

Settings under this key are applied as policy. The `DisableAntiSpyware` value (policy "Turn off Microsoft Defender Antivirus") stops Microsoft Defender Antivirus from running when enabled; it is ignored on devices with platform 4.18.2108.4 or later that are onboarded to Microsoft Defender for Endpoint, and it is protected by tamper protection. A gpresult report shows these entries under "Registry item (Key path: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender)" when set via Group Policy preferences.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide (Device scope policy) |

# values

| value name | type | description |
| --- | --- | --- |
| `DisableAntiSpyware` | REG_DWORD | 1 turns off Microsoft Defender Antivirus; 0 force-enables it even if non-Microsoft antivirus is installed. Legacy setting, ignored on MDE-onboarded devices with platform 4.18.2108.4+. |
| `DisableAntiVirus` | REG_DWORD | Legacy setting to disable Microsoft Defender Antivirus; should be cleared before onboarding to Defender for Endpoint. |

# subkeys

| subkey | description |
| --- | --- |
| `Policy Manager` | Contains settings such as `AllowRealTimeMonitoring`, listed among keys protected by tamper protection. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender"` | List the key's values. |
| `GPresult.exe /h gpresult.html` | Generate a report of active group policies to see whether Defender is turned off by policy. |
