---
created: 2026-11-21
fullpath: 'C:\Windows\System32\sdclt.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - sdclt.exe
  - sdclt
url:
  - https://learn.microsoft.com/windows/compatibility/windows-7-backup-and-restore-deprecated
---

**fullpath**:C:\Windows\System32\sdclt.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 05:17 UTC_ - no Learn page found names `sdclt.exe`. The closest Learn content covers the Windows 7 Backup and Restore feature, which Microsoft deprecated in Windows 8 (replaced by File History; its Control Panel applet was renamed *Windows 7 File Recovery*). Learn does not state that sdclt.exe is that feature's binary.

## simple description

> ### 2026-11-21 Claude said
> sdclt.exe is the Windows Backup and Restore program, the Control Panel tool that came with Windows 7 for backing up files and creating system images. It is still included in Windows 10 and 11 as "Backup and Restore (Windows 7)". Users rarely run it directly; it normally opens from Control Panel. It is an auto-elevating Microsoft binary, which means it can run with administrator rights without showing a UAC prompt.
>
> **SOC NOTE**: Because it auto-elevates, sdclt.exe has well-known UAC bypass techniques (MITRE ATT&CK T1548.002). Attackers plant a command in user-writable registry keys that sdclt reads at launch, such as `HKCU\Software\Microsoft\Windows\CurrentVersion\App Paths\control.exe` or the `IsolatedCommand` value under `HKCU\Software\Classes\exefile\shell\runas\command` (used with `sdclt.exe /kickoffelev`). Look for sdclt.exe spawning unexpected child processes such as cmd.exe or powershell.exe, and for writes to those keys.
>
> _Not documented on Microsoft Learn at 2026/11/21 05:17 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 05:17 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 05:17 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 05:17 UTC_
