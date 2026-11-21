---
created: 2026-11-21
fullpath: 'C:\Windows\System32\spool\tools\PrintBrm.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - printing
aliases:
  - "PrintBrm.exe"
  - "Printbrm"
  - "Printer Migration"
url:
  - https://learn.microsoft.com/windows/iot/iot-enterprise/optimize/removable-packages/microsoft-windows-printing-premiumtools
  - https://learn.microsoft.com/troubleshoot/windows-server/printing/back-up-restore-printers
---

**fullpath**: C:\Windows\System32\spool\tools\PrintBrm.exe

# description

PrintBrm.exe is the print services migration (backup/restore) command-line tool. It ships in the Microsoft-Windows-Printing-PremiumTools package together with printbrmui.exe (Printer Migration wizard), printbrmengine.exe and printbrmps.dll. It backs up and restores printer queues, drivers and settings to .printerExport files, as does the Print Management snap-in.

## simple description

> ### 2026-11-21 Claude said
> PrintBrm.exe is a built-in Windows tool that backs up printers (queues, drivers, ports, settings) into a single file and restores them on another server. Admins use it when migrating print servers. It can target remote print servers by UNC name. It writes Application events with a PrintBRM source.
>
> **SOC NOTE**: Can be abused to pack or unpack arbitrary files into/from .printerExport CAB-style archives, and has been used to plant malicious printer drivers or to stage/exfiltrate data (LOLBAS entry; related to T1105/T1560). Restoring an attacker-supplied backup installs drivers that run in spoolsv.exe as SYSTEM. Investigate unexpected PrintBrm executions, especially with -r and files from user paths.
>

# purpose

Backs up and restores print queues, printer drivers and printer settings, locally or on a remote print server, for print server migration. Run it from `%WINDIR%\System32\Spool\Tools` at an elevated prompt.

# typical use cases

| usage | description |
| --- | --- |
| `Printbrm -s \\<server> -b -f <file>.printerExport` | Back up the printers of a (remote) print server to a file. |
| `Printbrm -s \\<server> -r -f <file>.printerExport` | Restore printers from a backup file to the destination server. |
| `Printbrm /?` | Show the complete syntax. |

# options

| option | description |
| --- | --- |
| `-s` | UNC name of the source or destination computer. |
| `-b` | Perform a backup. |
| `-r` | Perform a restore. |
| `-f` | File name for the printer settings file (.printerExport). |
| `/?` | Display the complete syntax. |
