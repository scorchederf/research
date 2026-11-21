---
created: 2026-11-21
fullpath: 'c:\windows\system32\change.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - remote-desktop
aliases:
  - change.exe
  - change
  - chglogon
  - chgport
  - chgusr
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/change
  - https://learn.microsoft.com/windows-server/administration/windows-commands/change-logon
  - https://learn.microsoft.com/windows-server/administration/windows-commands/change-port
  - https://learn.microsoft.com/windows-server/administration/windows-commands/change-user
  - https://learn.microsoft.com/windows-server/administration/windows-commands/remote-desktop-services-terminal-services-command-reference
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/disable-terminal-server-client-logons
---

**fullpath**:c:\windows\system32\change.exe

# description

change changes Remote Desktop Session Host server settings for logons, COM port mappings, and install mode. It is one of the Remote Desktop Services (Terminal Services) command-line tools; the older chglogon, chgport and chgusr commands map to its subcommands.

## simple description

> ### 2026-11-21 Claude said
> change.exe is a built-in Remote Desktop Services utility. It lets an administrator turn new RDP logons on or off (for maintenance), remap COM ports for old DOS applications, and switch the server into "install mode" before installing software for all users. On most workstations it is rarely used.
>
> **SOC NOTE**: `change logon /disable` or `/drain` can be used to lock out remote administrators during an intrusion or ransomware deployment (impact, akin to T1531 Account Access Removal). `change user /install` changes registry shadowing under `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install`, which could be abused to plant per-user settings. Look for process creation events (4688/Sysmon 1) from unexpected parents.
>

# purpose

Manage RD Session Host logon state, COM port mapping and .ini/registry install mode from the command line. You must be an administrator to run `change logon`.

# typical use cases

| usage | description |
| --- | --- |
| `change logon /query` | Displays the current logon status. |
| `change logon /disable` | Disables client logons (not the console); logons are re-enabled at restart. |
| `change logon /enable` | Enables logons from client sessions. |
| `change port com12=com1` | Maps COM12 to COM1 for an MS-DOS-based application. |
| `change port /query` | Displays the current port mappings. |
| `change user /install` | Disables .ini file mapping before installing an application. |
| `change user /execute` | Reverts to standard .ini file mapping after installing. |

# options

| option | description |
| --- | --- |
| `logon` | Enables or disables logons from client sessions, or displays current logon status. |
| `logon /query` | Displays the current logon status, whether enabled or disabled. |
| `logon /enable` | Enables logons from client sessions, but not from the console. |
| `logon /disable` | Disables subsequent logons from client sessions, but not from the console; current users are not affected. |
| `logon /drain` | Disables logons from new client sessions but allows reconnections to existing sessions. |
| `logon /drainuntilrestart` | Same as `/drain` until the computer is restarted. |
| `port` | Lists or changes COM port mappings to be compatible with MS-DOS applications. |
| `port <portX>=<portY>` | Maps COM `<portX>` to `<portY>`. |
| `port /d <portX>` | Deletes the mapping for COM `<portX>`. |
| `port /query` | Displays the current port mappings. |
| `user` | Changes the install mode for the RD Session Host server. |
| `user /execute` | Enables .ini file mapping to the home directory (default). |
| `user /install` | Disables .ini file mapping; .ini files are read/written to the system directory and registry entries are shadowed under `HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Terminal Server\Install`. |
| `user /query` | Displays the current setting for .ini file mapping. |
| `/?` | Displays help at the command prompt. |
