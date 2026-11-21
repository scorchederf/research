---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - event-log
aliases:
  - "Logs"
  - "winevt\\Logs"
  - "%SystemRoot%\\System32\\winevt\\Logs"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/application-management/move-event-viewer-log-files
  - https://learn.microsoft.com/windows/win32/eventlog/eventlog-key
  - https://learn.microsoft.com/windows-server/networking/dns/dns-logging-and-diagnostics
---

**fullpath**:C:\Windows\System32\winevt\Logs

# description

Default folder for Windows Event Log files. Event Viewer, `wevtutil.exe` and the Event Log service use it; each channel's file path is stored in the registry (the `File` value under the Eventlog key) and can be changed.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the actual .evtx files behind Event Viewer: Security, System, Application and hundreds of Microsoft-Windows-* logs.
> Each log is a binary file that grows to a maximum size and then overwrites older events by default.
> It is one of the first places analysts collect from during an investigation.
>
> **SOC NOTE**: Core forensic artifact. Attackers clear or delete logs here (T1070.001); look for Security 1102 and System 104, missing/truncated files, or the EventLog service being stopped. Collect the whole folder (e.g., with KAPE) for timeline analysis.
>

# purpose

By default Event Viewer log files are located in `%SystemRoot%\System32\winevt\Logs`. If the `File` registry value is not specified, it defaults to `%SystemRoot%\system32\winevt\logs\` plus a name based on the event log key. When moving logs elsewhere, Microsoft recommends matching this folder's permissions (Authenticated Users read only; NT SERVICE\EventLog full control).

# common files found

| file | description |
| --- | --- |
| `Application.evtx` | Events logged by programs. |
| `Security.evtx` | Logon attempts and resource-use audit events. |
| `System.evtx` | Events logged by Windows system components. |
| `Directory Service.evtx` | Active Directory events (domain controllers only). |
| `DNS Server.evtx` | DNS Server events (DNS servers only). |
| `File Replication Service.evtx` | Replication events between domain controllers. |
| `Microsoft-Windows-DNSServer%4Analytical.etl` | DNS Server analytic log, when enabled. |
