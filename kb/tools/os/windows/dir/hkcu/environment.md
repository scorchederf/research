---
created: 2026-11-21
fullpath: 'HKCU\Environment'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
aliases:
  - Environment
  - HKEY_CURRENT_USER\Environment
  - user environment variables
url:
  - https://learn.microsoft.com/powershell/scripting/samples/working-with-registry-entries
  - https://learn.microsoft.com/windows/win32/procthread/environment-variables
  - https://learn.microsoft.com/windows/win32/shell/user-environment-variables
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
---

**fullpath**:HKCU\Environment

# description

`HKCU\Environment` holds the per-user environment variables of the signed-in user, such as the user **Path** entry. Windows maintains one environment block per user and one for the computer; system-wide variables live under `HKLM\System\CurrentControlSet\Control\Session Manager\Environment`. Related tools are the System Control Panel Environment Variables dialog, `set`, `reg.exe` and PowerShell `Set-ItemProperty`.

## simple description

> ### 2026-11-21 Claude said
> This registry key stores the environment variables that belong only to the current user, such as a personal PATH, TEMP and TMP. When the user signs in, Windows merges these values with the system-wide variables to build the environment every new program receives. Users can change it without admin rights, through System Properties or `setx`. Programs started afterwards see the new values.
>
> **SOC NOTE**: Because it is user-writable, attackers use it for persistence and hijacking: the `UserInitMprLogonScript` value runs a script at logon (MITRE ATT&CK T1037.001), and changing PATH, TEMP or `windir`/`COR_PROFILER`-style variables enables search-order hijacking or profiler DLL loading (T1574.007, T1574.012). Look for new or modified values in Sysmon Event ID 13, NTUSER.DAT in offline forensics, and unusual paths (AppData, Temp, Public) in PATH.
>

# purpose

Environment variables specify search paths for files, directories for temporary files, application-specific options and similar information. Every process gets a copy of its parent's environment block, usually the block of the signed-in user, which includes the system variables. The **Path** entry under `HKEY_CURRENT_USER\Environment` specifies where to find executable files. After programmatic changes, broadcast a `WM_SETTINGCHANGE` message with *lParam* set to "Environment" so applications such as the shell pick up the update. A user-defined environment variable can be up to 32,767 characters.

# hive

| property | value |
| --- | --- |
| hive | HKCU (HKEY_CURRENT_USER) |
| scope | per-user |

# values

| value name | type | description |
| --- | --- | --- |
| `Path` | _Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_ | Specifies where to find executable files for the user; entries are separated with `;`. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Environment"` | List the key's values. |
| `Get-ItemProperty -Path HKCU:\Environment -Name Path` | Read the user Path entry with PowerShell. |
| `reg add HKCU\Environment /v Path /d <newpath> /f` | Overwrite the user Path entry. |
