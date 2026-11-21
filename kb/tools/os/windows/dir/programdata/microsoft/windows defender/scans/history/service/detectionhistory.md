---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows Defender\Scans\History\Service\DetectionHistory'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - defender
  - forensics
aliases:
  - DetectionHistory
  - Protection history
url:
  - https://learn.microsoft.com/answers/a/12135593
  - https://learn.microsoft.com/answers/a/7959580
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-security-center-antivirus
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-microsoftdefenderantivirus
---

**fullpath**:C:\ProgramData\Microsoft\Windows Defender\Scans\History\Service\DetectionHistory

# description

Microsoft Defender Antivirus folder holding the detection history shown as Protection history in the Windows Security app (Virus & threat protection > Protection history). The `Scans` folder is protected and normally cannot be opened even by administrators. Retention of items in the scan history folder is controlled by the "Turn on removal of items from scan history folder" policy (`PurgeItemsAfterDelay`, default 30 days).

## simple description

> ### 2026-11-21 Claude said
> This folder holds Microsoft Defender's record of every threat it detected, which feeds the "Protection history" page in Windows Security. Each detection is stored as a small binary file with details like the threat name, file path, process and time. Windows locks the folder down so normal users and even admins can't browse it easily.
>
> **SOC NOTE**: DetectionHistory files are valuable forensic artifacts that can survive event log clearing, revealing malware names, paths and timestamps (parse with tools like KAPE/Defender detection history parsers). Attackers clearing this folder (often in Safe Mode) or the Defender Operational log is indicator removal (MITRE ATT&CK T1070, T1562.001). Correlate with Microsoft-Windows-Windows Defender/Operational events 1116/1117.
>

# purpose

Stores per-detection records used by the Windows Security Protection history view. Microsoft Q&A answers note that clearing the Defender event log does not clear Protection history; the DetectionHistory folder must be deleted (from Safe Mode, as access is denied in normal mode) to clear it. Items in the scan history folder are removed after the number of days set by `PurgeItemsAfterDelay` (`Software\Policies\Microsoft\Windows Defender\Scan`); 0 keeps them forever.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
