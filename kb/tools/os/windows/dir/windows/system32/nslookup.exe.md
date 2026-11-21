---
created: 2026-11-21
fullpath: 'C:\Windows\System32\nslookup.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dns
  - network
aliases:
  - nslookup.exe
  - nslookup
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/nslookup
---

**fullpath**:C:\Windows\System32\nslookup.exe

# description

`nslookup` displays information used to diagnose Domain Name System (DNS) infrastructure. It is a built-in Windows command, available when TCP/IP is installed, and works in interactive or noninteractive mode.

## simple description

> ### 2026-11-21 Claude said
> nslookup.exe is the classic Windows tool for querying DNS servers: it resolves names to IP addresses, IPs to names, and can look up specific record types like MX, TXT or SRV. Admins use it to troubleshoot name resolution. You can run one query from the command line or enter an interactive prompt to issue many queries.
>
> **SOC NOTE**: Used for discovery (MITRE T1018, T1016, e.g. `nslookup -type=SRV _ldap._tcp.dc._msdcs.<domain>` to find DCs) and abused to retrieve payloads via DNS TXT records (T1071.004/T1105, e.g. `nslookup -q=txt` piped into PowerShell). Flag nslookup spawned by Office, script hosts, or with TXT queries to unusual domains; correlate with DNS client logs/Sysmon 22.
>

# purpose

Diagnoses DNS infrastructure. In noninteractive mode, the first parameter is the name or IP to look up and the second is the DNS server; in interactive mode (`nslookup` or `nslookup -`) multiple queries and settings can be entered.

# typical use cases

| usage | description |
| --- | --- |
| `nslookup mydomain.com 1.1.1.1` | Looks up IP addresses for a domain using DNS server 1.1.1.1. |
| `nslookup 4.4.4.4` | Reverse-looks up a name for an IP on the default server. |
| `nslookup -debug mydomain.com` | Turns on debug output for packets sent. |
| `nslookup -type=AAAA mydomain.com` | Returns only IPv6 records. |
| `nslookup -debug -type=A+AAAA -nosearch -recurse mydomain.com 1.1.1.1` | Combines options and record types. |
| `nslookup - 1.1.1.1` | Enters interactive mode with 1.1.1.1 as default server. |

# options

| option | description |
| --- | --- |
| `exit` | Exits nslookup. |
| `finger` | Connects with the finger server on the current computer. |
| `help` | Displays a short summary of subcommands. |
| `ls` | Lists information for a DNS domain. |
| `lserver` | Changes the default server to the specified DNS domain (using the initial server). |
| `root` | Changes the default server to the root server of the DNS name space. |
| `server` | Changes the default server to the specified DNS domain. |
| `set` | Changes configuration settings that affect lookups. |
| `set all` | Prints current configuration settings. |
| `set class` | Changes the query class. |
| `set d2` | Turns exhaustive debugging mode on or off. |
| `set debug` | Turns debugging mode on or off. |
| `set domain` | Changes the default DNS domain name. |
| `set port` | Changes the default TCP/UDP DNS name server port. |
| `set querytype` | Changes the resource record type for the query. |
| `set recurse` | Tells the server to query other servers if it doesn't have the information. |
| `set retry` | Sets the number of retries. |
| `set root` | Changes the name of the root server used for queries. |
| `set search` | Appends search-list domain names to the request until an answer is received. |
| `set srchlist` | Changes the default DNS domain name and search list. |
| `set timeout` | Changes the initial seconds to wait for a reply. |
| `set type` | Changes the resource record type for the query. |
| `set vc` | Specifies whether to use a virtual circuit for requests. |
| `view` | Sorts and lists output of the previous `ls` subcommand(s). |

