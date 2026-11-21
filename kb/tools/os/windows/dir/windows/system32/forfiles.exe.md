---
created: 2026-11-21
fullpath: 'C:\Windows\System32\forfiles.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - cmd
  - batch
aliases:
  - forfiles.exe
  - forfiles
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/forfiles
---

**fullpath**:C:\Windows\System32\forfiles.exe

# description

`forfiles.exe` is a built-in Windows command that selects files (optionally recursively and by date) and runs a command on each one. It is most commonly used in batch files and is documented in the Windows Commands reference.

## simple description

> ### 2026-11-21 Claude said
> forfiles runs a command against every file that matches a pattern, for example deleting logs older than 30 days. You give it a folder, a file mask, an optional age filter and the command to run, using variables like @file and @path. It is mainly used in maintenance batch scripts.
>
> **SOC NOTE**: A known LOLBin for indirect command execution (MITRE T1202): `forfiles /p c:\windows\system32 /m notepad.exe /c "calc.exe"` launches arbitrary programs with forfiles as the parent, evading parent-child detections. Hunt for forfiles.exe spawning cmd/powershell/rundll32 or unusual binaries, and for `0x` hex-encoded characters in `/c`.
>

# purpose

Runs a command on or passes arguments to multiple files, e.g. running `type` on all .txt files in a tree. It can select files by absolute or relative date (`/d`), build archive trees using variables such as @FSIZE and @FDATE, differentiate files from directories via @ISDIR, and include special characters using hexadecimal `0xHH`.

# typical use cases

| usage | description |
| --- | --- |
| `forfiles /P c:\ /S /M *.bat /C "cmd /c echo @file is a batch file"` | Lists all batch files on drive C. |
| `forfiles /P c:\ /S /M * /C "cmd /c if @isdir==TRUE echo @file is a directory"` | Lists all directories on drive C. |
| `forfiles /S /M *.* /D -365 /C "cmd /c echo @file is at least one year old."` | Lists files at least one year old. |
| `forfiles /S /M *.* /D -01/01/2007 /C "cmd /c echo @file is outdated."` | Lists files older than January 1, 2007. |
| `forfiles /S /M *.* /C "cmd /c echo The extension of @file is 0x09@ext"` | Lists extensions with a tab inserted via hex code. |

# options

| option | description |
| --- | --- |
| `/P <pathname>` | Path to start the search from; default is the current working directory. |
| `/M <searchmask>` | Searches files matching the search mask; default `*`. |
| `/S` | Searches subdirectories recursively. |
| `/C <command>` | Runs the command on each file; wrap in double quotes. Default `"cmd /c echo @file"`. |
| `/D [{+\|-}][{<date>\|<days>}]` | Selects files by last modified date (regional format) or relative days (0-32,768); `+` is default. |
| `/?` | Displays help. |
| `@FILE` | Variable: file name. |
| `@FNAME` | Variable: file name without extension. |
| `@EXT` | Variable: file name extension. |
| `@PATH` | Variable: full path of the file. |
| `@RELPATH` | Variable: relative path of the file. |
| `@ISDIR` | Variable: TRUE if a directory, otherwise FALSE. |
| `@FSIZE` | Variable: file size in bytes. |
| `@FDATE` | Variable: last modified date stamp. |
| `@FTIME` | Variable: last modified time stamp. |
