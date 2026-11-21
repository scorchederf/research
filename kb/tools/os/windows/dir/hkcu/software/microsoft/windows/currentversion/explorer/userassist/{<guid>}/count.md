---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{<GUID>}\Count'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - forensics
aliases:
  - UserAssist
  - UserAssist Count
url:
---

**fullpath**:HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{<GUID>}\Count

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> UserAssist is a per-user registry key where Windows Explorer records programs and shortcuts the user launched through the GUI (Start menu, desktop, Explorer). Each GUID subkey tracks a category, such as executables or shortcut files, and its Count subkey holds one value per item. Value names are ROT13-encoded paths and the binary data holds a run count, focus time and last-run timestamp.
>
> **SOC NOTE**: UserAssist is a key evidence-of-execution artifact (MITRE ATT&CK T1204 user execution context): it shows what a specific user ran interactively and when, even after the binary is deleted. Decode with RegRipper, Registry Explorer or similar tools; wiping or disabling it (Start_TrackProgs = 0) is an anti-forensics indicator (T1070). It doesn't log command-line executions.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKCU |
| scope | per-user |
| backing file | Ntuser.dat |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{<GUID>}\Count"` | List the key's values. |
