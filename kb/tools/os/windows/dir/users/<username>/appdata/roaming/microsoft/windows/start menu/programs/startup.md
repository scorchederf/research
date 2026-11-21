---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - autostart
  - persistence
aliases:
  - 'Startup'
  - 'shell:startup'
  - 'Startup folder'
url:
  - https://learn.microsoft.com/windows/win32/w8cookbook/startup-apps
---

**fullpath**: C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

# description

Per-user Startup folder under the Start menu. Microsoft classifies startup apps as those using Run keys, RunOnce keys, and the per-user and public Startup folders under the Start menu; Task Manager's Startup tab lists them and lets users disable them, showing each app's startup impact.

## simple description

> ### 2026-11-21 Claude said
> Anything (usually shortcuts) placed in this folder starts automatically when that user signs in. You can open it with `shell:startup` in the Run dialog. It only affects the one user; the all-users equivalent is under ProgramData. Programs that need admin elevation will not start from here.
>
> **SOC NOTE**: Common persistence location (MITRE T1547.001 Registry Run Keys / Startup Folder). Look for .lnk, .bat, .vbs, .js, .hta or .exe files, especially recently created ones; Sysmon event 11 (file create) in this path is a good detection. Disabled items are tracked in HKCU\...\Explorer\StartupApproved\StartupFolder.
>

# purpose

Holds items that Windows starts automatically after the user signs in; one of the startup app mechanisms controlled from Task Manager's Startup tab.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
