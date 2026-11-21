---
created: 2026-11-21
fullpath: 'C:\Windows\SYSVOL\domain'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - SYSVOL\domain
  - SYSVOL
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/missing-sysvol-and-netlogon-shares
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/rebuild-sysvol-tree-and-content-in-a-domain
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/relocate-sysvol-tree-frs-for-replication
  - https://learn.microsoft.com/windows/win32/vss/backing-up-and-restoring-an-frs-replicated-sysvol-folder
---

**fullpath**:C:\Windows\SYSVOL\domain

# description

`SYSVOL\domain` is the replica set root of the SYSVOL tree on an Active Directory domain controller. It contains the Group Policy templates (`Policies`) and logon scripts (`scripts`) that are replicated between domain controllers by FRS or DFS Replication and exposed through the `SYSVOL` and `NETLOGON` shares.

## simple description

> ### 2026-11-21 Claude said
> On a domain controller, this folder holds the real files behind the SYSVOL share: Group Policy Objects and logon scripts for the whole domain. Every domain-joined computer reads from here when it applies Group Policy. The folder `SYSVOL\sysvol\<domain name>` is a reparse point (junction) that points back to this folder. Changes made here replicate to all other domain controllers.
>
> **SOC NOTE**: SYSVOL is readable by all authenticated users, so attackers search it for credentials (e.g. Group Policy Preferences `cpassword` in `Groups.xml`, MITRE ATT&CK T1552.006) and scripts with hard-coded secrets. With write access, attackers modify GPOs or scripts to execute code domain-wide (T1484.001 Group Policy Modification). Monitor file changes under `Policies\{GUID}` and `scripts` (Event 5145/4663 with auditing) and new GPO GUID folders.
>

# purpose

Default replica set root for the SYSVOL folder. Replication distributes a consistent copy of Group Policy settings and scripts among domain controllers; member computers and domain controllers access its contents through the Sysvol and Netlogon shares. Only the Group Policy template is replicated via SYSVOL; the Group Policy container is replicated through Active Directory. Each `{GUID}` folder under `Policies` should map one-to-one to a GPO in Active Directory.

# common files found

| item | description |
| --- | --- |
| `DO_NOT_REMOVE_NtFrs_PreInstall_Directory` | FRS pre-install working folder. |
| `Policies` | Group Policy templates; one `{GUID}` folder per GPO. |
| `Policies\{GUID}\Adm`, `MACHINE`, `USER` | Subfolders of each GPO folder. |
| `Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}` | Default Domain Policy. |
| `Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}` | Default Domain Controllers Policy. |
| `scripts` | Logon scripts; shared as NETLOGON. |
