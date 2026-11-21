---
created: 2026-11-21
fullpath: 'C:\Windows\SysWOW64\schtasks.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - scheduled-tasks
  - lolbin
aliases:
  - "schtasks.exe"
  - "schtasks"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/schtasks
---

**fullpath**: C:\Windows\SysWOW64\schtasks.exe

# description

schtasks.exe is the built-in command-line tool for Task Scheduler; this is the 32-bit copy in SysWOW64. It schedules commands and programs to run periodically or at a specific time, adds and removes tasks, starts and stops tasks on demand, and displays and changes tasks. It performs the same operations as Scheduled Tasks in Control Panel.

## simple description

> ### 2026-11-21 Claude said
> schtasks.exe creates, changes, runs, queries and deletes scheduled tasks from the command line, on the local or a remote computer. Admins and software installers use it constantly. The SysWOW64 version is the 32-bit build used by 32-bit processes on 64-bit Windows. Tasks are stored in C:\Windows\System32\Tasks and the registry TaskCache.
>
> **SOC NOTE**: One of the most abused persistence/execution tools (T1053.005 Scheduled Task). Watch for /create with /ru SYSTEM, /sc onlogon/onstart, actions pointing to user-writable paths or encoded PowerShell, and remote /s usage for lateral movement. Correlate with Security 4698/4699/4702 and TaskScheduler/Operational 106/140/200/201. A 32-bit schtasks.exe launched by a 32-bit malware process is a useful clue.
>

# purpose

Schedules commands and programs to run periodically or at a specific time; adds and removes tasks; starts and stops tasks on demand; displays and changes scheduled tasks. Managing all tasks requires membership in Administrators (locally, or on the remote computer, or via /u credentials).

# typical use cases

| usage | description |
| --- | --- |
| `schtasks /query` | Display tasks scheduled to run on the computer. |
| `schtasks /create` | Schedule a new task. |
| `schtasks /run` | Start a scheduled task immediately, ignoring the schedule. |
| `schtasks /delete` | Delete a scheduled task. |

# options

| option | description |
| --- | --- |
| `/change` | Changes properties of a task: the program it runs (/tr), the run-as account (/ru), its password (/rp), or adds the interactive-only property (/it). |
| `/create` | Schedules a new task. |
| `/delete` | Deletes a scheduled task. |
| `/end` | Stops a program started by a task. |
| `/query` | Displays tasks scheduled to run on the computer. |
| `/run` | Starts a scheduled task immediately using the saved program, account and password, ignoring the schedule. |
