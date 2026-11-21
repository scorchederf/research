---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-DNSServer%4Analytical.etl'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - etl
  - dns
aliases:
  - Microsoft-Windows-DNSServer/Analytical
  - DNS Server analytic log
url:
  - https://learn.microsoft.com/windows-server/networking/dns/dns-logging-and-diagnostics
  - https://learn.microsoft.com/windows-server/networking/dns/monitor-dns-over-https
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-DNSServer%4Analytical.etl

# description

Default file for the DNS Server Analytical event log, part of enhanced DNS logging and diagnostics in Windows Server. Analytic logging is off by default and is enabled in Event Viewer (DNS-Server > Show Analytic and Debug Logs > Analytical > Enable logging); events can also be traced with ETW provider GUID `{EB79061A-A566-4698-9119-3ED2807060E7}`. Related: DNS-Server Audit log, `%windir%\System32\dns\Dns.log` debug log.

## simple description

> ### 2026-11-21 Claude said
> This .etl file stores the DNS Server analytic events, which record individual DNS queries and responses handled by a Windows DNS server. It only exists on servers with the DNS role where an admin turned analytic logging on. It can grow quickly on busy servers. It is one of the best sources for seeing which clients looked up which names.
>
> **SOC NOTE**: High forensic value for C2 and exfiltration hunting (T1071.004, T1568): per-query records with client IP, QNAME, QTYPE and RCODE. Its absence on a DC means DNS query history must come from other sources (Sysmon 22 on clients, network sensors). Attackers with admin can disable the channel (T1562.002).
>

# purpose

Records analytic events (per-query/response activity, including DNS over HTTPS events 597-600) of the DNS Server service; a 5% performance impact is noted at around 100,000 queries per second.


