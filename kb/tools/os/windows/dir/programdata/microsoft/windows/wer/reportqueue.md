---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows\WER\ReportQueue'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - wer
  - forensics
aliases:
  - ReportQueue
  - WER ReportQueue
url:
  - https://learn.microsoft.com/windows-server/failover-clustering/troubleshooting-using-wer-reports
  - https://learn.microsoft.com/windows-hardware/drivers/wdf/accessing-umdf-metadata-in-wer-reports
  - https://learn.microsoft.com/windows/win32/wer/wer-settings
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-errorreporting
---

**fullpath**:C:\ProgramData\Microsoft\Windows\WER\ReportQueue

# description

`ReportQueue` is the Windows Error Reporting (WER) folder that holds reports waiting to be uploaded to Microsoft (Watson). WER reports are stored under `%ProgramData%\Microsoft\Windows\WER`; reports already uploaded move to `ReportArchive`. WER settings are in `HKLM` / `HKCU\Software\Microsoft\Windows\Windows Error Reporting`, and the **Configure Report Queue** policy (`DisableQueue`) controls queuing.

## simple description

> ### 2026-11-21 Claude said
> When a program or service crashes or hangs, Windows Error Reporting writes a report folder here before sending it to Microsoft. Each subfolder (like `AppCrash_...` or `NonCritical_...`) contains a `Report.wer` text file and sometimes memory dumps and logs. Reports stay here until they are uploaded or cleaned up.
>
> **SOC NOTE**: Crash reports can reveal exploitation attempts or failing malware (process name, faulting module, path, time). Memory dumps (`.hdmp`, `.mdmp`) may contain credentials or decrypted payloads, so treat them as sensitive. Attackers also abuse WER (`werfault.exe`) for LSASS dumping (T1003.001) and DLL sideloading. Check `Report.wer` for unknown executables in user-writable paths.
>

# purpose

Holds queued WER reports so they can be sent to Watson; also a source for troubleshooting, for example failover cluster resource failures or UMDF driver host crashes.

# common files found

| file | description |
| --- | --- |
| `<ReportType>_<name>_<hash>\Report.wer` | Report file with WER information; start triage from it to see what failed. |
| `NonCritical_HostProblem_*\Report.wer` | UMDF `WUDFHostProblem` reports with UMDF metadata (Windows 8.1). |
| `*.evtx` | Event logs collected with cluster resource failure reports. |
| `memory.hdmp` | Dump files collected for hung processes such as RHS or `clussvc.exe`. |
