---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RDPClient%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - evtx
  - remote-desktop
aliases:
  - Microsoft-Windows-TerminalServices-RDPClient%4Operational.evtx
  - Microsoft-Windows-TerminalServices-RDPClient/Operational
url:
  - https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-security
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RDPClient%4Operational.evtx

# description

Event log file for the **Microsoft-Windows-TerminalServices-RDPClient/Operational** channel, written by the Remote Desktop client (mstsc). Microsoft's Azure Local security event set collects event ID 1024 from this channel to log attempted Terminal Services connections to remote servers.

## simple description

> ### 2026-11-21 Claude said
> This log is written on the machine where someone runs the Remote Desktop client. It records outgoing RDP connection attempts, including the destination server name or IP. It is useful to see where a user or attacker connected to from this host. It is enabled by default.
>
> **SOC NOTE**: Source-side evidence of RDP lateral movement (T1021.001): event 1024 (connecting to server), 1102 (destination IP) and 1029 (hash of username) show outbound RDP from a compromised host even if the destination logs are wiped.
>

# purpose

Records outbound Remote Desktop client activity.

| event ID | description |
| --- | --- |
| 1024 | Log attempted TS connect to remote server (query `Microsoft-Windows-TerminalServices-RDPClient/Operational!*[System[(EventID=1024)]]`). |

