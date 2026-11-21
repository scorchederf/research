---
created: 2026-11-21
fullpath: 'C:\Program Files\dotnet\shared\Microsoft.NETCore.App\<version>\createdump.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - createdump.exe
  - createdump
url:
  - https://learn.microsoft.com/troubleshoot/developer/webapps/aspnetcore/practice-troubleshoot-linux/3-3-debuggers-collect-core-dumps
  - https://learn.microsoft.com/troubleshoot/developer/webapps/aspnetcore/practice-troubleshoot-linux/lab-2-1-capture-dumps-createdump
  - https://learn.microsoft.com/troubleshoot/developer/webapps/aspnetcore/practice-troubleshoot-linux/lab-1-3-capture-core-crash-dumps
  - https://learn.microsoft.com/dotnet/core/diagnostics/collect-dumps-crash
---

**fullpath**:C:\Program Files\dotnet\shared\Microsoft.NETCore.App\<version>\createdump.exe

# description

createdump is the .NET (Core) dump-collection utility installed with every .NET Core runtime, in the runtime directory (find it with `dotnet --list-runtimes`). The runtime invokes it to write crash dumps when `DOTNET_DbgEnableMiniDump` / `COMPlus_DbgEnableMiniDump` is set, and it can be run manually; related tools are dotnet-dump and ProcDump.

## simple description

> ### 2026-11-21 Claude said
> createdump.exe ships inside every .NET runtime folder and writes a memory dump of a .NET process, either on demand (`createdump <PID>`) or automatically when an app crashes and dump settings are enabled. It is Microsoft-signed and lives next to coreclr.dll. Developers use the dumps to debug crashes and hangs.
>
> **SOC NOTE**: Because it can dump any process the user can open, createdump.exe is a known LOLBin for credential dumping: `createdump.exe -u -f out.dmp <lsass PID>` (MITRE ATT&CK T1003.001). Alert on createdump targeting lsass or non-.NET processes, on copies outside the dotnet folder, and on large .dmp files created by it.
>

# purpose

Generates dump files of .NET processes that include the managed state, so SOS / dotnet-dump commands can resolve type and function names. It produces minimally sized minidumps, works for non-root users, captures on-demand or crash dumps, and detects most stack overflow failures.

# typical use cases

| usage | description |
| --- | --- |
| `createdump <PID>` | Write one dump of the target process. |
| `createdump <PID> -f <filepath>` | Write the dump to the specified file path (`%d` inserts the PID). |
| `set DOTNET_DbgEnableMiniDump=1` | Enable automatic dump generation by the runtime on crash. |

# options

| option    | description    |
| --- | --- |
| `<PID>` | Process ID of the target process. |
| `-f <filepath>` | Path/file name template for the dump file. |
