---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\remote.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows-kits
  - executable
  - debugging
aliases:
  - remote.exe
  - Remote tool
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/remote-tool
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/remote-server-syntax
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/remote-client-syntax
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/remote-tool-concepts
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/remote-tool-examples
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/starting-a-remote-exe-session
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/extra-tools
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\remote.exe

# description

The Remote tool (Remote.exe) is a command-line tool that lets you run and control any console program from a remote computer over a named pipe. It is included in Debugging Tools for Windows (Windows Kits), and is typically used to remotely control console debuggers such as KD, CDB and NTSD (the `.remote` debugger command creates a Remote.exe server).

## simple description

> ### 2026-11-21 Claude said
> remote.exe is an old Microsoft debugging utility that shares a console program over the network. On the server you run something like `remote /s cmd test1`, and anyone who connects with `remote /c server test1` can type commands into that console and see its output. It was built for remote kernel/user debugging but works with any console program, including cmd.exe. It is signed by Microsoft and installed with the Windows SDK/WDK debuggers.
>
> **SOC NOTE**: Because it does not authenticate users and by default lets anyone who knows the session name connect, `remote /s cmd <name>` is effectively a Microsoft-signed bind shell over SMB named pipes (MITRE ATT&CK T1021.002 / T1059.003; listed in LOLBAS for execution/ADS abuse). Hunt for remote.exe outside developer machines, `/s` with cmd/powershell, copies of remote.exe in unusual paths, and named pipe creation (Sysmon 17/18) by remote.exe.
>

# purpose

Runs a console program on a server and opens a named pipe so clients can connect, send commands and see output; also queries the sessions running on a server. Multiple server sessions and multiple clients per session are supported. It can compromise security because it does not authenticate users or use Windows permissions, though `/u` and `/ud` can include or exclude users and groups. Type `@k` on the server to end a session and `@q` on a client to disconnect.

# typical use cases

| usage | description |
| --- | --- |
| `remote /s cmd test1` | Start a server session. |
| `remote /c server01 test1` | Connect a client. |
| — | Share a debugger session: start KD/CDB under remote.exe, or run `.remote MyBrokenBox` in the debugger, then `remote /c server2 MyBrokenBox`. |
| `remote /q Computer` | List visible sessions on a computer. |

# options

| option    | description    |
| --- | --- |
| `/s` | Starts a server session. |
| `Command` | (Server) Command that starts the console-based program; quote if it contains spaces. |
| `SessionName` | Name of the remote session; not case-sensitive. |
| `/f` | Color of the text in the server command window. |
| `/b` | Background color of the server command window. |
| `Color` | black, blue, green, cyan, red, purple, yellow, white, lblack, lblue, lgreen, lred, lpurple, lyellow, lwhite. |
| `/u` | (Server) Users or groups permitted to connect; everyone else is denied. |
| `/ud` | (Server) Users or groups denied permission to connect. |
| `User` | User or group in [domain \| computer]\{user \| group} format. |
| `/v` | (Server) Makes a session visible. |
| `/-v` | (Server) Makes a remote debugger session invisible. |
| `/c` | Connects the client to a remote session. |
| `Server` | (Client) Computer name of the server that established the session. |
| `/L Lines` | (Client) Number of console lines sent to the client (default 200). |
| `/k ColorFile` | (Client) Text file mapping output keywords to text colors. |
| `/q Computer` | Displays the visible remote sessions available on the specified computer. |
