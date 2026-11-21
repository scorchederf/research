---
created: 2026-11-21
fullpath: 'C:\$MFT'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - ntfs
  - forensics
aliases:
  - $MFT
  - $Mft
  - Master File Table
  - MFT
url:
  - https://learn.microsoft.com/windows/win32/fileio/master-file-table
  - https://learn.microsoft.com/windows/win32/devnotes/master-file-table
  - https://learn.microsoft.com/troubleshoot/windows-server/backup-and-storage/ntfs-reserves-space-for-mft
  - https://learn.microsoft.com/openspecs/windows_protocols/ms-fscc/b04c3bd0-79dc-4e58-b8ed-74f19fc2ea0a
  - https://learn.microsoft.com/sysinternals/downloads/ntfsinfo
---

**fullpath**:C:\$MFT

# description

`$MFT` is the NTFS Master File Table, a reserved metadata file in the volume root that indexes every file. There is at least one MFT entry for every file on the volume, including the MFT itself (record 0). All information about a file (size, time stamps, permissions, data content) is stored in MFT entries or in space they describe; `$MftMirr` holds a backup of the first four records.

## simple description

> ### 2026-11-21 Claude said
> The `$MFT` is the master index of an NTFS drive: one record (usually 1 KB) per file or folder, holding its name, timestamps, size, permissions and where its data lives. Very small files are stored directly inside the record. It is hidden and locked while Windows runs, so you need special tools to copy it.
>
> **SOC NOTE**: Core forensic artifact: parsing it (MFTECmd, analyzeMFT) gives a full file timeline including deleted files whose records are not yet reused, and comparing `$STANDARD_INFORMATION` with `$FILE_NAME` timestamps detects timestomping (T1070.006). Raw access to `\\.\C:` or tools copying `$MFT` (also used to steal `NTDS.dit`/SAM, T1003) is suspicious on non-forensic hosts.
>

# purpose

Stores the information required to retrieve files from an NTFS volume. NTFS reserves space around it (the MFT zone, 12.5% by default, adjustable with `NtfsMftZoneReservation`) to keep it contiguous. When files are deleted their entries are marked free for reuse, but the MFT does not shrink.
