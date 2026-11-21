---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "xbootmgr.exe"
  - "Xbootmgr"
url:
  - https://learn.microsoft.com/windows-hardware/test/wpt/xperf-backward-compatibility-support
  - https://learn.microsoft.com/windows-hardware/test/wpt/windows-performance-toolkit-technical-reference
---

**fullpath**:C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe

# description

Xbootmgr.exe is the legacy on/off transition trace capture tool of the Windows Performance Toolkit (Windows ADK). Windows Performance Recorder (WPR) still supports command-line recordings created with Xperf.exe and Xbootmgr.exe, and Windows Performance Analyzer (WPA) opens them; Xperfview is no longer supported.

## simple description

> ### 2026-11-21 Claude said
> Xbootmgr records performance traces across boot, shutdown, standby and hibernate transitions by configuring tracing, rebooting the machine and collecting ETL files. It is used by engineers to analyze slow boots. Its modern replacement is WPR's On/Off profiles.
>
> **SOC NOTE**: Rarely seen outside lab/OEM machines. It reboots the system and enables kernel tracing, so unexpected use could hide reboots or cause disruption; boot ETL traces it produces can contain detailed process and file activity useful for forensics. Treat execution on production servers as unusual.
>

# purpose

Captures on/off transition traces (boot, shutdown, standby/resume, hibernate/resume) for analysis in WPA. The `-a boot`, `bootprefetch` and `winlogon` Xperf actions summarize such traces.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
