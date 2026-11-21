---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{<TaskGUID>}'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - {<TaskGUID>}
  - TaskCache Tasks
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/system-management-components/task-schedular-service-is-not-available
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{<TaskGUID>}

# description

Per-task registry key in the Task Scheduler cache. Each registered scheduled task has a GUID-named subkey under TaskCache\Tasks, with matching entries under TaskCache\Tree (by task path) and one of TaskCache\Plain, Logon or Boot. Task files live in C:\Windows\System32\Tasks.

## simple description

> ### 2026-11-21 Claude said
> Every scheduled task on Windows has a key here named after its GUID. It stores the task's path, actions, triggers and other metadata, and the Task Scheduler service uses it as its registry cache. The Tree key maps the readable task name to this GUID. If the key and the task file get out of sync, Task Scheduler shows errors.
>
> **SOC NOTE**: Prime persistence artifact (T1053.005). Attackers create tasks or hide them by deleting the Tree key's SD value (Tarrask technique) so they vanish from schtasks and the GUI but still run. Compare Path values against C:\Windows\System32\Tasks and 4698/4702 events; parse the Actions value to find the executed command.
>

# purpose

Holds the cached registration data for one scheduled task, keyed by task GUID. Microsoft troubleshooting guidance deletes these keys (with the matching Tree and Plain/Logon/Boot entries) to remove corrupted tasks or leftover `at` tasks, after backing up the Tasks key.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SOFTWARE |

# values

| value name | type | description |
| --- | --- | --- |
| `Path` | REG_SZ | Task path in the Task Scheduler library, for example `\\At1` for tasks created by `at`. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{<TaskGUID>}"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks" /s /v Path` | List the Path of every cached task. |
