---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - debugging
  - gflags
  - persistence
aliases:
  - SilentProcessExit
  - Silent Process Exit
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/registry-entries-for-silent-process-exit
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/setting-and-clearing-flags-for-silent-process-exit
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/enable-silent-process-exit-monitoring
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit

# description

Registry key that stores global settings for Silent Process Exit monitoring, and (in `SilentProcessExit\<ProcessName>` subkeys) per-application settings. It is configured with the Silent Process Exit tab of GFlags, part of Debugging Tools for Windows, together with the `FLG_MONITOR_SILENT_PROCESS_EXIT` (0x200) flag in Image File Execution Options.

## simple description

> ### 2026-11-21 Claude said
> Windows can watch a chosen program and react when it is killed or exits on its own, for example by writing a crash dump or launching another program. The settings for this feature live under this key. It is meant for developers debugging unexpected terminations. Normally the key is empty or absent on most machines.
>
> **SOC NOTE**: Abused for persistence and execution (MITRE T1546.012 Image File Execution Options Injection): setting `GlobalFlag=0x200` under IFEO plus `ReportingMode=1` and `MonitorProcess=<payload>` here runs the payload whenever the target process exits. It is also abused for credential theft by configuring `LocalDump` on `lsass.exe` and forcing a silent exit to get an LSASS dump. Hunt for new subkeys, `MonitorProcess` values, and Application log events from source `Process Exit Monitor` (Event ID 3000).
>

# purpose

Global settings apply to all processes registered for silent exit monitoring; application settings under `SilentProcessExit\<ProcessName>` override them. Monitoring detects self termination (`ExitProcess`) and cross-process termination (`TerminateProcess`), but not normal exit of the last thread or kernel-initiated termination. When a silent exit is detected the monitor can show a notification, log an event (source **Process Exit Monitor** in the Application log), write dump files, or launch a monitor process.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SOFTWARE` |

# values

| value name | type | description |
| --- | --- | --- |
| `ReportingMode` | REG_DWORD | Application setting only. Bitwise OR of LAUNCH_MONITORPROCESS (0x1), LOCAL_DUMP (0x2) and NOTIFICATION (0x4). |
| `IgnoreSelfExits` | REG_DWORD | Application setting only. 0x0 detects self and cross-process termination; 0x1 ignores self termination. |
| `MonitorProcess` | REG_SZ | Command line of the process launched on silent exit; supports `%e` (exiting PID), `%i` (initiating PID), `%t` (initiating thread), `%c` (status code). |
| `LocalDumpFolder` | REG_SZ | Folder for dump files; default `%TEMP%\Silent Process Exit`. |
| `MaxNumberOfDumpFiles` | REG_DWORD | Maximum number of dump files in the dump folder; default 10. |
| `DumpType` | REG_DWORD | Bitwise OR of `MINIDUMP_TYPE` values (Micro, Mini, Heap or Custom). |
| `ModuleIgnoreList` | REG_MULTI_SZ | Modules whose terminations of the process are ignored. |

# subkeys

| subkey | description |
| --- | --- |
| `<ProcessName>` | Per-application settings for an image name (for example `notepad.exe`); override the global settings. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit" /s` | List all per-process subkeys and their values. |
