---
created: 2026-11-21
fullpath: 'c:\windows\system32\shell32.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - dll
  - shell
aliases:
  - 'shell32.dll'
  - 'Shell32.dll'
  - 'Windows Shell DLL'
url:
  - https://learn.microsoft.com/windows/win32/shell/versions
  - https://learn.microsoft.com/windows/win32/shell/shell
  - https://learn.microsoft.com/windows/win32/api/shellapi/nf-shellapi-shell_notifyicona
---

**fullpath**: c:\windows\system32\shell32.dll

# description

Shell32.dll is one of the two DLLs (with Shlwapi.dll) that contain almost all of the Windows Shell programming elements. Each Shell API documents a minimum Shell32.dll version; since Windows XP it ships only with Windows itself. It implements Shell objects and functions such as the `Shell` automation object, `Shell_NotifyIcon` and `Shell_MergeMenus` (import library Shell32.lib).

## simple description

> ### 2026-11-21 Claude said
> shell32.dll is the core library behind the Windows user interface: File Explorer, the desktop, file icons, context menus, the Run dialog and many common dialogs use it. Programs call into it to open files with their default app (ShellExecute), show tray icons or browse folders. It is a normal, signed Windows system file loaded by almost every GUI process. It also contains many of the classic Windows icons.
>
> **SOC NOTE**: Legitimate file, but its exports are abused for proxy execution: `rundll32.exe shell32.dll,ShellExec_RunDLL <cmd>` and `rundll32 shell32.dll,Control_RunDLL <file.cpl>` launch payloads (MITRE T1218.011 Rundll32, T1218.002 Control Panel). A shell32.dll outside System32/SysWOW64 or unsigned indicates DLL search-order hijacking/masquerading (T1574.001, T1036.005). Hunt for rundll32 command lines referencing shell32 with ShellExec_RunDLL.
>

# purpose

Provides the Shell API: Shell objects (for example `Shell`, `IShellDispatch3`), notification-area icons, menus and image index caching used by Explorer and applications.

# versions

| version | distribution platform |
| --- | --- |
| 4.0 | Windows 95 and Windows NT 4.0 |
| 4.71 | Internet Explorer 4.0 |
| 4.72 | Internet Explorer 4.01 and Windows 98 |
| 5.0 | Windows 2000 and Windows Me |
| 6.0 | Windows XP |
| 6.0.1 | Windows Vista |
| 6.1 | Windows 7 |
