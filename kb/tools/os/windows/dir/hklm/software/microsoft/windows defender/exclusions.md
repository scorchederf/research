---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - defender
  - exclusions
aliases:
  - Windows Defender Exclusions
  - Microsoft Defender Antivirus exclusions
url:
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-exclusions-overview
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-exclusions-configure
  - https://learn.microsoft.com/defender-endpoint/switch-to-mde-phase-2
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-defender
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions

# description

Registry location of Microsoft Defender Antivirus custom exclusions configured locally (Windows Security, `Add-MpPreference`, WMI `MSFT_MpPreference`). Group Policy and MDM exclusions are written to the parallel policy key `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Exclusions`.

## simple description

> ### 2026-11-21 Claude said
> This key stores the list of files, folders, file extensions and processes that Microsoft Defender Antivirus is told to skip when scanning. Admins add exclusions to fix performance or compatibility problems. Each exclusion is a hole in protection. The key is normally protected so only SYSTEM/Defender can change it, especially with Tamper Protection on.
>
> **SOC NOTE**: Attackers add exclusions (e.g. `Add-MpPreference -ExclusionPath C:\Users\Public`) to hide payloads - MITRE T1562.001 Impair Defenses. Defender logs configuration changes as Event ID 5007 in Microsoft-Windows-Windows Defender/Operational; review new `Paths`, `Processes` and `Extensions` values, especially broad paths, temp folders or name-only process exclusions.
>

# purpose

Holds Microsoft Defender Antivirus custom exclusions. Learn describes file and folder (path) exclusions, file extension exclusions, process exclusions (files opened by a process are skipped; the process itself is not excluded) and contextual exclusions. Built-in OS exclusions are delivered via security intelligence updates and don't appear in the standard exclusion lists. Tamper protection protects exclusions only when certain conditions are met.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SOFTWARE` |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# subkeys

| subkey | description |
| --- | --- |
| `Paths` | File and folder exclusions (`ExclusionPath`): a specific file or everything in a folder. |
| `Extensions` | File extension exclusions (`ExclusionExtension`), applied anywhere on the device. |
| `Processes` | Process exclusions (`ExclusionProcess`): files opened by the listed processes are skipped. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions" /s` | List all exclusion subkeys and values. |
| `Add-MpPreference -ExclusionExtension ".test"` | Adds a file extension exclusion. |
| `Add-MpPreference -ExclusionProcess "c:\internal\test.exe"` | Adds a process exclusion. |
| `regedit.exe /s c:\temp\MDAV_Exclusion.reg` | Imports an exported exclusions key (policy key example from the migration guide). |
