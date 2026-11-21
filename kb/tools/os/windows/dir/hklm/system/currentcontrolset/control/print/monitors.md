---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - print-spooler
  - persistence
aliases:
  - "Monitors"
  - "Print Monitors key"
url:
  - https://learn.microsoft.com/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintmonitor
  - https://learn.microsoft.com/windows-hardware/drivers/print/initializing-a-print-monitor
  - https://learn.microsoft.com/windows-hardware/drivers/print/installing-a-print-monitor
  - https://learn.microsoft.com/windows-hardware/drivers/print/storing-port-configuration-information
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors

# description

Registry location where the print spooler registers installed print monitors (language monitors and port monitors). Monitors are added with the spooler's AddMonitor function or via a printer INF, and removed with DeleteMonitor. Related to the Print Spooler service (spoolsv.exe) and port monitors such as TCPMON and WSDMON.

## simple description

> ### 2026-11-21 Claude said
> Each subkey under Monitors is a print monitor the Print Spooler loads, and its Driver value names the DLL. When the spooler service starts it loads all of these DLLs into spoolsv.exe, which runs as SYSTEM. Normal entries include Local Port, Standard TCP/IP Port and WSD Port.
>
> **SOC NOTE**: Well-known persistence and privilege-escalation spot (MITRE ATT&CK T1547.010 Port Monitors): adding a subkey with a Driver value pointing to a malicious DLL in System32 makes spoolsv.exe load it as SYSTEM at every boot. Hunt for new subkeys or unsigned DLLs, Sysmon EID 13 writes to this key, and AddMonitor API usage.
>

# purpose

When the spooler is first started, it loads all of the monitor DLLs that have been installed, calls each monitor's initialization function, then enumerates and opens the ports each port monitor supports. The InitializePrintMonitor pRegistryRoot parameter points to a MonitorName registry key, where MonitorName is the name given when AddMonitor was called; the monitor can store its own values there, and DeleteMonitor removes the key and everything under it. Print monitors should store configuration using the spooler registry functions (MONITORREG) rather than the Win32 registry API, so data goes to the correct local or cluster registry.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# subkeys

| subkey | description |
| --- | --- |
| `<MonitorName>` | One key per installed monitor, named as specified when AddMonitor was called; holds monitor-specific values and is deleted by DeleteMonitor. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors"` | List the key's values. |
