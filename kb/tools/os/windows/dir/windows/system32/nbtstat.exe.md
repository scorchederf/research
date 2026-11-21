---
created: 2026-11-21
fullpath: 'C:\Windows\System32\nbtstat.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - network
  - netbios
aliases:
  - "nbtstat.exe"
  - "nbtstat"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/nbtstat
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/nbtstat-a-not-resolve-computer-name
---

**fullpath**:C:\Windows\System32\nbtstat.exe

# description

nbtstat displays NetBIOS over TCP/IP (NetBT) protocol statistics, NetBIOS name tables for local and remote computers, and the NetBIOS name cache, and can refresh the cache and names registered with WINS. It is a built-in Windows command, available only if TCP/IP is installed on a network adapter.

## simple description

> ### 2026-11-21 Claude said
> nbtstat.exe is a built-in network troubleshooting tool for NetBIOS over TCP/IP, the legacy Windows name service. It can show which NetBIOS names a computer has registered, list the local NetBIOS name cache, and show active NetBIOS sessions. Administrators use it to troubleshoot name resolution and WINS problems.
>
> **SOC NOTE**: Attackers use `nbtstat -a`/`-A` and `nbtstat -n`/`-c` for host and network discovery (T1016 System Network Configuration Discovery, T1018 Remote System Discovery); the `<1C>`/`<1B>` suffixes reveal domain controllers. nbtstat runs in bursts against many IPs are a recon indicator; review process creation logs and NetBIOS (UDP 137) traffic.
>

# purpose

Displays NetBT statistics, local and remote NetBIOS name tables, the NetBIOS name cache and session table, and purges or refreshes cached and WINS-registered names. Parameters are case-sensitive.

# typical use cases

| usage | description |
| --- | --- |
| `nbtstat /a CORP07` | Display the NetBIOS name table of the remote computer CORP07. |
| `nbtstat /A 10.0.0.99` | Display the NetBIOS name table of the remote computer at 10.0.0.99. |
| `nbtstat /n` | Display the NetBIOS name table of the local computer. |
| `nbtstat /c` | Display the contents of the local NetBIOS name cache. |
| `nbtstat /R` | Purge the NetBIOS name cache and reload pre-tagged Lmhosts entries. |
| `nbtstat /RR` | Release and re-register NetBIOS names with the WINS server. |
| `nbtstat /S 5` | Display NetBIOS session statistics by IP address every five seconds. |

# options

| option | description |
| --- | --- |
| `/a <remotename>` | Displays the NetBIOS name table of a remote computer by NetBIOS computer name. |
| `/A <IPaddress>` | Displays the NetBIOS name table of a remote computer by IP address. |
| `/c` | Displays the NetBIOS name cache and resolved IP addresses. |
| `/n` | Displays the NetBIOS name table of the local computer. |
| `/r` | Displays NetBIOS name resolution statistics. |
| `/R` | Purges the NetBIOS name cache and reloads pre-tagged entries from Lmhosts. |
| `/RR` | Releases and refreshes local NetBIOS names registered with WINS servers. |
| `/s` | Displays NetBIOS client and server sessions, converting destination IPs to names. |
| `/S` | Displays NetBIOS client and server sessions by destination IP address only. |
| `<interval>` | Redisplays selected statistics every interval seconds until CTRL+C. |
| `/?` | Displays help at the command prompt. |
