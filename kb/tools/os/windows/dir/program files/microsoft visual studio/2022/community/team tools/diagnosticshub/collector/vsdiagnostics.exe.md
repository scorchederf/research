---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Visual Studio\2022\Community\Team Tools\DiagnosticsHub\Collector\VSDiagnostics.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visual-studio
  - profiling
aliases:
  - 'VSDiagnostics.exe'
  - 'Visual Studio Diagnostics CLI'
url:
  - https://learn.microsoft.com/visualstudio/profiling/profile-apps-from-command-line?view=visualstudio
  - https://learn.microsoft.com/visualstudio/profiling/running-profiling-tools-with-or-without-the-debugger?view=visualstudio
---

**fullpath**: C:\Program Files\Microsoft Visual Studio\2022\Community\Team Tools\DiagnosticsHub\Collector\VSDiagnostics.exe

# description

Command-line collector of the Visual Studio profiling tools, shipped with Visual Studio and the Remote Tools for Visual Studio. It attaches to or launches a process with a collection agent (configured by JSON files in `Collector\AgentConfigs`) and exports data to a `.diagsession` file opened in Visual Studio. Related tool: VSInstr.exe for instrumentation.

## simple description

> ### 2026-11-21 Claude said
> VSDiagnostics.exe lets developers profile an application (CPU usage, .NET memory allocations, instrumentation, database queries) from the command line without opening Visual Studio. You start a numbered session, attach to a process ID or launch an executable, then stop it to write a .diagsession file. It is installed with Visual Studio or the Remote Tools.
>
> **SOC NOTE**: Signed Microsoft binary that can attach to arbitrary processes and launch executables (`/launch:`), so it can act as a proxy-execution LOLBin (T1218) and read process data. Unexpected use on servers or by non-developers, or `start ... /launch:` of unusual binaries, warrants review. Collection agents load DLLs by CLSID from config files - a tampered AgentConfigs JSON could load a malicious DLL.
>

# purpose

Collects performance data (CPU Usage, .NET Object Allocation, Instrumentation, Database) from a process and writes it to a .diagsession file.

# typical use cases

| usage | description |
| --- | --- |
| `VSDiagnostics.exe start 1 /attach:<pid> /loadConfig:AgentConfigs\CPUUsageLow.json` | Start session 1 and attach the CPU Usage (low sampling) agent to a process. |
| `VSDiagnostics start <id> /launch:<ExeToProfile> /loadConfig:AgentConfigs\PerfInstrumentation.json` | Launch an executable and collect instrumentation data. |
| `VSDiagnostics.exe stop <id> /output:<path to file>` | Stop the session and write the .diagsession file. |

# options

| option | description |
| --- | --- |
| `start <id>` | Starts a collection session; id must be a number between 1-255. |
| `/attach:<pid>` | PID of the process to profile. |
| `/launch:<ExeToProfile>` | Starts an executable instead of attaching; supported by all tools (some, like Instrumentation and .NET Allocation, don't support attach). |
| `/loadConfig:<configFile>` | Configuration file for the collection agent to launch. |
| `stop <id>` | Stops the collection session. |
| `/output:<path>` | Output .diagsession file for stop. |
