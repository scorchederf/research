---
created: 2026-11-21
fullpath: 'C:\Windows\System32\robocopy.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - robocopy.exe
  - Robocopy
  - Robust File Copy
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy
---

**fullpath**:C:\Windows\System32\robocopy.exe

# description

Robocopy is a built-in Windows command-line tool that copies file data from one location to another, with options for mirroring, multi-threading, restartable and backup-mode copies, ACL/owner/audit copying, throttling, logging and job files. Its exit codes 0-7 indicate success variants and 8 or higher indicate at least one failure.

## simple description

> ### 2026-11-21 Claude said
> Robocopy ("Robust File Copy") is the Windows power tool for copying or mirroring folders, often used for backups and file-server migrations. It can resume interrupted copies, copy permissions and timestamps, use many threads, and log everything. `/mir` makes the destination an exact mirror, deleting extra files. It ships with every modern Windows version.
>
> **SOC NOTE**: Attackers use robocopy to stage and exfiltrate data to shares (MITRE ATT&CK T1039, T1074, T1048) and `/b` backup mode to read files despite ACLs (e.g. NTDS.dit, hives) when holding SeBackupPrivilege. `/mir` or `/purge` against an empty source can be used destructively (T1485). Watch for robocopy with `/b`, `/zb`, `/mt` to external UNC paths, or copying from sensitive locations; logs (`/log`) left on disk are useful evidence.
>

# purpose

Copies file data between locations with copy, file selection, retry, logging and job options. When copying from the root of a device, the destination directory adopts hidden and system attributes; `/purge` and `/mir` skip System Volume Information in top-level directories.

# typical use cases

| usage | description |
| --- | --- |
| `robocopy c:\reports "\\marketing\videos" yearly-report.mov /mt /z` | Copy a file to a share, multi-threaded and restartable. |
| `robocopy C:\Users\Admin\Records D:\Backup /E /ZB /LOG:C:\Logs\Backup.log` | Copy all files and subdirectories including empty ones. |
| `robocopy C:\Users\Admin\Records D:\Backup /MIR /R:2 /W:5 /LOG:C:\Logs\Backup.log` | Mirror a folder with 2 retries, 5 seconds apart. |
| `robocopy C:\Users\Admin\Records D:\Backup /S /E /COPY:DAT /MT:16 /LOG:C:\Logs\Backup.log` | Copy with 16 threads keeping data, attributes and timestamps. |
| `robocopy C:\Users\Admin\Records D:\Backup /S /MAXAGE:7 /MOV /LOG:C:\Logs\Backup.log` | Move files, excluding files older than 7 days. |
| `robocopy C:\Records D:\Backup /iorate:1m` | Copy while limiting I/O to 1 MB per second. |
| `robocopy C:\Source C:\Destination /XC /XN /XO` | Skip files that already exist in the destination. |

# options

