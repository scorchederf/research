---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Windows\UsrClass.dat'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - registry-hive
  - forensics
aliases:
  - "UsrClass.dat"
  - "USRCLASS.DAT"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/user-profiles-and-logon/desktop-location-unavailable
  - https://learn.microsoft.com/windows/win32/sysinfo/hkey-classes-root-key
---

**fullpath**: C:\Users\<username>\AppData\Local\Microsoft\Windows\UsrClass.dat

# description

UsrClass.dat is the per-user classes registry hive, stored in the user profile next to (but separate from) NTUSER.DAT. It holds the user's file associations and COM registrations that appear under HKEY_CURRENT_USER\Software\Classes and are merged into HKEY_CLASSES_ROOT.

## simple description

> ### 2026-11-21 Claude said
> UsrClass.dat is the user's part of HKCR: file type associations, COM objects and shell settings that only apply to that user. Windows loads it at logon together with NTUSER.DAT. If it is read-only or has wrong permissions, the profile may fail to load. Forensic tools parse it offline.
>
> **SOC NOTE**: Key forensic artifact: ShellBags (Local Settings\Software\Microsoft\Windows\Shell\BagMRU) prove folder access, including deleted/removable/network folders. Also a persistence spot for per-user COM hijacking (T1546.015) since HKCU\Software\Classes\CLSID overrides HKLM without admin rights. Collect it with its .LOG1/.LOG2 transaction logs.
>

# purpose

Stores per-user class registrations. Typically located at C:\Users\<user_name>\AppData\Local\Microsoft\Windows. Since MS15-003 (update 3021674), Windows checks access to NTUSER.DAT and UsrClass.dat; if the file is read-only or the user lacks permissions, profile loading fails (e.g. User Profiles Service event 1542 'Windows cannot load classes registry file').
