---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - network
aliases:
  - Interfaces
  - Tcpip\Parameters\Interfaces
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/networking/tcpip-and-nbt-configuration-parameters
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces

# description

Per-adapter TCP/IP configuration key of the Tcpip.sys protocol driver. Each subkey is named by the ID of a network adapter TCP/IP is bound to and holds values specific to that adapter, written by the network connection properties UI and the DHCP Client service. Global TCP/IP settings live in the parent `Tcpip\Parameters` key.

## simple description

> ### 2026-11-21 Claude said
> This key stores IPv4 settings for each network adapter, one subkey per adapter GUID. It contains things like the IP address, subnet mask, default gateway, DNS servers and DHCP-assigned values including lease times and the DHCP server. It is a quick way to see the network configuration a machine has had.
>
> **SOC NOTE**: Forensically, the interface subkeys reveal IP addresses, DHCP servers, domain names and (via DhcpNetworkHint / last write times) networks the host connected to, useful for timeline and location analysis. Attackers may modify NameServer values to redirect DNS (MITRE ATT&CK T1565 / T1557).
>

# purpose

Holds adapter-specific TCP/IP parameters. To map an adapter ID to a connection name, view `HKLM\SYSTEM\CurrentControlSet\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}\<ID for Adapter>\Connection` (Name value). Parameters with DHCP and static values may or may not exist depending on configuration; a restart is required for changes.

# hive

| property | value |
| --- | --- |
| hive | HKLM (HKEY_LOCAL_MACHINE\System) |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\Config\System` (supporting files System, System.alt, System.log, System.sav) |

# values

| value name | type | description |
| --- | --- | --- |
| `DefaultGateway` | REG_MULTI_SZ | List of gateways for packets not destined for a directly connected subnet; overrides DhcpDefaultGateway (per adapter subkey). |
| `EnableDhcp` | REG_DWORD | If 1, the DHCP client tries to configure the first IP interface on the adapter (per adapter subkey). |
| `IPAddress` | REG_MULTI_SZ | List of IP addresses for the adapter (per adapter subkey). |
| `MTU` | REG_DWORD | Overrides the default Maximum Transmission Unit for the interface; range 68 to the network MTU (per adapter subkey). |
| `UseZeroBroadcast` | REG_DWORD | If 1, IP uses zeros-broadcasts (0.0.0.0) instead of ones-broadcasts (per adapter subkey). |

# subkeys

| subkey | description |
| --- | --- |
| `<ID for Adapter>` | One subkey per network adapter that TCP/IP is bound to, holding that adapter's values. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /s` | List all adapter subkeys and their values. |
