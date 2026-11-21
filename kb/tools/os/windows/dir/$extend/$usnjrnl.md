---
created: 2026-11-21
fullpath: 'C:\$Extend\$UsnJrnl'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - ntfs
  - forensics
aliases:
  - $UsnJrnl
  - USN change journal
  - update sequence number (USN) change journal
url:
  - https://learn.microsoft.com/windows/win32/fileio/change-journals
  - https://learn.microsoft.com/windows/win32/fileio/change-journal-records
  - https://learn.microsoft.com/windows/win32/fileio/creating-modifying-and-deleting-a-change-journal
  - https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil-usn
---

**fullpath**:C:\$Extend\$UsnJrnl

# description

The update sequence number (USN) change journal is maintained per volume by the NTFS (and ReFS) file system; each change to a file or directory appends a record with the change reason and file name. It is accessed through `FSCTL_*_USN_JOURNAL` control codes or `fsutil usn`. Learn documents the journal but does not describe the `$Extend\$UsnJrnl` metadata file path itself.

## simple description

> ### 2026-11-21 Claude said
> $UsnJrnl is a hidden NTFS system metadata file that stores the volume's USN change journal. Every time a file is created, renamed, written, or deleted, NTFS adds a small record saying which file changed and why. Backup, indexing and replication services use it to find changed files quickly. The data lives in the $J alternate data stream and old records are trimmed as the journal reaches its maximum size.
>
> **SOC NOTE**: A key DFIR artifact: it shows file creation, rename and deletion (with timestamps and file names) even after files are wiped, helping reconstruct tool drops, ransomware encryption/renames, and exfil staging. Attackers may delete it with `fsutil usn deletejournal` (MITRE T1070 Indicator Removal) - look for that command line. Collect `$Extend\$UsnJrnl:$J` with raw-disk tools alongside $MFT and $LogFile.
>

# purpose

Lets applications determine changes to a volume without scanning it, and allows recovery of file system indexing after a failure. Records note the type of change (reason flags such as `USN_REASON_DATA_OVERWRITE`, `USN_REASON_CLOSE`) but not enough to reverse it. NTFS trims old records when the journal exceeds MaximumSize plus AllocationDelta at checkpoints. Administrators can create, modify and delete the journal (Administrators group required).


