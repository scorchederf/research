---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\OneDrive\logs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - onedrive
  - logs
aliases:
  - OneDrive logs
url: []
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\OneDrive\logs

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> This per-user folder holds the diagnostic logs of the OneDrive sync app (OneDrive.exe). There are subfolders per account type such as `Business1` and `Personal`, plus `Common`. The main files (`SyncDiagnostics.log`, `*.odl`, `*.odlgz`) are obfuscated binary logs meant for Microsoft support.
>
> **SOC NOTE**: Decoded ODL logs (e.g. with open-source ODL parsers) reveal file sync, upload and delete activity, account names and folder paths, useful for data exfiltration investigations (T1567.002) and user activity timelines. SyncDiagnostics.log shows sync state and quotas.
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
