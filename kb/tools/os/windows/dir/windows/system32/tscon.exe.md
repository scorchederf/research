---
created: 2026-11-21
fullpath: 'C:\Windows\System32\tscon.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - remote-desktop
  - lateral-movement
aliases:
  - tscon.exe
  - tscon
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/tscon
---

**fullpath**:C:\Windows\System32\tscon.exe

# description

`tscon.exe` connects to another session on a Remote Desktop Session Host server. It is part of the Remote Desktop Services (Terminal Services) command set. Requires Full Control or Connect special access permission.

## simple description

> ### 2026-11-21 Claude said
> tscon lets you switch your current Remote Desktop session to another existing session on the same server. Normally you need that user's password unless it is your own session. Related tools are query session, tsdiscon and logoff. It is mostly used by admins to reconnect to disconnected sessions.
>
> **SOC NOTE**: Known RDP session hijacking technique (MITRE T1563.002): running tscon as SYSTEM (e.g. via a service or psexec -s) connects to another user's session without their password. Alert on tscon.exe launched by SYSTEM, via services.exe/cmd created services, or with /dest:. Look for Event IDs 4778/4779 and TerminalServices-LocalSessionManager events.
>

# purpose

Connects the current user to another Remote Desktop session, disconnecting the current one.

# typical use cases

| usage | description |
| --- | --- |
| `tscon 12` | Connects to session 12 and disconnects the current session. |
| `tscon 23 /password:mypass` | Connects to session 23 using the owning user's password. |
| `tscon TERM03 /v /dest:TERM05` | Connects session TERM03 to session TERM05 and disconnects TERM05. |

# options

| option | description |
| --- | --- |
| `<sessionID>` | ID of the session to connect to; with `/dest` you can also specify the current session's name. |
| `<sessionname>` | Name of the session to connect to. |
| `/dest:<sessionname>` | Name of the current session, which disconnects when you connect; can connect another user's session to a different session. |
| `/password:<pw>` | Password of the user who owns the target session; required when the connecting user does not own it. |
| `/password:*` | Prompts for the password of the target session's owner. |
| `/v` | Displays information about the actions being performed. |
| `/?` | Displays help at the command prompt. |
