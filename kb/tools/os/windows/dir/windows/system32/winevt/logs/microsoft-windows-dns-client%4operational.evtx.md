---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-DNS-Client%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - evtx
  - dns
aliases:
  - Microsoft-Windows-DNS-Client%4Operational.evtx
  - Microsoft-Windows-DNS-Client/Operational
url:
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-DNS-Client%4Operational.evtx

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This is the event log file for the DNS Client service's Operational channel. When enabled, it records DNS queries made by the machine, including the name queried and the result (event 3006/3008/3020 etc.). It is disabled by default and can grow quickly. It gives per-host DNS visibility without network capture.
>
> **SOC NOTE**: Enabling this log gives endpoint DNS telemetry for detecting C2 beaconing, DGA domains and DNS tunneling (T1071.004, T1568). Event 3008 (query completed) includes the QueryName and results; correlate with process data from Sysmon event 22.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
