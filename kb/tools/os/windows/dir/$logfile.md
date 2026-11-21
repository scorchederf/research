---
created: 2026-11-21
fullpath: 'C:\$LogFile'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - ntfs
  - forensics
aliases:
  - $LogFile
  - NTFS log file
url:
  - https://learn.microsoft.com/openspecs/windows_protocols/ms-fscc/b04c3bd0-79dc-4e58-b8ed-74f19fc2ea0a
  - https://learn.microsoft.com/windows-server/storage/file-server/ntfs-overview
---

**fullpath**:C:\$LogFile

# description

$LogFile is an NTFS reserved file name in the volume root that holds the transactional logging file. NTFS keeps this transaction-based log with checkpoint information so that after a system failure it can replay the log and restore file system consistency at the next startup; it sits alongside other metadata files such as $Mft, $MftMirr, $Volume and the $Extend directory.

## simple description

> ### 2026-11-21 Claude said
> $LogFile is a hidden NTFS system file that journals changes to file system metadata, so the volume can be repaired after a crash. It isn't visible in Explorer and can't be opened normally while Windows runs. It is typically a few tens of megabytes and wraps around as new changes are recorded.
>
> **SOC NOTE**: $LogFile is a forensic source for recent file creations, renames and deletions (including timestamp changes useful for detecting timestomping, MITRE ATT&CK T1070.006). Collect it with raw-disk tools (KAPE, FTK Imager) together with $MFT and $UsnJrnl:$J, and parse with LogFileParser or similar. Its short retention means it should be collected early.
>

# purpose

NTFS transaction log used to recover file system consistency after a failure.
