---
created: 2026-11-21
fullpath: 'C:\Windows'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
aliases:
  - Windows
  - %WINDIR%
  - %SystemRoot%
url:
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-setup-log-files-and-event-logs?view=windows-11
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files
---

**fullpath**:C:\Windows

# description

`C:\Windows` is the Windows installation directory, referenced by the `%WINDIR%` / `%SystemRoot%` environment variables. It contains the operating system binaries (System32), registry hive files (`System32\Config`), setup and servicing logs, and folders used by components such as Configuration Manager (`CCM`).

## simple description

> ### 2026-11-21 Claude said
> C:\Windows is the main operating system folder. It holds Windows' own programs and DLLs (System32, SysWOW64), drivers, fonts, the registry hive files, logs and temporary files. Normal users can read most of it but cannot write to it.
>
> **SOC NOTE**: Malware often hides by copying itself into C:\Windows or its subfolders with system-like names (MITRE ATT&CK T1036.005 Match Legitimate Name or Location). Watch for executables in writable subfolders like C:\Windows\Temp and C:\Windows\Tasks, misspelled names, and system binaries running from the wrong path. Key artifacts here include Prefetch, the registry hives, event logs (System32\winevt\Logs) and Panther setup logs.
>

# purpose

Holds the installed operating system and its data. Learn documents several log and data locations under it: Windows Setup logs in `%WINDIR%\Panther`, Plug and Play install logs in `%WINDIR%\Inf\Setupapi*.log`, bug-check memory dumps at `%WINDIR%\Memory.dmp`, Sysprep logs in `%WINDIR%\System32\Sysprep\Panther`, and most registry hive supporting files in `%SystemRoot%\System32\Config`.

# common files found

| file | description |
| --- | --- |
| `Panther` | Windows Setup action logs after disk configuration (and Setup.etl performance events). |
| `Inf\Setupapi*.log` | Plug and Play device installation logs. |
| `Memory.dmp` | Memory dump from bug checks. |
| `System32\Sysprep\Panther` | Sysprep logs. |
| `System32\Config` | Supporting files for most registry hives (SAM, SECURITY, SOFTWARE, SYSTEM, DEFAULT). |
| `CCM\Logs` | Configuration Manager client logs, when the client is installed. |
