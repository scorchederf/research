---
created: 2026-11-21
fullpath: 'C:\Windows\System32\taskkill.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-commands
aliases:
  - "taskkill.exe"
  - "taskkill"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill
---

**fullpath**: C:\Windows\System32\taskkill.exe

# description

Built-in Windows command that ends one or more tasks or processes by process ID or image name, locally or on a remote computer. It replaces the older **kill** tool. Use it together with `tasklist` to find the PID of the process to end.

## simple description

> ### 2026-11-21 Claude said
> taskkill is the command-line way to close programs, like "End task" in Task Manager. You can target a process by its name (e.g. notepad.exe) or its process ID, force it to stop with /f, and also kill its child processes with /t. It can also act on remote computers with credentials. Administrators and scripts use it routinely.
>
> **SOC NOTE**: Ransomware and other malware use taskkill to stop AV/EDR, backup and database processes before encryption (T1489 Service Stop, T1562.001 Impair Defenses). Look for bursts of `taskkill /f /im` against security products, sqlservr.exe, veeam, etc., in process-creation logs (Security 4688, Sysmon 1). Remote use with /s /u /p also exposes credentials on the command line.
>

# purpose

Ends processes by PID or image name, optionally forcefully and including child processes, with filters (status, user name, memory use, services, window title, loaded modules, etc.) to select the target set. Remote processes are always ended forcefully; the WINDOWTITLE and STATUS filters are not supported remotely.

# typical use cases

| usage | description |
| --- | --- |
| `taskkill /pid 1230 /pid 1241 /pid 1253` | End processes with IDs 1230, 1241 and 1253. |
| `taskkill /f /fi "USERNAME eq NT AUTHORITY\SYSTEM" /im notepad.exe` | Forcefully end Notepad.exe if it was started by the system. |
| `taskkill /s srvmain /u maindom\hiropln /p p@ssW23 /fi "IMAGENAME eq note*" /im *` | End all processes whose image name begins with "note" on remote computer Srvmain using alternate credentials. |
| `taskkill /pid 2134 /t /fi "username eq administrator"` | End PID 2134 and its child processes, only if started by Administrator. |
| `taskkill /f /fi "PID ge 1000" /im *` | Forcefully end all processes with PID greater than or equal to 1000. |

# options

| option | description |
| --- | --- |
| `/s <computer>` | Name or IP address of a remote computer (no backslashes). Default is the local computer. |
| `/u <domain>\<username>` | Run with the permissions of the specified user. Only valid with **/s**. |
| `/p <password>` | Password of the account given in **/u**. |
| `/fi <filter>` | Filter to select tasks; can be repeated, `*` selects all. Filters: STATUS, IMAGENAME, PID, SESSION, CPUtime, MEMUSAGE, USERNAME, SERVICES, WINDOWTITLE, MODULES. |
| `/pid <processID>` | Process ID of the process to end. |
| `/im <imagename>` | Image name of the process to end; `*` for all image names (only when a filter is applied). |
| `/f` | Forcefully end processes. Ignored for remote processes, which are always ended forcefully. |
| `/t` | End the specified process and any child processes it started. |
