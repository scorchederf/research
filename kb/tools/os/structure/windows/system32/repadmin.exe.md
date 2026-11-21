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

> ### 2026-11-21 Claude said
> Repadmin is an Active Directory admin tool for checking and troubleshooting replication, the process that keeps domain controllers in sync. It can show whether replication is healthy, list each domain controller's replication partners and errors, show detailed change history (metadata) for any directory object, and force replication immediately. It's installed on domain controllers and on admin workstations with RSAT. Normal users and endpoints should never need it.
>
> **SOC NOTE**: Repadmin is useful in investigations: `repadmin /showobjmeta` shows when and on which DC an attribute (for example a password, group membership or `adminCount`) was last changed, helping you time account manipulation. Attackers with high privileges may use replication features themselves; DCSync attacks (MITRE ATT&CK T1003.006) abuse the same replication rights, though usually via tools like Mimikatz rather than repadmin. Running repadmin outside known admin systems, or `/rodcpwdrepl` pushing passwords to RODCs, is worth questioning.
>

# purpose

- View the replication topology from each DC's perspective, and replication metadata and up-to-dateness vectors.
- Force replication events and KCC recalculation.
- Monitor forest replication health (e.g. daily `/showrepl` reports).
- Microsoft warns incorrect use can harm the replication topology; its main use is monitoring.

# typical use cases

| usage | description |
| --- | --- |
| `repadmin /showrepl * /csv > showrepl.csv` | Forest-wide replication status as CSV. |
| `repadmin /showrepl * /csv \| convertfrom-csv \| out-gridview` | Interactive grid in PowerShell. |
| `repadmin /showobjmeta <DC> <DN of DC computer account>` | Compare password attribute metadata. |
| `repadmin.exe /options DC_NAME +IS_GC` | Make a DC a global catalog. |
| `repadmin <cmd> <args> [/u:{domain\user}] [/pw:{password \| *}] [/retry[:<retries>][:<delay>]] [/csv]` | Syntax. |

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
