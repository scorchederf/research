---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - user-profile
aliases:
  - AppData\Local
  - %LOCALAPPDATA%
  - local_app_data
url:
  - https://learn.microsoft.com/deployedge/edge-learnmore-create-user-directory-vars
  - https://learn.microsoft.com/windows/win32/shell/about-user-profiles
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/performance-issues-custom-default-user-profile
  - https://learn.microsoft.com/microsoft-desktop-optimization-pack/app-v/appv-application-publishing-and-client-interaction
  - https://learn.microsoft.com/microsoftteams/vdi-2
---

**fullpath**:C:\Users\<username>\AppData\Local

# description

AppData\Local (`%LOCALAPPDATA%`) is the per-user application data folder inside each user profile under `C:\Users\<username>`. Unlike AppData\Roaming, which can be redirected with Folder Redirection, its contents stay on the local machine.

## simple description

> ### 2026-11-21 Claude said
> AppData\Local is a hidden folder in every user profile where applications store per-user data that should stay on this one computer, such as caches, logs, temp files and local settings. It does not roam with the user between machines. Many apps (browsers, Teams, OneDrive) and per-user installers keep data or even executables here. Its Temp subfolder is the user's %TEMP% directory.
>
> **SOC NOTE**: Heavily abused because standard users can write to it: malware staging and execution from `Temp` and random subfolders, per-user persistence, DLL search-order hijacking of apps installed here (T1574.001), and credential theft from browser stores (`Google\Chrome\User Data`, `Microsoft\Edge\User Data`, T1555.003). Forensic value: browser history/caches, `Microsoft\Windows\WebCache`, thumbcache, `ConnectedDevicesPlatform` (ActivitiesCache.db) and `Microsoft\Windows\UsrClass.dat` (ShellBags). Flag executables launched from here.
>

# purpose

Stores per-user application data that does not roam: the Edge `${local_app_data}` path variable resolves to it, App-V keeps per-user copy-on-write package state here, Teams VDI stores SlimCore data here, and Windows stores the user tile image in `AppData\Local\Temp` and the WebCache database in `AppData\Local\Microsoft\Windows\WebCache`.

# common files found

- `Temp\` - user temp folder; holds `<username>.bmp` user tile images.
- `Microsoft\Windows\WebCache\` and `Microsoft\Windows\WebCacheLock.dat` - per-user web cache database.
- `Microsoft\TeamsVDI\` and `Packages\Microsoft.Teams.SlimCoreVdiHost.win-x64_8wekyb3d8bbwe\LocalCache\` - Teams VDI SlimCore data.
- `Packages\<PackageFamilyName>\` - packaged app data.
- App-V package VFS copy-on-write locations.
