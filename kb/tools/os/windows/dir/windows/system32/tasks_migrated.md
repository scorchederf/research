---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Tasks_Migrated'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - scheduled-tasks
aliases:
  - Tasks_Migrated
url:
---

**fullpath**:C:\Windows\System32\Tasks_Migrated

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> Tasks_Migrated is a folder Windows Setup creates during an in-place upgrade (feature update) to hold scheduled task definition files carried over from the previous Windows installation. The files are XML task definitions like those in C:\Windows\System32\Tasks, but they are not themselves read by the Task Scheduler service. After a successful upgrade it usually contains copies of the old tasks and can linger for a long time.
>
> **SOC NOTE**: Useful for forensics: it can preserve older versions of scheduled tasks (including malicious persistence, MITRE ATT&CK T1053.005) that were later deleted or modified in System32\Tasks, and timestamps reflect upgrade time. Compare its contents to System32\Tasks and the TaskCache registry keys; a task present here but missing in the live tree may indicate cleanup by an attacker.
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
