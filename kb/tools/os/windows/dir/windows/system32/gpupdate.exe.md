---
created: 2026-11-21
fullpath: 'C:\Windows\System32\gpupdate.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - group-policy
aliases:
  - gpupdate.exe
  - gpupdate
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/gpupdate
  - https://learn.microsoft.com/powershell/module/grouppolicy/invoke-gpupdate
---

**fullpath**:C:\Windows\System32\gpupdate.exe

# description

`gpupdate` updates Group Policy settings on the local computer. It is a built-in Windows command in System32; the GroupPolicy PowerShell module's `Invoke-GPUpdate` schedules gpupdate remotely.

## simple description

> ### 2026-11-21 Claude said
> gpupdate.exe forces Windows to refresh its Group Policy settings instead of waiting for the background refresh interval (about 90 minutes). Admins and helpdesk staff run `gpupdate /force` after changing a GPO. It can refresh user policy, computer policy, or both, and may request a logoff or reboot for settings that only apply then. It is a normal, signed Windows binary.
>
> **SOC NOTE**: Mostly benign, but after an attacker modifies a GPO (e.g. adding a scheduled task or startup script - MITRE T1484.001 Domain Policy Modification), they may run `gpupdate /force` to push it immediately. Remote `Invoke-GPUpdate` creates scheduled tasks on targets. Correlate with 5136 (directory object modified) on DCs and Group Policy Operational log events (e.g. 4016/5312/8001).
>

# purpose

Refreshes User and/or Computer Group Policy settings; by default only changed settings are applied unless `/force` is used.

# typical use cases

| usage | description |
| --- | --- |
| `gpupdate /force` | Reapplies all user and computer policy settings. |
| `gpupdate /target:computer` | Refreshes only computer policy. |
| `gpupdate /target:user /logoff` | Refreshes user policy and logs off if an extension requires it. |
| `gpupdate /boot` | Restarts the computer after policy is applied if required. |
| `gpupdate /sync` | Makes the next foreground policy application synchronous. |

# options

| option | description |
| --- | --- |
| `/target:{computer \| user}` | Updates only User or only Computer policy settings; both by default. |
| `/force` | Reapplies all policy settings, not only changed ones. |
| `/wait:<VALUE>` | Seconds to wait for policy processing (default 600; `0` = don't wait; `-1` = wait indefinitely). |
| `/logoff` | Logs off after update if a client-side extension (e.g. Folder Redirection) requires it. |
| `/boot` | Restarts after update if an extension (e.g. computer Software Installation) requires it. |
| `/sync` | Makes the next foreground policy application synchronous; `/force` and `/wait` are ignored. |
| `/?` | Displays Help at the command prompt. |

