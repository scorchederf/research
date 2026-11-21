---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-TaskScheduler%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - task-scheduler
aliases:
  - Microsoft-Windows-TaskScheduler%4Operational.evtx
  - Microsoft-Windows-TaskScheduler/Operational
  - Task Scheduler operational log
url:
  - https://learn.microsoft.com/troubleshoot/mem/intune/device-protection/troubleshoot-bitlocker-policies
  - https://learn.microsoft.com/troubleshoot/windows-client/system-management-components/0x80041323-running-scheduled-tasks
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/troubleshoot-scheduled-tasks-not-running
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-TaskScheduler%4Operational.evtx

# description

The on-disk file of the Microsoft-Windows-TaskScheduler/Operational event log, shown in Event Viewer under Applications and Services Logs > Microsoft > Windows > TaskScheduler > Operational. It records Task Scheduler service activity and task run history.

## simple description

> ### 2026-11-21 Claude said
> This file is the Task Scheduler Operational event log. Every time a scheduled task is registered, started, finished or fails, Task Scheduler can write an event here. On many systems it is disabled by default and must be enabled to collect history. The %4 in the name stands for the / in the channel name.
>
> **SOC NOTE**: Key evidence for persistence and execution via scheduled tasks (MITRE ATT&CK T1053.005): Event 106 task registered, 140 updated, 141 deleted, 200/201 action started/completed, 129 process created. Correlate with Security 4698/4702 and the task XML in C:\Windows\System32\Tasks. Clearing or disabling the log (T1070.001) is suspicious.
>

# purpose

Used for troubleshooting tasks that do not run or fail, for example the BitLocker MDM policy refresh task or tasks failing with 0x80041323 (Task Scheduler service too busy). Documented events include 706 (compatibility module task status update failed), 131/132 (task queue quota exceeded/approaching) and 133/134 (task engine quota exceeded/approaching). The log must be enabled manually before it records data.
