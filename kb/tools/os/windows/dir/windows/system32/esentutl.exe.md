---
created: 2026-11-21
fullpath: 'C:\Windows\System32\esentutl.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - ese
  - database
aliases:
  - esentutl.exe
  - esentutl
  - Esentutl.exe
url:
  - https://learn.microsoft.com/windows/win32/extensible-storage-engine/extensible-storage-engine-files
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/use-ntdsutil-manage-ad-files
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/jet-database-errors-recovery-steps
---

**fullpath**:C:\Windows\System32\esentutl.exe

# description

`esentutl.exe` is the Extensible Storage Engine (ESE/ESENT) database utility built into Windows. It inspects database headers and logs, performs soft recovery, and checks integrity/defragments ESE databases such as the Active Directory `ntds.dit`; NTDSUTIL provides equivalent commands for AD.

## simple description

> ### 2026-11-21 Claude said
> esentutl is a maintenance tool for ESE databases, the database format used by Active Directory, Windows Search, WebCache and many other Windows components. It can show whether a database was shut down cleanly, replay transaction logs, check integrity and defragment. Admins mostly use it when repairing AD or other ESE databases.
>
> **SOC NOTE**: LOLBin: `esentutl /y /vss` copies locked files via Volume Shadow Copy, used to steal ntds.dit, SAM/SYSTEM hives or browser WebCache (T1003.003, T1003.002, T1105); `/y` can also copy to/from ADS and UNC paths. Alert on esentutl with /vss or targeting ntds.dit, SAM, or remote paths.
>

# purpose

Diagnoses, recovers and maintains ESE databases and transaction logs.

# typical use cases

| usage | description |
| --- | --- |
| `esentutl.exe -mh sample.edb` | Reads the database header and prints its state (Clean Shutdown or Dirty Shutdown). |
| `esentutl.exe -ml edb.log` | Identifies the generation of the current transaction log when the engine is not active. |
| `esentutl /r path\ntds.dit` | Performs soft recovery (replays transaction logs) on the AD database. |
| `esentutl /k` | Physical consistency check (checksum) of a database. |

# options

| option | description |
| --- | --- |
| `-mh` | Dumps the database header, including shutdown state. |
| `-ml` | Dumps information about a transaction log file. |
| `-r` / `/r` | Soft recovery: replays transaction log files to bring a dirty database to a clean state. |
| `/k` | Physical consistency check (no NTDSUTIL equivalent). |
| `/g` | ESE logical consistency (integrity) check; equivalent to NTDSUTIL FILES INTEGRITY. |
| `/d` | Offline defragmentation. |
| `/?` | Displays help. |
