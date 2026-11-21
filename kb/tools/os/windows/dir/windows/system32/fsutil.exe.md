---
created: 2026-11-21
fullpath: 'C:\Windows\System32\fsutil.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - filesystem
aliases:
  - fsutil.exe
  - fsutil
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil
  - https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil-file
  - https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil-behavior
---

**fullpath**:C:\Windows\System32\fsutil.exe

# description

`fsutil` performs tasks related to FAT and NTFS file systems, such as managing reparse points, handling sparse files, or dismounting a volume. It is a built-in Windows command; run without parameters it lists the supported subcommands. You must be an administrator or a member of the Administrators group to use it.

## simple description

> ### 2026-11-21 Claude said
> fsutil.exe is a built-in Windows command-line tool for low-level file system administration. Admins use it to query volume information, manage the USN change journal, create hard links, set file system behaviour flags and work with sparse files and reparse points. It requires administrative rights and talks directly to NTFS/ReFS/FAT features that normal tools do not expose. On a typical workstation it is rarely run by users.
>
> **SOC NOTE**: Attackers use `fsutil usn deletejournal` to destroy the USN journal (T1070 Indicator Removal) and ransomware commonly runs `fsutil behavior set SymlinkEvaluation R2L:1 R2R:1` to follow remote symlinks before encrypting shares; `fsutil file createnew` and `fsutil fsinfo drives` also appear in discovery/staging. Hunt for fsutil.exe process creation (Sysmon 1 / 4688) with `usn deletejournal`, `behavior set`, or `setzerodata` command lines, especially from scripts or non-admin parents.
>

# purpose

Manages FAT and NTFS file system features: short (8.3) names, CLFS logs, dev drives, the volume dirty bit, files, hard links, object IDs, quotas, self-healing repair, reparse points, transactional resource managers, sparse files, storage tiers, transactions, the USN change journal, volumes and WIM-backed files. Only advanced users with a thorough understanding of Windows should use it.

# typical use cases

| usage | description |
| --- | --- |
| `fsutil` | Display the list of supported subcommands. |
| `fsutil file findbysid scottb c:\users` | Find files owned by user scottb on drive C (Disk Quotas must be enabled). |
| `fsutil file queryallocranges offset=1024 length=64 c:\temp\sample.txt` | Query the allocated ranges for a file on an NTFS volume. |
| `fsutil behavior query disablelastaccess` | Query a file system behavior parameter. |

# options

| option | description |
| --- | --- |
| `8dot3name` | Queries or changes short name (8.3) behavior, removes short names in a directory, and scans for registry keys impacted by stripping short names. |
| `behavior` | Queries (`query`) or changes (`set`) file system behavior parameters such as `disable8dot3`, `disablelastaccess`, `disabledeletenotify`, `encryptpagingfile`, `mftzone` and `symlinkevaluation`. Most changes need a restart. |
| `clfs` | Creates or corrects authentication codes for Common Log File System (CLFS) logfiles. |
| `devdrv` | Manages dev drive, a volume tuned for developer scenarios, and the minifilters attached to it. |
| `dirty` | Queries or sets a volume's dirty bit; when set, autochk checks the volume at next restart. |
| `file` | Finds files by owner, queries allocated ranges, sets short name, valid data length or zero data, creates a new file of a given size, and maps file IDs to names. |
| `fsinfo` | Lists drives and queries drive type, volume info, NTFS-specific volume info or file system statistics. |
| `hardlink` | Lists hard links for a file or creates a hard link. |
| `objectid` | Manages object identifiers used to track files and directories. |
| `quota` | Manages per-user disk quotas on NTFS volumes. |
| `repair` | Queries or sets the self-healing state of the volume and initiates on-disk verification. |
| `reparsepoint` | Queries or deletes reparse points (used for junctions, mount points and filter drivers). |
| `resource` | Creates, starts, stops, queries or modifies a Transactional Resource Manager. |
| `sparse` | Manages sparse files. |
| `tiering` | Manages storage tier functions such as setting/disabling flags and listing tiers. |
| `transaction` | Commits, rolls back or displays info about a transaction. |
| `usn` | Manages the update sequence number (USN) change journal, a persistent log of all changes made to files on the volume. |
| `volume` | Dismounts a volume, queries free space, or finds a file using a specified cluster. |
| `wim` | Discovers and manages WIM-backed files. |
