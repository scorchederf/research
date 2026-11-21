---
created: 2026-11-21
fullpath: 'C:\Windows\System32\repadmin.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - repadmin.exe
  - repadmin
  - Repadmin
url:
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc770963(v=ws.11)
  - https://learn.microsoft.com/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/diagnose-replication-failures
---

**fullpath**:C:\Windows\System32\repadmin.exe

# description

Repadmin.exe helps administrators diagnose Active Directory replication between domain controllers. It is built into Windows Server when the AD DS or AD LDS role is installed, and ships with the AD DS tools in Remote Server Administration Tools (RSAT). It requires administrative credentials on each targeted DC.

## simple description

A command-line tool for checking and troubleshooting Active Directory replication. It shows replication status, topology and metadata, and can force replication between domain controllers.

# purpose

- View the replication topology from each DC's perspective, and replication metadata and up-to-dateness vectors.
- Force replication events and KCC recalculation.
- Monitor forest replication health (e.g. daily `/showrepl` reports).
- Microsoft warns incorrect use can harm the replication topology; its main use is monitoring.

# typical use cases

- Forest-wide replication status as CSV: `repadmin /showrepl * /csv > showrepl.csv`
- Interactive grid in PowerShell: `repadmin /showrepl * /csv | convertfrom-csv | out-gridview`
- Compare password attribute metadata: `repadmin /showobjmeta <DC> <DN of DC computer account>`
- Make a DC a global catalog: `repadmin.exe /options DC_NAME +IS_GC`

Syntax: `repadmin <cmd> <args> [/u:{domain\user}] [/pw:{password | *}] [/retry[:<retries>][:<delay>]] [/csv]`

# options

| option    | description    |
| --- | --- |
| `/kcc` | Forces the KCC on targeted DCs to immediately recalculate the inbound replication topology. |
| `/prp` | Specifies the Password Replication Policy (PRP) for read-only domain controllers (RODCs). |
| `/queue` | Displays inbound replication requests the DC must issue to become consistent with its source partners. |
| `/replicate` | Triggers immediate replication of a directory partition from a source DC to a destination DC. |
| `/replsingleobj` | Replicates a single object between any two DCs that share directory partitions. |
| `/replsummary` | Identifies DCs failing inbound or outbound replication and summarizes the results. |
| `/rodcpwdrepl` | Triggers replication of passwords for specified users from the source DC to one or more RODCs. |
| `/showattr` | Displays the attributes of an object. |
| `/showobjmeta` | Displays replication metadata for an object (attribute ID, version, USNs, originating server GUID, timestamp). |
| `/showrepl` | Displays replication status from the DC's last inbound replication attempt. |
| `/showutdvec` | Displays the highest committed USN for the DC and its transitive partners. |
| `/syncall` | Synchronizes a DC with all replication partners. |
| `/?, /help` | Displays available commands. |
| `/?:<cmd>, /help:<cmd>` | Shows arguments, syntax and examples for a command. |
| `/experthelp` | Displays commands for advanced users. |
| `/listhelp` | Shows syntax variations for DSA_NAME, DSA_LIST, NCNAME and OBJ_LIST. |
| `/oldhelp` | Help for Windows 2000 / Server 2003 repadmin commands. |
| `/u:<domain\user>` | Domain and user with permission to perform operations in AD DS (UPN not supported). |
| `/pw:<password | *>` | Password for the /u user. |
| `/retry[:<retries>][:<delay>]` | Retries binding to the target DC on RPC errors 1722 or 1753. |
| `/csv` | Displays /showrepl results in CSV format. |
