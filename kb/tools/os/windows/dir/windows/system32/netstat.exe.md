---
created: 2026-11-21
fullpath: 'C:\Windows\System32\netstat.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - networking
  - windows-commands
aliases:
  - 'netstat.exe'
  - 'netstat'
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/netstat
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/determine-which-program-use-block-tcp-ports
---

**fullpath**: C:\Windows\System32\netstat.exe

# description

Built-in Windows command that displays active TCP connections, listening ports, Ethernet statistics, the IP routing table and IPv4/IPv6 statistics. It's available only if TCP/IP is installed. Related tools: `route print` (equivalent to `-r`), Task Manager to map PIDs, and Sysinternals TCPView/Tcpvcon.

## simple description

> ### 2026-11-21 Claude said
> netstat shows what network connections the computer has right now and which ports it is listening on. With -o it shows the process ID owning each connection, and with -b the program name. Admins use it to troubleshoot and to see what is talking to the network.
>
> **SOC NOTE**: Frequently run by attackers for discovery (MITRE T1049 System Network Connections Discovery); `netstat -ano` from unusual parents (Office, web server, scripts) is suspicious. For responders, `netstat -anob` quickly maps suspicious remote IPs/ports to processes (C2, listeners, reverse shells).
>

# purpose

Displays network connections, listening ports, protocol statistics and the routing table; used without parameters it shows active TCP connections.

# typical use cases

| usage | description |
| --- | --- |
| `netstat -ano` | Show all connections and listening ports numerically with owning PID. |
| `netstat -e -s` | Display Ethernet statistics and statistics for all protocols. |
| `netstat -s -p tcp udp` | Statistics for only TCP and UDP. |
| `netstat -o 5` | Active TCP connections with PIDs every 5 seconds. |
| `netstat -anobq` | All connections, listening and bound nonlistening ports, numeric, with PID and executable. |

# options

| option | description |
| --- | --- |
| `-a` | Displays all active TCP connections and the TCP and UDP ports on which the computer is listening. |
| `-b` | Displays the executable involved in creating each connection or listening port; can be time-consuming and requires sufficient permissions. |
| `-e` | Displays Ethernet statistics; can be combined with -s. |
| `-n` | Displays addresses and port numbers numerically without name resolution. |
| `-o` | Includes the process ID (PID) for each connection; combinable with -a, -n and -p. |
| `-p <Protocol>` | Shows connections for tcp, udp, tcpv6 or udpv6; with -s also icmp, ip, icmpv6, ipv6. |
| `-q` | Displays all connections, listening ports, and bound nonlistening TCP ports. |
| `-r` | Displays the IP routing table (equivalent to route print). |
| `-s` | Displays statistics by protocol. |
| `<interval>` | Redisplays information every interval seconds; CTRL+C to stop. |
| `/?` | Displays help. |
