---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Defender\ConfigSecurityPolicy.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - defender
aliases:
  - ConfigSecurityPolicy.exe
  - Microsoft Security Client Policy Configuration Tool
url:
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-windows
  - https://learn.microsoft.com/defender-endpoint/standard-device-connectivity-urls-gov
---

**fullpath**:C:\Program Files\Windows Defender\ConfigSecurityPolicy.exe

# description

ConfigSecurityPolicy.exe is the Microsoft Security Client Policy Configuration Tool, a Microsoft Defender Antivirus process visible on the Task Manager Details tab (it has no service). It ships with Microsoft Defender Antivirus in `C:\Program Files\Windows Defender` and under `C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.*`, next to MsMpEng.exe, NisSrv.exe, MpCmdRun.exe and MpDefenderCoreService.exe, and is listed among the antivirus processes that require network connectivity for Defender for Endpoint.

## simple description

> ### 2026-11-21 Claude said
> ConfigSecurityPolicy.exe is a helper that applies Microsoft Defender security policy settings. It runs briefly when Defender policy is configured. It is signed by Microsoft and lives in the Defender program folder or the versioned Platform folder. End users don't interact with it.
>
> **SOC NOTE**: LOLBAS documents ConfigSecurityPolicy.exe as a download utility: passing a URL as an argument makes it fetch the file into the INetCache (MITRE ATT&CK T1105 Ingress Tool Transfer). Alert on command lines containing http/https, unexpected parent processes (cmd, powershell, Office), and copies of the binary outside the Defender folders.
>

# purpose

Microsoft Security Client policy configuration helper for Microsoft Defender Antivirus.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
