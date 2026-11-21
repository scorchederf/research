---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - tools/windbg
aliases:
  - windbg.exe
  - WinDbg (Classic)
  - Microsoft Windows Debugger
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/windbg-command-line-options
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/debuggers-in-the-debugging-tools-for-windows-package
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/enabling-postmortem-debugging
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/debug-universal-drivers---step-by-step-lab--echo-kernel-mode-
  - https://learn.microsoft.com/windows-hardware/drivers/gettingstarted/writing-a-kmdf-driver-based-on-a-template
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe

# description

WinDbg (Classic) is the Microsoft Windows Debugger, a Windows-based GUI debugger for user-mode and kernel-mode debugging, including the Windows kernel, drivers, system services and applications. The x64 build is installed with the Windows Driver Kit / Windows kit installation (Debugging Tools for Windows) at `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64`. It is the graphical counterpart to CDB/NTSD and KD/NTKD; the newer WinDbg (formerly WinDbg Preview) uses the same engine and supports the same commands, extensions and workflows.

## simple description

A graphical Microsoft debugger for analysing crash dumps and debugging live user-mode programs and the Windows kernel.

# purpose

- Debug user-mode applications and kernel-mode components (kernel, drivers, system services).
- Source-level debugging using PDB symbols (Visual Studio symbol formats) and public names from COFF/.dbg symbols.
- View source, set breakpoints, inspect variables (including C++ objects), stack traces and memory; run commands in the Debugger Command window.
- Kernel debugging typically uses two machines (host and target); remote debugging is supported for user- and kernel-mode targets.
- Can be registered as the postmortem (JIT) debugger, and associated with .dmp, .mdmp and .wew files.
- On the host, run the same bitness of debugger as the target (x64 for 64-bit targets, x86 for 32-bit).

# typical use cases

- **Network kernel debugging of a target machine** (after `bcdedit /dbgsettings` on the target):
  `windbg -k net:port=50000,key=1.2.3.4`
- **Set WinDbg as the postmortem debugger** (run from both x64 and x86 folders to cover 64- and 32-bit apps):
  `windbg.exe -I`
  Writes AeDebug `Debugger = "<Path>\WinDbg -p %ld -e %ld -g"` and `Auto = 1`; 32-bit settings live under `HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\AeDebug`.
- **Launch and debug a program with arguments:** `windbg myexe arg1 arg2`
- **Attach to a running process:** `windbg -p <PID>` or `windbg -pn <name>`
- **Open a crash dump:** `windbg -z <DumpFile>`

# options

Syntax notes: options are case-sensitive except `-j`; `/` may replace the leading `-`. `-server`/`-remote` must be first; an *executable* must be last (text after it is passed to the program).

