---
created: 2026-11-21
fullpath: 'C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_1.11.2521.0_x64__8wekyb3d8bbwe\AppInstaller.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - msix
  - app-installer
aliases:
  - "AppInstaller.exe"
  - "App Installer"
  - "Microsoft Desktop App Installer"
url:
  - https://learn.microsoft.com/windows/msix/app-installer/install-update-app-installer
  - https://learn.microsoft.com/windows/msix/app-installer/app-installer-root
  - https://learn.microsoft.com/windows/msix/app-installer/app-installer-file-overview
  - https://learn.microsoft.com/windows/msix/app-installer/troubleshoot-appinstaller-issues
  - https://learn.microsoft.com/windows/msix/app-installer/app-installer-authentication-manager--overview
---

**fullpath**:C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_1.11.2521.0_x64__8wekyb3d8bbwe\AppInstaller.exe

# description

`AppInstaller.exe` is the main executable of App Installer (package `Microsoft.DesktopAppInstaller`), shipped with Windows 10 1803+ and Windows 11 and updated through the Microsoft Store. It installs MSIX/MSIXBundle packages and `.appinstaller` files by double-click and is also the package that delivers winget.

## simple description

> ### 2026-11-21 Claude said
> AppInstaller.exe is the Windows app that opens when you double-click an .msix or .appinstaller file and offers an 'Install' button.
> It lets users install packaged apps without PowerShell.
> The version in the folder name (1.11.2521.0) is an older release; the app updates itself from the Store.
>
> **SOC NOTE**: ms-appinstaller: protocol was abused for malware delivery (T1204 / T1553 via signed MSIX, e.g. Storm-0569/1113) and is disabled by default since December 2023. Review AppxDeployment-Server logs and DiagOutputDir for unexpected package installs.
>

# purpose

Installs MSIX packages, optional packages and related sets from local files, the web, or network shares (https, http, smb). Logs are in Event Viewer under `Microsoft > Windows > AppxDeployment-Server` and in `%LocalAppData%\Packages\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\LocalState\DiagOutputDir`. The `ms-appinstaller` protocol is controlled by the EnableMSAppInstallerProtocol policy.

# typical use cases

| usage | description |
| --- | --- |
| `(Get-AppxPackage Microsoft.DesktopAppInstaller).Version` | Shows the installed App Installer version. |
| `winget upgrade Microsoft.AppInstaller` | Updates App Installer with winget. |
| `ms-appinstaller:?source=https://website.com/app.msix&msixauth=aad` | Installs from a URI, requesting Entra ID authentication (protocol must be enabled by policy). |

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
