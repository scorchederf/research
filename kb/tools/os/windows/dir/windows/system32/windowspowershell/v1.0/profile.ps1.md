---
created: 2026-11-21
fullpath: 'C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - profile.ps1
  - AllUsersAllHosts profile
  - $PSHOME\Profile.ps1
url:
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles
  - https://learn.microsoft.com/powershell/scripting/learn/shell/creating-profiles
  - https://learn.microsoft.com/powershell/scripting/dev-cross-plat/performance/startup-performance
  - https://learn.microsoft.com/powershell/scripting/whats-new/migrating-from-windows-powershell-51-to-powershell-7
---

**fullpath**:C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1

# description

profile.ps1 in `$PSHOME` is the "All Users, All Hosts" PowerShell profile script; for Windows PowerShell 5.1, `$PSHOME` is C:\Windows\System32\WindowsPowerShell\v1.0. It is the first of the four profile scripts (AllUsersAllHosts, AllUsersCurrentHost, CurrentUserAllHosts, CurrentUserCurrentHost) that PowerShell runs at startup; its path is exposed as `$PROFILE.AllUsersAllHosts`.

## simple description

> ### 2026-11-21 Claude said
> This file is a PowerShell script that runs automatically every time any user starts any PowerShell host on the machine (console, ISE, VS Code, remoting hosts that load profiles). Admins use it to add aliases, functions, modules or settings for everyone. It doesn't exist by default and needs admin rights to create. Because it runs for every user, it is a powerful place to put code.
>
> **SOC NOTE**: Writing to this profile is a classic persistence and privilege-escalation trick (MITRE ATT&CK T1546.013 Event Triggered Execution: PowerShell Profile) - code runs whenever an admin opens PowerShell. Any existence or modification of this file should be reviewed; check file creation events (Sysmon 11), PowerShell script block logging (4104) at startup, and compare with `$PROFILE | Select-Object *` on the host.
>

# purpose

Customizes the PowerShell environment for all users and all hosts: add aliases, functions and variables, load modules, create PowerShell drives, run arbitrary commands and change preference settings. Profiles run in order AllUsersAllHosts, AllUsersCurrentHost, CurrentUserAllHosts, CurrentUserCurrentHost, so later profiles can override this one. Running a profile on Windows requires an execution policy of at least `RemoteSigned`. Profile processing is the last phase of PowerShell startup and can cause slow startup or errors.
