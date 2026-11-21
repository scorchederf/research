---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - user-profiles
  - forensics
aliases:
  - ProfileList
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/user-profiles-and-logon/renaming-user-account-not-change-profile-path
  - https://learn.microsoft.com/troubleshoot/windows-server/licensing-and-activation/windows-not-genuine-error
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/registry-changes-in-x64-based-windows
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList

# description

ProfileList contains one subkey per user SID describing that account's local user profile, including the ProfileImagePath value that points at the profile folder. It is part of the Windows user profile service, and it is one of the registry keys shared between the 32-bit and 64-bit registry views on x64 Windows.

## simple description

> ### 2026-11-21 Claude said
> ProfileList maps each account's security identifier (SID) to its profile folder on disk, such as C:\Users\alice. Windows uses it at logon to find and load the right profile. Entries ending in .bak usually mean a profile was corrupted and Windows created a temporary one.
>
> **SOC NOTE**: Every user who has logged on interactively gets a SID subkey here, so it shows which accounts have used the machine, including deleted or domain accounts (MITRE ATT&CK T1087 account discovery uses it too). Unexpected new SIDs or profile paths, or tampering with ProfileImagePath to redirect a profile, are worth investigating; the key's last-write time helps build timelines.
>

# purpose

Map user SIDs to local profile locations and profile state used by the User Profile Service.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SOFTWARE |

# values

| value name | type | description |
| --- | --- | --- |
| `ProfileImagePath` | REG_EXPAND_SZ | Path of the user's profile folder (under `<User SID>`); edit it to point to a renamed profile folder. |
| `Flags` | REG_DWORD | Profile flags (for example 0x0c for S-1-5-18). |
| `State` | REG_DWORD | Profile state. |
| `RefCount` | REG_DWORD | Profile reference count. |
| `Sid` | REG_BINARY | Binary SID of the account. |

# subkeys

| subkey | description |
| --- | --- |
| `<User SID>` | One subkey per user account profile. |
| `S-1-5-18` | LocalSystem profile (%systemroot%\system32\config\systemprofile). |
| `S-1-5-19` | LocalService profile (C:\Windows\ServiceProfiles\LocalService). |
| `S-1-5-20` | NetworkService profile (C:\Windows\ServiceProfiles\NetworkService). |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"` | List the key's values and SID subkeys. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" /s /v ProfileImagePath` | Show the profile path for every SID. |
