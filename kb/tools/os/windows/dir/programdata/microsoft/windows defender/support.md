---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows Defender\Support'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - defender
  - antivirus
  - logs
aliases:
  - Windows Defender Support
  - Defender Support folder
url:
  - https://learn.microsoft.com/defender-endpoint/command-line-arguments-microsoft-defender-antivirus
  - https://learn.microsoft.com/defender-endpoint/collect-diagnostic-data
---

**fullpath**:C:\ProgramData\Microsoft\Windows Defender\Support

# description

Microsoft Defender Antivirus support/diagnostics folder. `MpCmdRun.exe -GetFiles` saves the compressed diagnostic package here as `MpSupportFiles.cab`, and `MpCmdRun.exe -Trace` writes trace files here.

## simple description

> ### 2026-11-21 Claude said
> This folder holds Microsoft Defender Antivirus diagnostic logs and support packages. You'll typically find MPLog-*.log (the detailed Defender operational log), MPDetection-*.log and, after running MpCmdRun -GetFiles, MpSupportFiles.cab. Microsoft support uses these to troubleshoot Defender.
>
> **SOC NOTE**: MPLog files are an excellent forensic artifact: they record detections, scans, exclusions, process image paths seen by real-time protection and SDN queries, often surviving after event logs are cleared. Attackers tampering with Defender (T1562.001) may leave traces here; check for deleted logs and for MpCmdRun usage.
>

# purpose

Default output location for Defender Antivirus diagnostic data. `MpCmdRun.exe -GetFiles` creates `MpSupportFiles.cab` here (optionally copied elsewhere with `-SupportLogLocation` or the *Define the directory path to copy support log files* policy). `MpCmdRun.exe -Trace` stores results as `MPTrace-<YYYMMDD>-<UTC HHMMSS>-<GUID>.bin`.

# common files found

| file | description |
| --- | --- |
| `MpSupportFiles.cab` | Compressed Defender Antivirus diagnostic log package created by `MpCmdRun.exe -GetFiles`. |
| `MPTrace-<YYYMMDD>-<UTC HHMMSS>-<GUID>.bin` | Microsoft Antimalware Service trace created by `MpCmdRun.exe -Trace`. |
