---
created: 2026-11-21
fullpath: 'C:\Users\Default'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - profile
aliases:
  - Default
  - Default user profile
  - Default User
url:
  - https://learn.microsoft.com/windows/win32/shell/profiles-directory
  - https://learn.microsoft.com/windows/win32/api/userenv/nf-userenv-getdefaultuserprofiledirectorya
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/customize-the-default-user-profile-by-using-copyprofile?view=windows-11
  - https://learn.microsoft.com/troubleshoot/windows-server/user-profiles-and-logon/desktop-location-unavailable
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/performance-issues-custom-default-user-profile
---

**fullpath**:C:\Users\Default

# description

`C:\Users\Default` is the default user profile: profile information that applies to the default user, and the template Windows uses to build a profile for each new user. Its path is returned by `GetDefaultUserProfileDirectory` (Windows XP used `C:\Documents and Settings\Default User`). It can be customized with the `CopyProfile` unattend setting during Sysprep.

## simple description

> ### 2026-11-21 Claude said
> This hidden folder is the template for new user accounts. When someone signs in to a computer for the first time, Windows copies this folder (including its `NTUSER.DAT` registry hive) to create their personal profile. Changes made here affect every user created afterwards. Nobody normally signs in as "Default".
>
> **SOC NOTE**: Writing to this folder or loading and editing `C:\Users\Default\NTUSER.DAT` is a persistence method: a Startup-folder shortcut or Run key planted here is copied to every new profile (T1547.001). Files with recent modification times in this folder, or `reg load` of its `NTUSER.DAT`, are unusual and worth checking. Compare it against a clean image during investigations.
>

# purpose

Windows uses the default user profile as a template to assign a profile to each new user, so customizing it configures settings for all accounts created later. New user profiles are derived from `C:\users\default\` during first-time logons.

# common files found

| file | description |
| --- | --- |
| `NTUSER.DAT` | Default user registry hive; can be loaded under `HKEY_USERS` with Registry Editor's Load Hive to edit and then unloaded. A Read-only flag on it causes profile load failures. |
| `AppData\Local\Microsoft\Windows\WebCache` | Should not exist in a custom default profile; including the cache database causes poor performance and is not supported. |
| `AppData\Local\Microsoft\Windows\WebCacheLock.dat` | Should be deleted from a custom default profile for the same reason. |
