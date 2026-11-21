---
created: 2026-11-21
fullpath: 'C:\Users'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - user-profile
aliases:
  - Users
  - Profiles directory
  - Documents and Settings
  - ProfilesDirectory
url:
  - https://learn.microsoft.com/windows/win32/shell/profiles-directory
  - https://learn.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-shell-setup-folderlocations-profilesdirectory
  - https://learn.microsoft.com/windows/win32/api/userenv/nf-userenv-getdefaultuserprofiledirectoryw
  - https://learn.microsoft.com/troubleshoot/windows-client/shell-experience/apps-not-start-without-user-profile-programdata
  - https://learn.microsoft.com/windows/win32/shell/about-user-profiles
---

**fullpath**:C:\Users

# description

`C:\Users` is the profiles directory where Windows stores user profile information; it was named "Documents and Settings" in Windows XP. Its path is returned by `GetProfilesDirectory` and can be changed at deployment with the unattend `ProfilesDirectory` setting, which Microsoft does not recommend outside test environments.

## simple description

> ### 2026-11-21 Claude said
> C:\Users holds one folder per user who has logged on to the machine, plus Default (the template for new profiles) and Public. Each profile contains the user's Desktop, Documents, Downloads, AppData and the NTUSER.DAT registry hive. A new folder appears the first time an account logs on.
>
> **SOC NOTE**: Profile folder names and creation times show which accounts have logged on interactively and when (useful for spotting new or attacker-created accounts). Per-user artifacts here (NTUSER.DAT, UsrClass.dat, AppData, Recent, PowerShell history) are central to timeline analysis. `C:\Users\Public` is a frequent malware staging location since all users can write to it.
>

# purpose

Holds per-user profiles. A profile consists of a registry hive (NTuser.dat, loaded as HKEY_CURRENT_USER at logon) and a set of profile folders. Moving the Users directory from its default location breaks Microsoft Store apps.

# common files found

| folder | description |
| --- | --- |
| `Default` | Profile information that applies to the default user (template for new profiles). |
| `<User>` | Profile information for the specified user; each user has their own subdirectory. |
| `All Users` | Kept for backward compatibility; ProgramData holds program information for all users in Windows Vista and later. |
| `<User>\NTuser.dat` | The user's registry hive, mapped to HKEY_CURRENT_USER at logon. |
