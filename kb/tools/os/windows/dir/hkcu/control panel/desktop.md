---
created: 2026-11-21
fullpath: 'HKCU\Control Panel\Desktop'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - hkcu
  - screensaver
  - persistence
aliases:
  - 'Desktop'
  - 'HKEY_CURRENT_USER\Control Panel\Desktop'
url:
  - https://learn.microsoft.com/windows/win32/devnotes/scrnsave-exe
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/troubleshoot-unexpected-rds-session-locks-or-disconnections
  - https://learn.microsoft.com/troubleshoot/windows-client/group-policy/group-policy-screensaver-setting-not-work
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/dpi-related-apis-and-registry-settings?view=windows-11
  - https://learn.microsoft.com/windows/win32/cimwin32prov/win32-desktop
---

**fullpath**:HKCU\Control Panel\Desktop

# description

Per-user registry key holding desktop appearance settings such as the screen saver, DPI scaling and desktop pattern. Values are written by the Display/Personalization Control Panel and the Screen Saver Settings console (`control desk.cpl,,1`), and are exposed through WMI `Win32_Desktop`. Group Policy equivalents live under `HKCU\Software\Policies\Microsoft\Windows\Control Panel\Desktop`.

## simple description

> ### 2026-11-21 Claude said
> This key stores each user's desktop look-and-feel: which screen saver runs, after how long, whether it asks for a password, DPI scaling and font metrics. It is loaded from the user's own profile, so every user has their own copy. Changing it needs no admin rights.
>
> **SOC NOTE**: `SCRNSAVE.EXE` is a known user-level persistence point (T1546.002 Event Triggered Execution: Screensaver): pointing it at a malicious .scr/.exe runs it when the screen saver starts. Also check `ScreenSaverIsSecure`/`ScreenSaveTimeOut` changes that weaken session locking. Monitor registry writes (Sysmon 13) to these values and unusual .scr files outside System32.
>

# purpose

Stores the current user's desktop settings. Screen saver locking requires three REG_SZ values here (`ScreenSaveActive`, `ScreenSaverIsSecure`, `ScreenSaveTimeOut`), which are written when configured through the Screen Saver Settings console; policy settings take precedence. Since Windows 7/Windows Server 2008 R2, `ScreenSaveTimeOut` doesn't exist by default. The key also holds DPI scaling settings set from the Display Control Panel.

# hive

| property | value |
| --- | --- |
| hive | HKCU (HKEY_CURRENT_USER) |
| scope | per-user (screen saver is a user configuration) |

# values

| value name | type | description |
| --- | --- | --- |
| `SCRNSAVE.EXE` | REG_SZ | Name of the screen saver executable file; deleted when (None) is selected. Superseded by the Screen saver executable name Group Policy. |
| `ScreenSaveActive` | REG_SZ | Enable (1) or disable (0) the screen saver. |
| `ScreenSaverIsSecure` | REG_SZ | Password protected (1) or unprotected (0). |
| `ScreenSaveTimeOut` | REG_SZ | Idle time in seconds before the screen saver launches; not present by default since Windows 7. |
| `Win8DpiScaling` |  | 0 = different scale factor per display (Windows 8.1 default); 1 = same scale factor on all displays. |
| `DesktopDPIOverride` |  | Offset from each display's default scale factor (<0 smaller, 0 default, >0 larger). |
| `LogPixels` |  | System-wide scale in Windows 8 scaling mode: 96 = 100%, 120 = 125%, 144 = 150%, 192 = 200%. |
| `Pattern` |  | Name of the pattern used as the desktop background (Win32_Desktop.Pattern). |

# subkeys

| subkey | description |
| --- | --- |
| `WindowMetrics` | Window and icon metrics such as `IconTitleWrap` (Win32_Desktop mapping). |

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Control Panel\Desktop"` | List the key's values. |
| `reg query "HKCU\Control Panel\Desktop" /v SCRNSAVE.EXE` | Show the configured screen saver executable. |
| `control desk.cpl,,1` | Open the Screen Saver Settings console that writes these values. |
