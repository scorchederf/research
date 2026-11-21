---
created: 2026-11-21
fullpath: 'C:\Windows\System32\route.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - networking
aliases:
  - "route.exe"
  - "route"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/route_ws2008
---

**fullpath**: C:\Windows\System32\route.exe

# description

`route` displays and modifies entries in the local IP routing table. It is a built-in Windows command, available when the TCP/IP protocol is installed on a network adapter. Related tools include `netsh interface ipv4 add route` and the PowerShell NetTCPIP cmdlets.

## simple description

> ### 2026-11-21 Claude said
> route.exe is a built-in command-line tool for viewing and changing how the computer decides where to send network traffic. `route print` shows the routing table, and `route add` / `route delete` change it. Administrators use it for troubleshooting or adding static routes. Persistent routes are saved in the registry so they survive reboots.
>
> **SOC NOTE**: Mostly used for discovery (T1016 System Network Configuration Discovery) via `route print`. Malicious use includes adding routes to redirect or black-hole traffic, e.g. sending security product or update traffic to a null gateway (T1562 Impair Defenses), or enabling pivoting. Check HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\PersistentRoutes for unexpected entries.
>

# purpose

Shows and changes the IP routing table. Used without parameters it displays help. Persistent routes added with `/p` are stored in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\PersistentRoutes`.

# typical use cases

| usage | description |
| --- | --- |
| `route print` | Display the entire IP routing table. |
| `route print 10.*` | Display routes that begin with 10. |
| `route add 0.0.0.0 mask 0.0.0.0 192.168.12.1` | Add a default route via gateway 192.168.12.1. |
| `route add 10.41.0.0 mask 255.255.0.0 10.27.0.1` | Add a route to 10.41.0.0/16 via next hop 10.27.0.1. |
| `route /p add 10.41.0.0 mask 255.255.0.0 10.27.0.1` | Add the same route persistently. |
| `route add 10.41.0.0 mask 255.255.0.0 10.27.0.1 metric 7` | Add a route with cost metric 7. |
| `route add 10.41.0.0 mask 255.255.0.0 10.27.0.1 if 0x3` | Add a route using interface index 0x3. |
| `route delete 10.41.0.0 mask 255.255.0.0` | Delete the route to 10.41.0.0/16. |
| `route delete 10.*` | Delete all routes beginning with 10. |
| `route change 10.41.0.0 mask 255.255.0.0 10.27.0.25` | Change the next hop of an existing route. |

# options

| option    | description    |
| --- | --- |
| `/f` | Clears the routing table of all entries that are not host routes, the loopback route or multicast routes; if combined with a command, the table is cleared first. |
| `/p` | With `add`, adds a persistent route stored in the registry; with `print`, lists persistent routes. Ignored for other commands. |
| `<command>` | Command to run: `add`, `change`, `delete` or `print`. |
| `<destination>` | Network destination of the route: network address, host address, or 0.0.0.0 for the default route. |
| `mask <netmask>` | Specifies the subnet mask for the destination; defaults to 255.255.255.255. |
| `<gateway>` | Next hop IP address over which the destination is reachable. |
| `metric <metric>` | Integer cost (1-9999); the lowest metric is chosen among matching routes. |
| `if <interface>` | Interface index (decimal or hex with 0x) for the route; if omitted, determined from the gateway. |
| `/?` | Displays help at the command prompt. |
