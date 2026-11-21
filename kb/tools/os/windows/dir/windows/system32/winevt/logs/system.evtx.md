---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\System.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - windows
aliases:
  - "System.evtx"
  - "System log"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/application-management/move-event-viewer-log-files
  - https://learn.microsoft.com/windows/win32/eventlog/eventlog-key
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-eventlog
---

**fullpath**:C:\Windows\System32\winevt\Logs\System.evtx

# description

System.evtx is the file backing the Windows System event log, stored by default in `%SystemRoot%\System32\winevt\Logs`. It is written by the Windows Event Log service and viewed in Event Viewer under Windows Logs > System. Its path and size are configured under `HKLM\SYSTEM\CurrentControlSet\Services\Eventlog\System` or by the `Channel_LogFilePath_4` policy.

## simple description

> ### 2026-11-21 Claude said
> The System log records events from Windows components: service starts and stops, driver loads, shutdowns and restarts, time changes, hardware and disk errors. It is one of the three classic Windows logs alongside Application and Security. Any user can generally read it, and its size is limited so old events are overwritten.
>
> **SOC NOTE**: Key events: 7045 (new service installed, T1543.003, e.g. PsExec), 7036/7040 (service state/start-type changes), 104 (log cleared, T1070.001), 1074/6005/6006 (shutdown/startup), 6008 (unexpected shutdown). Also contains TPM and driver errors. Collect early, as default size limits cause roll-over.
>

# purpose

Contains events that are logged by Windows system components; these events are predetermined by Windows. The log file can be moved to another folder via Event Viewer log properties, PowerShell or the `File` value of the Eventlog registry key (the folder needs correct permissions, including Full Control for `NT SERVICE\EventLog`). `MaxSize` sets the maximum size (multiple of 64K) and `Retention` controls overwriting.


