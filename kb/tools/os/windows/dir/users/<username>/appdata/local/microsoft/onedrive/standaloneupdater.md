---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\OneDrive\StandaloneUpdater'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - onedrive
aliases:
  - StandaloneUpdater
  - OneDriveStandaloneUpdater
url: []
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\OneDrive\StandaloneUpdater

# description

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> This folder belongs to the per-user OneDrive sync app and is used by its standalone updater, which keeps OneDrive up to date independently of Windows Update. It typically holds `OneDriveStandaloneUpdater.exe` related files, logs and downloaded installers. A scheduled task named `OneDrive Standalone Update Task-<SID>` runs the updater periodically.
>
> **SOC NOTE**: Being user-writable and launched by a scheduled task, OneDrive update components have been abused for DLL sideloading/hijacking (MITRE ATT&CK T1574.001/.002) and persistence. Check for unsigned DLLs or executables here and for tampering with the `OneDrive Standalone Update Task`.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_
