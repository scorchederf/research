---
created: 2026-11-21
fullpath: 'C:\Windows\System32\where.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lolbin
aliases:
  - where.exe
  - where
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/where
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_command_precedence?view=powershell-7.6
---

**fullpath**:C:\Windows\System32\where.exe

# description

where.exe displays the location of files that match a search pattern, searching the current directory and the PATH by default. It is a built-in Windows command. In PowerShell `where` is an alias for `Where-Object`, so `where.exe` must be typed with its extension.

## simple description

> ### 2026-11-21 Claude said
> where.exe finds files by name, like `which` on Linux. By default it looks in the current folder and every folder in PATH, and it can also search recursively. Admins and scripts use it to check which copy of a program will run. It is a harmless built-in tool.
>
> **SOC NOTE**: Used for discovery (T1083 File and Directory Discovery), e.g. `where /r C:\ *.kdbx` or hunting for config/credential files, and to locate tooling. Recursive searches over user profiles or network shares from unusual parents (cmd spawned by Office, remote shells) are suspicious. Logged in 4688/Sysmon 1 with full command line.
>

# purpose

Locate files matching a pattern in PATH, a given path, an environment variable's paths, or recursively.

# typical use cases

| usage | description |
| --- | --- |
| `where /r c:\ test` | Find all files named Test on drive C and its subdirectories. |
| `where $public:*.*` | List all files in the Public directory using an environment variable. |
| `where /r \\computer1\c notepad.*` | Find files named Notepad on a remote computer's C share recursively. |

# options

| option | description |
| --- | --- |
| `/r <Dir>` | Recursive search starting with the specified directory. |
| `/q` | Return an exit code (0 success, 1 failure) without displaying matches. |
| `/f` | Display results in quotation marks. |
| `/t` | Display file size and last modified date and time. |
| `[$<ENV>:\|<Path>:]<Pattern>[ ...]` | Search pattern (wildcards `*` and `?`); optionally limited to paths in an environment variable or a path. Not used with `/r`. |
| `/?` | Display help. |
