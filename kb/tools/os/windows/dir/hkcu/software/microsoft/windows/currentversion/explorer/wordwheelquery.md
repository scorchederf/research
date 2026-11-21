---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - windows
aliases:
  - "WordWheelQuery"
url: []
---

**fullpath**:HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> WordWheelQuery stores the search terms the user typed into the File Explorer search box. Each term is a numbered binary value (UTF-16 string) and the `MRUListEx` value records the order of use. It lives in the user's NTUSER.DAT.
>
> **SOC NOTE**: Forensic artifact showing what a user (or attacker using their session) searched for in Explorer, e.g. "password", "vpn" or project names, supporting file and directory discovery findings (MITRE ATT&CK T1083). The MRUListEx order plus key last-write time dates the most recent search. Clearing Explorer history removes it.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# hive

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# values

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery"` | List the key's values. |
