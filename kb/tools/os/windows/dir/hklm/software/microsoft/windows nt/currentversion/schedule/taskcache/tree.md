---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - task-scheduler
  - persistence
aliases:
  - TaskCache\Tree
url: []
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree

# description

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> This registry key is the Task Scheduler's index of scheduled tasks, laid out exactly like the folders you see in Task Scheduler (for example `\Microsoft\Windows\...`). Each task has a subkey here that points, by GUID, to its full definition stored under `TaskCache\Tasks`. The Task Scheduler service reads this cache together with the XML files in `C:\Windows\System32\Tasks`. Values include `Id` (the task GUID), `Index` and `SD` (security descriptor).
>
> **SOC NOTE**: Key artifact for scheduled-task persistence (MITRE T1053.005). Attackers create tasks here, and some malware (for example the Tarrask/HAFNIUM technique) deletes the `SD` value to hide a task from `schtasks /query` and the GUI while it keeps running. Compare Tree entries against `C:\Windows\System32\Tasks` and against Security Event 4698/4699 and TaskScheduler/Operational events 106/140/141. Only SYSTEM can modify the key by default.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SOFTWARE` |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree" /s` | List every task folder and task entry with its values. |
