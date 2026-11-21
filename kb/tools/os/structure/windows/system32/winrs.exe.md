---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winrs.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - winrs.exe
  - winrs
  - Windows Remote Shell
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/winrs
---

**fullpath**:C:\Windows\System32\winrs.exe

# description

Winrs (Windows Remote Management) enables you to manage and execute programs remotely over WinRM. Active shells and winrs configuration are managed with the WinRM tool (URI aliases `shell/cmd` and `winrm/config/winrs`).

## simple description

> ### 2026-11-21 Claude said
> Winrs is the Windows Remote Shell client: it runs a command on another computer over WinRM (HTTP 5985 / HTTPS 5986) and shows the output locally. It is built into Windows and works wherever WinRM is enabled, such as most servers. Admins use it for quick remote commands without PowerShell remoting. On the target, commands run under the winrshost.exe process.
>
> **SOC NOTE**: Attackers use winrs for lateral movement and remote execution with stolen credentials (MITRE ATT&CK T1021.006 Windows Remote Management). Plaintext `/u:` and `/p:` on the command line can expose credentials in process logs. On the target look for winrshost.exe spawning cmd/other processes, Microsoft-Windows-WinRM/Operational events (e.g. 91 shell created) and logon type 3 events (4624).
>

# purpose

Run commands and programs on a remote endpoint through a WinRM remote shell, with options for authentication, encryption, environment, profile and credential delegation.

# typical use cases

- `winrs /r:myserver command`
- `winrs /r:contoso.com /usessl command`
- `winrs /r:myserver /ad /u:administrator /p:$%fgh7 dir \\anotherserver\share`

# options

| option    | description    |
| --- | --- |
| `/remote:<endpoint>` | Target endpoint as NetBIOS name or `[<transport>://]<target>[:<port>]`; defaults to `/r:localhost`. |
| `/unencrypted` | Messages to the remote shell aren't encrypted (ignored with HTTPS). |
| `/username:<username>` | Username on the command line; requires `/password`. |
| `/password:<password>` | Password on the command line; requires `/username`. |
| `/timeout:<seconds>` | Deprecated. |
| `/directory:<path>` | Starting directory for the remote shell (default %USERPROFILE%). |
| `/environment:<string>=<value>` | Sets an environment variable when the shell starts; repeat for multiple. |
| `/noecho` | Disables echo. |
| `/noprofile` | Doesn't load the user's profile; required if the remote user isn't a local admin. |
| `/allowdelegate` | Allows the user's credentials to access a remote share on another machine. |
| `/compression` | Turns on compression (default off). |
| `/usessl` | Uses an SSL connection with the default WinRM port. |
| `/?` | Displays help at the command prompt. |
