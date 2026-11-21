---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "cdb.exe"
  - "CDB"
  - "NTSD"
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/cdb-command-line-options
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe

# description

CDB is the console user-mode debugger in Debugging Tools for Windows (Windows SDK/WDK). Its command-line syntax is identical to NTSD; the only difference is that NTSD spawns a new console window while CDB inherits the invoking window. It can act as a debugging server, client or smart client for DbgSrv.

## simple description

> ### 2026-11-21 Claude said
> CDB is Microsoft's command-line debugger for user-mode programs. It can launch or attach to a process, read and change its memory, run debugger scripts, and open crash dumps. Developers use it for scripted debugging and remote debugging. It is signed by Microsoft.
>
> **SOC NOTE**: A well-known LOLBin: `cdb.exe -cf script.txt target.exe` or `-c` can run attacker shellcode in a process, and attaching to lsass enables credential dumping (MITRE ATT&CK T1218, T1055, T1003.001). `-iae`/`-iaec` set the AeDebug postmortem debugger, a persistence trick (T1546.012-style). Alert on cdb.exe on non-developer hosts and on AeDebug registry changes.
>

# purpose

Debugs user-mode processes and dump files from the console. Only `-remote`, `-server`, `-g` and `-G` are case-sensitive; the hyphen can be replaced with `/`; parameterless options can be concatenated (`cdb -odGg winmine`). `-remote`/`-server` must be first, and an executable must be last (any text after it is passed to the program).

# typical use cases

| usage | description |
| --- | --- |
| `cdb myexe arg1 arg2` | Launches myexe with arguments under the debugger. |
| `cdb -p PID` | Attaches to a running process by PID. |
| `cdb -z DumpFile` | Opens a user-mode crash dump. |
| `cdb -iae` | Installs CDB as the postmortem debugger. |
| `start cdb [parameters]` | Same as ntsd [parameters]: runs CDB in a new console window. |

# options

| option | description |
| --- | --- |
| `-server ServerTransport` | Creates a debugging server; must be the first parameter. |
| `-remote ClientTransport` | Creates a debugging client and connects to a running debugging server; must be first. |
| `-premote SmartClientTransport` | Creates a smart client and connects to a running process server. |
| `-2` | Runs a console target application in a new console window. |
| `--` | Debugs the Client Server Run-Time Subsystem (CSRSS). |
| `-aExtension` | Sets the default extension DLL (default userexts). |
| `-bonc` | Breaks into the target as soon as the session begins. |
| `-c "command"` | Specifies the initial debugger command(s) to run at start-up. |
| `-cf "filename"` | Script file executed when the debugger starts (default ntsd.ini in current directory). |
| `-cfr "filename"` | Script file executed at start and every time the target restarts. |
| `-cimp` | Starts with a DbgSrv implicit command line (client side of dbgsrv -pc). |
| `-clines lines` | Sets the approximate number of commands in history accessible during remote debugging. |
| `-d` | Passes control of this debugger to the kernel debugger. Not with -ddefer or -noio. |
| `-ddefer` | Passes control to the kernel debugger unless a debugging client is connected. |
| `-e Event` | Signals that the specified event occurred; used when starting the debugger programmatically. |
| `-ee {masm\|c++}` | Sets the default expression evaluator (default MASM). |
| `-failinc` | Ignores questionable symbols; with minidumps, does not load modules whose images can't be mapped. |
| `-g` | Ignores the initial breakpoint in the target application. |
| `-G` | Ignores the final breakpoint at process termination (same as sxd epr). |
| `-hd` | Specifies that the debug heap should not be used. |
| `-i ImagePath` | Specifies the location of the executables that generated the fault. |
| `-iae` | Installs CDB as the postmortem debugger; must be used alone. |
| `-iaec KeyString` | Installs CDB as postmortem debugger and appends KeyString to the AeDebug registry key; used alone. |
| `-isd` | Turns on the CREATE_IGNORE_SYSTEM_DEFAULT flag for any process creations. |
| `-iu KeyString` | Registers debugger remoting as a URL type (remdbgeng://); used alone. |
| `-kqm` | Starts CDB/NTSD in quiet mode. |
| `-lines` | Enables source line debugging. |
| `-log{a\|au\|o\|ou} LogFile` | Logs to a file; a = append, o = overwrite, u = Unicode. |
| `-myob` | Continues running if there is a version mismatch with dbghelp.dll. |
| `-n` | Noisy symbol load: verbose output from the symbol handler. |
| `-netsyms {yes\|no}` | Allows or disallows loading symbols from a network path. |
| `-noinh` | Prevents processes created by the debugger from inheriting handles. |
| `-noio` | Prevents the debugging server from being used for input or output. |
| `-noshell` | Prohibits all .shell commands. |
| `-nosqm` | Disables telemetry data collection and upload. |
| `-o` | Debugs all child processes launched by the target. |
| `-p PID` | Specifies the decimal process ID of a running process to debug. |
| `-pb` | Prevents the initial break-in when attaching to a target process. |
| `-pd` | Does not terminate the target at the end of the debugging session. |
| `-pe` | Indicates that the target application is already being debugged. |
| `-pn Name` | Specifies the (unique) name of a running process to debug. |
| `-pr` | Starts the target process running when the debugger attaches. |
| `-psn ServiceName` | Specifies the name of a service contained in the process to debug. |
| `-pt Seconds` | Specifies the break time-out in seconds (default 30). |
| `-pv` | Attaches to the target process noninvasively. |
| `-pvr` | Like -pv but the target process is not suspended. |
| `-QR Server` | Lists all debugging servers on the specified network server; used alone. |
| `-r BreakErrorLevel` | Error level (0-3) that causes the target to break; only meaningful on checked builds. |
| `-robp` | Allows setting a breakpoint on a read-only memory page. |
| `-s` | Disables lazy symbol loading. |
| `-sdce` | Displays File access error dialog boxes during symbol load. |
| `-ses` | Performs strict evaluation of all symbol files. |
| `-sflags 0xNumber` | Sets all symbol handler options at once. |
| `-sicv` | Ignores the CV record. |
| `-sins` | Ignores the symbol path and executable image path environment variables. |
| `-snc` | Turns off C++ translation. |
| `-snul` | Disables automatic symbol loading for unqualified names. |
| `-srcpath SourcePath` | Specifies the source file search path. |
| `-sup` | Searches the public symbol table during every symbol search. |
| `-t PrintErrorLevel` | Error level (0-3) that causes an error message to display; checked builds only. |
| `-v` | Enables verbose output. |
| `-version` | Prints the debugger version string. |
| `-vf` | Enables default ApplicationVerifier settings. |
| `-vf:<opts>` | Enables given ApplicationVerifier settings. |
| `-w` | Debugs 16-bit applications in a separate VDM. |
| `-wake PID` | Ends sleep mode for the user-mode debugger with that PID; used alone. |
| `-x{e\|d\|n\|i} Exception` | Controls debugger behaviour for the specified exception or event. |
| `-x` | Disables first-chance break on access violations (same as -xd av). |
| `-y SymbolPath` | Specifies the symbol search path. |
| `-z DumpFile` | Specifies a crash dump file to debug; can be repeated. |
| `-zp PageFile` | Specifies a modified page file for use with .pagein. |
| `executable` | Command line of a process to launch and debug; must be last. |
| `-?` | Displays command-line help text. |
