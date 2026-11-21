---
created: 2026-11-21
fullpath: 'C:\Windows\System32\extrac32.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows-commands
  - lolbin
aliases:
  - extrac32.exe
  - Extrac32
  - extract
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/extract
---

**fullpath**:C:\Windows\System32\extrac32.exe

# description

Extrac32.exe extracts files from cabinet (.cab) files or copies compressed sources. Originally part of Internet Explorer and now part of Windows, it replaces Extract.exe, which is neither provided nor supported on Windows 10 and Windows Server 2016 and newer.

## simple description

> ### 2026-11-21 Claude said
> extrac32 unpacks .cab archive files, which Windows and installers use to package files. It can also simply copy a file with the `/C` switch. It does not print anything to the console, so even `/?` output must be piped through `more`. It is a standard Windows tool.
>
> **SOC NOTE**: LOLBAS entry (MITRE T1105 Ingress Tool Transfer, T1564.004 NTFS ADS): `extrac32 /Y /C \\webdav\share\file.exe C:\path\file.exe` copies/downloads files, and it can extract CABs into alternate data streams. Malicious documents have dropped payloads in CABs extracted with extrac32. Investigate extrac32 runs from Office, scripts or with UNC/WebDAV sources.
>

# purpose

Extracts files from a cabinet (two or more files) or from a compressed single-file source, optionally renaming it, and copies files with `/C`. It can follow a cabinet chain with `/A`. It produces no console output.

# typical use cases

| usage | description |
| --- | --- |
| `extrac32.exe /? \| more` | Show help (output is otherwise not displayed). |
| `Extrac32 /E /L C:\out cabinet.cab` | Extract all files from a cabinet into C:\out. |
| `Extrac32 /D cabinet.cab` | Display the cabinet directory. |
| `Extrac32 /Y /C source destination` | Copy source file to destination without prompting. |

# options

| option | description |
| --- | --- |
| `cabinet` | Cabinet file (contains two or more files). |
| `filename` | File to extract from the cabinet; wildcards and multiple names allowed. |
| `source` | Compressed file (a cabinet with only one file). |
| `newname` | New file name for the extracted file; default is the original name. |
| `/A` | Process ALL cabinets, following the cabinet chain. |
| `/C` | Copy source file to destination (to copy from DMF disks). |
| `/D` | Display cabinet directory (use with filename to avoid extract). |
| `/E` | Extract (use instead of *.* to extract all files). |
| `/L dir` | Location to place extracted files; default is current directory. |
| `/Y` | Do not prompt before overwriting an existing file. |
