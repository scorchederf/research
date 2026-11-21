---
created: 2026-11-21
fullpath: 'c:\windows\system32\wlrmdr.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lolbin
aliases:
  - "wlrmdr.exe"
  - "Windows Logon Reminder"
url:
  - https://learn.microsoft.com/windows/win32/shell/how-to-exclude-items-from-taskbar-pinning-and-recent-frequent-lists
---

**fullpath**:c:\windows\system32\wlrmdr.exe

# description

`wlrmdr.exe` (Windows Logon Reminder) is a Windows system binary. Learn only lists it among programs that are not pinnable to the taskbar and are excluded from the most-frequently-used list.

## simple description

> ### 2026-11-21 Claude said
> wlrmdr.exe is the Windows Logon Reminder, which shows balloon/toast reminders such as password-expiry or credential notices to the logged-on user.
> It is launched by Windows itself, normally briefly and without user interaction.
> Most users never run it directly.
>
> **SOC NOTE**: LOLBAS entry: `wlrmdr.exe -s 3600 -f 0 -t _ -m _ -a 11 -u <exe>` executes an arbitrary program (T1218 System Binary Proxy Execution). Alert on wlrmdr with `-u` or spawning non-Windows children.
>

# purpose

Windows logon reminder process; Learn documents only that Wlrmdr.exe is automatically excluded from taskbar pinning and the MFU list (values under `HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\FileAssociation\AddRemoveApps` / `HostApps`).

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
