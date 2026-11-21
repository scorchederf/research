---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - debugger
  - windows-kits
aliases:
  - windbg.exe
  - WinDbg
  - WinDbg (Classic)
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/windbg-command-line-options
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/debugging-using-windbg
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe

# description

`windbg.exe` here is WinDbg (Classic), the 64-bit graphical debugger from Debugging Tools for Windows in the Windows SDK/WDK (Windows Kits 10). It debugs user-mode processes, kernel targets and crash dump files; related tools include cdb, kd and the newer WinDbg app.

## simple description

> ### 2026-11-21 Claude said
> WinDbg is Microsoft's debugger for Windows programs, drivers and crash dumps. Developers and support engineers use it to analyse blue screens (.dmp files), attach to running processes or debug the kernel over a cable/network. This copy is the 64-bit classic version installed with the Windows SDK/Driver Kit.
>
> **SOC NOTE**: Being Microsoft-signed, it can attach to processes (e.g. `-pn lsass.exe`) to read memory or inject code, and `-c` runs debugger commands including `.shell` (MITRE T1003.001, T1055, T1218); `-I` installs it as postmortem debugger (AeDebug persistence, T1546.012-like). Flag windbg/cdb on non-developer hosts and attaches to lsass.
>

# purpose

Launches debugging sessions: start and debug a new executable, attach to a running process by PID/name/service, open dump files, start kernel debugging sessions (`-k`, `-kl`, `-kx`), act as remote debugging server/client, and register itself as postmortem debugger or file handler. All options are case-sensitive except `-j`; `-server`/`-remote` must be first and the executable must be last.

# typical use cases

| usage | description |
| --- | --- |
| `windbg myexe arg1 arg2` | Launches myexe with arguments and debugs it. |
| `windbg -p <PID>` | Attaches to a running process by decimal process ID. |
| `windbg -z <DumpFile>` | Opens a crash dump file for analysis. |
| `windbg -y <SymbolPath> -z <DumpFile>` | Opens a dump with a specific symbol path. |
| `windbg -kl` | Starts a local kernel debugging session. |
| `windbg -IS` | Silently installs WinDbg as the postmortem debugger. |

# options

| option | description |
| --- | --- |
| `-server ServerTransport` | Creates a debugging server; must be first on the command line. |
| `-remote ClientTransport` | Creates a debugging client connected to an existing server; must be first. |
| `-premote SmartClientTransport` | Creates a smart client connected to a process server. |
| `-aExtension` | Sets the default extension DLL (no space, no .dll). |
| `-b` | No longer supported. |
| `-c "command"` | Initial debugger command(s) to run at start-up, separated by semicolons. |
| `-clines lines` | Approximate number of commands in history for remote debugging. |
| `-d` | (Kernel mode only) Breaks in as soon as a kernel module loads after reboot. |
| `-ee {masm\|c++}` | Sets the default expression evaluator; MASM is default. |
| `-failinc` | Ignores questionable symbols; won't load unmappable modules in minidumps. |
| `-g` | (User mode only) Ignores the initial breakpoint. |
| `-G` | (User mode only) Ignores the final breakpoint at process termination. |
| `-hd` | (User mode only) Don't use the debug heap. |
| `-I[S]` | Installs WinDbg as postmortem debugger; S = silent. Must be used alone. |
| `-IA[S]` | Associates WinDbg with .dmp, .mdmp and .wew files; S = silent. Must be used alone. |
| `-IU KeyString` | Registers debugger remoting as URL type (`remdbgeng://`). Must be used alone. |
| `-i ImagePath` | Location of the executables that generated the fault. |
| `-j` | Allow journaling. |
| `-k [ConnectType]` | (Kernel mode only) Starts a kernel debugging session. |
| `-kl` | (Kernel mode only) Kernel debugging on the same machine. |
| `-kx ExdiOptions` | (Kernel mode only) Kernel debugging using an EXDI driver. |
| `-log{o\|a} LogFile` | Logs to a file; `-logo` overwrites, `-loga` appends. |
| `-lsrcpath` | Sets the local source path for a remote client; must follow `-remote`. |
| `-n` | Noisy symbol load: verbose symbol handler output. |
| `-noinh` | (User mode only) Created processes don't inherit debugger handles. |
| `-noprio` | Prevents any priority change. |
| `-noshell` | Prohibits all `.shell` commands while the debugger runs. |
| `-o` | (User mode only) Debugs all child processes of the target. |
| `-openPrivateDumpByHandle Handle` | Specifies the handle of a crash dump file to debug. |
| `-p PID` | Decimal process ID to debug (already running). |
| `-pb` | (User mode only) No initial break-in when attaching. |
| `-pd` | (User mode only) Target isn't terminated when the session ends. |
| `-pe` | (User mode only) Target is already being debugged (re-attach). |
| `-pn Name` | Name of the (unique) process to debug. |
| `-pr` | (User mode only) Starts the target running when attaching. |
| `-psn ServiceName` | Name of a service contained in the process to debug. |
| `-pt Seconds` | Break timeout in seconds; default 30. |
| `-pv` | (User mode only) Attaches noninvasively. |
| `-Q` | Suppresses "Save Workspace?"; workspaces not saved. |
| `-QS` | Suppresses "Reload Source?"; sources not reloaded. |
| `-QSY` | Suppresses "Reload Source?" and reloads sources. |
| `-QY` | Suppresses "Save Workspace?" and saves workspaces. |
| `-robp` | Allows breakpoints on read-only memory pages. |
| `-sdce` | Displays File access error messages during symbol load. |
| `-secure` | Activates Secure Mode. |
| `-ses` | Strict evaluation of symbol files. |
| `-sflags 0xNumber` | Sets all symbol handler options at once. |
| `-sicv` | Symbol handler ignores the CV record. |
| `-sins` | Ignores symbol path and image path environment variables. |
| `-snc` | Turns off C++ translation. |
| `-snul` | Disables automatic symbol loading for unqualified names. |
| `-srcpath SourcePath` | Source file search path (semicolon-separated). |
| `-sup` | Searches the public symbol table during every symbol search. |
| `-T Title` | Sets the WinDbg window title. |
| `-v` | Enables verbose output. |
| `-W Workspace` | Loads the named workspace. |
| `-WF Filename` | Loads the workspace from a file (usually .wew). |
| `-WX` | Disables automatic workspace loading. |
| `-y SymbolPath` | Symbol search path (semicolon-separated). |
| `-z DumpFile` | Crash dump file to debug; can be repeated. |
| `-zp PageFile` | Specially-modified page file for use with `.pagein`. |
| `executable` | Command line of a process to launch and debug; must be last. |
| `-?` | Pops up the HTML Help window. |
