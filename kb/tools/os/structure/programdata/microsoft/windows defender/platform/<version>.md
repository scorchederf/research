---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows Defender\Platform\<version>'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - defender
aliases:
  - <antimalware platform version>
  - Defender Platform folder
url:
  - https://learn.microsoft.com/defender-endpoint/command-line-arguments-microsoft-defender-antivirus
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-updates
  - https://learn.microsoft.com/defender-endpoint/enable-update-mdav-to-latest-ws
---

**fullpath**:C:\ProgramData\Microsoft\Windows Defender\Platform\<version>

# description

Versioned folder holding the current Microsoft Defender Antivirus antimalware platform binaries, delivered through platform updates (Windows Update, WSUS, SUP, Update Catalog KB4052623). The latest MpCmdRun.exe is always located here when available; otherwise the in-box copy in `C:\Program Files\Windows Defender` is used.

## simple description

> ### 2026-11-21 Claude said
> When Microsoft Defender Antivirus updates its platform (monthly), it installs the new binaries into a folder named after the version, e.g. `4.18.25070.5-0`. The Defender service (MsMpEng.exe), MpCmdRun.exe, NisSrv.exe, MpDefenderCoreService.exe and supporting DLLs then run from here instead of Program Files. Several version folders can exist side by side; the highest is normally active. Only SYSTEM/TrustedInstaller should write here.
>
> **SOC NOTE**: Attackers abuse this location to sideload DLLs or copy MpCmdRun.exe elsewhere for downloads (`-DownloadFile`, LOLBAS, T1105), and tamper tools may try to create fake higher-version folders or symlinks to hijack the platform path (T1562.001 Impair Defenses). Alert on non-SYSTEM writes, unsigned files, or a version folder that doesn't match genuine Microsoft releases; also review MpCmdRun usage such as `-RemoveDefinitions -All`. Defender's own logs live in `C:\ProgramData\Microsoft\Windows Defender\Support` and the Microsoft-Windows-Windows Defender/Operational event log.
>

# purpose

Holds the latest antimalware platform version of Microsoft Defender Antivirus, including MpCmdRun.exe. Microsoft recommends running MpCmdRun from `%ProgramData%\Microsoft\Windows Defender\Platform\<antimalware platform version>` and provides an enhanced `cd` command that changes to the newest version folder, falling back to `%ProgramFiles%\Windows Defender`. In-box platform versions per Windows 10 release range from `4.10.14393.3683` (1607) to `4.18.1909.6` (2004).

# common files found

- MpCmdRun.exe - Microsoft Defender Antivirus command-line tool (scans, signature updates, `-WdEnable`, `-Restore`, `-CheckExclusion`, `-ValidateMapsConnection`).
