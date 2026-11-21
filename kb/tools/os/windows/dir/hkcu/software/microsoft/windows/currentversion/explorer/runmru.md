---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - RunMRU
  - Run dialog history
url:
  - https://learn.microsoft.com/answers/a/12880989
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
---

**fullpath**:HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU

# description

RunMRU is the per-user registry key that stores the most-recently-used command history of the Explorer Run dialog (Win+R). Learn coverage is limited to Microsoft Q&A, which lists RunMRU and `TypedPaths` among the sources of Run dialog history and notes that on Windows 11 entries may also come from IE/file URI history.

## simple description

> ### 2026-11-21 Claude said
> When a user types a command into the Win+R Run box, Explorer saves it in this key so it appears in the drop-down next time. Values are named with letters (a, b, c...) holding the command text, usually ending in `\1`, and an `MRUList` value records the order, most recent first. It is per user, stored in that user's NTUSER.DAT. Clearing it removes the visible history.
>
> **SOC NOTE**: RunMRU is a key execution artifact: it shows commands a user (or an attacker with interactive/RDP access, or a victim of "ClickFix"/fake CAPTCHA lures) typed in Win+R, such as `powershell -w hidden ...` or `mshta http://...` (MITRE ATT&CK T1204.004 Malicious Copy and Paste, T1059). Order via `MRUList` plus the key's last-write time dates the most recent entry. An empty key on an active account may indicate anti-forensic clearing.
>

# purpose

Stores Run dialog command history for the current user. Clearing RunMRU (and `TypedPaths`) clears classic Run history, but Q&A notes that file path URIs shown in the Run dialog on Windows 11 can come from IE history instead.

# hive

| property | value |
| --- | --- |
| hive | HKEY_CURRENT_USER |
| scope | per-user |
| backing file | `Ntuser.dat` |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU"` | List the key's values. |
| `reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths"` | List typed Explorer address-bar paths (related history). |
