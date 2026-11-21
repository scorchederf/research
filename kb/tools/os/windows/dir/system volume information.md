---
created: 2026-11-21
fullpath: 'C:\System Volume Information'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - system-restore
  - vss
aliases:
  - System Volume Information
url:
  - https://learn.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatesystemvolumeinformationfolder
  - https://learn.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtlcreatesystemvolumeinformationfolder
  - https://learn.microsoft.com/windows/win32/sr/legacy-system-restore-reference
  - https://learn.microsoft.com/troubleshoot/sql/database-engine/install/windows/permission-error-use-volume-mount-point
---

**fullpath**:C:\System Volume Information

# description

System Volume Information is a hidden system folder in the root directory of a volume, created by the file system support routines FltCreateSystemVolumeInformationFolder / RtlCreateSystemVolumeInformationFolder with an ACL granting full access only to the local SYSTEM account. It holds volume-level data such as the System Restore repository.

## simple description

> ### 2026-11-21 Claude said
> System Volume Information is a hidden folder at the root of every drive that only the SYSTEM account can open. Windows stores restore points, Volume Shadow Copy data, search index and other per-volume databases there. Users and even administrators get Access Denied by default. It should not be deleted or have its permissions changed.
>
> **SOC NOTE**: Forensically rich: volume shadow copies preserve older versions of files, registry hives and event logs, and Syscache.hve tracks executed binaries on some versions. Ransomware deletes shadow copies with vssadmin/wmic (MITRE ATT&CK T1490), and attackers copy NTDS.dit/SAM from shadow copies (T1003.003). Files hidden here by attackers are easy to miss.
>

# purpose

Created in the root directory of a volume with FILE_ATTRIBUTE_HIDDEN and FILE_ATTRIBUTE_SYSTEM and an inheritable ACE giving full control to SYSTEM. On Windows XP SP2 it contained the System Restore repository, with one `_restore{GUID}` folder holding restore point folders RP1..RPn.

# common files found

| file | description |
| --- | --- |
| `_restore{GUID}\RPn` | Legacy (Windows XP SP2) System Restore restore point folders. |
| `_restore{GUID}\_driver.cfg` | Legacy System Restore SR_PERSISTENT_CONFIG data. |
| `ResumeKeyFilter.Store` | Created on Windows Server; only SYSTEM has permission on it. |
