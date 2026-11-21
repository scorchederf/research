---
created: 2026-11-21
fullpath: 'C:\Users\<username>\.dotnet\tools\dotnet-counters.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - dotnet
  - diagnostics
aliases:
  - "dotnet-counters.exe"
  - "dotnet-counters"
url:
  - https://learn.microsoft.com/dotnet/core/diagnostics/dotnet-counters
---

**fullpath**:C:\Users\<username>\.dotnet\tools\dotnet-counters.exe

# description

dotnet-counters is a .NET global tool for ad-hoc health monitoring and first-level performance investigation, observing counters published through the EventCounter or Meter APIs. This path is where `dotnet tool install --global dotnet-counters` places it for the user. Related tools: dotnet-trace, PerfView.

## simple description

> ### 2026-11-21 Claude said
> dotnet-counters is a Microsoft diagnostic tool that shows live performance numbers (CPU, GC, exceptions, requests) for running .NET applications. It is installed per user as a .NET global tool, which is why it lives in the user's .dotnet\tools folder. Developers use it to check app health before deeper profiling.
>
> **SOC NOTE**: Low abuse potential, but it attaches to other .NET processes via the diagnostics IPC (named pipe), so unexpected use on servers may indicate reconnaissance of running apps. Executables in user-profile tool folders bypass Program Files ACLs; verify signature/hash if found on non-developer machines.
>

# purpose

Monitors or collects performance counter values from .NET processes, either attaching by process ID/name or launching an app as a child process, and lists monitorable .NET processes.

# typical use cases

| usage | description |
| --- | --- |
| `dotnet-counters ps` | List the .NET processes that can be monitored. |
| `dotnet-counters monitor --process-id 1902 --refresh-interval 3` | Show refreshing System.Runtime counters for a process every 3 seconds. |
| `dotnet-counters collect --process-id 1902 --refresh-interval 3 --format csv` | Collect counters to a CSV file. |
| `dotnet-counters collect --format json --counters System.Runtime,Microsoft.AspNetCore.Hosting -- dotnet mvc.dll` | Launch an app as a child process and collect runtime and ASP.NET Core counters from startup to JSON. |

# options

| option | description |
| --- | --- |
| `--version` | Displays the version of the dotnet-counters utility. |
| `-h\|--help` | Shows command-line help. |
| `collect` | Periodically collect selected counter values and export them to a file format for post-processing. |
| `monitor` | Display periodically refreshing values of selected counters. |
| `ps` | List the dotnet processes that can be monitored. |
| `-p\|--process-id <PID>` | ID of the process to collect from or monitor (collect, monitor). |
| `-n\|--name <name>` | Name of the process to collect from or monitor (collect, monitor). |
| `--diagnostic-port` | Diagnostic port used to communicate with the process (named pipe on Windows); used to monitor from app startup (collect, monitor). |
| `--refresh-interval <SECONDS>` | Seconds to delay between updating the displayed counters (collect, monitor). |
| `--counters <COUNTERS>` | Comma-separated list of counters as provider_name[:counter_name] (collect, monitor). |
| `--format <csv\|json>` | Export format (collect only). |
| `-o\|--output <output>` | Name of the output file (collect only). |
| `-- <command>` | Launch a .NET application with the given command and monitor/collect from it (collect, monitor). |
