---
created: 2026-11-21
fullpath: 'C:\Windows\Tasks'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - windows
aliases:
  - "Tasks"
  - "Scheduled Tasks folder"
url:
  - https://learn.microsoft.com/windows/win32/taskschd/tasks
  - https://learn.microsoft.com/troubleshoot/windows-client/system-management-components/task-schedular-service-is-not-available
---

**fullpath**:C:\Windows\Tasks

# description

`C:\Windows\Tasks` is the legacy Scheduled Tasks folder used by Task Scheduler 1.0. Task 1.0 tasks are stored here as `.job` files named after the task. Task Scheduler 2.0 tasks are stored as XML files under `C:\Windows\System32\Tasks` instead.

## simple description

> ### 2026-11-21 Claude said
> This folder holds old-style scheduled task files with a .job extension, created by Task Scheduler 1.0 APIs or the legacy `at` command. On current Windows most tasks live in System32\Tasks, so this folder is usually empty or only has a few legacy jobs. The Task Scheduler service reads it.
>
> **SOC NOTE**: Any new .job file here is a persistence lead (MITRE ATT&CK T1053.005 Scheduled Task, T1053.002 At). Legacy `At1.job`-style files from the `at` command are especially suspicious on modern systems. Compare with System32\Tasks and the TaskCache registry keys, and check Microsoft-Windows-TaskScheduler/Operational and Security 4698 events.
>

# purpose

Data that describes a Task Scheduler 1.0 task is kept in a task file in the Scheduled Tasks folder; the name of these files is the task name followed by `.job`. Task 1.0 tasks can run Win32, Win16, OS/2 and MS-DOS applications, .bat and .cmd files, or any registered file type. Legacy `at` tasks (e.g. `At1.job`) here can prevent the Task Scheduler service from starting after an OS upgrade and may need cleanup.

# common files found

| file | description |
| --- | --- |
| `*.job` | Task Scheduler 1.0 task files named after the task. |
| `At1.job`, `At2.job` | Legacy tasks created with the at command. |
