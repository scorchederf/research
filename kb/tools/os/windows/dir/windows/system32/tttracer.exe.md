---
created: 2026-11-21
fullpath: 'C:\Windows\System32\tttracer.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - debugging
aliases:
  - tttracer.exe
  - Time Travel Debugging (TTD) recorder
  - PartnerTTD
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/windows-tss/introduction-to-troubleshootingscript-toolset-tss
  - https://learn.microsoft.com/windows-hardware/drivers/debuggercmds/time-travel-debugging-ttd-exe-command-line-util
---

**fullpath**:C:\Windows\System32\tttracer.exe

# description

tttracer.exe is the in-box Time Travel Debugging (TTD/TTT/iDNA) recorder referenced by the TroubleShootingScript toolset (TSS), whose `-TTDPath` switch points to the folder containing tttracer.exe (PartnerTTD). On Learn, TTD recording is otherwise documented through WinDbg and the separately installed TTD.exe command-line utility.

## simple description

> ### 2026-11-21 Claude said
> tttracer.exe records a 'time travel' trace of a running program: every instruction it executes, so a debugger can later replay it forwards and backwards. It is built into Windows 10 1703 and later. Recording needs admin rights and slows the target process a lot.
>
> **SOC NOTE**: Because tttracer can attach to any process and record its full memory activity, it can be abused to dump credentials or secrets, e.g. by tracing lsass.exe (MITRE ATT&CK T1003.001) and it is a known LOLBin that can also launch programs (T1218). Trace files (.run) can contain sensitive data. Alert on tttracer.exe executions outside of developer/debug activity, especially with `-attach` against security-sensitive processes.
>

# purpose

Record Time Travel Debugging traces of a process for later replay in WinDbg. TSS uses it via `-TTD <PID|ProcessName.exe|ServiceName>` with `-TTDMode` Full (`-dumpfull`, default), Ring (ring buffer) or onLaunch, and `-TTDMaxFile` for maximum log size. Learn notes TTD recordings may contain personally identifiable or security-related information such as file paths, registry, memory or file contents.

# typical use cases

| usage | description |
| --- | --- |
| `.\TSS.ps1 -TTD notepad.exe` | Start TTD recording of a process through TSS (default Full mode). |
| `.\TSS.ps1 -TTD <PID> -TTDMode Ring -TTDMaxFile <size in MB>` | Record into a ring buffer limited to the given size. |
| `.\TSS.ps1 -TTD <ProcessName.exe> -TTDPath <Folder path to tttracer.exe>` | Force TSS to use a specific tttracer.exe folder. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
