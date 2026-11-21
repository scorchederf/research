---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Windows PowerShell.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - powershell
aliases:
  - Windows PowerShell.evtx
  - Windows PowerShell event log
url:
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.diagnostics/get-winevent
  - https://learn.microsoft.com/troubleshoot/windows-server/application-management/move-event-viewer-log-files
---

**fullpath**:C:\Windows\System32\winevt\Logs\Windows PowerShell.evtx

# description

Classic `Windows PowerShell` event log file stored in the default event log folder `%SystemRoot%\System32\winevt\Logs`. It is written by the `PowerShell` provider and can be read with `Get-WinEvent -Path`; Learn's examples show engine state events (400, 403) and provider lifecycle events (600).

## simple description

> ### 2026-11-21 Claude said
> This is the classic Windows PowerShell log, separate from the newer PowerShell/Operational log. Every time a PowerShell engine starts or stops it writes events here (400 engine start, 403 engine stop, 600 provider start, 800 pipeline execution when module logging is on). Event 400 includes the host application command line, which often reveals how PowerShell was launched.
>
> **SOC NOTE**: Very useful for detecting PowerShell abuse (MITRE ATT&CK T1059.001), including downgrade attacks: an event 400 with `EngineVersion=2.0` indicates PowerShell v2, which bypasses Script Block Logging. `HostApplication` in event 400/600 exposes encoded commands (`-enc`). Clearing this log (T1070.001) is itself suspicious.
>

# purpose

Stores events from the `PowerShell` provider, such as engine state changes (`Engine state is changed from None to Available` = 400, `Available to Stopped` = 403) and provider starts (600).
