---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - debugging
aliases:
  - Image File Execution Options
  - IFEO
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/gflags-details
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/gflags-overview
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/example-13---listing-image-files-with-global-flags
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/debugging-winlogon
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options

# description

Image File Execution Options (IFEO) is the registry key where Windows stores program-specific ("image file") debugging settings for all users of the computer, in a subkey named for each image file. These settings are typically written by GFlags (gflags.exe), the Global Flags Editor shipped with Debugging Tools for Windows. Related settings include the system-wide `GlobalFlag` under `Session Manager` and the `SilentProcessExit` key.

## simple description

> ### 2026-11-21 Claude said
> IFEO is a registry key where each subkey is named after a program file (for example `notepad.exe`). Values in that subkey change how Windows starts the program, such as launching it under a debugger, enabling heap checking, or setting mitigation options. Developers use it to troubleshoot crashes. Windows reads it every time a process with that name is created.
>
> **SOC NOTE**: The `Debugger` value is a classic persistence and hijack technique (MITRE ATT&CK T1546.012): setting `sethc.exe` or `utilman.exe` Debugger to `cmd.exe` gives a SYSTEM shell at the logon screen, and pointing a security tool's Debugger at a non-existent file blocks it from running. `GlobalFlag` 0x200 combined with `SilentProcessExit` `MonitorProcess` is another persistence path. Monitor registry writes here (Sysmon 12/13) and audit all subkeys that contain `Debugger`.

# purpose

Program-specific settings are stored in a `GlobalFlag` registry entry for each program and take effect when the program is restarted. The Debugger feature specifies that a particular program always runs in a debugger; it is effective immediately. GFlags displays flags for one image file but not all image files that have flags set, so `reg query` is used to find them.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide (program-specific settings for all users of the computer) |

# values

| value name | type | description |
| --- | --- | --- |
| `USTEnabled` |  | Windows adds the image file name to this value when "Create user mode stack trace database" (ust, 0x1000) is set for an image file. |

# subkeys

| subkey | description |
| --- | --- |
| `<ImageFileName>\GlobalFlag` | Program-specific global flag settings for the image file. |
| `<ImageFileName>\PageHeapFlags` | Page heap options for an image file. |
| `<ImageFileName>\StackTraceDatabaseSizeInMb` | User mode stack trace database size (tracedb). |
| `<ImageFileName>\UseLargePages` | Load image using large pages if possible. |
| `<ImageFileName>\Debugger` | Debugger command line used to always start the image file in a debugger (for example `ntsd -d -x -g` for WinLogon.exe). |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"` | List the key's values. |
| `reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /v GlobalFlag /s` | Recursively find every image file that has a GlobalFlag entry and show its value. |
