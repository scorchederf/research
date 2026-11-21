---
created: 2026-11-21
fullpath: 'c:\windows\system32\reset.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "reset.exe"
  - "reset session"
  - "rwinsta"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/reset-session
  - https://learn.microsoft.com/windows-server/administration/windows-commands/rwinsta
  - https://learn.microsoft.com/windows-server/administration/windows-commands/remote-desktop-services-terminal-services-command-reference
---

**fullpath**:c:\windows\system32\reset.exe

# description

reset.exe implements the `reset session` Remote Desktop Services command, which resets (deletes) a session on a Remote Desktop Session Host server. `rwinsta` is the same command. Related commands are `query session`, `tsdiscon`, `logoff` and `tscon`.

## simple description

> ### 2026-11-21 Claude said
> reset.exe is the command-line tool behind `reset session`, used to forcibly end a Remote Desktop or console session, usually when it hangs. Programs in the session are closed without saving. You can always reset your own session, but resetting other users' sessions requires Full Control permission.
>
> **SOC NOTE**: Attackers may use `reset session`/`rwinsta` to kick legitimate admins or other attackers out of sessions, or to destroy evidence of an interactive session (MITRE ATT&CK T1531 Account Access Removal). Correlate with TerminalServices-LocalSessionManager events (e.g. 24 disconnect, 23 logoff) and Security 4634/4779.
>

# purpose

Resets a session on an RD Session Host server; this should be done only when the session malfunctions or appears to have stopped responding. Resetting another user's session without warning can cause data loss.

# typical use cases

| usage | description |
| --- | --- |
| `reset session rdp-tcp#6` | Resets the session named rdp-tcp#6. |
| `reset session 3` | Resets the session with session ID 3. |

# options

| option | description |
| --- | --- |
| `<sessionname>` | Name of the session to reset (find with query session). |
| `<sessionID>` | ID of the session to reset. |
| `/server:<servername>` | Terminal server containing the session; default is the current RD Session Host server. |
| `/v` | Displays information about the actions being performed. |
| `/?` | Displays help at the command prompt. |
