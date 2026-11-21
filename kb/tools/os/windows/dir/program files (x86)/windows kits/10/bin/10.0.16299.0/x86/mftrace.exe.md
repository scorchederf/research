---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x86\mftrace.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-sdk
  - media-foundation
  - tracing
aliases:
  - 'mftrace.exe'
  - 'MFTrace'
url:
  - https://learn.microsoft.com/windows/win32/medfound/using-mftrace
  - https://learn.microsoft.com/windows/win32/medfound/mftrace-keywords
  - https://learn.microsoft.com/windows/win32/medfound/mftrace
---

**fullpath**: C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x86\mftrace.exe

# description

MFTrace is a Windows SDK tool for generating trace logs for Microsoft Media Foundation applications. It uses the Detours library to hook Media Foundation API calls and can also record ETW and WPP traces, either by starting a new process or attaching to an existing one. Output goes to stdout, a text file or an ETL file.

## simple description

> ### 2026-11-21 Claude said
> mftrace is a developer tool from the Windows SDK that records what a media (audio/video) application does inside Media Foundation. It can launch a program or attach to a running one and log the API calls it makes. It can also convert saved ETL trace files to text.
>
> **SOC NOTE**: It injects a Detours hooking DLL into target processes (`-a <PID or name>`) and can launch arbitrary commands, so it can act as a signed proxy-execution / code-injection tool (T1218, T1055). Its presence is expected only on developer machines; execution elsewhere or attaching to sensitive processes is suspicious.
>

# purpose

Generates trace logs (Detours, ETW, WPP) for Media Foundation applications and converts ETL files to text.

# typical use cases

| usage | description |
| --- | --- |
| `mftrace.exe wmplayer.exe Wildlife.wmv` | Create a new process and trace it. |
| `mftrace.exe -a wmplayer.exe` | Attach to an existing process by name. |
| `mftrace.exe -a 9132` | Attach to an existing process by PID. |
| `mftrace.exe -a wmplayer.exe -o trace.txt` | Send trace output to a text file. |
| `mftrace.exe -c config.xml -o trace.etl` | Trace ETW or WPP events to an ETL file. |
| `mftrace.exe -o trace.txt trace.etl` | Convert an ETL file to a text file. |

# options

| option | description |
| --- | --- |
| `-a <Process ID or Process Name>` | Attach to a running process. |
| `-c <Configuration File>` | Read settings from the specified configuration file. |
| `-dc` | Disable tracing for child processes (enabled by default). |
| `-es` | Enable public symbols. |
| `-k <Keywords>` | Comma-separated list of keywords to filter traces. |
| `-l <Level>` | Trace level: 0 None, 1 Critical, 2 Error, 3 Warning, 4 Informative, 5 Verbose, 16 Debug. |
| `-o <Output File>` | Write output to a .etl, .log or .txt file (default stdout). |
| `-v` | Enable verbose mode. |
| `-?` | Display usage information. |
| `COMMAND` | Command-line arguments to create a new process. |
| `ETL_FILE` | Existing ETL file to convert to text output. |
