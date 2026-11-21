---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - environment
aliases:
  - "Session Manager\Environment"
  - "System environment variables"
url:
  - https://learn.microsoft.com/windows/win32/procthread/environment-variables
  - https://learn.microsoft.com/windows/win32/cimwin32prov/win32-environment
---

**fullpath**: HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment

# description

Registry key holding the system (machine-wide) environment variables such as Path, TEMP, windir and PATHEXT. User environment variables are stored separately under HKEY_USERS\<user>\Environment. The WMI class Win32_Environment returns variables from both locations.

## simple description

> ### 2026-11-21 Claude said
> This key stores environment variables that apply to every user and service on the machine, like PATH. Windows builds each new process's environment from it at logon/startup. Editing it via System Properties > Environment Variables writes here. Changes reach running apps only after a WM_SETTINGCHANGE broadcast or restart.
>
> **SOC NOTE**: Attackers modify Path (search-order hijacking, T1574.007), add variables like COR_PROFILER (T1574.012) or windir/SystemRoot tricks for UAC bypass, or set __PSLockdownPolicy. Monitor writes with Sysmon 13 / Security 4657 and compare Path to baseline.
>

# purpose

Stores system environment variables. To programmatically add or modify system environment variables, add them to this key and broadcast WM_SETTINGCHANGE with lParam set to "Environment" so applications such as the shell pick up the update; SetEnvironmentVariable has no effect on system variables.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"` | List the key's values. |
| `Get-CimInstance Win32_Environment` | List system and user environment variables via WMI. |
