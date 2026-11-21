---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - logon
aliases:
  - Winlogon
  - Winlogon registry key
url:
  - https://learn.microsoft.com/windows/win32/secauthn/msgina-dll-features
  - https://learn.microsoft.com/troubleshoot/windows-server/user-profiles-and-logon/cannot-log-on-windows
  - https://learn.microsoft.com/windows/win32/secauthn/registering-a-winlogon-notification-package
  - https://learn.microsoft.com/windows/win32/secauthn/registry-entries
  - https://learn.microsoft.com/windows/win32/wfp/wfp-registry-values
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon

# description

The Winlogon registry key holds values that control the availability and behavior of standard logon features, such as the legal notice, automatic logon, the user shell (Shell) and Userinit.exe. Winlogon searches this key for the default shell (explorer.exe) and user initialization program (userinit.exe) when a user logs on. Historically it also hosted Winlogon notification packages (Notify subkey) and Windows File Protection settings.

## simple description

> ### 2026-11-21 Claude said
> This registry key configures how Windows logs users on. It tells Winlogon which program to run to set up the user's session (Userinit) and which shell to start (normally explorer.exe), and holds settings like auto-logon credentials, the legal notice banner and whether to show the last user name. Because it controls what runs at every logon, it is one of the most sensitive keys in the system.
>
> **SOC NOTE**: Classic persistence location (MITRE T1547.004 Winlogon Helper DLL): attackers append payloads to `Userinit` or `Shell` (e.g. `C:\Windows\system32\userinit.exe,evil.exe`) or add Notify subkeys. `AutoAdminLogon`/`DefaultPassword` can expose plaintext credentials (T1552.002). Monitor with Sysmon event 13 / 4657 auditing, and compare Shell and Userinit against the defaults `explorer.exe` and `C:\Windows\system32\userinit.exe,`.
>

# purpose

Stores Winlogon configuration: legal notice text, last-user-name display, automatic logon, unauthenticated shutdown, and the Userinit.exe and shell programs started after logon. If Shell or Userinit point to wrong or deleted files, Windows logs on and immediately logs off; if correcting them doesn't resolve the issue, Microsoft advises the machine should be considered compromised.

# hive

| property | value |
| --- | --- |
| hive | HKLM (HKEY_LOCAL_MACHINE) |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `LegalNoticeCaption` | REG_SZ | Caption of the legal notice dialog box shown before logon. |
| `LegalNoticeText` | REG_SZ | Message of the legal notice dialog box shown before logon. |
| `DontDisplayLastUserName` | REG_SZ | When set to 1, the last logged-on user name is not displayed in the logon dialog. |
| `AutoAdminLogon` | REG_SZ | Set to 1 to log on a user automatically at every start using default information. |
| `IgnoreShiftOverride` | REG_SZ | Set to 1 to disable the SHIFT key override of AutoAdminLogon during boot. |
| `ShutdownWithoutLogon` | REG_SZ | 1 includes a Shutdown button in the logon dialog; 0 excludes it. |
| `Shell` | REG_SZ | Comma-separated list of shell programs Userinit.exe runs; default is `explorer.exe`. |
| `Userinit` | REG_SZ | User initialization program; default `C:\windows\system32\userinit.exe`. Sets up the user environment, restores network uses, runs logon scripts, then starts the shell. |
| `SFCDllCacheDir` | REG_SZ | Windows File Protection cache location (default `%systemroot%\system32\dllcache`); not supported as of Windows Vista. |
| `SFCQuota` | REG_DWORD | Windows File Protection DLL cache size; not supported as of Windows Vista. |
| `SFCScan` | REG_DWORD | Windows File Protection scan-at-boot option; not supported as of Windows Vista. |

# subkeys

| subkey | description |
| --- | --- |
| `Notify` | Contains Winlogon notification package subkeys (Asynchronous, DllName, Impersonate, and event handler function names such as Logon, Logoff, Lock, Unlock, Startup, Shutdown, StartShell). Winlogon loads registered packages at start. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell` | Show the configured shell program(s). |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit` | Show the configured Userinit program. |
