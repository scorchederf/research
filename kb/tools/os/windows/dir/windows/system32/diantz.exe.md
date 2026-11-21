---
created: 2026-11-21
fullpath: 'c:\windows\system32\diantz.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows-commands
  - cab
aliases:
  - diantz.exe
  - makecab
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/diantz
  - https://learn.microsoft.com/windows-server/administration/windows-commands/makecab
---

**fullpath**:c:\windows\system32\diantz.exe

# description

diantz packages existing files into a cabinet (.cab) file. It performs the same actions as the makecab command and is documented in the Windows Commands reference.

## simple description

> ### 2026-11-21 Claude said
> diantz.exe is a built-in Windows tool that compresses files into Microsoft Cabinet (.cab) archives, identical in function to makecab.exe. It can take a single file or a directive file describing many files. It is rarely used by end users today.
>
> **SOC NOTE**: Listed in LOLBAS: attackers use diantz to compress data for exfiltration (T1560.001 Archive via Utility) and to write files into alternate data streams or remote UNC shares, and to download/copy payloads. Any diantz execution on a workstation, especially with UNC paths or ':' ADS syntax, is suspicious.
>

# purpose

Compress a source file into a .cab. If the destination is omitted, the last character of the source file name is replaced with an underscore.

# typical use cases

| usage | description |
| --- | --- |
| `diantz <source> [<destination>]` | Compress one file into a cabinet. |
| `diantz /f <directives_file>` | Build a cabinet using a directives file. |

# options

| option | description |
| --- | --- |
| `<source>` | File to compress. |
| `<destination>` | Name for the compressed file; default replaces the last source character with _. |
| `/f <directives_file>` | File with diantz directives (may be repeated). |
| `/d var=<value>` | Defines a variable with the specified value. |
| `/l <dir>` | Location to place the destination (default current directory). |
| `/v[<n>]` | Debugging verbosity level (0=none ... 3=full). |
| `/?` | Displays help at the command prompt. |

