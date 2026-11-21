---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - user-profile
aliases:
  - Roaming
  - "%APPDATA%"
  - FOLDERID_RoamingAppData
  - CSIDL_APPDATA
  - Application Data
url:
  - https://learn.microsoft.com/windows/win32/shell/knownfolderid
  - https://learn.microsoft.com/windows/deployment/usmt/usmt-recognized-environment-variables
  - https://learn.microsoft.com/windows/win32/shell/about-user-profiles
  - https://learn.microsoft.com/microsoft-desktop-optimization-pack/app-v/appv-application-publishing-and-client-interaction
---

**fullpath**:C:\Users\<username>\AppData\Roaming

# description

The per-user Roaming AppData folder (known folder `FOLDERID_RoamingAppData`, `%APPDATA%`, CSIDL_APPDATA) serves as a common repository for application-specific data. Its legacy name and path were "Application Data" (`%USERPROFILE%\Application Data`). It is part of the user profile and roams with roaming user profiles; it is the folder App-V roams and that folder redirection can target.

## simple description

> ### 2026-11-21 Claude said
> AppData\Roaming is where applications store a user's settings and data that should follow the user between computers in a domain with roaming profiles. Browsers, Office, Teams, and many other apps keep config files here. It is hidden by default and fully writable by the user, without admin rights.
>
> **SOC NOTE**: Very common malware drop and persistence location (MITRE ATT&CK T1547.001 via `Microsoft\Windows\Start Menu\Programs\Startup`, T1074 Data Staged). Executables running from `%APPDATA%` are suspicious. High forensic value: browser profiles, PowerShell PSReadLine `ConsoleHost_history.txt`, Recent items/Jump Lists (`Microsoft\Windows\Recent`) and credential stores (T1555) live here.
>

# purpose

Per-user (PERUSER folder type) storage for application data that roams with the profile. Default path `%APPDATA%` (`%USERPROFILE%\AppData\Roaming`). App-V stores user catalog files under `%appdata%\Microsoft\AppV\Client\Catalog`.

# common files found

| path | description |
| --- | --- |
| `Microsoft\Windows\Cookies` | Common repository for Internet cookies (CSIDL_COOKIES). |
| `Microsoft\AppV\Client\Catalog` | App-V user catalog files. |
