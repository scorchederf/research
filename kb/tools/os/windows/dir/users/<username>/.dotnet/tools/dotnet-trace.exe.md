---
created: 2026-11-21
fullpath: 'C:\Users\<username>\.dotnet\tools\dotnet-trace.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - diagnostics
  - lolbin
aliases:
  - "dotnet-trace.exe"
  - "dotnet-trace"
url:
  - https://learn.microsoft.com/dotnet/core/diagnostics/dotnet-trace
  - https://learn.microsoft.com/dotnet/core/diagnostics/tools-overview
  - https://learn.microsoft.com/dotnet/core/diagnostics/eventsource-collect-and-view-traces
---

**fullpath**:C:\Users\<username>\.dotnet\tools\dotnet-trace.exe

# description

dotnet-trace is a cross-platform .NET diagnostic tool that collects traces of a running .NET process without a native profiler, built on the runtime's EventPipe. It is installed as a .NET global tool with `dotnet tool install --global dotnet-trace` (which places it in the user's `.dotnet\tools` folder) or downloaded directly; related tools include dotnet-counters, dotnet-dump, dotnet-gcdump and PerfView.

## simple description

> ### 2026-11-21 Claude said
> dotnet-trace is a developer tool for recording performance and diagnostic events from .NET applications. This path is where .NET global tools are installed per user, so its presence means someone ran `dotnet tool install -g dotnet-trace`. Traces are saved as .nettrace files that can be opened in Visual Studio or PerfView.
>
> **SOC NOTE**: dotnet-trace can attach to any .NET process running as the same user and record events, which can expose sensitive data (for example SQL command text or connection strings via DiagnosticSource providers) (T1005/T1119). It can also launch arbitrary programs with `collect -- <command>` (proxy execution). Unexpected installs on non-developer endpoints or .nettrace files in odd locations deserve review.
>

# purpose

Collects, converts and reports on .NET EventPipe traces: `collect` from a running process or a launched child process, `collect-linux` for machine-wide Linux traces, `convert` to Chromium/Speedscope, `ps` to list .NET processes, `list-profiles` and `report`.

# typical use cases

| usage | description |
| --- | --- |
| `dotnet tool install --global dotnet-trace` | Install dotnet-trace as a global tool. |
| `dotnet-trace ps` | List .NET processes that can be traced. |
| `dotnet-trace collect --process-id <PID>` | Collect a trace from a running process until Enter is pressed. |
| `dotnet-trace collect -- hello.exe arg1 arg2` | Launch hello.exe and trace it from runtime startup. |
| `dotnet-trace collect --diagnostic-port myport.sock` | Wait for an app started with DOTNET_DiagnosticPorts to connect and trace it. |
| `dotnet-trace @myprofile.rsp` | Run dotnet-trace with arguments read from a response file. |

# options

| option | description |
| --- | --- |
| `-h\|--help` | Shows command-line help. |
| `--version` | Displays the version of the dotnet-trace utility. |
| `collect --buffering-mode <Drop\|Block>` | Sets how the runtime buffers events; Drop (default) drops events on overflow, Block makes threads wait (requires .NET 11+ target). |
| `collect --buffersize <size>` | Size of the in-memory buffer in MB; default 256 MB. |
| `collect --clreventlevel <clreventlevel>` | Verbosity of CLR events (logalways, critical, error, warning, informational, verbose); applies only with --clrevents. |
| `collect --clrevents <clrevents>` | CLR runtime provider keywords separated by + (for example gc+gchandle); ignored if the runtime provider is set via --providers or --profile. |
| `collect --dsrouter {ios\|ios-sim\|android\|android-emu}` | Starts dotnet-dsrouter and connects to it. |
| `collect --format {Chromium\|NetTrace\|Speedscope}` | Output format for the trace; default NetTrace. |
| `collect -n, --name <name>` | Name of the process to collect the trace from. |
| `collect --diagnostic-port <port-address[,(listen\|connect)]>` | Sets the diagnostic port (named pipe on Windows) used to communicate with the traced process. |
| `collect --duration <dd:hh:mm:ss>` | Time for the trace to run. |
| `collect -o\|--output <trace-file-path>` | Output path; default `<appname>_<yyyyMMdd>_<HHmmss>.nettrace`. |
| `collect -p\|--process-id <PID>` | Process ID to collect the trace from. |
| `collect --profile <names>` | Predefined provider sets: dotnet-common, dotnet-sampled-thread-time, gc-verbose, gc-collect, database. |
| `collect --providers <providers>` | Comma-separated EventPipe providers in the form `KnownProviderName[:Flags[:Level[:KeyValueArgs]]]`. |
| `collect -- <command>` | Launches a .NET 5+ application as a child process and traces it from startup. |
| `collect --show-child-io` | Shows the input and output streams of the launched child process. |
| `collect --resume-runtime` | Resumes the runtime once the session is initialized; default true. |
| `collect --stopping-event-provider-name` | Stops the trace on the first event from the matching provider. |
| `collect --stopping-event-event-name` | Stops the trace on the matching event name; requires the provider name option. |
| `collect --stopping-event-payload-filter` | Stops the trace on an event containing all specified payload field:value pairs; requires provider and event name. |
| `collect-linux ...` | Linux-only (kernel 6.4+, root) machine-wide collection with --providers, --clreventlevel, --clrevents, --perf-events, --profile, -o, --duration, -n, -p and --probe. |
| `convert [<input-filename>] --format <Chromium\|NetTrace\|Speedscope>` | Converts a nettrace file to another format; default input trace.nettrace. |
| `convert -o\|--output <output-filename>` | Output filename; the target format extension is added. |
| `ps` | Lists .NET processes that traces can be collected from, with command-line arguments. |
| `list-profiles` | Lists pre-built tracing profiles and their providers. |
| `report <tracefile> topN -n\|--number <n>` | Reports the top N methods that have been on the callstack the longest. |
| `report <tracefile> topN --inclusive` | Uses inclusive time instead of exclusive time. |
| `report <tracefile> topN -v\|--verbose` | Outputs method parameters in full. |
