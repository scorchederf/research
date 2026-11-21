---
created: 2026-11-21
fullpath: 'C:\Windows\NTDS'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - active-directory
  - domain-controller
aliases:
  - "NTDS"
  - "%SystemRoot%\\NTDS"
  - "Ntds folder"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/use-ntdsutil-manage-ad-files
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/0xc00002e1-error-start-domain-controller
  - https://learn.microsoft.com/windows/win32/vss/in-box-vss-writers
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/use-online-dbdump-feature-ldp-dot-exe
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/jet-database-errors-recovery-steps
---

**fullpath**:C:\Windows\NTDS

# description

`C:\Windows\NTDS` is the default folder on a domain controller holding the Active Directory Domain Services database (`ntds.dit`) and its transaction logs. It is managed with `ntdsutil` (files info, move DB, move logs, recover, compact) and backed up through the NTDS VSS writer.

## simple description

> ### 2026-11-21 Claude said
> This folder exists on domain controllers and contains the Active Directory database, ntds.dit, plus its log files.
> ntds.dit holds every user, group, computer and their password hashes for the whole domain.
> It is locked while AD is running, so it is normally only touched by AD itself, backups, and ntdsutil.
>
> **SOC NOTE**: Crown-jewel target: theft of ntds.dit + SYSTEM hive gives all domain hashes (T1003.003 NTDS). Watch for `ntdsutil "ac i ntds" ifm`, vssadmin/diskshadow shadow copies, esentutl copies, or reads of ntds.dit from shadow volumes, and for ntds.dit files appearing in unusual folders.
>

# purpose

Default location for the AD database and logs. `ntdsutil files info` shows paths such as Database `C:\WINDOWS\NTDS\ntds.dit`, Backup dir `C:\WINDOWS\NTDS\dsadata.bak`, Working dir and Log dir `C:\WINDOWS\NTDS`. Locations are also stored under `HKLM\System\CurrentControlSet\Services\NTDS\Parameters`. Directory Services can fail to start if NTFS permissions on the NTDS folder are too restrictive or the folder is compressed.

# common files found

| file | description |
| --- | --- |
| `ntds.dit` | The Active Directory database; one per domain controller, reported by the NTDS VSS writer. |
| `edb.log`, `edb00001.log` | Database transaction log files. |
| `res1.log`, `res2.log` | Reserved transaction log files. |
| `temp.edb` | Temporary database file. |
| `Edb.chk` | Checkpoint file. |
| `dsadata.bak` | Default backup directory. |
| `Ntds.dmp` | Output of the online dbdump feature (created next to the .dit). |
