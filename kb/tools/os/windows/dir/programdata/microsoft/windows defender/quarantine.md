---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows Defender\Quarantine'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - defender
  - quarantine
aliases:
  - "Quarantine"
  - "Microsoft Defender Antivirus Quarantine folder"
url:
  - https://learn.microsoft.com/defender-endpoint/restore-quarantined-files-microsoft-defender-antivirus
  - https://learn.microsoft.com/defender-endpoint/command-line-arguments-microsoft-defender-antivirus
  - https://learn.microsoft.com/defender-endpoint/configure-remediation-microsoft-defender-antivirus
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-defender
---

**fullpath**:C:\ProgramData\Microsoft\Windows Defender\Quarantine

# description

The Quarantine folder holds files that Microsoft Defender Antivirus has quarantined as suspicious. It is part of Microsoft Defender Antivirus, which lives under `%ProgramData%\Microsoft\Windows Defender`; quarantined items are listed and restored with the Windows Security app, `MpCmdRun.exe -Restore`, or the Microsoft Defender for Endpoint portal.

## simple description

> ### 2026-11-21 Claude said
> This folder is where Microsoft Defender Antivirus keeps files it has taken away from their original location because it thinks they are malicious. Files here are stored in an encoded/encrypted form (in subfolders such as `Entries`, `ResourceData` and `Resources`) so they cannot run by accident. Administrators can list and restore items with `MpCmdRun.exe -Restore` or the Windows Security app. Only SYSTEM and administrators can normally read the folder.
>
> **SOC NOTE**: The quarantine is a goldmine during an investigation: it holds copies of the malware Defender caught, and the ResourceData blobs can be decoded (RC4 with a known static key) to recover the original sample and its original path. Attackers may delete the folder or run `MpCmdRun -Restore` to bring their tools back (T1562.001 Impair Defenses). Correlate with Defender Operational log events 1116/1117 (detection/action) and 1009 (restore).
>

# purpose

Microsoft Defender Antivirus quarantines suspicious files depending on how it is configured. The Configure removal of items from Quarantine folder policy (`DaysToRetainCleanedMalware`, registry `Software\Policies\Microsoft\Windows Defender\Quarantine`, value `PurgeItemsAfterDelay`) sets how many days items are kept before being removed; if not configured, Group Policy remediation guidance lists a default of 90 days, while the Policy CSP states items are kept indefinitely. Quarantined items can be listed with `MpCmdRun.exe -Restore -ListAll` and restored with `-Name`, `-FilePath` or `-Path`.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
