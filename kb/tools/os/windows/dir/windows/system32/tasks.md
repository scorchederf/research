---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Tasks'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - task-scheduler
aliases:
  - "Tasks"
  - "Task Scheduler task folder"
url:
  - https://learn.microsoft.com/windows/win32/taskschd/tasks
  - https://learn.microsoft.com/windows/win32/taskschd/task-scheduler-schema
  - https://learn.microsoft.com/windows/win32/taskschd/boot-trigger-example--xml-
---

**fullpath**:C:\Windows\System32\Tasks

# description

Learn describes Task Scheduler tasks, which are stored in task folders and defined in XML validated against the Task Scheduler schema; it does not document this specific on-disk path. Tasks are registered with ITaskFolder::RegisterTask or Schtasks.exe.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the XML definition files of all Task Scheduler 2.0 scheduled tasks, mirroring the folder tree shown in Task Scheduler. Each file describes triggers, the account the task runs as, and the actions (programs) to run. It is protected and normally changed only through Task Scheduler APIs or schtasks.
>
> **SOC NOTE**: Key persistence location (MITRE ATT&CK T1053.005 Scheduled Task). Review new or modified task XML files for actions launching scripts, LOLBins or binaries in user-writable paths; correlate with Security 4698/4702, TaskScheduler/Operational 106/140/200, and the TaskCache keys under HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule. Tasks without a matching XML or with a deleted SD value may be hidden.
>

# purpose

Stores created tasks. ACLs on tasks and task folders can grant or deny access to users and groups; if the Local System account is denied access to a task file or folder, Task Scheduler can produce unexpected results. Task definitions contain RegistrationInfo, Triggers, Principal, Settings and Actions elements.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
