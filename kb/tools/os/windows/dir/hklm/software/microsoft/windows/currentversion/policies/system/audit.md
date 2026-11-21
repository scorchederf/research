---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - auditing
  - group-policy
aliases:
  - Audit
  - Include command line in process creation events
url:
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-auditsettings
  - https://learn.microsoft.com/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing
  - https://learn.microsoft.com/azure/governance/policy/samples/guest-configuration-baseline-windows
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/debug-customscriptextension-runcommand-scripts
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit

# description

Registry key used by the "Include command line in process creation events" policy (AuditSettings.admx, Computer Configuration > Administrative Templates > System > Audit Process Creation). It is also exposed through the Policy CSP `ADMX_AuditSettings/IncludeCmdLine` and checked by the Windows security baseline (CCE-36925-6, CIS 18.8.3.1).

## simple description

> ### 2026-11-21 Claude said
> This key controls whether Windows records the full command line of every new process in the Security log. With it enabled, event 4688 ("A new process has been created") shows exactly what arguments a program was run with. It only has an effect if "Audit Process Creation" auditing is also turned on.
>
> **SOC NOTE**: Command-line logging is one of the most valuable detection sources (encoded PowerShell, LOLBin arguments, lateral movement tooling). Attackers may set `ProcessCreationIncludeCmdLine_Enabled` to 0 to impair defenses (MITRE ATT&CK T1562.002); alert on changes to this value. Command lines can contain secrets, so restrict who can read the Security log.
>

# purpose

When `ProcessCreationIncludeCmdLine_Enabled` is enabled, command line information for every process is logged in plain text in the Security event log as part of event 4688. The setting only applies when the Audit Process Creation policy (Advanced Audit Configuration > Detailed Tracking) is enabled. Default: Not configured (command line not included). Any user who can read security events can read the logged command-line arguments, which may contain passwords or other sensitive data.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide (Computer Configuration only) |

# values

| value name | type | description |
| --- | --- | --- |
| `ProcessCreationIncludeCmdLine_Enabled` | REG_DWORD | 1 = include the process command line in event 4688; 0 = do not include. Baseline expected value is 1. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit"` | List the key's values. |
| `reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit" /v "ProcessCreationIncludeCmdLine_Enabled" /t REG_DWORD /d 1 /f` | Turn on command line logging in process creation events. |
| `reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit" /v "ProcessCreationIncludeCmdLine_Enabled" /t REG_DWORD /d 0 /f` | Turn off command line logging in process creation events. |
