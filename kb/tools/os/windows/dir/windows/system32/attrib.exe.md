---
created: 2026-11-21
fullpath: 'C:\Windows\System32\attrib.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lolbin
  - filesystem
aliases:
  - "attrib.exe"
  - "attrib"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/attrib
---

**fullpath**:C:\Windows\System32\attrib.exe

# description

attrib displays, sets, or removes attributes assigned to files or directories; without parameters it displays attributes of all files in the current directory. It is a built-in Windows command documented in the Windows Commands reference; related tools include `xcopy`, which uses archive attributes.

## simple description

> ### 2026-11-21 Claude said
> attrib.exe is a built-in Windows command-line tool that shows or changes file attributes such as Read-only, Hidden, System and Archive. Administrators use it to unhide files, clear read-only flags, or mark files for backup. It ships with every Windows version in System32.
>
> **SOC NOTE**: Attackers use `attrib +h +s` to hide payloads, scripts and persistence files from Explorer (MITRE T1564.001 Hidden Files and Directories); ransomware and worms also run `attrib -r -s -h` on user files. Look for attrib.exe process creation (Sysmon 1 / Security 4688) with `+h`/`+s` on files in user-writable paths, Startup folders or USB drives.
>

# purpose

Displays, sets, or removes the Read-only, Archive, System, Hidden, Offline, Not Content Indexed, Scrub, Pinned, Unpinned and SMR Blob attributes for files or directories, optionally recursively.

# typical use cases

| usage | description |
| --- | --- |
| `attrib news86` | Display the attributes of the file news86 in the current directory. |
| `attrib +r report.txt` | Assign the Read-only attribute to report.txt. |
| `attrib -r b:\public\*.* /s` | Remove the Read-only attribute from files in the public directory and its subdirectories. |
| `attrib +a a:*.* & attrib -a a:*.bak` | Set the Archive attribute for all files on drive a:, then clear it for .bak files. |

# options

| option | description |
| --- | --- |
| `{+\|-}r` | Sets (+) or clears (-) the Read-only file attribute. |
| `{+\|-}a` | Sets or clears the Archive file attribute, which marks files changed since the last backup; xcopy uses it. |
| `{+\|-}s` | Sets or clears the System file attribute; it must be cleared before other attributes can be changed. |
| `{+\|-}h` | Sets or clears the Hidden file attribute; it must be cleared before other attributes can be changed. |
| `{+\|-}o` | Sets or clears the Offline file attribute. |
| `{+\|-}i` | Sets or clears the Not Content Indexed file attribute. |
| `{+\|-}x` | Sets or clears the Scrub file attribute. |
| `{+\|-}p` | Sets or clears the Pinned file attribute. |
| `{+\|-}u` | Sets or clears the Unpinned file attribute. |
| `{+\|-}b` | Sets or clears the SMR Blob file attribute. |
| `[<drive>:][<path>][<filename>]` | Location and name of the files or directories to view or change; supports ? and * wildcards. |
| `/s` | Applies attrib to matching files in the current directory and all subdirectories. |
| `/d` | Applies attrib to directories. |
| `/l` | Applies attrib to the symbolic link rather than its target. |
| `/?` | Displays help at the command prompt. |
