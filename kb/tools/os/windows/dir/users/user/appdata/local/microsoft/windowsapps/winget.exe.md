---
created: 2026-11-21
fullpath: 'C:\Users\user\AppData\Local\Microsoft\WindowsApps\winget.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - winget.exe
  - WinGet
  - Windows Package Manager
url:
  - https://learn.microsoft.com/windows/package-manager/winget/
---

**fullpath**:C:\Users\user\AppData\Local\Microsoft\WindowsApps\winget.exe

# description

winget.exe is the command-line client of the Windows Package Manager, delivered as part of the App Installer package on Windows 10 1809+, Windows 11 and Windows Server 2025. The copy under `%LOCALAPPDATA%\Microsoft\WindowsApps` is the per-user app execution alias; WinGet is also scriptable with the Microsoft.WinGet.Client PowerShell module.

## simple description

> ### 2026-11-21 Claude said
> WinGet is Microsoft's package manager for Windows, similar to apt on Linux: it can search for, install, upgrade, uninstall and export applications from the command line. The file in the user's WindowsApps folder is an execution alias, a small stub that launches the App Installer package. It becomes available after a user signs in for the first time. Installers it runs may still ask for elevation.
>
> **SOC NOTE**: Attackers can use winget to silently install remote-access tools or other software from public or custom sources (MITRE ATT&CK T1105, T1072), and `winget settings --enable LocalManifestFiles` with a crafted manifest can run arbitrary installers. Monitor winget command lines (install/source add/settings), new sources, and child installer processes; WinGet logs are under the App Installer package LocalState DiagOutputDir (opened via `winget --logs`).
>

# purpose

Discover, install, upgrade, remove and configure applications; it is the client interface to the Windows Package Manager service. Supported installer types: EXE, ZIP, INNO, NULLSOFT, MSI, WIX, APPX, MSIX, BURN, PORTABLE, FONT. Running in an Administrator prompt suppresses elevation prompts for installers.

# typical use cases

| usage | description |
| --- | --- |
| `winget search <appname>` | Search for a tool. |
| `winget install <appname>` | Install the application. |
| `winget --help` | List all commands. |
| `Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe` | PowerShell: request WinGet registration if it is not yet available. |

# options

| option | description |
| --- | --- |
| `install` | Installs the specified application. |
| `show` | Displays details for the specified application. |
| `source` | Adds, edits, removes, and updates the repositories accessed by WinGet. |
| `search` | Searches for an application. |
| `list` | Display installed packages. |
| `upgrade` | Upgrades the given specified application. |
| `uninstall` | Uninstalls the specified application. |
| `hash` | Generates the SHA256 hash for the installer. |
| `validate` | Validates a manifest file for submission to the repository. |
| `settings` | Open settings. |
| `features` | Shows the status of experimental features. |
| `export` | Exports a list of the installed packages. |
| `import` | Installs all the packages in a file. |
| `pin` | Manage package pins. |
| `configure` | Configures the system into a desired state. |
| `download` | Downloads the specified application's installer. |
| `repair` | Repairs the selected application. |
| `dscv3` | PowerShell DSC v3 resource commands. |
| `-v`, `--version` | Returns the current version of WinGet. |
| `--info` | Detailed information on WinGet, including license, privacy statement and configured group policies. |
| `-?`, `--help` | Shows additional help for WinGet. |
| `--wait` | Prompts the user to press any key before exiting. |
| `--logs`, `--open-logs` | Opens the default logs location. |
| `--verbose`, `--verbose-logs` | Enables verbose logging for winget. |
| `--nowarn`, `--ignore-warnings` | Suppresses warning outputs. |
| `--disable-interactivity` | Disables interactive prompts. |
| `--proxy` | Sets a proxy to use for this execution. |
| `--no-proxy` | Disables the use of proxy for this execution. |
