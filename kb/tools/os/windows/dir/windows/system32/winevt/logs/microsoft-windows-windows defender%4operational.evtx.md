---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Defender%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - defender
aliases:
  - Microsoft-Windows-Windows Defender%4Operational.evtx
  - Microsoft-Windows-Windows Defender/Operational
  - Windows Defender Operational log
url:
  - https://learn.microsoft.com/defender-endpoint/troubleshoot-microsoft-defender-antivirus
  - https://learn.microsoft.com/defender-endpoint/troubleshoot-microsoft-defender-antivirus-when-migrating
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Defender%4Operational.evtx

# description

The event log file behind the Microsoft-Windows-Windows Defender/Operational channel, where Microsoft Defender Antivirus records its events. It is viewed in Event Viewer under Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.

## simple description

> ### 2026-11-21 Claude said
> This .evtx file is the Microsoft Defender Antivirus operational log. Defender writes events here for scans, detections, remediation actions, signature updates and configuration changes. The "%4" in the file name stands for the "/" in the channel name. It is one of the most useful logs on a Windows endpoint for malware investigations.
>
> **SOC NOTE**: Key events: 1116/1117 (detection/action), 1006-1009, 5001 (real-time protection disabled), 5007 (configuration change, e.g. exclusions added), 5010/5012 (scanning disabled), 1121 (ASR block). Attackers tamper with Defender (T1562.001) or clear this log (T1070.001); 1116 entries persist evidence of tooling even when files were deleted.
>

# purpose

Stores Microsoft Defender Antivirus events, including scan start/complete/cancel (1000-1002), threat hashes (1120), attack surface reduction blocks (1121), Controlled Folder Access blocks (1127), engine failures (5008), scanning enabled/disabled (5009-5011), and configuration changes (5007, which "could be due to malware" if unexpected).
