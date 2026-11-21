---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Expand.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - cab
  - lolbin
aliases:
  - 'Expand.exe'
  - 'expand'
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/expand
---

**fullpath**:C:\Windows\System32\Expand.exe

# description

`expand.exe` expands one or more compressed files and extracts files from cabinet (.cab) files. It is a built-in Windows command; related tools are `makecab`/`diantz` (create cabinets) and `extrac32`.

## simple description

> ### 2026-11-21 Claude said
> Expand decompresses files that were compressed with Microsoft's cabinet format, either single compressed files or files inside a .cab archive. It can also list the contents of a .cab. It is a signed tool present on all Windows systems.
>
> **SOC NOTE**: Abused to unpack payloads delivered as .cab (T1140 Deobfuscate/Decode Files) and to copy files, including to/from alternate data streams or WebDAV/UNC paths (T1105, T1564.004). Look for expand.exe writing executables to user/temp folders, sourcing from remote paths, or spawned by Office/script hosts.
>

# purpose

Expands one or more compressed files and can retrieve compressed files from distribution disks. It can also run from the Windows Recovery Console with different parameters.

# typical use cases

| usage | description |
| --- | --- |
| `expand -d <source>.cab` | List the files in a cabinet without extracting them. |
| `expand <source>.cab -f:<files> <destination>` | Extract the specified files from a cabinet to a destination. |
| `expand -r <source> [<destination>]` | Expand files and rename them. |

# options

| option | description |
| --- | --- |
| `-r` | Renames expanded files. |
| `source` | Files to expand; can include drive, directory, file name and wildcards (`*` or `?`). |
| `destination` | Where files are expanded; must be an existing directory if *source* has multiple files and `-r` isn't used. |
| `-i` | Renames expanded files but ignores the directory structure. |
| `-d` | Displays a list of files in the source location without expanding them. |
| `-f:<files>` | Files in a .cab file to expand; wildcards allowed. |
| `/?` | Displays help at the command prompt. |
