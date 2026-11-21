---
created: 2026-11-21
fullpath: 'C:\Windows\System32\spool\PRINTERS'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - printing
  - spooler
aliases:
  - 'PRINTERS'
  - 'Spool folder'
  - 'DefaultSpoolDirectory'
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/printing/troubleshoot-printing-scenarios
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-exclusions-windows-server
---

**fullpath**: C:\Windows\System32\spool\PRINTERS

# description

Default Print Spooler spool folder (`%systemroot%\System32\Spool\Printers`). Its location is set by the `DefaultSpoolDirectory` value under `HKLM\SYSTEM\CurrentControlSet\Control\Print\Printers`. The Print Spooler service (spoolsv.exe) writes queued jobs here and deletes them when printed; Microsoft Defender automatically excludes it on Print Server role installs.

## simple description

> ### 2026-11-21 Claude said
> When you print, Windows first writes the job to this folder as a pair of files (.SHD for job settings, .SPL for the print data), and the Print Spooler service sends it to the printer. Normally the folder is empty or nearly empty because files are deleted after printing. Stuck or corrupt files here cause print queue problems.
>
> **SOC NOTE**: Leftover .SPL/.SHD files can contain the actual content of printed documents (EMF/XPS/RAW) - valuable for data-exfiltration or insider cases, and can be carved. The spooler folder and spoolsv.exe have been abused by PrintNightmare-style exploits (CVE-2021-34527, T1068/T1547.012 print processors); monitor unexpected files or DLLs written by spoolsv.exe.
>

# purpose

Holds spool files for print jobs in progress; files are removed as jobs print. Old or orphaned files can cause Print Spooler problems and are removed after stopping the spooler.

# common files found

| file | description |
| --- | --- |
| `*.SHD` | Shadow files for spooled print jobs (job information). |
| `*.SPL` | Spool files for print jobs (print data). |
| `*.TMP` | Temporary spooler files that antivirus scanning can interfere with. |
