---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows\WER\ReportArchive'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - wer
  - forensics
aliases:
  - ReportArchive
  - WER ReportArchive
url:
  - https://learn.microsoft.com/windows-server/failover-clustering/troubleshooting-using-wer-reports
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-errorreporting
---

**fullpath**:C:\ProgramData\Microsoft\Windows\WER\ReportArchive

# description

`ReportArchive` is a subfolder of the Windows Error Reporting store at `%ProgramData%\Microsoft\Windows\WER`. It holds reports that have already been uploaded to Watson; data in these reports is deleted but the `Report.wer` file persists. Its sibling `ReportQueue` holds reports waiting to be uploaded.

## simple description

> ### 2026-11-21 Claude said
> When an application or system component crashes or hangs, Windows Error Reporting creates a report folder. After the report is sent to Microsoft it is moved into ReportArchive. Each subfolder name usually includes the report type, the faulting application and a hash. The Report.wer text file records which program failed, when and with what module or exception.
>
> **SOC NOTE**: Report.wer files give a timeline of crashing processes, including malware, exploited apps or tools like Mimikatz crashing LSASS access attempts. Look for unusual executable names or paths in AppPath/Sig fields. Attackers may clear WER folders to hide evidence (T1070.004). Useful for detecting failed exploitation and process hollowing crashes.
>

# purpose

Stores Windows Error Reporting reports that were already uploaded. The Configure Report Archive policy (`DisableArchive` under `SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting`) controls whether all data or only parameters are stored and the maximum number of reports kept.

# common files found

| file | description |
| --- | --- |
| `Report.wer` | Persisting report file describing what failed; starting point for triage. |
| `Critical_<component>_<hash>_cab_<id>` folders | Per-report folders, e.g. failover cluster PhysicalDisk reports, which may include log (.evtx) and dump files such as `memory.hdmp`. |

