---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Teams.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - teams
  - microsoft-365
aliases:
  - Teams.exe
  - classic Teams
url:
  - https://learn.microsoft.com/microsoftteams/teams-client-vdi-requirements-deploy
  - https://learn.microsoft.com/troubleshoot/microsoftteams/teams-administration/include-exclude-teams-from-antivirus-dlp
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Teams.exe

# description

This is the main executable of the classic Microsoft Teams desktop client installed per-user by the classic Teams .EXE installer into `%localappdata%\Microsoft\Teams` with auto update enabled. Related files are `update.exe` and `current\squirrel.exe`; the new Teams client (ms-teams.exe) installs as MSIX under `C:\Program Files\WindowsApps` instead.

## simple description

> ### 2026-11-21 Claude said
> This is the classic (Electron-based) Microsoft Teams app, installed per user under AppData so it can update itself without admin rights. It was the standard Teams client until Microsoft replaced it with the new MSIX-based Teams; classic Teams is retired. Each user who installed it has their own copy.
>
> **SOC NOTE**: User-writable install paths make it a target for DLL side-loading and binary replacement (T1574.002); Update.exe (Squirrel) is a LOLBAS that can download and run payloads (T1218). Classic Teams also stored auth tokens in plaintext cookies/LevelDB under %appdata%\Microsoft\Teams (T1528). Presence on current systems may indicate an unpatched retired client.
>

# purpose

Runs the classic Teams client. Microsoft recommends adding `C:\Users\*\AppData\Local\Microsoft\Teams\current\teams.exe`, `update.exe`, `current\squirrel.exe` and `TeamsMeetingAddin` to antivirus/DLP exclusions to prevent start issues.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_
