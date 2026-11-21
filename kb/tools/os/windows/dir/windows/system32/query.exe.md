---
created: 2026-11-21
fullpath: 'c:\windows\system32\query.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - query.exe
  - query
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/query
  - https://learn.microsoft.com/windows-server/administration/windows-commands/query-session
  - https://learn.microsoft.com/windows-server/administration/windows-commands/query-user
  - https://learn.microsoft.com/windows-server/administration/windows-commands/query-process
  - https://learn.microsoft.com/windows-server/administration/windows-commands/remote-desktop-services-terminal-services-command-reference
---

**fullpath**:c:\windows\system32\query.exe

# description

query is a Remote Desktop Services (Terminal Services) command that displays information about processes, sessions and Remote Desktop Session Host servers. Its subcommands have standalone equivalents: qprocess (query process), qwinsta (query session), qappsrv (query termserver) and quser (query user).

## simple description

> ### 2026-11-21 Claude said
> query.exe shows who is logged on to a Windows machine and what they're running. `query user` lists signed-in users with session IDs, state and idle time; `query session` lists console and RDP sessions; `query process` lists processes per session. It works locally or against a remote server with `/server:`.
>
> **SOC NOTE**: Attackers run `query user` / `quser` / `qwinsta` for discovery (MITRE ATT&CK T1033 System Owner/User Discovery) to find active admin sessions before RDP hijacking with tscon (T1563.002) or credential theft. Remote use (`/server:`) is a lateral-movement reconnaissance signal; correlate process creation events with subsequent tscon/mstsc activity.
>

# purpose

Display information about processes, sessions and RD Session Host servers. A greater-than sign (`>`) marks the current session in output. Querying other users' sessions requires Full Control or special access permission.

# typical use cases

| usage | description |
| --- | --- |
| `query user` | Display all users logged on to the system. |
| `query user USER1 /server:Server1` | Display information about USER1 on Server1. |
| `query process *` | Display processes used by all sessions. |
| `query process /ID:2` | Display processes used by session ID 2. |
| `query session` | List active and listening sessions on the server. |

# options

| option    | description    |
| --- | --- |
| `query process` | Displays information about processes running on an RD Session Host server (`*`, `<processID>`, `<username>`, `<sessionname>`, `/id:<nn>`, `<programname>`, `/server:<servername>`). |
| `query session` | Displays information about sessions on an RD Session Host server (`<sessionname>`, `<username>`, `<sessionID>`, `/server:`, `/mode`, `/flow`, `/connect`, `/counter`). |
| `query termserver` | Displays a list of all RD Session Host servers on the network. |
| `query user` | Displays information about user sessions on an RD Session Host server (`<username>`, `<sessionname>`, `<sessionID>`, `/server:<servername>`). |
| `/server:<servername>` | Target RD Session Host server; default is the current server. |
| `/mode` | (query session) Displays current line settings. |
| `/flow` | (query session) Displays current flow-control settings. |
| `/connect` | (query session) Displays current connect settings. |
| `/counter` | (query session) Displays counters: total sessions created, disconnected and reconnected. |
| `/?` | Displays help at the command prompt. |
