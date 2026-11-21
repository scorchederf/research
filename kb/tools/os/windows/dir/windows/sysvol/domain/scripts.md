---
created: 2026-11-21
fullpath: 'C:\Windows\SYSVOL\domain\scripts'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - active-directory
aliases:
  - scripts
  - NETLOGON share
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/netlogon-share-not-present-after-install-ad-ds-on-full-read-only-domain-controller
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/missing-sysvol-and-netlogon-shares
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/relocate-sysvol-tree-frs-for-replication
---

**fullpath**:C:\Windows\SYSVOL\domain\scripts

# description

On a domain controller, `\Windows\SYSVOL\domain\scripts` is the folder that the Netlogon service shares out as the NETLOGON share. It is part of the SYSVOL tree, which is replicated between domain controllers by FRS or DFS Replication to distribute a consistent copy of Group Policy settings and scripts.

## simple description

> ### 2026-11-21 Claude said
> This folder on domain controllers is published as the NETLOGON share and typically stores logon scripts and other files that every domain computer and user can read. Its contents replicate to every domain controller in the domain. Any authenticated user can usually read it.
>
> **SOC NOTE**: Attackers search NETLOGON/SYSVOL for scripts containing hard-coded credentials (MITRE ATT&CK T1552.001/T1552.006) and, with write access, plant or modify logon scripts for domain-wide execution and persistence (T1037.003 Network Logon Script, T1484.001). Monitor file changes here (Security 5145 / 4663) and review ACLs.
>

# purpose

Holds logon scripts and related files exposed through the NETLOGON share. The Netlogon service shares this folder when `HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\SysvolReady` is set to 1; if Netlogon reads that flag before NTFRS creates the folder, the NETLOGON share is not created (workaround: toggle SysvolReady 0 then 1).

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
