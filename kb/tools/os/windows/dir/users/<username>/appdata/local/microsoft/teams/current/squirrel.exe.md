---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Squirrel.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - teams
aliases:
  - Squirrel.exe
  - squirrel.exe
url:
  - https://learn.microsoft.com/troubleshoot/microsoftteams/teams-administration/include-exclude-teams-from-antivirus-dlp
  - https://learn.microsoft.com/microsoftteams/teams-client-vdi-requirements-deploy
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Squirrel.exe

# description

`squirrel.exe` is a process of the classic Microsoft Teams desktop app, installed per-user under `%localappdata%\Microsoft\Teams` by the classic Teams .EXE installer (auto-update enabled). Learn lists it, alongside `teams.exe` and `update.exe`, among the processes to exclude from antivirus/DLP scanning to prevent classic Teams start-up issues.

## simple description

> ### 2026-11-21 Claude said
> Squirrel.exe is part of the Squirrel installer/update framework used by Electron apps like classic Microsoft Teams. It handles installing, updating and creating shortcuts for the per-user Teams install in AppData. Classic Teams has been retired in favor of new Teams (MSIX), so this file is mainly found on older or not-yet-cleaned machines.
>
> **SOC NOTE**: Squirrel.exe (and Update.exe) are known LOLBins: `--download`, `--update`, and `--processStart`/`--processStartAndWait` can fetch and execute arbitrary payloads from a user-writable path (MITRE T1218, T1105). Alert on Squirrel/Update.exe with URLs or unusual `--processStart` targets, and on copies outside the Teams folder.
>

# purpose

Part of classic Teams in the user's AppData install location; the classic per-user .EXE install auto-updates.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_
