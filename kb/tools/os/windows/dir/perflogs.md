---
created: 2026-11-21
fullpath: 'C:\PerfLogs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - performance
aliases:
  - PerfLogs
url:
  - https://learn.microsoft.com/windows-server/identity/ad-fs/deployment/configure-performance-monitoring
  - https://learn.microsoft.com/troubleshoot/windows-server/support-tools/troubleshoot-issues-performance-monitor
---

**fullpath**:C:\PerfLogs

# description

C:\PerfLogs is the default root for Performance Monitor data collector set output; the wizard defaults to `%systemdrive%\PerfLogs\Admin\<data_collector_set>`. It is used by Performance Monitor (perfmon) and logman, whose traces are stored under `c:\perflogs\Admin`.

## simple description

> ### 2026-11-21 Claude said
> PerfLogs is a folder at the root of the system drive created by Windows for Performance Monitor logs. It is usually empty unless someone runs data collector sets or logman traces. It exists on every default Windows install.
>
> **SOC NOTE**: Because it is a little-used, admin-created folder at the drive root, attackers often stage tools and data in C:\PerfLogs (MITRE ATT&CK T1074.001 Local Data Staging, T1036.005 masquerading in a trusted location). Any .exe, .dll, .ps1, .bat or archive here is suspicious; legitimate content is usually .blg/.etl/.csv logs in Admin or System subfolders.
>

# purpose

Default storage location for Performance Monitor data collector set logs.

# common files found

| path | description |
| --- | --- |
| `Admin\<data_collector_set>` | Default output folder for user-defined data collector sets. |
| `*.blg` | Performance Monitor binary log files produced by logman and data collector sets. |

