---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Temp\<process>.DMP'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - memory-dump
  - forensics
aliases:
  - <process>.DMP
  - Task Manager live user-mode memory dump
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/task-manager-live-dump
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/user-mode-dump-files
  - https://learn.microsoft.com/windows/win32/wer/collecting-user-mode-dumps
---

**fullpath**:C:\Users\<username>\AppData\Local\Temp\<process>.DMP

# description

User-mode memory dump file of a process, written to the user's `%LocalAppData%\Temp` folder. Task Manager stores live user-mode memory dumps (Processes or Details tab > right-click > Create memory dump file) in this directory. Other tools that create user-mode dumps include ProcDump, WinDbg/CDB (`.dump`), and Windows Error Reporting LocalDumps (default `%LOCALAPPDATA%\CrashDumps`).

## simple description

> ### 2026-11-21 Claude said
> A .DMP file here is a snapshot of a running program's memory, typically created by right-clicking a process in Task Manager and choosing "Create dump file". Developers and support engineers use these to debug crashes or hangs. The file is named after the process (for example `lsass.DMP`).
>
> **SOC NOTE**: An `lsass.DMP` (or similar) in a user's Temp folder is a classic sign of credential dumping via Task Manager (MITRE ATT&CK T1003.001); attackers also use procdump, comsvcs.dll MiniDump, or rundll32 for the same purpose. Dumps can contain passwords, tokens and keys, so treat them as sensitive. Correlate with Sysmon Event ID 10 (process access to lsass) and 11 (file create of .dmp) and Defender alerts.
>

# purpose

Holds a live user-mode memory dump created from Task Manager; when the dump completes, Task Manager shows the location of the `.dmp` file with an Open File Location option. A user-mode dump can be a full dump (entire process memory, executable image, handle table) or a minidump whose content depends on the options used, and can be analyzed with WinDbg.
