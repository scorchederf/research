---
created: 2026-11-21
fullpath: 'C:\Windows\System32\CustomShellHost.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - CustomShellHost.exe
  - Shell Launcher v2
url:
  - https://learn.microsoft.com/windows/configuration/shell-launcher/
  - https://learn.microsoft.com/windows/configuration/shell-launcher/configure
---

**fullpath**:C:\Windows\System32\CustomShellHost.exe

# description

CustomShellHost.exe is the host process used by Shell Launcher v2, the Windows feature that replaces `Explorer.exe` with a custom shell for kiosks, ATMs and digital signage. Shell Launcher v1 uses `Eshell.exe` instead. Shell Launcher is supported on Enterprise, Education and IoT Enterprise editions.

## simple description

> ### 2026-11-21 Claude said
> CustomShellHost.exe is the Windows component that runs a replacement desktop shell when Shell Launcher v2 is configured, for example on a kiosk that should show only one app instead of the normal Explorer desktop. It can launch either a classic Win32 app or a UWP app as the shell. It also handles what happens when the custom shell exits (restart shell, reboot, shut down or nothing). On normal desktops it is usually not running.
>
> **SOC NOTE**: Shell replacement is a persistence and evasion avenue: an attacker with admin rights could configure Shell Launcher (via WMI `WESL_UserSetting` or CSP) so a malicious program runs as the user's shell at every logon (related to MITRE ATT&CK T1547.004 Winlogon Helper / shell modification). CustomShellHost.exe running on a non-kiosk device, or the shell it launches being unexpected, warrants review.
>

# purpose

Shell Launcher v2 replaces `Explorer.exe` with `CustomShellHost.exe`, which can launch a Windows desktop application or a UWP app as the shell, launch secondary views on multiple monitors, and run the custom shell full screen. Shell Launcher processes the `Run` and `RunOnce` registry keys before starting the custom shell and applies a configurable exit action: `0` restart the shell, `1` restart the device, `2` shut down the device, `3` do nothing.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
