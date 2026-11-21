---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbem\Logs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - wmi
aliases:
  - Logs
  - WMI log folder
url:
  - https://learn.microsoft.com/windows/win32/wmisdk/logging-wmi-activity
  - https://learn.microsoft.com/windows/win32/wmisdk/wmi-log-files
  - https://learn.microsoft.com/windows/win32/wmisdk/wmi-provider-log-files
  - https://learn.microsoft.com/windows-hardware/drivers/kernel/general-techniques-for-testing-wmi-driver-support
---

**fullpath**:C:\Windows\System32\wbem\Logs

# description

`%windir%\system32\wbem\logs` is the Windows Management Instrumentation (WMI) log folder where WMI core components and WMI providers wrote text log files. Only administrators have read access to it. Starting with Windows Vista the WMI log files are no longer supported and WMI uses Event Tracing for Windows (ETW), viewable in Event Viewer or with `wevtutil`; Windows Driver Model (WDM) providers continue to log to text files.

## simple description

> ### 2026-11-21 Claude said
> This folder is where WMI, the Windows management engine used by admin tools and scripts, used to write its text log files. On modern Windows most WMI activity goes to the event log (Microsoft-Windows-WMI-Activity) instead, so this folder is often small or nearly empty. Some providers, such as the WDM provider, may still write logs like Wmiprov.log here.
>
> **SOC NOTE**: WMI is heavily abused for execution, lateral movement and persistence (MITRE ATT&CK T1047 Windows Management Instrumentation, T1546.003 WMI Event Subscription). On modern systems hunt in the Microsoft-Windows-WMI-Activity/Operational log (events 5857-5861) rather than this folder; unexpected or recently written files here, or text logs referencing unusual providers or namespaces, are worth review on legacy hosts.
>

# purpose

The WMI log folder stores logs that record events, trace or diagnostic data, errors and activities of WMI core components and providers. Before Windows Vista its location was set by `HKLM\SOFTWARE\Microsoft\WBEM\CIMOM\Logging Directory` (default `%windir%\system32\wbem\logs`), with logging level and `Log File Max Size` values under the same key. WMI errors handled by the WDM provider (Wmiprov.dll) are still logged to `%windir%\system32\wbem\logs\wmiprov.log`.

# common files found

| file | description |
| --- | --- |
| `Wmiprov.log` | Management data, warnings and errors from WMI-enabled WDM drivers and the WDM Provider, including MOF compile status. |
| `Ntevt.log` | Trace messages from the Event Log Provider. |
| `Dsprovider.log` | Log file of the Directory Services provider (listed on Learn as a provider log). |
| `ViewProvider.log` | Example log for the View Provider when provider logging is enabled through `HKLM\SOFTWARE\Microsoft\WBEM\PROVIDERS\Logging\ViewProvider`. |
| `WMITracing.log` | Records WMI service activity when WMI event tracing is enabled (see Tracing WMI Activity). |
