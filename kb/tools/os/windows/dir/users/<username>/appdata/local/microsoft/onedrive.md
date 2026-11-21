---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\OneDrive'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - onedrive
aliases:
  - OneDrive
  - %localappdata%\Microsoft\OneDrive
url:
  - https://learn.microsoft.com/sharepoint/deploy-on-windows
  - https://learn.microsoft.com/sharepoint/per-machine-installation
  - https://learn.microsoft.com/sharepoint/install/configure-syncing-with-the-onedrive-sync-app
  - https://learn.microsoft.com/troubleshoot/sharepoint/sync/install-or-access-onedrive-error-0x80070005
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\OneDrive

# description

Per-user installation folder of the OneDrive sync app (OneDrive.exe). By default OneDriveSetup.exe installs per user under `%localappdata%\Microsoft\OneDrive`; the per-machine option (`/allusers`) installs under Program Files instead. Related: OneDriveSetup.exe, OneDrive Group Policy templates.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the OneDrive sync client program files for one user, including OneDrive.exe, versioned subfolders and the updater. It is a program folder, not where synced documents are stored (those are in the user's OneDrive folder). Because it is in the user profile, the user can write to it without admin rights. It exists for almost every Windows 10/11 user.
>
> **SOC NOTE**: User-writable program folder: classic target for DLL sideloading (T1574.002) against OneDrive.exe/OneDriveStandaloneUpdater.exe (e.g. malicious version.dll or secur32.dll), and for persistence via the OneDrive Run key. Check for unsigned DLLs, unexpected files next to OneDrive.exe and logs under `logs\` for sync activity useful in exfiltration investigations.
>

# purpose

Holds the per-user OneDrive sync app binaries and updater; `OneDrive.exe` can be started with `/configure_business:<tenantId>`.

# common files found

| file | description |
| --- | --- |
| `OneDrive.exe` | The OneDrive sync app, started per user. |
| `<BuildNumber>\adm\OneDrive.admx` / `OneDrive.adml` | Group Policy templates to copy to the central store. |
| `update\OneDriveSetup.exe` | Installer used to update OneDrive. |
