---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - persistence
aliases:
  - StartUp
  - Common Startup
  - CSIDL_COMMON_STARTUP
  - FOLDERID_CommonStartup
url:
  - https://learn.microsoft.com/windows/deployment/usmt/usmt-recognized-environment-variables
  - https://learn.microsoft.com/windows/win32/msi/installation-context
  - https://learn.microsoft.com/windows/win32/w8cookbook/startup-apps
  - https://learn.microsoft.com/windows/win32/cimwin32prov/win32-startupcommand
---

**fullpath**:C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

# description

This is the all-users (common) Startup folder, identified as `CSIDL_COMMON_STARTUP` / `FOLDERID_CommonStartup`. It contains programs that appear in the Startup folder for all users. Windows Installer uses it as `StartUpFolder` for per-machine installs; per-user installs use `FOLDERID_Startup` in the user profile.

## simple description

> ### 2026-11-21 Claude said
> Anything placed in this folder (usually a shortcut) runs automatically when any user signs in to the computer. It is the shared version of the personal Startup folder in each user's AppData. Writing here needs administrator rights.
>
> **SOC NOTE**: Classic persistence location (T1547.001 Registry Run Keys / Startup Folder). Look for new `.lnk`, `.bat`, `.vbs`, `.js`, `.exe` or `.url` files, especially ones pointing into Temp, AppData or Public. File creation is captured by Sysmon Event ID 11; Autoruns, `Win32_StartupCommand` and Task Manager's Startup tab list the entries.
>

# purpose

Starts programs automatically at user logon for every user. Learn classifies items here as startup apps alongside Run and RunOnce registry keys; Task Manager's Startup tab lists them, shows their impact and lets users disable them. The WMI class `Win32_StartupCommand` enumerates them.

# common files found

| file | description |
| --- | --- |
| `*.lnk` | Shortcuts to programs that start for all users at logon. |
