---
created: 2026-11-21
fullpath: 'C:\Windows\System32\cmd.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - shell
aliases:
  - cmd.exe
  - cmd
  - Command Prompt
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/cmd
---

**fullpath**:C:\Windows\System32\cmd.exe

# description

cmd.exe is the Windows command interpreter; running `cmd` starts a new instance, and without parameters it displays the operating system version and copyright information. It is part of Windows, reads AutoRun and EnableExtensions settings from `HKLM`/`HKCU\Software\Microsoft\Command Processor`, and Microsoft points users needing more advanced scripting to PowerShell.

## simple description

> ### 2026-11-21 Claude said
> cmd.exe is the classic Windows Command Prompt. It runs built-in commands, batch files and other programs, and supports pipes, redirection and environment variables. It is used constantly by admins, installers and scripts. Every Windows system has it.
>
> **SOC NOTE**: cmd.exe is the most common execution wrapper for attacks (MITRE ATT&CK T1059.003 Windows Command Shell). Watch for `cmd /c` spawned by Office, browsers, w3wp.exe, sqlservr.exe or wmiprvse.exe, heavy obfuscation (^, %VAR:~x,y%, delayed expansion), and persistence via the Command Processor AutoRun value (T1546). Process creation events (4688/Sysmon 1) with full command lines are essential.
>

# purpose

Start a command interpreter to run commands, batch files and programs.

# typical use cases

| usage | description |
| --- | --- |
| `cmd /c <string>` | Run a command and exit. |
| `cmd /k <string>` | Run a command and keep the prompt open. |
| `<command1> \| <command2>` | Pipe output of one command to another. |
| `<command1> \|\| <command2>` | Run command2 only if command1 fails. |
| `<command1> > <file1.txt>` | Redirect output to a file. |
| `<command1> && <command2> && <command3>` | Run each command only if the previous one succeeded. |
| `set <VariableName>=<value>` | Add an environment variable. |

# options

| option | description |
| --- | --- |
| `/c` | Carries out the command specified by `<string>` and then exits. |
| `/k` | Carries out the command specified by `<string>` and keeps running. |
| `/s` | With `/c` or `/k`, strips the first and last quotes around `<string>`. |
| `/q` | Turns echo off. |
| `/d` | Disables execution of AutoRun commands. |
| `/a` | Formats command output as ANSI. |
| `/u` | Formats command output as Unicode. |
| `/t:{<b><f> \| <f>}` | Sets background and foreground colors (hex digits 0-f). |
| `/e:on` | Enables command extensions. |
| `/e:off` | Disables command extensions. |
| `/f:on` | Enables file and directory name completion. |
| `/f:off` | Disables file and directory name completion. |
| `/v:on` | Enables delayed environment variable expansion (`!var!`). |
| `/v:off` | Disables delayed environment variable expansion. |
| `<string>` | Specifies the command to carry out. |
| `/?` | Displays help at the command prompt. |
