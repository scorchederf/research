---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - forensics
  - mru
aliases:
  - "OpenSavePidlMRU"
url: []
---

**fullpath**:HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> OpenSavePidlMRU stores the most recently used files that a user opened or saved through the standard Windows Open/Save As common dialog. Entries are grouped in subkeys by file extension (plus a '*' subkey for all), each holding binary shell item IDs (PIDLs) and an MRUListEx order. It lives in the user's NTUSER.DAT.
>
> **SOC NOTE**: Strong user-activity artifact: shows files (including on removable media or network shares) a user interacted with via dialogs, useful for data-staging or exfiltration investigations (T1074, T1005). Parse with RegRipper/Registry Explorer; the key's LastWrite time dates the most recent entry per extension.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKCU |
| scope | per-user |
| backing file | Ntuser.dat |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU"` | List the key's values. |
