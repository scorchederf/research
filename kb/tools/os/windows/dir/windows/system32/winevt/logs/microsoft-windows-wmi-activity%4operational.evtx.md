---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-WMI-Activity%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - event-log
  - wmi
aliases:
  - Microsoft-Windows-WMI-Activity%4Operational.evtx
  - Microsoft-Windows-WMI-Activity/Operational
  - WMI-Activity Operational log
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/troubleshoot-wmi-high-cpu-issues
  - https://learn.microsoft.com/windows/win32/wmisdk/tracing-wmi-activity
  - https://learn.microsoft.com/windows/win32/wmisdk/wmi-log-files
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-WMI-Activity%4Operational.evtx

# description

Event log file backing the Microsoft-Windows-WMI-Activity/Operational channel, shown in Event Viewer under Applications and Services Logs > Microsoft > Windows > WMI-Activity. Since Windows Vista, the WMI service uses Event Tracing for Windows (ETW) instead of text log files, with events viewable in Event Viewer or with `wevtutil`. Related channels are WMI-Activity/Trace and Debug (analytic/debug logs, disabled by default).

## simple description

> ### 2026-11-21 Claude said
> This file stores the WMI-Activity Operational event log. WMI (Windows Management Instrumentation) is a management interface used by admins, software and attackers to query and control Windows. The log records WMI provider loads, client errors and, importantly, permanent WMI event subscriptions. It is enabled by default on modern Windows.
>
> **SOC NOTE**: Event ID 5861 records permanent WMI event consumer bindings, a common persistence technique (MITRE ATT&CK T1546.003); 5857 shows provider DLL loads (useful for malicious providers) and 5858 shows failed queries with client process ID and user. WMI is also used for remote execution and discovery (T1047). Clearing or tampering with this file is anti-forensics (T1070.001).
>

# purpose

Records incoming WMI operations as operational events. For example, Event ID 5857 reports a provider starting, with the host process (`wmiprvse.exe`), process ID and provider path, which helps identify which WmiPrvse.exe instance hosts a given provider when troubleshooting high CPU. More detailed per-query tracing (e.g. `IWbemServices::ExecQuery` with client machine, user and ClientProcessId) is in the Trace channel, which must be enabled via Event Viewer (View > Show Analytic and Debug Logs) or `Wevtutil.exe sl Microsoft-Windows-WMI-Activity/Trace /e:true`. Events can be exported as .xml, .csv or .evtx.
