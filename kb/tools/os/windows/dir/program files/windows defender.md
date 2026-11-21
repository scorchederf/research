---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Defender'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - defender
  - antivirus
aliases:
  - "Windows Defender"
  - "Microsoft Defender Antivirus inbox folder"
url:
  - https://learn.microsoft.com/defender-endpoint/command-line-arguments-microsoft-defender-antivirus
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-updates
---

**fullpath**:C:\Program Files\Windows Defender

# description

Installation folder of the inbox (OS-shipped) Microsoft Defender Antivirus binaries. Platform updates install newer versions to C:\ProgramData\Microsoft\Windows Defender\Platform\<antimalware platform version>, while this folder keeps the version shipped with the operating system. Related tool: MpCmdRun.exe.

## simple description

> ### 2026-11-21 Claude said
> This is where Windows ships the built-in Microsoft Defender Antivirus files, such as MpCmdRun.exe (command-line tool), MsMpEng.exe (engine service) and MpClient.dll. Newer platform versions usually run from ProgramData\Microsoft\Windows Defender\Platform, so this copy may be older. Admins use MpCmdRun.exe from here to scan, update signatures or collect diagnostics.
>
> **SOC NOTE**: MpCmdRun.exe is abused as a LOLBin (-DownloadFile, T1105) and attackers use -RemoveDefinitions -All to strip signatures (T1562.001). MsMpEng/MpClient DLL side-loading has been seen when binaries are copied elsewhere. Watch for MpCmdRun command lines and tampering with this folder.
>

# purpose

Holds the OS-shipped Defender Antivirus platform. MpCmdRun.exe is located here and in the versioned Platform folder (the latest version is always in the Platform folder if available); the folder isn't on PATH, so admins change to it before running MpCmdRun. `MpCmdRun.exe -ResetPlatform` resets platform binaries back to %ProgramFiles%\Windows Defender, i.e. the version shipped with the operating system.

# common files found

| file | description |
| --- | --- |
| `MpCmdRun.exe` | Command-line tool to run scans, manage security intelligence updates, collect diagnostics and configure Microsoft Defender Antivirus. |
