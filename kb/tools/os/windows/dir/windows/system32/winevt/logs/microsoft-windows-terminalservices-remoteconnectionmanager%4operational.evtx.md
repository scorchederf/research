---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - evtx
  - rdp
aliases:
  - Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational
url:
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/troubleshoot-rds-instability-september-2026-windows-updates
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/iaas-logs
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/event-tracing-for-windows-simplified
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational.evtx

# description

Event log file backing the `Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational` channel of Remote Desktop Services. Learn lists it among the RDS logs to review when troubleshooting RDS, and among the files collected from Windows IaaS VM disks. Related logs: LocalSessionManager/Operational, RemoteConnectionManager/Admin, RdpCoreTS/Operational.

## simple description

> ### 2026-11-21 Claude said
> This file stores events from the Remote Connection Manager, the part of Remote Desktop that accepts incoming RDP connections. It records when a remote client connects and passes network-level authentication. Every Windows machine with RDP enabled writes to it. Analysts use it to see who connected over RDP and from which IP address.
>
> **SOC NOTE**: Event ID 1149 ("User authentication succeeded") records the username, domain and source IP of successful network-level RDP authentication, even when Security log 4624 has rolled over; key for lateral movement (T1021.001) and brute-force follow-up. Attackers may clear it (T1070.001) — look for 104/1102 log-cleared events.
>

# purpose

Records operational events of the RDS Remote Connection Manager (TermService listener). Learn recommends reviewing it, together with LocalSessionManager/Operational, RdpCoreTS/Operational, System and Application, when diagnosing RDS instability. Its ETW provider can also be traced with logman and converted with `tracerpt`.


