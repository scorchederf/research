---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Admin.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - rdp
  - remote-desktop
aliases:
  - 'Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Admin.evtx'
  - 'Microsoft-Windows-TerminalServices-RemoteConnectionManager/Admin'
url:
  - https://learn.microsoft.com/azure/virtual-desktop/insights-glossary
  - https://learn.microsoft.com/azure/virtual-desktop/insights-costs
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/iaas-logs
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Admin.evtx

# description

Event log file for the **Microsoft-Windows-TerminalServices-RemoteConnectionManager/Admin** channel, written by the Remote Desktop Services Remote Connection Manager. Azure Virtual Desktop Insights collects it (Error, Warning and Information) and it is included in Azure IaaS VM log collections.

## simple description

> ### 2026-11-21 Claude said
> This log is written by the part of Remote Desktop Services that accepts incoming RDP connections. The Admin channel records errors and warnings about the RDP listener, certificates, licensing and connection setup. It sits next to the RemoteConnectionManager Operational log, which holds the per-connection events.
>
> **SOC NOTE**: Useful for spotting RDP listener/configuration problems, certificate (TLS) failures and misconfiguration around the time of suspected RDP abuse (T1021.001). For actual inbound connection attempts, pair with RemoteConnectionManager/Operational 1149, LocalSessionManager 21/24/25 and Security 4624 (type 10)/4625. Log clearing (T1070.001) leaves gaps; check 104/1102.
>

# purpose

Learn lists this channel as one of the required Windows Event Logs for Azure Virtual Desktop Insights (Error, Warning and Information levels), alongside Application, System, TerminalServices-LocalSessionManager/Operational and FSLogix logs, and estimates 1,000-10,000 events per VM per day for healthy environments. The file path appears in the list of files collected from Windows IaaS VM disks.

