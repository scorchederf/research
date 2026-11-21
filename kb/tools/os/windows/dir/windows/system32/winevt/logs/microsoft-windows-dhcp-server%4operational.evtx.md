---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-DHCP-Server%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - evtx
  - dhcp
aliases:
  - Microsoft-Windows-DHCP-Server/Operational
  - DHCP Server Operational Events
url:
  - https://learn.microsoft.com/windows-server/networking/technologies/dhcp/dhcp-server-events
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/troubleshoot-dhcp-guidance
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-DHCP-Server%4Operational.evtx

# description

Event log file for the DHCP Server operational channel (Applications and Services Logs > Microsoft > Windows > DHCP-Server). It exists on Windows Server with the DHCP Server role. Related channels: DHCP Server Administrative, System, Filter Notification and Audit events; debug logs in `%windir%\System32\Dhcp`.

## simple description

> ### 2026-11-21 Claude said
> This file stores operational events from the Windows DHCP Server role. It records configuration changes such as scopes created, modified, activated or deleted, reservations, filters, policies and failover changes, often including who made them. It only exists on servers running DHCP. Admins use it for change tracking and troubleshooting.
>
> **SOC NOTE**: Useful for detecting rogue configuration changes (e.g. DNS option changed to an attacker server, IDs 76/135; filters added 123/127) that enable AiTM/DNS hijacking (T1557.003). Events include the account (%2/%3) that performed the change. Cross-check with Security 4624/4672 for the admin session.
>

# purpose

Logs DHCP server operational events whenever scopes, options, reservations, filters, policies or failover relationships change. Example IDs: 70 scope configured, 71 modified, 72 deleted, 73/74 activated/deactivated, 76 option update, 119/120 exclusion ranges, 123-128 allow/deny filter changes, 20241-20250 failover changes, 20311 shared secret changed.


