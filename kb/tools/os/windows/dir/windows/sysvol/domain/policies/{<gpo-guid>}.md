---
created: 2026-11-21
fullpath: 'C:\Windows\SYSVOL\domain\Policies\{<GPO-GUID>}'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - active-directory
  - group-policy
  - sysvol
aliases:
  - "{<GPO-GUID>}"
  - "Group Policy Template"
  - "GPT"
url:
  - https://learn.microsoft.com/windows/win32/vss/backing-up-and-restoring-an-frs-replicated-sysvol-folder
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/manage-group-policy-adm-file
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/reset-user-rights-in-default-domain-group-policy
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/rebuild-sysvol-tree-and-content-in-a-domain
---

**fullpath**:C:\Windows\SYSVOL\domain\Policies\{<GPO-GUID>}

# description

Per-GPO folder in the SYSVOL share on a domain controller, named after the Group Policy object's GUID; it holds the Group Policy Template (GPT). SYSVOL is replicated between domain controllers by DFSR or FRS, while the matching Group Policy container is replicated through Active Directory. Managed with the Group Policy Management Console and Group Policy Object Editor.

## simple description

> ### 2026-11-21 Claude said
> Every Group Policy object in an Active Directory domain has a folder here named after its GUID (for example the Default Domain Policy is {31B2F340-016D-11D2-945F-00C04FB984F9}). It holds the files that make up the policy: registry.pol settings, security templates, scripts and preferences. Domain-joined computers read these files over the \\domain\SYSVOL share when they apply Group Policy.
>
> **SOC NOTE**: High-value target: an attacker with write access to a GPO folder can push scheduled tasks, scripts or registry changes domain-wide (T1484.001). Legacy Groups.xml/ScheduledTasks.xml preferences may contain cpassword values (T1552.006). Monitor 5136/5145 events and file changes under Policies, and compare GPT.INI version numbers against expected changes.
>

# purpose

Each domain GPO maintains a single folder in SYSVOL named the Group Policy Template (GPT). Only the GPT is replicated by SYSVOL replication; the Group Policy container is replicated through Active Directory, and both must be available for Group Policy to work. There should be a one-to-one mapping between valid GPOs in Active Directory and GUID-named folders in SYSVOL\domain\policies; a folder whose GUID is not in Active Directory is an orphaned GPO.

# common files found

| file | description |
| --- | --- |
| `Gpt.ini` | Controls the GPO template version numbers; edited to increase the version after manual template changes. |
| `Machine\Microsoft\Windows NT\SecEdit\Gpttmpl.inf` | Security template holding settings such as user rights assignments (e.g. in the Default Domain Policy). |
| `Adm\*.adm` | Administrative template (ADM) files stored in the GPT when the GPO was created or edited with ADM-based editors. |
