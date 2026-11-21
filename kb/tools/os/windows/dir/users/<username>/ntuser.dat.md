---
created: 2026-11-21
fullpath: 'C:\Users\<username>\NTUSER.DAT'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - registry-hive
  - user-profile
aliases:
  - "NTUSER.DAT"
  - "Ntuser.dat"
  - "NTuser.man"
url:
  - https://learn.microsoft.com/windows/win32/shell/about-user-profiles
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
  - https://learn.microsoft.com/windows/win32/shell/mandatory-user-profiles
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/customize-the-default-user-profile-by-using-copyprofile?view=windows-11
---

**fullpath**: C:\Users\<username>\NTUSER.DAT

# description

`NTUSER.DAT` is the per-user registry hive file stored in the root of each user profile folder. Windows loads it at logon and maps it to `HKEY_CURRENT_USER`; its supporting transaction log is `Ntuser.dat.log`. The Default User profile has its own `C:\Users\Default\NTUSER.DAT` used as the template for new profiles.

## simple description

> ### 2026-11-21 Claude said
> NTUSER.DAT is the file on disk that holds everything you see under HKEY_CURRENT_USER in the registry for one user. It contains that user's settings: desktop, Explorer history, recently opened files, run keys and application preferences. It is hidden and locked while the user is logged on. Each user profile under C:\Users has its own copy.
>
> **SOC NOTE**: One of the richest forensic artifacts: UserAssist, RecentDocs, RunMRU, TypedPaths, ShellBags (partly), MountPoints2 and HKCU Run/RunOnce persistence (T1547.001) all live here. Attackers modify it for persistence and COM hijacking (T1546.015). Collect it with transaction logs (.LOG1/.LOG2) and parse with tools like Registry Explorer/RegRipper. Offline loading uses reg load or regedit Load Hive.
>

# purpose

Stores the user's registry-based preferences and configuration as part of the user profile. The hive is loaded at logon and mapped to `HKEY_CURRENT_USER`. Renaming `NTuser.dat` to `NTuser.man` on a profile server makes the profile a read-only mandatory profile. An offline hive (for example the Default User's) can be loaded in Registry Editor under `HKEY_USERS` with **File** > **Load Hive**, edited, then unloaded.
