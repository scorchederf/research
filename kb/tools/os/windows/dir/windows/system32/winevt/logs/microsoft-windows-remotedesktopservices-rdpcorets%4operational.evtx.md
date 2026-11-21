---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - rdp
aliases:
  - Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Operational.evtx
  - RdpCoreTS Operational log
url:
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Operational.evtx

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> This event log records the low-level RDP protocol activity of the Remote Desktop server component (RdpCoreTS). It logs incoming TCP/UDP connections to the RDP listener, transport negotiation, security/encryption setup and disconnect reasons. It exists on any Windows machine that accepts Remote Desktop connections. It is found in Event Viewer under Applications and Services Logs > Microsoft > Windows > RemoteDesktopServices-RdpCoreTS > Operational.
>
> **SOC NOTE**: Key RDP forensic source (MITRE ATT&CK T1021.001 Remote Desktop Protocol): event 131 records the client IP:port of every accepted connection, even failed or pre-authentication ones, and 98/99/102/103 show transport and disconnect info. Combine with Security 4624 (LogonType 10) / 4625, TerminalServices-LocalSessionManager (21/24/25) and RemoteConnectionManager (1149) to reconstruct RDP sessions and detect brute force (T1110).
>
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
