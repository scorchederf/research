---
created: 2026-11-21
fullpath: 'C:\Windows\System32\config'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - registry
  - forensics
aliases:
  - config
  - Registry hive folder
url:
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/remotely-edit-the-registry
  - https://learn.microsoft.com/windows/win32/vss/registry-backup-and-restore-operations-under-vss
---

**fullpath**:C:\Windows\System32\config

# description

The `%SystemRoot%\System32\Config` folder holds the supporting files for most registry hives (all except the per-user `HKEY_CURRENT_USER` hive, which lives in `Ntuser.dat`). These files are loaded into memory at startup and updated as the system runs; the active mapping is listed under `HKLM\System\CurrentControlSet\Control\hivelist`.

## simple description

> ### 2026-11-21 Claude said
> This folder contains the files that make up the Windows registry for the whole machine: SAM (local accounts and password hashes), SECURITY, SOFTWARE, SYSTEM and DEFAULT. Windows keeps them locked while running, so they cannot simply be copied. Backup tools use Volume Shadow Copy to read them. If these files are damaged, Windows may not boot.
>
> **SOC NOTE**: Prime credential-theft target (MITRE T1003.002 Security Account Manager, T1003.004 LSA Secrets): attackers dump SAM/SYSTEM/SECURITY via `reg save`, shadow copies (`vssadmin`, `esentutl`, `ntdsutil`) or HiveNightmare (CVE-2021-36934 weak ACLs). Watch for access to these files by unusual processes and for `.sav`/copies in temp folders. For forensics, the hives plus `.LOG1/.LOG2` transaction logs and `RegBack` give system configuration, services, USB history, and accounts.
>

# purpose

Stores the hive files and their transaction logs and backups. File name extensions indicate the type: no extension is a complete copy of the hive data, `.alt` is a backup copy of the critical System hive, `.log` is a transaction log of changes, and `.sav` is a backup copy made at the end of the text-mode stage of Setup. Hives can be loaded offline into Registry Editor (**File > Load Hive**) for repair, for example when troubleshooting a corrupted hive.

# common files found

| file | description |
| --- | --- |
| `SAM`, `Sam.log`, `Sam.sav` | Supporting files for `HKEY_LOCAL_MACHINE\SAM`. |
| `SECURITY`, `Security.log`, `Security.sav` | Supporting files for `HKEY_LOCAL_MACHINE\Security`. |
| `SOFTWARE`, `Software.log`, `Software.sav` | Supporting files for `HKEY_LOCAL_MACHINE\Software`. |
| `SYSTEM`, `System.alt`, `System.log`, `System.sav` | Supporting files for `HKEY_LOCAL_MACHINE\System` and `HKEY_CURRENT_CONFIG`. |
| `DEFAULT`, `Default.log`, `Default.sav` | Supporting files for `HKEY_USERS\.DEFAULT`. |
