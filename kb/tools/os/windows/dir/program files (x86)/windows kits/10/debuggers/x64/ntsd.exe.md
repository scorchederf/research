---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\ntsd.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - debugger
  - debugging-tools-for-windows
  - lolbin
aliases:
  - ntsd.exe
  - NTSD
  - Microsoft NT Symbolic Debugger
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/cdb-command-line-options
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/debuggers-in-the-debugging-tools-for-windows-package
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/debugging-using-cdb-and-ntsd
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\ntsd.exe

# description

Microsoft NT Symbolic Debugger (NTSD), a user-mode console debugger from Debugging Tools for Windows (Windows SDK/WDK). It is identical to CDB except that it spawns a new console window; related tools are CDB, KD and WinDbg.

## simple description

> ### 2026-11-21 Claude said
> NTSD is a text-based debugger for user-mode programs. It can launch or attach to processes, open dump files, set breakpoints and inspect memory. It has the same options as CDB. It is installed with the Debugging Tools for Windows, not by default.
>
> **SOC NOTE**: Signed Microsoft debugger that can execute shellcode/commands via `-c`/`-cf` scripts or `.shell`, dump process memory such as LSASS (`-pv -p <pid> -c ".dump /ma ..."`), and be registered as AeDebug postmortem debugger for persistence (MITRE ATT&CK T1127, T1003.001, T1546). Treat execution on non-developer systems as suspicious.
>

# purpose

Debugs user-mode processes and dump files, and can act as debugging server/client.

# typical use cases

| usage | description |
| --- | --- |
| `ntsd [parameters]` | Start NTSD in a new console window (equivalent to `start cdb [parameters]`). |
| `ntsd -p PID` | Attach to a running process. |
| `ntsd -z DumpFile` | Open a crash dump file. |
| `ntsd -iae` | Install NTSD as the postmortem debugger. |

# options

| option | description |
| --- | --- |
| `-server ServerTransport` | Create a debugging server; must be first on the command line. |
| `-remote ClientTransport` | Create a debugging client connecting to a running server; must be first. |
| `-premote SmartClientTransport` | Create a smart client connecting to a process server. |
| `-2` | Run a target console application in a new console window. |
| `--` | Debug the Client Server Run-Time Subsystem (CSRSS). |
| `-aExtension` | Set the default extension DLL (default userexts). |
| `-bonc` | Break into the target as soon as the session begins. |
| `-c "command"` | Initial debugger command(s) to run at start-up. |
| `-cf "filename"` | Script file run at start (default ntsd.ini in current directory). |
| `-cfr "filename"` | Script file run at start and on every target restart. |
| `-cimp` | Start with a DbgSrv implicit command line (client side of dbgsrv -pc). |
| `-clines lines` | Approximate number of commands in remote command history. |
| `-d` | Pass control to the kernel debugger; not with `-ddefer` or `-noio`. |
| `-ddefer` | Pass control to the kernel debugger unless a client is connected. |
| `-e Event` | Signal that the event occurred (programmatic start only). |
| `-ee {masm\|c++}` | Default expression evaluator. |
| `-failinc` | Ignore questionable symbols. |
| `-g` | Ignore the initial breakpoint. |
| `-G` | Ignore the final breakpoint at process termination. |
| `-hd` | Do not use the debug heap. |
| `-i ImagePath` | Location of the executables that generated the fault. |
| `-iae` | Install as postmortem debugger. |
| `-iaec KeyString` | Install as postmortem debugger, appending KeyString to the AeDebug key. |
| `-isd` | Set CREATE_IGNORE_SYSTEM_DEFAULT for process creations. |
| `-iu KeyString` | Register debugger remoting as a URL type. |
| `-kqm` | Start in quiet mode. |
| `-lines` | Enable source line debugging. |
| `-log{a\|au\|o\|ou} LogFile` | Log to a file (append/overwrite, optionally Unicode). |
| `-myob` | Continue on dbghelp.dll version mismatch. |
| `-n` | Noisy symbol load. |
| `-netsyms {yes\|no}` | Allow or disallow loading symbols from a network path. |
| `-noinh` | Created processes do not inherit debugger handles. |
| `-noio` | Debugging server not used for input/output. |
| `-noshell` | Prohibit all `.shell` commands. |
| `-nosqm` | Disable telemetry collection and upload. |
| `-o` | Debug all child processes of the target. |
| `-p PID` | Attach to a running process by ID. |
| `-pb` | No initial break-in when attaching. |
| `-pd` | Do not terminate the target at session end. |
| `-pe` | Target is already being debugged (re-attach). |
| `-pn Name` | Attach to a running process by unique name. |
| `-pr` | Resume the target when attaching. |
| `-psn ServiceName` | Attach to the process containing the named service. |
| `-pt Seconds` | Break time-out (default 30). |
| `-pv` | Attach noninvasively. |
| `-pvr` | Like `-pv` but without suspending the target. |
| `-QR Server` | List debugging servers on a network server. |
| `-r BreakErrorLevel` | Error level that breaks into the debugger (checked builds only). |
| `-robp` | Allow breakpoints on read-only memory pages. |
| `-s` | Disable lazy symbol loading. |
| `-sdce` | Show File access error dialogs during symbol load. |
| `-ses` | Strict evaluation of symbol files. |
| `-sflags 0xNumber` | Set all symbol handler options at once. |
| `-sicv` | Ignore the CV record. |
| `-sins` | Ignore symbol and image path environment variables. |
| `-snc` | Turn off C++ translation. |
| `-snul` | Disable automatic symbol loading for unqualified names. |
| `-srcpath SourcePath` | Source file search path. |
| `-sup` | Search the public symbol table on every symbol search. |
| `-t PrintErrorLevel` | Error level that displays an error message (checked builds only). |
| `-v` | Verbose output. |
| `-version` | Print the debugger version string. |
| `-vf` | Enable default Application Verifier settings. |
| `-vf:<opts>` | Enable given Application Verifier settings. |
| `-w` | Debug 16-bit applications in a separate VDM. |
| `-wake PID` | End sleep mode for the user-mode debugger with that PID. |
| `-x{e\|d\|n\|i} Exception` | Control debugger behavior for an exception or event. |
| `-x` | Disable first-chance break on access violations. |
| `-y SymbolPath` | Symbol search path. |
| `-z DumpFile` | Crash dump file to debug (repeatable). |
| `-zp PageFile` | Modified page file for `.pagein`. |
| `executable` | Command line of a new process to launch and debug; must be last. |
| `-?` | Display command-line help. |
