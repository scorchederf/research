---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - hkcu
  - forensics
aliases:
  - TypedPaths
url:
  - https://learn.microsoft.com/answers/a/12880989
---

**fullpath**:HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths

# description

`TypedPaths` is a per-user Explorer registry key that Microsoft Q&A lists, next to `RunMRU`, as one of the history sources checked when clearing Run dialog and Explorer path history. Learn has no reference page for the key itself.

## simple description

> ### 2026-11-21 Claude said
> This key stores the paths a user typed into the File Explorer address bar, for example `C:\Users\Bob\Desktop` or `\\server\share`. Windows keeps the most recent entries (usually up to 25) as values `url1`, `url2`, and so on, with `url1` the newest. Explorer uses them for the address bar drop-down. Each user has their own copy in their `NTUSER.DAT`.
>
> **SOC NOTE**: Strong user-activity evidence: shows folders, UNC shares and admin shares (`\\host\C$`) a user browsed by hand, which helps with discovery (T1083, T1135) and lateral movement timelines. The key LastWrite time dates the newest entry. Empty or recently cleared keys may point to anti-forensics (T1070). Parse it offline from `NTUSER.DAT` with tools such as RegRipper or Registry Explorer.
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKCU |
| scope | per-user |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths"` | List the key's values. |
