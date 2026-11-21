---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Windows Advanced Threat Protection\Status
  - MDE onboarding status key
url:
  - https://learn.microsoft.com/defender-endpoint/troubleshoot-onboarding
  - https://learn.microsoft.com/defender-endpoint/configure-endpoints-sccm
  - https://learn.microsoft.com/purview/device-onboarding-sccm
  - https://learn.microsoft.com/windows/client-management/mdm/windowsadvancedthreatprotection-csp
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status

# description

This key holds the onboarding status of Microsoft Defender for Endpoint (formerly Windows Defender ATP). The SENSE service writes it when it starts for the first time; the `OnboardingState` value is monitored by Configuration Manager compliance rules and checked by the onboarding scripts.

## simple description

> ### 2026-11-21 Claude said
> This registry key tells you whether a Windows device is onboarded to Microsoft Defender for Endpoint. `OnboardingState` = 1 means the Sense (MDE sensor) service onboarded successfully; the key also usually stores the organization ID and last-connected time. It is maintained by the SENSE service, not by admins.
>
> **SOC NOTE**: Useful to confirm EDR coverage during an investigation: a missing key or `OnboardingState` other than 1 means the device was never onboarded or was offboarded (possible defense evasion, MITRE ATT&CK T1562.001). Pair with `sc query sense` and the policy key `HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection`.
>

# purpose

Records the Defender for Endpoint onboarding state. Onboarding scripts fail with event 35 if this value isn't found and event 40 if the SENSE onboarding status isn't 1. The same state is exposed by the WindowsAdvancedThreatProtection CSP `HealthState/OnboardingState` node.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `OnboardingState` | REG_DWORD | Onboarding status written by the SENSE service; `1` means the device is onboarded (used as the compliance rule value). |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status" /v OnboardingState` | Check whether the device is onboarded (1). |
