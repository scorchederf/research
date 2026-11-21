---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Packages\Microsoft.Windows.Search_cw5n1h2txyewy'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - search
  - appx
aliases:
  - Microsoft.Windows.Search_cw5n1h2txyewy
  - Microsoft.Windows.Cortana_cw5n1h2txyewy
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/shell-experience/fix-problems-in-windows-search
---

**fullpath**:C:\Users\<username>\AppData\Local\Packages\Microsoft.Windows.Search_cw5n1h2txyewy

# description

This is the per-user AppData folder for the Microsoft.Windows.Search package on Windows 10 (in some earlier versions named Microsoft.Windows.Cortana_cw5n1h2txyewy; on Windows 11 the equivalent is MicrosoftWindows.Client.CBS_cw5n1h2txyewy). The package itself is installed under C:\Windows\SystemApps\Microsoft.Windows.Search_cw5n1h2txyewy.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the per-user data for the Windows taskbar/Start search experience. It stores settings, caches, and local state for the search app of each user. If it's deleted, Windows rebuilds it the next time search runs.
>
> **SOC NOTE**: Forensically, its LocalState/AppCache files and related databases can contain recent search terms, app suggestions, and history that reveal what a user looked for or launched. Unexpected executables in this folder are suspicious, since it should hold only app data.
>

# purpose

Per-user application data for Windows Search. Learn's "Fix problems in Windows Search" (Solution 6) regenerates it: delete `%USERPROFILE%\AppData\Local\Packages\Microsoft.Windows.Search_cw5n1h2txyewy`, delete `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search`, re-register with `Add-AppxPackage -Path "C:\Windows\SystemApps\Microsoft.Windows.Search_cw5n1h2txyewy\Appxmanifest.xml" -DisableDevelopmentMode -Register`, and restart.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_
