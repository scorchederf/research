---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-DNSServer%4Audit.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - eventlog
  - dns
aliases:
  - Microsoft-Windows-DNSServer%4Audit.evtx
  - DNS-Server Audit log
  - Microsoft-Windows-DNSServer/Audit
url:
  - https://learn.microsoft.com/windows-server/networking/dns/dns-logging-and-diagnostics
  - https://learn.microsoft.com/azure/azure-monitor/reference/tables/dnsauditevents
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-DNSServer%4Audit.evtx

# description

Event log file for the DNS Server audit channel (Applications and Services Logs > Microsoft > Windows > DNS-Server > Audit) on Windows Server with the DNS Server role. Audit logging is enabled by default and records changes to server, zone and resource record settings.

## simple description

> ### 2026-11-21 Claude said
> This is the event log file where a Windows DNS server records audit events. Every time someone changes DNS server settings, zones or records, an event is written here. It also logs dynamic updates, zone transfers and DNSSEC signing. You view it in Event Viewer under DNS-Server > Audit.
>
> **SOC NOTE**: Valuable for detecting malicious DNS record changes (e.g. ADIDNS wildcard/record injection for spoofing or MITM), zone deletions and listen-address changes. Key IDs: 513 zone delete, 515 record create, 516 record delete, 541 server setting, 557 listen address. Forward to SIEM (Sentinel table DnsAuditEvents).
>

# purpose

Change tracking for the DNS Server: audit events for zone operations, dynamic updates, configuration changes, server operations and DNSSEC operations (event IDs 513-582). ETW provider GUID `{EB79061A-A566-4698-9119-3ED2807060E7}`.
