---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbem\WmiPrvSE.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - wmi
aliases:
  - WmiPrvSE.exe
  - WMI Provider Host
url:
  - https://learn.microsoft.com/windows/win32/wmisdk/provider-hosting-and-security
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/troubleshoot-wmi-high-cpu-issues
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/scenario-guide-troubleshoot-wmiprvse-quota-exceeded-issues
  - https://learn.microsoft.com/windows/win32/wmisdk/providing-data-to-wmi
---

**fullpath**:C:\Windows\System32\wbem\WmiPrvSE.exe

# description

`WmiPrvSE.exe` (WMI Provider Host) is the shared host process into which Windows Management Instrumentation loads provider DLLs, so that a failing provider does not stop the WMI service (Winmgmt, hosted in svchost.exe). Several instances can run at once, each under LocalSystem, NetworkService or LocalService.

## simple description

> ### 2026-11-21 Claude said
> WmiPrvSE.exe runs the WMI providers that answer management queries such as "list processes" or "read the event log". It is started on demand by the WMI service and exits when idle. Several copies running at once is normal. It is not normally started by a user.
>
> **SOC NOTE**: Processes spawned by WmiPrvSE.exe (cmd.exe, powershell.exe, rundll32.exe) are a strong indicator of remote WMI execution such as `wmic process call create` or Impacket wmiexec (T1047), and of WMI event subscription persistence (T1546.003). Check Microsoft-Windows-WMI-Activity/Operational (5857 provider load, 5860/5861 subscriptions) and Security 4688 parent-child chains.
>

# purpose

Hosts coupled in-process WMI providers (COM DLLs such as `ntevt.dll` for `MS_NT_EVENTLOG_PROVIDER`, `cimwin32.dll`). The provider's `__Win32Provider.HostingModel` property decides which shared host and account are used. Learn troubleshooting covers identifying the hosted providers per PID, high CPU, and quota-exceeded stops (WMI-Activity event 5612, e.g. `PrivatePageCount` exceeding `MemoryPerHost`).

# typical use cases

| usage | description |
| --- | --- |
| `tasklist /m ntevt.dll` | Find the current WmiPrvSE.exe PID that has a given provider DLL loaded. |

# options

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_
