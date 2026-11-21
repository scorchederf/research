---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-GroupPolicy%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - grouppolicy
aliases:
  - Microsoft-Windows-GroupPolicy%4Operational.evtx
  - Microsoft-Windows-GroupPolicy/Operational
  - Group Policy operational log
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/applying-group-policy-troubleshooting-guidance
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/group-policy-error-7016-1091-1202
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-GroupPolicy%4Operational.evtx

# description

This file stores the Microsoft-Windows-GroupPolicy/Operational event log, written by the Group Policy service (source Microsoft-Windows-GroupPolicy) on Windows Vista/Server 2008 and later. It records each phase of Group Policy processing, correlated by ActivityID. Related tools are Event Viewer, `gpupdate`, and the gpsvc.log debug log.

## simple description

> ### 2026-11-21 Claude said
> This is the event log file where Windows records detailed Group Policy processing: when policy refreshes start and end, which GPOs and client-side extensions ran, how long they took, and any errors. The `%4` in the name stands for the `/` in the log name. Admins use it to see why a policy did or didn't apply.
>
> **SOC NOTE**: Useful for spotting malicious GPO deployment (MITRE ATT&CK T1484.001): it shows which GPOs were applied and when, the DC contacted, and CSE runs (e.g. Scheduled Tasks, Scripts, Registry). Key IDs include 4016/5016 (CSE start/end), 7016 (CSE completion with error), 5312/5313 (GPO lists), 1129, 1097, 1002, 1006.
>

# purpose

Records the pre-processing, processing, and post-processing phases of each Group Policy instance. Each instance has a unique ActivityID; filter with a custom view query such as `<Select Path="Microsoft-Windows-GroupPolicy/Operational">*[System/Correlation/@ActivityID='{...}']</Select>`. Events include 4016 (CSE begins processing), 5016 (CSE completed successfully; E_PENDING expected for Audit CSE), and 7016 (CSE completed with an error code, e.g. Security extension).
