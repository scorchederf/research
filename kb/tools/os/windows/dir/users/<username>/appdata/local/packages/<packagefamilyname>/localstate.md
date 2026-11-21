---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Packages\<PackageFamilyName>\LocalState'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - uwp
  - msix
  - appdata
aliases:
  - 'LocalState'
  - 'ApplicationData.LocalFolder'
  - 'local app data store'
url:
  - https://learn.microsoft.com/uwp/api/windows.storage.applicationdata.localfolder?view=winrt-28000
  - https://learn.microsoft.com/windows/apps/package-and-deploy/msix-windows10-windows11
  - https://learn.microsoft.com/windows/powertoys/command-palette/microsoft-commandpalette-extensions-toolkit/utilities_basesettingspath
  - https://learn.microsoft.com/windows/apps/develop/data/store-and-retrieve-app-data
---

**fullpath**: C:\Users\<username>\AppData\Local\Packages\<PackageFamilyName>\LocalState

# description

Per-user, per-package local app data folder of a packaged (UWP/MSIX) app, exposed to code as `ApplicationData.Current.LocalFolder` and the `ms-appdata:///local/` URI. Packaged apps get it as their redirected local app data path (`Packages/{pfn}/LocalState`). Data here is deleted when the app is uninstalled unless MSIX Persistent Identity (Windows 11) is used.

## simple description

> ### 2026-11-21 Claude said
> Every Store/MSIX app gets its own private folder under AppData\Local\Packages, named after its package family name, and LocalState is where the app saves its local files and databases. Only that app (and the user/admins) normally use it. Examples: Teams, Windows Terminal settings.json, Sticky Notes database. It disappears when the app is removed.
>
> **SOC NOTE**: Rich forensic source: app databases (e.g., Sticky Notes plum.sqlite, Your Phone, Teams, Terminal settings) live here. Because packaged apps write here without admin rights, malware dropped as MSIX/AppX packages (T1204, sideloaded AppX) also stores payloads/config here. Check Indexed subfolder and timestamps when profiling user activity.
>

# purpose

Root folder of the local app data store for a packaged app, used for data preserved between sessions that shouldn't roam. Content can be backed up to the cloud on devices that support app data backup; a folder named `Indexed` under it is indexed for in-app search.

# common files found

| file | description |
| --- | --- |
| `Indexed\` | Optional folder; Windows indexes the content and properties of files inside it for search by the app. |
