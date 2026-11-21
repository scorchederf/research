---
created: 2026-11-21
fullpath: 'C:\Windows\System32\spoolsv.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - service
  - printing
aliases:
  - spoolsv.exe
  - Print Spooler
  - Spooler
url:
  - https://learn.microsoft.com/windows-hardware/drivers/print/introduction-to-spooler-components
  - https://learn.microsoft.com/troubleshoot/windows-server/printing/print-spooler-service-not-running
  - https://learn.microsoft.com/troubleshoot/windows-server/printing/troubleshoot-printing-scenarios
  - https://learn.microsoft.com/troubleshoot/windows-server/printing/spooler-xml-file-grow-spoolsv-exe-high-cpu
  - https://learn.microsoft.com/security-updates/securitybulletins/2010/ms10-061
  - https://learn.microsoft.com/security-updates/securitybulletins/2013/ms13-050
---

**fullpath**:C:\Windows\System32\spoolsv.exe

# description

`Spoolsv.exe` is the print spooler's API server, implemented as the Print Spooler service (`Spooler`) that starts with the operating system and runs until shutdown. It exports an RPC interface for the server side of the spooler Win32 API, used locally by `Winspool.drv` and remotely by `Win32spl.dll`, and passes most calls to print providers through the router `Spoolss.dll`. All spooler components run in user mode.

## simple description

> ### 2026-11-21 Claude said
> `spoolsv.exe` is the Print Spooler service. It takes print jobs from applications, stores them in the spool folder, loads printer drivers and sends jobs to printers. It runs as SYSTEM on almost every Windows machine, including domain controllers, even when no printer is used.
>
> **SOC NOTE**: Frequent attack target: PrintNightmare (CVE-2021-34527/1675) for remote code execution and privilege escalation via malicious driver DLLs (T1068, T1547.012 Print Processors / port monitors), and the "printer bug" (MS-RPRN) to coerce DC authentication for relay (T1187). Suspicious signs: spoolsv spawning `cmd`/`powershell`, new DLLs in `System32\spool\drivers`, Event IDs 316/808 in `PrintService` logs. Disable the service on DCs and servers that don't print.
>

# purpose

Manages printing: retrieves the location of the correct printer driver, loads it, spools high-level function calls into a print job and schedules print jobs, then hands completed jobs to the print router.

# typical use cases

| usage | description |
| --- | --- |
| `net stop spooler` | Stop the Print Spooler service (elevated). |
| `net start spooler` | Start the Print Spooler service (elevated). |
| `Restart-Service -Name spooler` | Restart the Print Spooler service from elevated PowerShell to clear stuck jobs. |
| `sc stop spooler` | Stop the spooler, used with setting `Start` = 4 under `HKLM\SYSTEM\CurrentControlSet\services\Spooler` to disable it as a mitigation. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
