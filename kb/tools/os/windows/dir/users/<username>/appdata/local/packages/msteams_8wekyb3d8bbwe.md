---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Packages\MSTeams_8wekyb3d8bbwe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - teams
  - msix
  - appdata
aliases:
  - 'MSTeams_8wekyb3d8bbwe'
  - 'New Teams package data folder'
url:
  - https://learn.microsoft.com/microsoftteams/teams-client-vdi-requirements-deploy
  - https://learn.microsoft.com/troubleshoot/microsoftteams/teams-administration/clear-teams-cache
  - https://learn.microsoft.com/fslogix/how-to-configure-odfc-containers
---

**fullpath**: C:\Users\<username>\AppData\Local\Packages\MSTeams_8wekyb3d8bbwe

# description

Per-user package data folder of the new Microsoft Teams client (MSIX package `MSTeams_8wekyb3d8bbwe`). It contains code (JavaScript bundles), code cache, browser caches, user-data databases (such as conversations) and web storage; the app itself installs under `C:\Program Files\WindowsApps\MSTeams_[version]_[arch]__8wekyb3d8bbwe`. VDI/FSLogix profile solutions must roam it (FSLogix `IncludeTeams`).

## simple description

> ### 2026-11-21 Claude said
> This is where the new Teams app stores everything for one user: settings, caches, logs and local databases. Clearing the cache means deleting LocalCache\Microsoft\MSTeams or resetting the app. It is created when the user first runs new Teams and is removed if the app is uninstalled.
>
> **SOC NOTE**: Forensic value: Teams logs (LocalCache\Microsoft\MSTeams\Logs) and IndexedDB/LevelDB stores can reveal chats, meetings, file shares and sign-in accounts. Teams has been abused for phishing/vishing and DLL sideloading; check for unexpected DLLs or modified files in these folders and recent tma_addin_msi.txt install logs.
>

# purpose

Holds user and app data for the new Teams client: settings, caches, databases and logs.

# common files found

| file | description |
| --- | --- |
| `AC\` | Package folder that must exist as a directory and roam with the profile. |
| `AppData\` | Package folder that must roam. |
| `LocalCache\` | Local cache; `LocalCache\Microsoft\MSTeams` holds the Teams cache that is deleted to clear it. |
| `LocalCache\Microsoft\MSTeams\Logs\tma_addin_msi.txt` | Installation log for the Teams Meeting add-in MSI. |
| `LocalState\` | Package local state folder. |
| `RoamingState\` | Package roaming state folder. |
| `Settings\settings.dat` | Teams user settings and configuration. |
| `SystemAppData\` | Package system app data folder. |
| `TempState\` | Package temporary state folder. |
