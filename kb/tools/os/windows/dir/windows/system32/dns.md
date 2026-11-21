---
created: 2026-11-21
fullpath: 'C:\Windows\System32\dns'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - dns-server
aliases:
  - dns
  - %systemroot%\System32\Dns
url:
  - https://learn.microsoft.com/windows-server/networking/dns/dns-logging-and-diagnostics
  - https://learn.microsoft.com/azure/dns/dns-import-export
  - https://learn.microsoft.com/windows-server/administration/windows-commands/dnscmd
  - https://learn.microsoft.com/windows-server/networking/dns/quickstart-install-configure-dns-server
  - https://learn.microsoft.com/windows/win32/dns/microsoftdns-server
---

**fullpath**:C:\Windows\System32\dns

# description

`%systemroot%\System32\dns` is the DNS directory of the Windows Server DNS Server role. It is the default folder for file-backed zone files, the default location of the DNS debug log (`dns.log`) and the default output folder of `dnscmd /zoneexport`.

## simple description

> ### 2026-11-21 Claude said
> On Windows servers running the DNS Server role, this folder holds the DNS zone files (.dns) for non-AD-integrated zones, backups, and the DNS debug log when enabled. On workstations it normally does not exist or is empty.
>
> **SOC NOTE**: Zone files and exports here can reveal the internal host inventory useful for reconnaissance. The DNS debug log (dns.log) records queries and is valuable for hunting C2 domains and DNS tunnelling. Historically DnsAdmins abuse loaded a ServerLevelPluginDll into dns.exe (MITRE ATT&CK T1574); also watch for log paths changed or log files deleted.
>

# purpose

Stores DNS server data. Starting with the 2026-11 cumulative updates, DNS Server only honors debug log paths under `C:\Windows\System32\dns\`; a path outside it triggers Event ID 506 and the log is relocated to `C:\Windows\System32\dns\log\dns.log`, and changing `LogFilePath` requires local Administrators membership. When the DNS role is removed, standard zone files remain here but are not reloaded on reinstall.

# common files found

| file | description |
| --- | --- |
| `<zone>.dns` | Zone files for zones hosted on Windows DNS (full path shown on the zone's General tab). |
| `dns.log` | DNS debug log (default `%windir%\system32\dns`, `LogFilePath` default `%system32%\dns\dns.log`). |
| `log\dns.log` | Relocated debug log location when a configured path is outside the dns directory. |
| `<zoneexportfile>` | Resource record list created by `dnscmd /zoneexport`. |
