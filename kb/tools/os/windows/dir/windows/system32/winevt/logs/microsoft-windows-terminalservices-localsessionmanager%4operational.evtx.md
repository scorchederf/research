---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - remote-desktop
aliases:
  - Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx
  - Microsoft-Windows-TerminalServices-LocalSessionManager/Operational
  - LocalSessionManager Operational log
url:
  - https://learn.microsoft.com/azure/virtual-desktop/insights-glossary
  - https://learn.microsoft.com/azure/virtual-desktop/insights-costs
  - https://learn.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-terminalservices-localsessionmanager
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx

# description

The on-disk event log file for the `Microsoft-Windows-TerminalServices-LocalSessionManager/Operational` channel. The LocalSessionManager component is responsible for starting the computer and implementing Windows Fast User Switching, and its Operational log is one of the default Windows Event Logs collected by Azure Virtual Desktop Insights (Error, Warning and Information events).

## simple description

> ### 2026-11-21 Claude said
> This file stores the events written by the Local Session Manager, the Windows service that creates and tracks user sessions (console and Remote Desktop). Every time a user logs on, logs off, disconnects or reconnects a session, an event is written here. The `%4` in the name is an encoded `/`, so in Event Viewer it appears under Applications and Services Logs > Microsoft > Windows > TerminalServices-LocalSessionManager > Operational.
>
> **SOC NOTE**: Key RDP / lateral-movement artifact (MITRE T1021.001). Event IDs 21 (logon), 22 (shell start), 23 (logoff), 24 (disconnect), 25 (reconnect) record user, session ID and source IP; 39/40 record disconnect reasons. Correlate with Security 4624 (type 10) and RemoteConnectionManager 1149. Attackers clearing it (T1070.001) leaves gaps; check System 104.
>

# purpose

Records operational events of the TerminalServices LocalSessionManager component, which handles session start-up and Fast User Switching. Azure Virtual Desktop Insights lists this channel as a required Windows Event Log (Error, Warning and Information), and estimates per-VM event volume of roughly 1,000 to 10,000 events per day across its default logs.
