---
created: 2026-11-21
fullpath: 'C:\Windows\NTDS\ntds.dit'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - ntds.dit
  - NTDS.DIT
  - Active Directory database
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/use-ntdsutil-manage-ad-files
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/jet-database-errors-recovery-steps
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/0xc00002e1-error-start-domain-controller
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/ad-database-offline-defragmentation
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/complete-semantic-database-analysis-ad-db
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/troubleshoot-directory-service-initialization-failure
---

**fullpath**:C:\Windows\NTDS\ntds.dit

# description

Ntds.dit is the local Active Directory database file on a domain controller, an ESENT (Jet) database stored by default in C:\WINDOWS\NTDS together with its transaction logs (edb.log, edbNNNNN.log, res1.log, res2.log, temp.edb). It is managed with Ntdsutil.exe (files, compact, semantic database analysis) and can be recovered with Esentutl.exe; its locations are recorded under `HKLM\System\CurrentControlSet\Services\NTDS\Parameters`.

## simple description

> ### 2026-11-21 Claude said
> Ntds.dit is the database that holds everything in Active Directory: users, groups, computers, GPO links and, most importantly, the password hashes of every domain account. It only exists on domain controllers and is locked by LSASS while Active Directory is running. Admins rarely touch it directly; they use ntdsutil for maintenance, backup and Install From Media. Losing or corrupting it stops the domain controller from starting.
>
> **SOC NOTE**: Stealing ntds.dit (plus the SYSTEM hive for the boot key) gives an attacker every domain hash - MITRE ATT&CK T1003.003 (OS Credential Dumping: NTDS). Watch for `ntdsutil "ac i ntds" "ifm" "create full"`, `vssadmin create shadow` / `diskshadow` / `esentutl /y /vss` copying ntds.dit, wbadmin backups, and DCSync alternatives. Look for ntds.dit copies outside C:\Windows\NTDS, Event 8222/7036 for VSS, Event 325/326 (ESENT) and 4688 process creation for these tools.
>

# purpose

Stores the Active Directory data for a domain controller. Directory Services opens the file in exclusive mode, so file maintenance (recovery, offline defragmentation with `compact to`, semantic analysis, moving the database or logs) must be done with AD DS stopped or in Directory Services Restore Mode. If the file is missing, corrupt, compressed, on an unavailable or full disk, or has too-restrictive NTFS permissions, LSASS cannot start the directory service and the DC restarts with stop code 0xC00002E1 / 0xC00002E2. Database, log and working directory paths are listed by `ntdsutil files info` and stored in the registry under `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\NTDS\Parameters` (DSA Working Directory, Database Log files path, Database Backup path). Paths are limited to MAX_PATH (260 characters), and database or log files from one DC must never be copied to another DC.
