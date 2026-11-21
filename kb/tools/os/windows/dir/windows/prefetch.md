---
created: 2026-11-21
fullpath: 'C:\Windows\Prefetch'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - prefetch
  - forensics
aliases:
  - Prefetch
  - Windows Prefetch
url:
  - https://learn.microsoft.com/sysinternals/resources/archive/v03n02
  - https://learn.microsoft.com/answers/a/8149054
  - https://learn.microsoft.com/answers/a/12857375
---

**fullpath**:C:\Windows\Prefetch

# description

`\Windows\Prefetch` is where the Windows prefetcher stores trace files for boot and application startup. The Cache Manager traces page faults during the first minutes of boot and the first seconds of application start, and the Task Scheduler writes the processed trace here. Related to the SysMain (Superfetch) service and the defragmenter's layout optimization.

## simple description

> ### 2026-11-21 Claude said
> Windows watches which files a program loads when it starts and saves that list in a .pf file in this folder. Next time, Windows preloads those files so the app opens faster. Each file is named after the executable plus a hash of its path, for example NOTEPAD.EXE-AF43252301.PF. Deleting the files is harmless; they get recreated.
>
> **SOC NOTE**: Prefetch is a top forensic artifact for program execution evidence: the .pf files record the executable name, run count, last run times (up to 8 on Win8+) and files/directories referenced. It can prove a tool such as psexec, mimikatz or a renamed binary ran even if the binary was deleted. Attackers may delete .pf files (T1070.004). Disabled by default on many servers.
>

# purpose

Holds prefetch trace files used to speed up boot and application startup, plus the layout list used by the defragmenter to place referenced files contiguously.

# common files found

| file | description |
| --- | --- |
| `<APPNAME>.EXE-<hash>.pf` | Trace file for an application; name is the executable plus a hex hash of its path. |
| `NTOSBOOT-B00DFAAD.PF` | Trace file for the boot scenario. |
| `Layout.ini` | Ordered list of files and directories referenced during boot/app starts, used for defragmentation. |
| `ResPriHMStaticDb.edb` | Database file associated with the Prefetch/SysMain subsystem (per Microsoft Q&A). |

