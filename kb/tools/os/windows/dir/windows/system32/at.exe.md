---
created: 2026-11-21
fullpath: 'C:\WINDOWS\System32\At.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - scheduled-tasks
  - deprecated
aliases:
  - At.exe
  - at
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/at
  - https://learn.microsoft.com/troubleshoot/windows-client/system-management-components/use-at-command-to-schedule-tasks
---

**fullpath**:C:\WINDOWS\System32\At.exe

# description

`at.exe` schedules commands and programs to run on a local or remote computer at a specified time and date via the Schedule (Task Scheduler) service. It was deprecated in Windows 8 / Windows Server 2012 and removed in later Insider builds; `schtasks` is the replacement.

## simple description

> ### 2026-11-21 Claude said
> at.exe is the old command-line task scheduler: you tell it a time and a command and Windows runs it, optionally on a remote computer and on repeating days. Tasks run as SYSTEM by default. It has been replaced by schtasks and Task Scheduler and only works for administrators.
>
> **SOC NOTE**: Classic attacker tool for remote execution and persistence (MITRE T1053.002 Scheduled Task/Job: At); `at \\host 12:00 cmd /c ...` runs as SYSTEM on remote machines. Tasks appear as `At1`, `At2`... in Task Scheduler; look for Security Event 4698, TaskScheduler Operational 106/200, and at.exe process creation on modern systems where its use is rare.
>

# purpose

Schedules commands, scripts or programs to run at a set time; used without parameters, lists scheduled commands. Requires the Schedule service and local Administrators membership. Doesn't load cmd.exe automatically, output isn't displayed, the current directory is systemroot, tasks are stored in the registry, and tasks stop after 72 hours by default. Tasks show in the Scheduled Tasks folder as `at<n>`.

# typical use cases

| usage | description |
| --- | --- |
| `at \\marketing` | Lists commands scheduled on the Marketing server. |
| `at \\corp 3` | Shows details of command ID 3 on the Corp server. |
| `at \\corp 08:00 cmd /c net share reports=d:\marketing\reports >> \\maintenance\reports\corp.txt` | Schedules a net share command and redirects output to a share. |
| `at \\marketing 00:00 /every:5,10,15,20,25,30 archive` | Runs archive.cmd every five days at midnight. |
| `at /delete` | Cancels all scheduled commands on the current server. |
| `at \\MyServer 8 /delete` | Cancels task ID 8 on MyServer. |
| `at 14:45 c:\test.bat ^>c:\output.txt` | Schedules a batch file and redirects output (escape `>` with `^`). |

# options

| option | description |
| --- | --- |
| `\\<computername>` | Specifies a remote computer; default is local. |
| `<id>` | Identification number of a scheduled command. |
| `/delete` | Cancels a scheduled command; without ID, cancels all. |
| `/yes` | Answers yes to all queries when deleting. |
| `<time>` | Time to run, 24-hour Hours:Minutes (00:00-23:59). |
| `/interactive` | Allows the command to interact with the logged-on user's desktop. |
| `/every:<date>[,...]` | Runs on every specified day of the week (M,T,W,Th,F,S,Su) or month (1-31). |
| `/next:<date>[,...]` | Runs on the next occurrence of the day. |
| `<command>` | Windows command, program (.exe/.com) or batch program (.bat/.cmd); use absolute or UNC paths. |
| `/?` | Displays help. |
