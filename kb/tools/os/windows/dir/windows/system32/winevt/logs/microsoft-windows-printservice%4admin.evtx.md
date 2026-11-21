---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-PrintService%4Admin.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - evtx
  - printing
aliases:
  - Microsoft-Windows-PrintService%4Admin.evtx
  - Microsoft-Windows-PrintService/Admin
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/printing/event-ids-associated-point-print-restrictions
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-PrintService%4Admin.evtx

# description

Event log file for the **Microsoft-Windows-PrintService/Admin** channel, written by the Print Spooler (source Microsoft-Windows-PrintService). It records spooler errors such as plug-in module load failures and printer driver installation failures, commonly associated with Point and Print restrictions.

## simple description

> ### 2026-11-21 Claude said
> This log holds administrative events from the Windows Print Spooler service. It shows errors when the spooler fails to load a DLL or install a printer driver. Admins use it to troubleshoot printer deployment issues. It is enabled by default.
>
> **SOC NOTE**: Key for PrintNightmare-style attacks (CVE-2021-34527/1675; T1068, T1547.012 print processors): event 808 (failed to load plug-in module) and 215/316 driver installs can reveal malicious DLLs loaded by spoolsv.exe. Also review PrintService/Operational and new files in spool\drivers.
>

# purpose

Records Print Spooler administrative errors.

| event ID | description |
| --- | --- |
| 808 | The print spooler failed to load a plug-in module <DLL Name> (e.g. error code 0x7e). |
| 215 | Installing printer driver <DriverName> failed with the given error code/HRESULT. |

