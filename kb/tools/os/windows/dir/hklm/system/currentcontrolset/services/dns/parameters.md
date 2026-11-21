---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - dns-server
aliases:
  - "DNS\Parameters"
  - "DNS Server service parameters"
url:
  - https://learn.microsoft.com/windows-server/networking/dns/network-ports
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/enable-disable-dns-dynamic-registration
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/a-record-registered-host-dns
---

**fullpath**: HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters

# description

Registry key holding configuration parameters for the Windows Server DNS Server service. Microsoft Learn documents values here for controlling EDNS0 probing and which IP addresses the DNS server publishes as A records. The same settings are normally managed with the DNS console (DNS Manager).

## simple description

> ### 2026-11-21 Claude said
> This key stores settings for the DNS Server role on Windows Server, i.e. the service that answers DNS queries for a domain. Each value changes how the DNS server behaves, for example which addresses it advertises or whether it uses EDNS0. It only exists on servers with the DNS Server role, usually domain controllers. The service reads these values when it starts.
>
> **SOC NOTE**: The ServerLevelPluginDll value under this key is a well-known privilege-escalation/persistence technique: members of DnsAdmins can set it (dnscmd /config /serverlevelplugindll) so dns.exe loads an attacker DLL as SYSTEM on a domain controller (T1574 Hijack Execution Flow, T1543). Monitor registry changes to this key (Sysmon 13, Security 4657) and DNS Server event 150/770 for plugin load failures/successes.
>

# purpose

Stores DNS Server service settings. DNS reads its registry entries only when it starts; changes made by editing the registry take effect after the DNS server is restarted, while the DNS console can change entries while the server runs.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

| value name | type | description |
| --- | --- | --- |
| `EnableEDNSProbes` | REG_DWORD | EDNS0 is enabled by default; set to `0x0` to disable EDNS0 on the DNS server. |
| `PublishAddresses` | REG_SZ | Space-separated list of IP addresses to publish; the DNS server creates A records only for these. Blank or absent means an A record for every IP address. Not added by default. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters"` | List the key's values. |
| `reg add "HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters" /v EnableEDNSProbes /t REG_DWORD /d 0` | Disable EDNS0 (restart the DNS Server service to apply). |
