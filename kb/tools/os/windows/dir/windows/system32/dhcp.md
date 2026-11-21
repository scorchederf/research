---
created: 2026-11-21
fullpath: 'C:\Windows\System32\dhcp'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - dhcp
  - DHCP server database folder
url:
  - https://learn.microsoft.com/powershell/module/dhcpserver/backup-dhcpserver?view=windowsserver2025-ps
  - https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverdatabase?view=windowsserver2025-ps
---

**fullpath**:C:\Windows\System32\dhcp

# description

Folder used by the Windows Server DHCP Server service for its database. Learn's DhcpServer PowerShell examples use C:\Windows\system32\dhcp\backup as a backup location and show the database file name dhcp.mdb, whose path and backup settings can be changed with Set-DhcpServerDatabase.

## simple description

> ### 2026-11-21 Claude said
> On a Windows DHCP server this folder holds the DHCP database (dhcp.mdb) with scopes, leases and reservations, plus its transaction logs and a backup subfolder. The DHCP service writes it continuously and backs it up on a schedule. On a machine without the DHCP Server role it is usually empty or absent.
>
> **SOC NOTE**: Lease records map IP to MAC and hostname over time, useful to attribute activity to a device. DHCP audit logs (DhcpSrvLog-*.log, often in this folder) show lease grants and rogue-device appearances. Members of DnsAdmins/DHCP Administrators or attackers on a DC may tamper with options here (T1557.003 DHCP spoofing).
>

# purpose

Holds the DHCP server service database and backups. `Backup-DhcpServer` backs up the database to a specified location; `Set-DhcpServerDatabase` changes the database file name, backup path, backup interval and cleanup interval.

# common files found

| file | description |
| --- | --- |
| `dhcp.mdb` | DHCP server database file (name used in Set-DhcpServerDatabase example). |
| `backup` | Backup folder used in the Backup-DhcpServer example. |
