---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - defender
  - mde
aliases:
  - Windows Advanced Threat Protection policy key
  - MDE onboarding key
url:
  - https://learn.microsoft.com/defender-endpoint/troubleshoot-onboarding
  - https://learn.microsoft.com/defender-endpoint/configure-endpoints-script
  - https://learn.microsoft.com/windows/client-management/mdm/windowsadvancedthreatprotection-csp
---

**fullpath**:HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection

# description

This policy key holds Microsoft Defender for Endpoint onboarding and offboarding data written by the onboarding tools, plus settings such as AllowSampleCollection. It is used by Microsoft Defender for Endpoint (the SENSE service); the WindowsAdvancedThreatProtection CSP provides the MDM equivalent for onboarding, health state and configuration.

## simple description

> ### 2026-11-21 Claude said
> This key is where Microsoft Defender for Endpoint stores its onboarding configuration on a device, written by the onboarding script, Group Policy, Configuration Manager or Intune. If the onboarding blob is missing or wrong, the device won't report to the Defender portal. It also holds settings such as whether files may be collected for deep analysis.
>
> **SOC NOTE**: Attackers with admin rights may delete or alter this key (or run an offboarding package) to disconnect a device from MDE (MITRE ATT&CK T1562.001 Impair Defenses). Monitor registry changes here (Sysmon Event ID 12/13, Security 4657), and check onboarding tool events 5 and 10, which point to permission problems on this key.
>

# purpose

Store Microsoft Defender for Endpoint onboarding/offboarding data and policy settings for the device.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `AllowSampleCollection` | REG_DWORD | Whether the device can share files for deep analysis: 0 = don't allow sample sharing, 1 = allow all file types (default if the value doesn't exist). |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection"` | List the key's values. |
| `sc query sense` | Check the health of the SENSE service when onboarding fails (event 15). |
