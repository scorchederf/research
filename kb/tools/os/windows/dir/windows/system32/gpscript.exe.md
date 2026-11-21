---
created: 2026-11-21
fullpath: 'C:\Windows\System32\gpscript.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - group-policy
  - scripts
aliases:
  - gpscript.exe
  - Group Policy scripts
url:
  - https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-scripts
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-grouppolicy
---

**fullpath**:C:\Windows\System32\gpscript.exe

# description

`gpscript.exe` is the Windows component that runs scripts assigned through Group Policy (startup, shutdown, logon and logoff scripts). Learn covers the scripts extension behavior and policies, but not the executable itself.

## simple description

> ### 2026-11-21 Claude said
> gpscript.exe is the Windows program that actually runs the scripts an administrator assigns with Group Policy, such as logon scripts that map drives or startup scripts that install software. Windows launches it automatically at startup, shutdown, logon and logoff. Users normally never run it by hand.
>
> **SOC NOTE**: Group Policy scripts are a common persistence and lateral-movement path (MITRE T1037.001 Logon Script, T1484.001 Group Policy Modification): attackers with GPO write rights add scripts in SYSVOL `Scripts` folders. Investigate children of gpscript.exe (e.g. powershell/cmd running unexpected code) and changes to `scripts.ini`/`psscripts.ini` in GPOs.
>

# purpose

Executes Group Policy scripts. Individual scripts run only when the computer starts and shuts down and when a user logs on and logs off, even though the script extension is processed during background refresh. Related policies: `MaxGPOScriptWaitPolicy` (default 600 seconds total for all scripts) and `Configure Logon Script Delay` (default five-minute wait before logon scripts on Windows 8.1+, `EnableLogonScriptDelay`).

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
