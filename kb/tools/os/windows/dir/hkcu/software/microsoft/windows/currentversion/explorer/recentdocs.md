---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - explorer
  - mru
aliases:
  - RecentDocs
url:
  - https://learn.microsoft.com/windows/win32/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-windowsexplorer
---

**fullpath**:HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> RecentDocs is a per-user registry key where File Explorer keeps a most-recently-used (MRU) list of files and folders the user opened. It has one subkey per file extension (e.g., `.docx`, `.pdf`) plus a `Folder` subkey, each with numbered binary values and an `MRUListEx` value giving the order. It is updated by the shell when documents are opened through Explorer or common file dialogs (`SHAddToRecentDocs`). It feeds the Recent Items list.
>
> **SOC NOTE**: Strong evidence of file and folder access (MITRE ATT&CK T1005 / T1083 context): shows names of documents a user opened, even after the files are deleted, and the key's LastWrite time with `MRUListEx` order dates the most recent item per extension. Parse from `NTUSER.DAT` with RegRipper/Registry Explorer. Clearing it is anti-forensics (T1070); the "Do not keep history of recently opened documents" policy (NoRecentDocsHistory) disables it.
>
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKCU |
| scope | per-user |
| backing file | `Ntuser.dat` |

# values

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs"` | List the key's values. |
