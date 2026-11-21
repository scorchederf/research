---
created: 2026-11-21
fullpath: 'C:\Windows\System32\fltMC.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - filter-manager
  - minifilter
aliases:
  - fltMC.exe
  - Fltmc.exe
  - fltmc
url:
  - https://learn.microsoft.com/windows-hardware/drivers/ifs/development-and-testing-tools
  - https://learn.microsoft.com/windows-hardware/drivers/ifs/loading-and-unloading
  - https://learn.microsoft.com/windows-hardware/drivers/ifs/when-the-filterunloadcallback-routine-is-called
---

**fullpath**:C:\Windows\System32\fltMC.exe

# description

Fltmc.exe is a system-supplied command-line utility for common Filter Manager (FltMgr) minifilter driver management operations: loading and unloading minifilters, attaching or detaching them from volumes, and enumerating minifilters, instances and volumes. Related tools are Fsutil.exe, the !fltkd debugger extension and Filter Verifier.

## simple description

> ### 2026-11-21 Claude said
> fltmc.exe manages file system minifilter drivers, the kernel drivers that sit on top of file systems (antivirus, EDR, backup, encryption, Sysmon). It can list loaded filters and their altitudes, and load or unload them. It needs an elevated prompt. Admins use it to see which security products are hooking disk I/O.
>
> **SOC NOTE**: Attackers run `fltmc unload <filter>` (e.g. SysmonDrv, WdFilter) to blind security tools (MITRE ATT&CK T1562.001), and plain `fltmc` listing for security software discovery (T1518.001). Alert on fltmc.exe with unload or detach arguments and on Sysmon Event 255 / unexpected filter unloads.
>

# purpose

Performs minifilter management from an administrator command prompt. `fltmc load` is an explicit load request (like FilterLoad); `fltmc unload` is a non-mandatory unload that the minifilter FilterUnloadCallback can refuse; `fltmc attach` / `fltmc detach` create or tear down instances on a volume.

# typical use cases

| usage | description |
| --- | --- |
| `fltmc help` | Show the full list of commands (administrator prompt). |
| `fltmc load <filter>` | Explicitly load a minifilter. |
| `fltmc unload <filter>` | Request a non-mandatory unload of a minifilter. |
| `fltmc attach <filter> <volume>` | Attach a minifilter instance to a volume. |
| `fltmc detach <filter> <volume>` | Detach a minifilter instance from a volume. |

# options

| option | description |
| --- | --- |
| `load` | Load a minifilter driver. |
| `unload` | Unload a minifilter driver; the minifilter may refuse a non-mandatory unload. |
| `attach` | Attach a minifilter instance to a volume. |
| `detach` | Detach a minifilter instance from a volume. |
| `help` | Display the full list of commands. |
