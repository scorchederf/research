---
created: 2026-11-21
fullpath: 'C:\Windows\System32\findstr.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows-commands
  - lolbin
aliases:
  - findstr.exe
  - findstr
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/findstr
---

**fullpath**:C:\Windows\System32\findstr.exe

# description

findstr is a built-in Windows command that searches for patterns of text in files, supporting literal strings and a limited regular-expression syntax. Related commands are `find` and the Sysinternals `strings` tool.

## simple description

> ### 2026-11-21 Claude said
> findstr is like grep for Windows: it searches files or piped output for text. Administrators and scripts use it all the time, for example `tasklist | findstr chrome`. It supports simple regular expressions and recursive searching of folders. On its own it is a normal, harmless tool.
>
> **SOC NOTE**: Commonly used in discovery and credential hunting (MITRE T1083, T1552.001 Credentials In Files), e.g. `findstr /si password *.xml *.ini *.config` or searching GPP `cpassword` in SYSVOL. Also listed in LOLBAS for downloading/ADS-writing via `findstr /V /L <x> \\server\share\file > file:ads` (T1105, T1564.004). Review command lines for password keywords, UNC paths and output redirection into alternate data streams.
>

# purpose

Searches files for text patterns. All options must precede the strings and file names; spaces separate multiple search strings unless `/c` is used; to search for multiple strings in a set of files, put each criterion on its own line in a text file. Accepted regex meta-characters are `.`, `*`, `^`, `$`, `[class]`, `[^class]`, `[x-y]`, `\x`, `\<string` and `string\>`.

# typical use cases

| usage | description |
| --- | --- |
| `findstr hello there x.y` | Search for *hello* or *there* in x.y. |
| `findstr /c:"hello there" x.y` | Search for the literal phrase *hello there*. |
| `findstr /s /i Windows *.*` | Case-insensitive recursive search of the current directory tree. |
| `findstr /b /n /r /c:"^ *FOR" *.bas` | Find lines starting with FOR (after spaces) and show line numbers. |
| `findstr /g:stringlist.txt /f:filelist.txt > results.out` | Use search strings and file list from files and save the results. |
| `findstr /s /i /m \<computer\> *.*` | List every file containing the word computer. |

# options

| option | description |
| --- | --- |
| `/b` | Matches the pattern if it is at the beginning of a line. |
| `/e` | Matches the pattern if it is at the end of a line. |
| `/l` | Processes search strings literally. |
| `/r` | Processes search strings as regular expressions (default). |
| `/s` | Searches the current directory and all subdirectories. |
| `/i` | Ignores case. |
| `/x` | Prints lines that match exactly. |
| `/v` | Prints only lines that don't contain a match. |
| `/n` | Prints the line number of each matching line. |
| `/m` | Prints only the file name if a file contains a match. |
| `/o` | Prints character offset before each matching line. |
| `/p` | Skips files with non-printable characters. |
| `/off[line]` | Does not skip files that have the offline attribute set. |
| `/f:<file>` | Gets a file list from the specified file. |
| `/c:<string>` | Uses the specified text as a literal search string. |
| `/g:<file>` | Gets search strings from the specified file. |
| `/d:<dirlist>` | Searches a semicolon-separated list of directories. |
| `/a:<colorattribute>` | Specifies color attributes with two hexadecimal digits. |
| `<strings>` | Text to search for. Required. |
| `[<drive>:][<path>]<filename>[...]` | File(s) to search. At least one is required. |
| `/?` | Displays Help. |