| option | description |
| --- | --- |
| `<source>` | Path to the source directory. |
| `<destination>` | Path to the destination directory. |
| `<file>` | File(s) to copy; wildcards supported; default `*.*`. |
| `/s` | Copies subdirectories, excluding empty directories. |
| `/e` | Copies subdirectories, including empty directories. |
| `/lev:<n>` | Copies only the top *n* levels of the source tree. |
| `/z` | Copies files in restartable mode. |
| `/b` | Copies files in backup mode, overriding ACLs that might block access. |
| `/zb` | Restartable mode; switches to backup mode if access is denied. |
| `/j` | Copies using unbuffered I/O (recommended for large files). |
| `/efsraw` | Copies all encrypted files in EFS RAW mode. |
| `/copy:<copyflags>` | File properties to copy: D data, A attributes, T timestamps, X skip ADS, S ACL, O owner, U auditing; default DAT. |
| `/dcopy:<copyflags>` | What to copy for directories: D, A, T, E extended attribute, X; default DA. |
| `/sec` | Copies files with security (`/copy:DATS`). |
| `/copyall` | Copies all file information (`/copy:DATSOU`). |
| `/nocopy` | Copies no file information (useful with `/purge`). |
| `/secfix` | Fixes file security on all files, even skipped ones. |
| `/timfix` | Fixes file times on all files, even skipped ones. |
| `/purge` | Deletes destination files and directories that no longer exist in the source. |
| `/mir` | Mirrors a directory tree (`/e` plus `/purge`). |
| `/mov` | Moves files, deleting them from the source after copying. |
| `/move` | Moves files and directories, deleting them from the source after copying. |
| `/a+:[RASHCNET]` | Adds the specified attributes to copied files. |
| `/a-:[RASHCNETO]` | Removes the specified attributes from copied files. |
| `/create` | Creates a directory tree and zero-length files only. |
| `/fat` | Creates destination files using 8.3 FAT file names only. |
| `/256` | Turns off support for paths longer than 256 characters. |
| `/mon:<n>` | Monitors the source and runs again when more than *n* changes are detected. |
| `/mot:<m>` | Monitors the source and runs again in *m* minutes if changes are detected. |
| `/rh:hhmm-hhmm` | Run times when new copies can be started. |
| `/pf` | Checks run times per file (not per pass). |
| `/ipg:<n>` | Inter-packet gap to free bandwidth on slow lines. |
| `/sj` | Copies junctions instead of link targets. |
| `/sl` | Copies symbolic links instead of following them. |
| `/mt:<n>` | Multi-threaded copies with *n* threads (1-128, default 8); not with `/ipg` or `/efsraw`. |
| `/nodcopy` | Copies no directory info. |
| `/nooffload` | Copies without the Windows Copy Offload mechanism. |
| `/compress` | Requests network compression during transfer, if applicable. |
| `/sparse:<y\|n>` | Enables or disables retaining sparse state; default yes. |
| `/noclone` | Doesn't attempt block cloning. |
| `/iomaxsize:<n>[kmg]` | Requested max I/O size per read/write cycle. |
| `/iorate:<n>[kmg]` | Requested I/O rate per second. |
| `/threshold:<n>[kmg]` | File size threshold for throttling. |
| `/a` | Copies only files with the Archive attribute set. |
| `/m` | Copies only files with the Archive attribute set, and resets it. |
| `/ia:[RASHCNETO]` | Includes only files with any of the specified attributes. |
| `/xa:[RASHCNETO]` | Excludes files with any of the specified attributes. |
| `/xf <filename>[ ...]` | Excludes files matching names or paths; wildcards supported. |
| `/xd <directory>[ ...]` | Excludes directories matching names and paths. |
| `/xc` | Excludes existing files with same timestamp but different size. |
| `/xn` | Excludes source files newer than the destination. |
| `/xo` | Excludes source files older than the destination. |
| `/xx` | Excludes extra files and directories present only in the destination. |
| `/xl` | Excludes lonely files and directories present only in the source. |
| `/im` | Includes modified files (differing change times). |
| `/is` | Includes the same files. |
| `/it` | Includes tweaked files (same name, size, times, different attributes). |
| `/max:<n>` | Excludes files bigger than *n* bytes. |
| `/min:<n>` | Excludes files smaller than *n* bytes. |
| `/maxage:<n>` | Excludes files older than *n* days or date (last modified). |
| `/minage:<n>` | Excludes files newer than *n* days or date (last modified). |
| `/maxlad:<n>` | Maximum last access date (excludes files unused since *n*). |
| `/minlad:<n>` | Minimum last access date (excludes files used since *n*). |
| `/xj` | Excludes junction points. |
| `/fft` | Assumes FAT file times (two-second precision). |
| `/dst` | Compensates for one-hour DST differences. |
| `/xjd` | Excludes junction points for directories. |
| `/xjf` | Excludes junction points for files. |
| `/r:<n>` | Retries on failed copies; default 1,000,000. |
| `/w:<n>` | Wait time between retries in seconds; default 30. |
| `/reg` | Saves `/r` and `/w` values as defaults in the registry. |
| `/tbd` | Waits for share names to be defined (retry error 67). |
| `/lfsm` | Low free space mode (copy, pause, resume); not with `/mt` or `/efsraw`. |
| `/lfsm:<n>[kmg]` | Floor size for low free space mode. |
| `/l` | Lists files only (no copy, delete or timestamp). |
| `/x` | Reports all extra files. |
| `/v` | Verbose output, shows skipped files. |
| `/ts` | Includes source file timestamps in output. |
| `/fp` | Includes full path names in output. |
| `/bytes` | Prints sizes as bytes. |
| `/ns` | Doesn't log file sizes. |
| `/nc` | Doesn't log file classes. |
| `/nfl` | Doesn't log file names. |
| `/ndl` | Doesn't log directory names. |
| `/np` | Doesn't display copy progress. |
| `/eta` | Shows estimated time of arrival of copied files. |
| `/log:<logfile>` | Writes status output to a log file (overwrite). |
| `/log+:<logfile>` | Writes status output to a log file (append). |
| `/unilog:<logfile>` | Writes status output as Unicode (overwrite). |
| `/unilog+:<logfile>` | Writes status output as Unicode (append). |
| `/tee` | Writes status output to console and log file. |
| `/njh` | No job header. |
| `/njs` | No job summary. |
| `/unicode` | Displays status output as Unicode. |
| `/job:<jobname>` | Derives parameters from a named job file. |
| `/save:<jobname>` | Saves parameters to a named job file. |
| `/quit` | Quits after processing the command line. |
| `/nosd` | No source directory is specified. |
| `/nodd` | No destination directory is specified. |
| `/if` | Includes the specified files. |
