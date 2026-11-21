---
created: 2026-11-21
fullpath: 'C:\Windows\System32\ipconfig.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - network
aliases:
  - "ipconfig.exe"
  - "ipconfig"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig
---

**fullpath**:C:\Windows\System32\ipconfig.exe

# description

Ipconfig displays all current TCP/IP network configuration values and refreshes DHCP and DNS settings. Without parameters it shows IPv4 and IPv6 addresses, subnet mask and default gateway for all adapters. It is a built-in Windows command.

## simple description

> ### 2026-11-21 Claude said
> Ipconfig is the built-in Windows command that shows a computer's IP addresses, gateways and DNS settings. It can also renew or release DHCP leases and show or clear the local DNS cache. Admins use it daily for network troubleshooting.
>
> **SOC NOTE**: Attackers run `ipconfig /all` early for system network configuration discovery (MITRE ATT&CK T1016), often alongside whoami, net and systeminfo. `ipconfig /displaydns` reveals recently resolved hostnames, which helps responders identify C2 domains; `/flushdns` may be used to remove that evidence.
>

# purpose

Display TCP/IP configuration for all adapters, renew or release DHCP/DHCPv6 leases, view or flush the DNS client resolver cache, re-register DNS names, and display or set the DHCP class ID.

# typical use cases

| usage | description |
| --- | --- |
| `ipconfig` | Displays the basic TCP/IP configuration for all adapters. |
| `ipconfig /all` | Displays the full TCP/IP configuration for all adapters. |
| `ipconfig /renew Local Area Connection` | Renews the DHCP configuration for only the Local Area Connection adapter. |
| `ipconfig /flushdns` | Flushes the DNS resolver cache when troubleshooting name resolution. |
| `ipconfig /showclassid Local*` | Displays the DHCP class ID for all adapters whose names start with Local. |
| `ipconfig /setclassid Local Area Connection TEST` | Sets the DHCP class ID for the Local Area Connection adapter to TEST. |

# options

| option | description |
| --- | --- |
| `/all` | Displays the full TCP/IP configuration for all adapters, physical and logical. |
| `/displaydns` | Displays the DNS client resolver cache, including Hosts file entries and recently resolved records. |
| `/flushdns` | Flushes and resets the DNS client resolver cache. |
| `/registerdns` | Initiates manual dynamic registration of DNS names and IP addresses. |
| `/release [<adapter>]` | Sends DHCPRELEASE to release the DHCP configuration for all or a specific adapter. |
| `/release6 [<adapter>]` | Sends DHCPRELEASE to the DHCPv6 server for all or a specific adapter. |
| `/renew [<adapter>]` | Renews DHCP configuration for all or a specific adapter. |
| `/renew6 [<adapter>]` | Renews DHCPv6 configuration for all or a specific adapter. |
| `/setclassid <adapter> [<classID>]` | Configures the DHCP class ID for an adapter; `*` for all; omitting classID removes it. |
| `/showclassid <adapter>` | Displays the DHCP class ID for an adapter; `*` for all. |
| `/allcompartments` | _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_ |
| `/?` | Displays Help at the command prompt. |
