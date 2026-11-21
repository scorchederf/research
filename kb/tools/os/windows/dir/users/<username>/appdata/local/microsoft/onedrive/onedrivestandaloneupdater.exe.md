---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - onedrive
aliases:
  - OneDriveStandaloneUpdater.exe
url: []
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

## simple description

> ### 2026-11-21 Claude said
> OneDriveStandaloneUpdater.exe is the updater component of the Microsoft OneDrive sync app when installed per-user in the user's AppData. It is normally launched by a scheduled task ('OneDrive Standalone Update Task-<SID>') roughly once a day to check for and install new OneDrive versions. It downloads update metadata and installers from Microsoft servers. Per-machine installs place it under Program Files instead.
>
> **SOC NOTE**: Because it lives in a user-writable folder and runs from a scheduled task, it is a known DLL side-loading/hijack target (MITRE T1574.002) - check for unsigned DLLs placed next to it (e.g. version.dll). Verify the Microsoft signature, and inspect the scheduled task definition for modified actions (T1053.005). Normal network traffic goes to Microsoft OneDrive/oneclient endpoints.
>
> _Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_