| option    | description    |
| --- | --- |
| `-server ServerTransport` | Creates a debugging server other debuggers can access. Must be first on the command line. |
| `-remote ClientTransport` | Creates a debugging client and connects to a running debugging server. Must be first on the command line. |
| `-premote SmartClientTransport` | Creates a smart client and connects to a running process server. |
| `-aExtension` | Sets the default extension DLL (default kdextx86.dll or kdexts.dll). No space after `a`; omit `.dll`. |
| `-b` | No longer supported. |
| `-c "command"` | Initial debugger command(s) to run at start-up, quoted; separate multiple with semicolons. For a client, must be intended for the server. |
| `-clines lines` | Approximate number of commands in the history accessible during remote debugging. |
| `-d` | (Kernel mode only) After a reboot, breaks into the target as soon as a kernel module is loaded. |
| `-ee {masm\|c++}` | Sets the default expression evaluator; MASM if omitted. |
| `-failinc` | Ignores questionable symbols; with minidumps, also skips modules whose images can't be mapped. |
| `-g` | (User mode only) Ignores the initial breakpoint in the target application. |
| `-G` | (User mode only) Ignores the final breakpoint at process termination; same effect as `sxd epr`. |
| `-hd` | (User mode only) Do not use the debug heap. |
| `-I[S]` | Installs WinDbg as the postmortem debugger; `S` = silent on success. Must be used alone; does not start WinDbg. |
| `-IA[S]` | Associates WinDbg with .dmp, .mdmp and .wew in the registry; `S` = silent on success. Must be used alone. |
| `-IU KeyString` | Registers debugger remoting as a URL type (`remdbgeng://RemotingOption`) to auto-launch a remote client. Must be used alone. |
| `-i ImagePath` | Location of the executables that generated the fault. Quote paths with spaces. |
| `-j` | Allow journaling. |
| `-k [ConnectType]` | (Kernel mode only) Starts a kernel debugging session. Without a ConnectType it must be the final entry. |
| `-kl` | (Kernel mode only) Kernel debugging session on the same machine as the debugger. |
| `-kx ExdiOptions` | (Kernel mode only) Kernel debugging session using an EXDI driver. |
| `-log{o\|a} LogFile` | Logs to a file; `-logo` overwrites, `-loga` appends. |
| `-lsrcpath` | Sets the local source path for a remote client; must follow `-remote`. |
| `-n` | Noisy symbol load: verbose output from the symbol handler. |
| `-noinh` | (User mode only) Processes created by the debugger don't inherit its handles. |
| `-noprio` | Prevents any priority change; WinDbg won't take CPU priority while active. |
| `-noshell` | Prohibits all `.shell` commands for as long as the debugger runs. |
| `-o` | (User mode only) Debugs all child processes launched by the target. |
| `-openPrivateDumpByHandle Handle` | Handle of a crash dump file to debug. |
| `-p PID` | Decimal process ID of a running process to debug. |
| `-pb` | (User mode only) No initial break-in request when attaching; avoids creating a break-in thread. |
| `-pd` | (User mode only) Target is not terminated at the end of the session. |
| `-pe` | (User mode only) Indicates the target is already being debugged (re-attach). |
| `-pn Name` | Name of a running process to debug (must be unique). |
| `-pr` | (User mode only) Starts the target running on attach (resume a suspended app). |
| `-psn ServiceName` | Name of a service in the running process to debug. |
| `-pt Seconds` | Break timeout in seconds (default 30). |
| `-pv` | (User mode only) Attach to the target noninvasively. |
| `-Q` | Suppresses "Save Workspace?"; workspaces not saved automatically. |
| `-QS` | Suppresses "Reload Source?"; sources not reloaded automatically. |
| `-QSY` | Suppresses "Reload Source?" and reloads sources automatically. |
| `-QY` | Suppresses "Save Workspace?" and saves workspaces automatically. |
| `-robp` | Allows a breakpoint on a read-only memory page (default fails). |
| `-sdce` | Displays **File access error** messages during symbol load. |
| `-secure` | Activates Secure Mode. |
| `-ses` | Strict evaluation of all symbol files; ignores questionable symbols. |
| `-sflags 0xNumber` | Sets all symbol handler options at once (hex recommended); overrides all defaults. |
| `-sicv` | Symbol handler ignores the CV record. |
| `-sins` | Ignores symbol path and executable image path environment variables. |
| `-snc` | Turns off C++ translation. |
| `-snul` | Disables automatic symbol loading for unqualified names. |
| `-srcpath SourcePath` | Source file search path; separate with `;`, quote paths with spaces. |
| `-sup` | Searches the public symbol table during every symbol search. |
| `-T Title` | Sets the WinDbg window title. |
| `-v` | Verbose debugger output. |
| `-W Workspace` | Loads the named workspace (offers to create it if missing). |
| `-WF Filename` | Loads the workspace from a file (usually .wew). |
| `-WX` | Disables automatic workspace loading. |
| `-y SymbolPath` | Symbol search path; separate with `;`, quote paths with spaces. |
| `-z DumpFile` | Crash dump file to debug; repeat `-z` to open several. |
| `-zp PageFile` | Specially modified page file for use with `.pagein` (not a standard page file). |
| `executable` | Command line of a process to launch and debug; must be last, remaining text passed as its arguments. |
| `-?` | Pops up the HTML Help window. |
