---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-Gateway%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - eventlog
  - rdp
aliases:
  - Microsoft-Windows-TerminalServices-Gateway%4Operational.evtx
  - Microsoft-Windows-TerminalServices-Gateway/Operational
url:
  - https://learn.microsoft.com/entra/identity/authentication/howto-mfa-nps-extension-rdg
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-Gateway%4Operational.evtx

# description

Event log file for the Remote Desktop Gateway operational channel, shown in Event Viewer under **Applications and Services Logs\Microsoft\Windows\TerminalServices-Gateway\Operational**. It is written on servers running the RD Gateway role service.

## simple description

> ### 2026-11-21 Claude said
> This file stores the RD Gateway server's operational events. RD Gateway lets users reach internal Remote Desktop hosts over HTTPS (port 443). The log records who connected through the gateway, from which IP, to which internal host, and whether they met the connection (CAP) and resource (RAP) authorization policies.
>
> **SOC NOTE**: Key for investigating external RDP access and lateral movement (T1133 External Remote Services, T1021.001). Useful event IDs include 200 (CAP passed), 300 (RAP passed), 302/303 (connected/disconnected with bytes and duration), 201/304 and 312 failures. Correlate client IPs with Security 4624/4625 on the gateway and target hosts; brute force against the gateway shows up here.
>

# purpose

Records RD Gateway authorization and connection events. Learn shows querying it with PowerShell: event ID 300 shows the user met resource authorization policy (RD RAP) requirements and was granted access, and event ID 200 is queried for successful sign-in through the connection authorization policy.

| usage | description |
| --- | --- |
| `Get-WinEvent -Logname Microsoft-Windows-TerminalServices-Gateway/Operational \| where {$_.ID -eq '300'} \| FL` | Show events where the user met RD RAP requirements and was granted access. |
| `Get-WinEvent -Logname Microsoft-Windows-TerminalServices-Gateway/Operational \| where {$_.ID -eq '200'} \| FL` | Show event ID 200 sign-in events. |
