---
created: 2026-11-21
fullpath: 'C:\Windows\System32\mmc.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - mmc
  - administration
aliases:
  - mmc.exe
  - Microsoft Management Console
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/mmc
---

**fullpath**:C:\Windows\System32\mmc.exe

# description

`mmc.exe` is the Microsoft Management Console host, built into Windows. It opens saved console files (`.msc`) containing snap-ins, can open them in author mode, and can force the 32-bit or 64-bit version of MMC.

## simple description

> ### 2026-11-21 Claude said
> MMC is the shell that hosts Windows admin tools such as Event Viewer, Services, Computer Management and Group Policy editors. Each tool is a snap-in saved in an .msc file that mmc.exe loads. Admins open it constantly, so its presence and normal use are expected. It can also open consoles that connect to remote computers.
>
> **SOC NOTE**: Malicious .msc files (GrimResource, 2024) abuse MMC to execute script via crafted consoles (MITRE T1218.014 MMC). Watch for mmc.exe opening .msc files from Downloads/Temp/email attachments, spawning cmd/powershell/script hosts, or loading the MMC20.Application COM object remotely for lateral movement (T1021.003 DCOM).
>

# purpose

Starts MMC with a new console or opens a saved console file; author mode allows changes to saved consoles.

# typical use cases

| usage | description |
| --- | --- |
| `mmc` | Opens a new, empty console. |
| `mmc %systemroot%\system32\<console_name>.msc` | Opens a saved console using an environment variable for the path. |
| `mmc <path>\<filename>.msc /a` | Opens a saved console in author mode to make changes. |

# options

| option | description |
| --- | --- |
| `<path>\<filename>.msc` | Starts mmc and opens a saved console; requires full path and file name. Without it, a new console opens. |
| `/a` | Opens a saved console in author mode, regardless of its default mode, without permanently changing it. |
| `/64` | Opens the 64-bit version of mmc (mmc64); use on 64-bit Windows for 64-bit snap-ins. |
| `/32` | Opens the 32-bit version of mmc (mmc32) to run 32-bit-only snap-ins on 64-bit Windows. |
