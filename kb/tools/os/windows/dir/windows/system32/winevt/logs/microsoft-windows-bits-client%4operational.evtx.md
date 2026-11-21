---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Bits-Client%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - eventlog
  - bits
aliases:
  - "Microsoft-Windows-Bits-Client%4Operational.evtx"
  - "Microsoft-Windows-Bits-Client/Operational"
  - "Bits-client Operational"
url:
  - https://learn.microsoft.com/windows/win32/bits/bits-return-values
---

**fullpath**: C:\Windows\System32\winevt\Logs\Microsoft-Windows-Bits-Client%4Operational.evtx

# description

Event log file for the Microsoft-Windows-Bits-Client/Operational channel of the Background Intelligent Transfer Service (BITS). In Event Viewer it appears under Applications and Services Logs\Microsoft\Windows\Bits-client\Operational. BITS is used by Windows Update, WSUS, Configuration Manager and applications to transfer files in the background.

## simple description

> ### 2026-11-21 Claude said
> This file stores the BITS client operational log. Every time a BITS transfer job is created, started, completed or fails, events are written here with the job name, owner and URL. Windows Update and many apps use BITS, so the log is normally busy. Analysts read it with Event Viewer or tools like EvtxECmd.
>
> **SOC NOTE**: Attackers use BITS (bitsadmin.exe, Start-BitsTransfer) to download payloads and for persistence via job notify commands (T1197 BITS Jobs). Event ID 3 (job created), 59 (transfer started, includes URL), 60 (transfer stopped) and 4 (job completed) reveal remote URLs, job names and owners; look for unusual hosts, raw IPs and jobs created by unexpected users.
>

# purpose

Records BITS client job activity. Microsoft Learn notes that when BITS returns BG_E_VALIDATION_FAILED (the application requested data from a website but the response was not valid), details are found in Event Viewer under Application Logs\Microsoft\Windows\Bits-client\Operational.
