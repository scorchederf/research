---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\DNS Server.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - dns
aliases:
  - "DNS Server.evtx"
  - "DNS Server log"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/application-management/move-event-viewer-log-files
  - https://learn.microsoft.com/windows-server/networking/dns/troubleshoot/troubleshoot-dns-server
  - https://learn.microsoft.com/windows-server/networking/dns/monitor-dns-over-https
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/events-407-408-in-dns-server-event-log
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/dns-server-logs-event-7062
---

**fullpath**:C:\Windows\System32\winevt\Logs\DNS Server.evtx

# description

`DNS Server.evtx` backs the classic DNS Server event log (Applications and Services Logs > DNS Server) on Windows Server hosts running the DNS Server role. It is separate from the `Microsoft-Windows-DNSServer/Audit` and `/Analytical` channels.

## simple description

> ### 2026-11-21 Claude said
> This file contains the DNS Server service's own event log on Windows DNS servers (often domain controllers).
> It records service start/stop, zone loading problems, socket binding errors and similar operational messages.
> It does not contain every DNS query; that needs analytic logging or debug logs.
>
> **SOC NOTE**: Useful for spotting DNS service failures, zone transfer/config problems and, on Server 2025 with DoH, DoH events 597-603. For attacks like ServerLevelPluginDll abuse (T1574/DnsAdmins), check for service restarts and plugin load errors here (e.g., events 150/770).
>

# purpose

The DNS Server log contains events related to resolving DNS names to or from IP addresses and is available only on DNS servers. It is one of the logs to check when troubleshooting (with Application and System). Examples include events 407/408 (cannot bind/open socket) and 7062 (packet addressed to itself).
