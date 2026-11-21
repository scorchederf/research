---
created: 2026-11-21
fullpath: 'c:\windows\system32\schtasks.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - exe
  - task-scheduler
  - persistence
aliases:
  - "schtasks.exe"
  - "SchTasks.exe"
  - "schtasks"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/schtasks
  - https://learn.microsoft.com/windows-server/administration/windows-commands/schtasks-create
  - https://learn.microsoft.com/windows-server/administration/windows-commands/schtasks-change
  - https://learn.microsoft.com/windows-server/administration/windows-commands/schtasks-run
  - https://learn.microsoft.com/windows/win32/taskschd/schtasks
---

**fullpath**:c:\windows\system32\schtasks.exe

# description

Schtasks.exe is the built-in command-line tool to create, change, delete, end, query and run scheduled tasks on local or remote computers. It is part of Windows and manages Task Scheduler; related tools include the Task Scheduler MMC (taskschd.msc) and the ScheduledTasks PowerShell module.

## simple description

> ### 2026-11-21 Claude said
> schtasks.exe lets you manage Windows scheduled tasks from the command line. You can create a task that runs a program on a schedule, at startup, at logon or on an event, and run it as a user or SYSTEM, locally or on a remote computer.
>
> **SOC NOTE**: One of the most abused binaries: persistence and execution via scheduled tasks (T1053.005), remote execution with /s, SYSTEM-level runs with /ru System, and /rl HIGHEST. Monitor Security 4698/4699/4702, TaskScheduler/Operational 106/140/200, task XML under C:\Windows\System32\Tasks, and command lines with /create /tr pointing to user-writable paths or encoded PowerShell.
>

# purpose

Schedules and manages tasks: /change modifies the program, run-as account, password or interactive-only property; /create schedules a new task; /delete removes one; /end stops a program started by a task; /query displays tasks; /run starts a task immediately ignoring its schedule. After testing a task, errors can be checked in SystemRoot\SchedLgU.txt.

# typical use cases

| usage | description |
| --- | --- |
| `schtasks /create /sc minute /mo 20 /tn "Security Script" /tr \\central\data\scripts\sec.vbs` | Run a script every 20 minutes. |
| `schtasks /create /tn MyApp /tr c:\apps\myapp.exe /sc onstart` | Run a program at every system start. |
| `schtasks /create /tn MyApp /tr c:\apps\myapp.exe /sc monthly /d 15 /ru System` | Run monthly with System account permissions. |
| `schtasks /create /s SRV01 /tn MyApp /tr c:\program files\corpapps\myapp.exe /sc daily /mo 10` | Schedule a task on a remote computer. |
| `schtasks /run /tn "Security Script"` | Start a task immediately. |
| `schtasks /change /tn MyApp /it` | Make a task run only when the run-as user is logged on. |
| `schtasks /query /v` | Verbose task listing (shows Run As User and Logon Mode). |

# options

| option | description |
| --- | --- |
| `/change` | Changes properties of a task (program /tr, account /ru, password /rp, interactive-only /it, and more). |
| `/create` | Schedules a new task. |
| `/delete` | Deletes a scheduled task. |
| `/end` | Stops a program started by a task. |
| `/query` | Displays tasks scheduled to run on the computer. |
| `/run` | Starts a scheduled task immediately, ignoring its schedule. |
| `/sc <scheduletype>` | (create) Schedule type: MINUTE, HOURLY, DAILY, WEEKLY, MONTHLY, ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT. |
| `/tn <taskname>` | (create) Unique task name, max 238 chars; may include folder\task name. |
| `/tr <taskrun>` | (create) Program or command the task runs; path max 262 chars; defaults to System32 if no path. |
| `/s <computer>` | Name or IP of a remote computer; default is local. |
| `/u [<domain>\]<user>` | Runs the command with this account's permissions; valid only with /s; must be admin on the remote computer. |
| `/p <password>` | Password for /u account; prompts if omitted; valid only with /s. |
| `/ru {[<domain>\]<user> \| system}` | Runs the task with the specified account, or the local System account. |
| `/rp <password>` | Password for the /ru account; not used with /ru System. |
| `/mo <modifier>` | How often the task runs within its schedule type (e.g. every n minutes 1-1439, LASTDAY, FIRST-FOURTH). |
| `/d <day>[,<day>...] \| *` | Day(s) of week (MON-SUN) or day of month (1-31) for WEEKLY/MONTHLY schedules. |
| `/m <month>[,<month>...]` | Month(s) JAN-DEC or * for MONTHLY schedules; required with LASTDAY. |
| `/i <idletime>` | Minutes idle (1-999) before the task starts; required with ONIDLE. |
| `/st <starttime>` | Start time HH:mm (24-hour); required for ONCE. |
| `/ri <interval>` | Repetition interval in minutes (1-599940); not for MINUTE, HOURLY, ONSTART, ONLOGON, ONIDLE, ONEVENT. |
| `/et <endtime>` | End time of day for MINUTE or HOURLY schedules. |
| `/du <duration>` | Maximum length HHHH:MM for MINUTE or HOURLY schedules. |
| `/k` | Stops the program at the time set by /et or /du (MINUTE/HOURLY only). |
| `/sd <startdate>` | Date the schedule starts, in the locale's short date format. |
| `/ed <enddate>` | Date the schedule ends; not valid for ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT. |
| `/ec <channelname>` | Event channel for an ONEVENT schedule. |
| `/it` | Run only when the run-as user is logged on (interactive only). |
| `/np` | No password stored; runs non-interactively as the user with local resources only. |
| `/z` | Delete the task when its schedule completes. |
| `/xml <xmlfile>` | Create the task from an XML file. |
| `/v1` | Create a task visible to pre-Vista systems; incompatible with /xml. |
| `/f` | Create the task and suppress warnings if it already exists. |
| `/rl <level>` | Run level LIMITED (default) or HIGHEST. |
| `/delay <delaytime>` | Delay after trigger in mmmm:ss; ONSTART, ONLOGON, ONEVENT only. |
| `/hresult` | Return process exit code in HRESULT format. |
| `/?` | Displays help. |
