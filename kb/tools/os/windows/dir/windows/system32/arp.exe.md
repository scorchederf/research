---
created: 2026-11-21
fullpath: 'C:\Windows\System32\arp.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - arp.exe
  - arp
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/arp
---

**fullpath**:C:\Windows\System32\arp.exe

# description

arp displays and modifies entries in the Address Resolution Protocol (ARP) cache, which maps IP addresses to Ethernet or Token Ring physical addresses, with a separate table per network adapter. It is a built-in Windows command.

## simple description

> ### 2026-11-21 Claude said
> arp shows which MAC address the computer has learned for each nearby IP address. Admins use it to troubleshoot local network problems or add static entries. Entries added with -s disappear when TCP/IP restarts. It only covers the local subnet.
>
> **SOC NOTE**: arp -a is common network discovery (T1016, T1018) by attackers and malware enumerating neighbouring hosts. Unexpected static entries or duplicate MACs for the gateway can indicate ARP spoofing/man-in-the-middle (T1557.002).
>

# purpose

View, add and delete ARP cache entries.

# typical use cases

| usage | description |
| --- | --- |
| `arp -a` | Display the ARP cache tables for all interfaces. |
| `arp -a -N 10.0.0.99` | Display the ARP cache table for the interface with IP 10.0.0.99. |
| `arp -s 10.0.0.80 00-AA-00-4F-2A-9C` | Add a static entry resolving 10.0.0.80 to that MAC. |

# options

| option    | description    |
| --- | --- |
| `-a` | Displays current ARP entries; with `inet_addr`, only that IP's entry. |
| `-g` | Same as `-a`. |
| `-v` | Verbose mode, including invalid and loopback entries. |
| `inet_addr` | IP address to display, delete or add. |
| `-N if_addr` | Shows entries for the interface with that IP; case-sensitive. |
| `-d` | Deletes the entry for `inet_addr`; `*` deletes all. |
| `-s` | Adds a static entry; lasts until the TCP/IP stack restarts. |
| `eth_addr` | MAC address (six hyphen-separated hex bytes) used with `-s`. |
| `if_addr` | IP of the interface whose table is modified with `-s` or `-d`. |
| `/?` | Displays help at the command prompt. |
