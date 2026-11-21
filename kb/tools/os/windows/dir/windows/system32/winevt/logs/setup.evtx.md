---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Setup.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
aliases:
  - Setup.evtx
  - Setup event log
url:
  - https://learn.microsoft.com/windows/win32/eventlog/eventlog-key
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/iaas-logs
  - https://learn.microsoft.com/troubleshoot/windows-server/application-management/move-event-viewer-log-files
---

**fullpath**:C:\Windows\System32\winevt\Logs\Setup.evtx

# description

Setup.evtx is the file backing the Windows "Setup" event log, stored in the default event log folder `%SystemRoot%\system32\winevt\logs\`. Learn lists it among the Windows event logs collected from Azure IaaS VM disks for diagnostics. Logs can be read with Event Viewer or `wevtutil`.

## simple description

> ### 2026-11-21 Claude said
> Setup.evtx is the 'Setup' log you see under Windows Logs in Event Viewer. It records installation of Windows updates, roles, features and servicing packages (CBS), including success, failure and reboot requirements. It is useful to see when patches were installed or removed.
>
> **SOC NOTE**: Use it to confirm patch installation/uninstallation times (e.g. events 1, 2, 3, 4 from Microsoft-Windows-Servicing), which helps spot attackers removing security updates (MITRE ATT&CK T1562.001) and builds the patch-level timeline during an incident. Missing or recently cleared logs indicate tampering (T1070.001).
>

# purpose

Stores Setup channel events. Event log files default to `%SystemRoot%\system32\winevt\logs\` with a file name based on the log name; the path can be changed with `wevtutil.exe`, `EvtSetChannelConfigProperty`, or the log's Properties in Event Viewer, and the event log folder grants Authenticated Users only Read access.
