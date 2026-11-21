---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\dbgsrv.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "dbgsrv.exe"
  - "DbgSrv"
  - "process server"
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/dbgsrv-command-line-options
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/activating-a-process-server
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\dbgsrv.exe

# description

DbgSrv (dbgsrv.exe) is the user-mode process server included in Debugging Tools for Windows (Windows SDK/WDK debuggers). A smart client such as CDB, NTSD or WinDbg connects to it with `-premote` to debug processes on the remote machine. It supports NPIPE, TCP, COM, SPIPE and SSL transports.

## simple description

> ### 2026-11-21 Claude said
> DbgSrv is a small Microsoft-signed server that lets a debugger on another computer attach to and control processes on this computer. It listens on a named pipe or TCP port, and can also start a new process (optionally suspended). It is mostly used by developers for remote debugging.
>
> **SOC NOTE**: Because it is Microsoft-signed and can create processes and give remote memory read/write access, dbgsrv is a known LOLBin: `dbgsrv.exe -t tcp:port=1234` opens a remote control channel, and `-c` can launch arbitrary commands (T1218 System Binary Proxy Execution, T1055 injection via debugger, T1003 credential dumping by attaching to LSASS). Its `IcfEnable` parameter opens firewall ports. Hunt for dbgsrv outside developer machines, new listening ports, and debugger attaches to lsass.exe.
>

# purpose

Activates a process server so smart clients can debug user-mode processes remotely. Run from an elevated prompt so clients can discover it. Transport parameters (for `-t`) include `pipe=`, `port=` (single or range), `clicon=` (reverse connection), `baud=`, `channel=`, `proto=`, `certuser=`/`machuser=`, `hidden`, `password=`, `ipversion=6` and `IcfEnable`, which opens the firewall ports and does not close them afterwards.

# typical use cases

| usage | description |
| --- | --- |
| `dbgsrv -t tcp:port=Socket` | Starts a process server listening on a TCP port. |
| `dbgsrv -t npipe:pipe=PipeName` | Starts a process server on a named pipe. |
| `dbgsrv -t <ServerTransport> -cs AppCmdLine` | Creates a new process suspended so a smart client (CDB with -pb -p PID) can attach. |
| `dbgsrv -t <ServerTransport> -pc notepad.exe` | Sets an implicit command line; `ntsd -premote <Transport> -cimp` then launches notepad.exe. |

# options

| option | description |
| --- | --- |
| `-t ServerTransport` | Specifies the transport protocol (see Activating a Process Server). |
| `-sifeo Executable` | Suspends the Image File Execution Option (IFEO) value for the given image so DbgSrv can be the IFEO debugger without recursion. Only with -c. |
| `-c` | Creates a new process; it is not debugged at creation, attach with -p from the smart client. |
| `s` | With -c (`-cs`), the newly created process is immediately suspended. |
| `AppCmdLine` | Full command line of the process to create; all text after -c[s] forms the string. |
| `-x` | Causes the remainder of the command line to be ignored. |
| `-pc` | Uses the remainder of the command line as the implicit command line for a pending process creation (client uses -cimp). |
| `-?` | Displays a message box with help text. |
