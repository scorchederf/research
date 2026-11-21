---
created: 2026-11-21
fullpath: 'c:\windows\system32\pktmon.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - network
aliases:
  - pktmon.exe
  - Packet Monitor
url:
  - https://learn.microsoft.com/windows-server/networking/technologies/pktmon/pktmon-syntax
---

**fullpath**:c:\windows\system32\pktmon.exe

# description

Packet Monitor (`pktmon.exe`) is an in-box, cross-component network diagnostics tool for packet capture, drop detection, filtering and counting, available on Windows 10 and Windows Server 2019 (1809) and later. Logs are ETL and can be converted to text or pcapng for Wireshark, or opened in Network Monitor.

## simple description

> ### 2026-11-21 Claude said
> pktmon is a packet sniffer built into Windows. It can capture network traffic at many points inside the Windows network stack and show where packets get dropped. It saves captures as ETL files that can be converted to pcapng for Wireshark. It needs administrator rights.
>
> **SOC NOTE**: Because it is built in, attackers can use pktmon to sniff credentials or traffic without installing tools (T1040 Network Sniffing). Look for `pktmon start -c` or `pktmon filter add` in command lines and unexpected `PktMon*.etl` files. For defenders it is a quick way to capture traffic on a host during triage.
>

# purpose

Captures packets and general ETW/WPP events through the networking stack, with up to 32 filters (MAC, IP, port, EtherType, transport protocol, VLAN, TCP flags, encapsulation). Logging modes: circular (default), multi-file, real-time and memory.

# typical use cases

| usage | description |
| --- | --- |
| `pktmon filter add -i 10.0.0.10 -t icmp` | Capture ICMP traffic to or from 10.0.0.10. |
| `pktmon filter add -p 53` | Capture traffic on port 53. |
| `pktmon filter add -i 10.0.0.10 -t tcp syn` | Capture SYN packets sent or received by 10.0.0.10. |
| `pktmon start -c` | Start capture with packet logging. |
| `pktmon start -c --comp nics` | Capture packets on network adapters only. |
| `pktmon start -c --comp 4,5 --type drop` | Capture only dropped packets passing components 4 and 5. |
| `pktmon start --capture --trace -p Microsoft-Windows-TCPIP` | Capture packets and log events from the TCPIP provider. |
| `pktmon counters` | Query packet counters during a capture. |
| `pktmon counters --json` | Get counters in JSON, including last drop reason. |
| `pktmon stop` | Stop all data collection. |
| `pktmon etl2txt <etl file>` | Convert the ETL log to text. |
| `pktmon list` | Show the networking stack layout and component IDs. |

# options

| option | description |
| --- | --- |
| `filter add` | Adds a capture filter; a packet must match all conditions of at least one filter. |
| `start` | Starts monitoring. |
| `-c` / `--capture` | Enables packet capture and logging plus packet counters. |
| `-o` | With `start`, enables packet counters only without logging packets. |
| `--comp` | Components to monitor: `nics` or a list of component IDs (default all). |
| `--type` | Filters by packet propagation status (dropped or flowing). |
| `-t` / `--trace` | Captures general events (ETW/WPP). |
| `-p` | With `--trace`, the event providers; for packet logging, bytes of each packet to log (0 = whole packet, default 128). |
| `-s` | Maximum log file size, or buffer size for memory logging mode. |
| `-e` | Applies a filter to encapsulated inner packets (VXLAN, GRE, NVGRE, IP-in-IP). |
| `counters` | Shows packet counters per component, Tx/Rx and drops. |
| `reset` | Resets counters to zero. |
| `stop` | Stops monitoring. |
| `etl2txt` | Converts an ETL log to text. |
| `list` | Lists networking components arranged by adapter bindings. |
