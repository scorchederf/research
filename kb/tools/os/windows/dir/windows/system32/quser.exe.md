---
created: 2026-11-21
fullpath: 'C:\Windows\System32\quser.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - quser.exe
  - quser
  - query user
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/quser
  - https://learn.microsoft.com/windows-server/administration/windows-commands/query-user
---

**fullpath**:C:\Windows\System32\quser.exe

# description

quser displays information about user sessions on a Remote Desktop Session Host server and is the same as the **query user** command. It is part of the Remote Desktop Services (Terminal Services) command set alongside qwinsta, qprocess, logoff and tscon.

## simple description

> ### 2026-11-21 Claude said
> quser lists who is logged on to a machine, which session they are in, whether the session is active or disconnected, how long it has been idle and when they logged on. Admins use it before rebooting servers or to find a user's session ID. It works locally or against a remote server with /server. A > marks your own session.
>
> **SOC NOTE**: Common discovery command in hands-on-keyboard intrusions (T1033 System Owner/User Discovery) and before RDP session hijacking via tscon (T1563.002). Remote use against many hosts suggests lateral-movement reconnaissance. Look for quser.exe in process-creation events (4688/Sysmon 1), especially spawned from remote shells or webshells.
>

# purpose

Find out whether a specific user is logged on to a Remote Desktop Session Host server. It returns the user name, session name, session ID, state (active or disconnected), idle time and logon date/time. Requires Full Control or special access permission.

# typical use cases

| usage | description |
| --- | --- |
| `quser` | Display information about all users logged on to the system. |
| `quser USER1 /server:Server1` | Display information about user USER1 on server Server1. |

# options

| option    | description    |
| --- | --- |
| `<username>` | Logon name of the user to query. |
| `<sessionname>` | Name of the session to query. |
| `<sessionID>` | ID of the session to query. |
| `/server:<servername>` | Remote Desktop Session Host server to query; defaults to the current server. |
| `/?` | Displays help at the command prompt. |
