---
created: 2026-11-21
fullpath: 'C:\Windows\System32\makecab.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - makecab.exe
  - makecab
  - diantz
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/makecab
---

**fullpath**:C:\Windows\System32\makecab.exe

# description

Makecab packages existing files into a cabinet (.cab) file. It is the same as the `diantz` command and is part of the Windows Commands set; related to the Microsoft Cabinet format and the `expand`/`extract` tools.

## simple description

> ### 2026-11-21 Claude said
> Makecab is a built-in Windows tool that compresses one or more files into a .cab archive, Microsoft's own compressed archive format. Installers, drivers and Windows updates use .cab files. It can compress a single file or follow a directives (.ddf) file to build multi-file cabinets. Its twin, diantz.exe, behaves identically.
>
> **SOC NOTE**: Attackers use makecab to compress collected data before exfiltration (MITRE ATT&CK T1560.001 Archive via Utility) and to pack payloads; cabinets can also be abused with `expand`/`extrac32` or `diantz` to write data into alternate data streams (T1564.004). Unusual parents (cmd from Office, PowerShell) or output .cab files in temp, public or user folders warrant review.
>

# purpose

Compress files into Microsoft Cabinet (.cab) archives, either a single source file or many files driven by a directives file.

# typical use cases

- Compress one file: `makecab file.txt file.cab`
- Build a cabinet from a directives file: `makecab /f files.ddf`

# options

| option    | description    |
| --- | --- |
| `<source>` | File to compress. |
| `<destination>` | Name for the compressed file. If omitted, the last character of the source name is replaced with an underscore (\_). |
| `/f <directives_file>` | A file with **makecab** directives (may be repeated). |
| `/d var=<value>` | Defines a variable with the specified value. |
| `/l <dir>` | Location to place destination (default is current directory). |
| `/v[<n>]` | Sets debugging verbosity level (0=none,...,3=full). |
| `/?` | Displays help at the command prompt. |
