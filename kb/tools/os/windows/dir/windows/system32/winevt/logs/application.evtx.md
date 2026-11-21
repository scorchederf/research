---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Application.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
aliases:
  - Application.evtx
  - Application log
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/application-management/move-event-viewer-log-files
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-eventlog
  - https://learn.microsoft.com/windows/win32/eventlog/eventlog-key
---

**fullpath**:C:\Windows\System32\winevt\Logs\Application.evtx

# description

File backing the Windows Application event log, in the default folder `%SystemRoot%\System32\winevt\Logs`. The Application log contains events logged by programs, as determined by their developers. Location can be changed via the `Software\Policies\Microsoft\Windows\EventLog\Application` policy or the Eventlog `File` registry value.

## simple description

> ### 2026-11-21 Claude said
> Application.evtx stores events written by applications and services, such as crashes (Event 1000 Application Error), installer messages (MsiInstaller), antivirus and database events. Any program can register an event source and write here. It is readable by most users. It is a standard first stop when troubleshooting or investigating.
>
> **SOC NOTE**: Useful evidence: MsiInstaller 1033/11707 show software installs, Application Error 1000/1001 crashes can reveal exploitation or injected processes, and some AV/EDR products log detections here. Attackers can write fake events or clear the log (MITRE ATT&CK T1070.001).
>

# purpose

Stores application-generated events. Default `MaxSize` and `Retention` are controlled through the Eventlog registry key.
