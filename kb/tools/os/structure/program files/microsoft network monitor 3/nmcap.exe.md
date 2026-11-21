---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Network Monitor 3\nmcap.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - network
  - capture
aliases:
  - nmcap.exe
  - NMCap
  - Network Monitor 3 command-line capture
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/network-monitor-3
  - https://learn.microsoft.com/troubleshoot/windows-client/networking/collect-data-using-network-monitor
---

**fullpath**:C:\Program Files\Microsoft Network Monitor 3\nmcap.exe

# description

Nmcap.exe is the command-line capture tool of Microsoft Network Monitor 3 (3.4 installs to `%Program Files%\Microsoft Network Monitor 3`). It captures with lower resource use than the GUI, can start/stop captures on conditions and create chained captures. Network Monitor is archived and no longer developed.

## simple description

> ### 2026-11-21 Claude said
> NMCap is the command-line packet capture tool that comes with Microsoft Network Monitor 3.4. Admins use it to record network traffic to .cap files without opening the GUI, often on servers. It can split captures into multiple smaller files. The product is old and no longer developed.
>
> **SOC NOTE**: Its presence means a packet sniffer and NDIS capture driver are installed; attackers can use it for network sniffing (T1040) to harvest cleartext credentials. Look for unexpected .cap files, nmcap.exe process creation and the Network Monitor driver bound to adapters.
>

# purpose

Capture network traffic from the command line with minimal system impact, with configurable start/stop conditions and chained capture files. Cannot save process information.

# typical use cases

| usage | description |
| --- | --- |
| — | Low-overhead capture on production systems instead of the Network Monitor GUI. |
| — | Chained captures that keep individual capture files small. |

# options

| option    | description    |
| --- | --- |
| _Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_ |  |
