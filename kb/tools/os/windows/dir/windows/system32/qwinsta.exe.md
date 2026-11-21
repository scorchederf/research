---
created: 2026-11-21
fullpath: 'C:\Windows\System32\qwinsta.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - rds
  - windows-commands
aliases:
  - qwinsta.exe
  - query session
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/qwinsta
  - https://learn.microsoft.com/windows-server/administration/windows-commands/query-session
  - https://learn.microsoft.com/windows-server/administration/windows-commands/remote-desktop-services-terminal-services-command-reference
---

**fullpath**:C:\Windows\System32\qwinsta.exe

# description

qwinsta displays information about sessions on a Remote Desktop Session Host server, including active sessions and other sessions the server runs. It is the same as the `query session` command and is part of the Remote Desktop Services (Terminal Services) command-line tools, alongside quser, rwinsta, tscon and tsdiscon.

## simple description

> ### 2026-11-21 Claude said
> qwinsta lists the logon sessions on a Windows machine or remote RDS server: session name, user, ID, state (active, disconnected, listen) and type. Admins use it to see who is logged on before rebooting or to find a session ID to reset. It works locally and against remote servers with /server. The current session is marked with a > symbol.
>
> **SOC NOTE**: Attackers use qwinsta/query session for discovery of logged-on users and RDP sessions (T1033 System Owner/User Discovery, T1049) before session hijacking with tscon (T1563.002). Remote use against many hosts in a short time is a lateral-movement reconnaissance indicator; look for it in 4688/Sysmon 1 process logs.
>

# purpose

Show session information on an RD Session Host server. A user can always query their own session; querying other sessions needs special access permission. With no session specified it shows all active sessions. Output columns: SESSIONNAME, USERNAME, ID, STATE, TYPE and DEVICE. Sessions whose initial state is DISABLED are not listed until enabled.

# typical use cases

| usage | description |
| --- | --- |
| `qwinsta /server:Server2` | Display information about all active sessions on server Server2. |
| `qwinsta modeM02` | Display information about active session modeM02. |

# options

| option | description |
| --- | --- |
| `<sessionname>` | Name of the session to query. |
| `<username>` | Name of the user whose sessions you want to query. |
| `<sessionID>` | ID of the session to query. |
| `/server:<servername>` | RD Session Host server to query. Default is the current server. |
| `/mode` | Displays current line settings. |
| `/flow` | Displays current flow-control settings. |
| `/connect` | Displays current connect settings. |
| `/counter` | Displays counters, including total sessions created, disconnected and reconnected. |
| `/?` | Displays help at the command prompt. |

