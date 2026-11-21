---
created: 2026-11-21
fullpath: 'C:\Windows\System32\tar.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - archive
  - lolbin
aliases:
  - tar.exe
  - tar
  - bsdtar
url:
  - https://learn.microsoft.com/windows/tar/
---

**fullpath**:C:\Windows\System32\tar.exe

# description

tar is a command-line archiving tool included with Windows that creates, lists and extracts archives including .tar, .tar.gz, .zip and .7z. The Windows build is based on libarchive's bsdtar and supports the same flags used on Linux and macOS.

## simple description

> ### 2026-11-21 Claude said
> tar.exe is the built-in Windows version of the classic Unix tar archiver, shipped since Windows 10 1803. It can pack folders into archives and unpack them, including zip files, without extra software. Admins and developers use it in scripts the same way as on Linux.
>
> **SOC NOTE**: Living-off-the-land tool for staging data before exfiltration (T1560.001 Archive via Utility) and for extracting dropped payloads; also used to read files to alternate data streams. Hunt for tar.exe creating archives of user documents or running from unusual parents (Office, script hosts); Sysmon event 1 and 4688 process creation capture command lines.
>

# purpose

Create, list and extract archive files directly from the command line without installing extra software, with the same flags developers use on other platforms so scripts carry over. Full options are available via `tar --help` or the FreeBSD bsdtar manual.

# typical use cases

| usage | description |
| --- | --- |
| `tar -xf archive.tar.gz` | Extract an archive. |
| `tar -czf archive.tar.gz .\my-folder` | Create a .tar.gz from a folder. |
| `tar -caf archive.zip .\my-folder` | Create a .zip from a folder; -a picks the format from the extension. |
| `tar -tf archive.tar.gz` | List archive contents without extracting. |

# options

| option | description |
| --- | --- |
| `-x` | Extract an archive. |
| `-f` | Specify the archive file. |
| `-c` | Create an archive. |
| `-z` | gzip compression (format-specific flag). |
| `-a` | Auto-select the archive format from the file extension, replacing -z, -j, -J and -Z. |
| `-t` | List contents of an archive. |
| `--help` | Show the full list of options. |
