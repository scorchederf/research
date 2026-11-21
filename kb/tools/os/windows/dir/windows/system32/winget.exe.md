---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winget.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - package-manager
aliases:
  - "winget.exe"
  - "WinGet"
  - "Windows Package Manager"
url:
  - https://learn.microsoft.com/windows/package-manager/winget/
---

**fullpath**: C:\Windows\System32\winget.exe

# description

WinGet is the command-line client for the Windows Package Manager service, used to discover, install, upgrade, remove and configure applications on Windows 10 (1809+), Windows 11 and Windows Server 2025. It ships as part of the **App Installer** system component (Microsoft Store on desktop, Windows Update on Server 2025) and becomes available after the user's first logon registers it. A PowerShell equivalent is the Microsoft.WinGet.Client module.

## simple description

> ### 2026-11-21 Claude said
> winget is Windows' built-in "app store on the command line". With one command you can search for, install, upgrade or uninstall software from Microsoft's community repository or the Microsoft Store, and it runs each app's installer silently. It is normally reached through an App Execution Alias that points into the App Installer package under C:\Program Files\WindowsApps; a copy in System32 is unusual on desktop Windows and worth checking.
>
> **SOC NOTE**: Attackers can use winget to pull and install remote-admin or tunnelling tools (AnyDesk, ngrok, etc.) with a signed Microsoft binary (T1105 Ingress Tool Transfer, T1219 Remote Access Software); custom `winget source add` repositories or `--ignore-local-archive-malware-scan` / hash-override settings are red flags. Check DiagOutputDir logs (`winget --logs`) and process-creation events for winget command lines. Verify the signature and location of any winget.exe found in System32.
>

# purpose

Client interface to the Windows Package Manager service. Without administrator privileges, installers that need elevation trigger a UAC prompt (declining fails the install); in an elevated prompt no elevation prompts appear. Supported installer types are EXE (Silent/SilentWithProgress), ZIP, INNO, NULLSOFT, MSI, WIX, APPX, MSIX, BURN, PORTABLE and FONT. Behaviour can be customised in `settings.json`.

# typical use cases

| usage | description |
| --- | --- |
| `winget search <appname>` | Search for an application. |
| `winget install <appname>` | Install the specified application. |
| `winget show <appname>` | Display details for an application. |
| `winget list` | Display installed packages. |
| `winget upgrade <appname>` | Upgrade the specified application. |
| `winget uninstall <appname>` | Uninstall the specified application. |
| `winget source` | Add, edit, remove and update the repositories WinGet accesses. |
| `winget hash <installer>` | Generate the SHA256 hash for an installer. |
| `winget validate <manifest>` | Validate a manifest for submission to the repository. |
| `winget export` / `winget import` | Export a list of installed packages / install all packages in a file. |
| `winget pin` | Manage package pins. |
| `winget configure` | Configure the system into a desired state. |
| `winget download <appname>` | Download an application's installer. |
| `winget repair <appname>` | Repair the selected application. |
| `winget settings` / `winget features` | Open settings / show the status of experimental features. |
| `winget dscv3` | PowerShell DSC v3 resource commands. |
| `Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe` | Request WinGet registration if it is not yet available after first logon. |

# options

| option | description |
| --- | --- |
| `-v`, `--version` | Return the current version of WinGet. |
| `--info` | Detailed WinGet information including license, privacy statement and configured group policies. |
| `-?`, `--help` | Show additional help. |
| `--wait` | Prompt the user to press any key before exiting. |
| `--logs`, `--open-logs` | Open the default logs location. |
| `--verbose`, `--verbose-logs` | Enable verbose logging. |
| `--nowarn`, `--ignore-warnings` | Suppress warning outputs. |
| `--disable-interactivity` | Disable interactive prompts. |
| `--proxy` | Set a proxy for this execution. |
| `--no-proxy` | Disable use of a proxy for this execution. |
