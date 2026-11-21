---
created: 2026-11-21
fullpath: 'C:\Windows\MEMORY.DMP'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - crash-dump
  - forensics
aliases:
  - MEMORY.DMP
  - Memory.dmp
  - complete memory dump
  - kernel memory dump
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/memory-dump-file-options
  - https://learn.microsoft.com/troubleshoot/windows-client/performance/stop-code-error-troubleshooting
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/automatic-memory-dump
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-setup-log-files-and-event-logs
---

**fullpath**:C:\Windows\MEMORY.DMP

# description

Default system crash dump file (`%SystemRoot%\Memory.dmp`) written after a bug check (Stop error) for kernel, complete, automatic and active memory dumps. Its path and type are set under `HKLM\System\CurrentControlSet\Control\CrashControl` (`DumpFile`, `CrashDumpEnabled`), and it is analyzed with the Windows debugger.

## simple description

> ### 2026-11-21 Claude said
> When Windows blue-screens, it writes the contents of memory to the page file and, on reboot, saves it as MEMORY.DMP. Depending on settings it holds kernel memory only or all physical RAM. Engineers open it with WinDbg to find the faulty driver. It can be very large and is overwritten by the next crash by default.
>
> **SOC NOTE**: May contain sensitive data (credentials, keys, LSASS memory for complete dumps) and is a useful memory forensics source (e.g. with Volatility). Attackers can force a crash (e.g. NotMyFault, `CrashOnCtrlScroll`) or read an existing dump to harvest secrets (MITRE ATT&CK T1003). Check `LastCrashTime` and System event 1001 BugCheck.
>

# purpose

Records system memory at the time of a crash for troubleshooting. Minidumps go to `%SystemRoot%\Minidump` instead.
