---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - persistence
  - appinit
aliases:
  - CurrentVersion\Windows
  - AppInit_DLLs
url:
  - https://learn.microsoft.com/windows/win32/dlls/secure-boot-and-appinit-dlls
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows

# description

Machine-wide registry key holding legacy Windows (user32/window manager) settings, notably the AppInit_DLLs mechanism that loads custom DLLs into every interactive process that loads user32. Learn notes that AppInit_DLLs is not recommended, is a desktop app certification failure, and is disabled when Secure Boot is enabled (Windows 8 and later).

## simple description

> ### 2026-11-21 Claude said
> This key stores system-wide settings for the Windows graphical subsystem. Its best-known values are AppInit_DLLs and LoadAppInit_DLLs, which tell Windows to load extra DLLs into every program that uses the standard window library. Very few legitimate products still use it. On Secure Boot systems the mechanism is disabled.
>
> **SOC NOTE**: AppInit_DLLs persistence/injection (T1546.010): attackers set `LoadAppInit_DLLs=1` and point `AppInit_DLLs` at a malicious DLL (also check the WOW6432Node copy). `RequireSignedAppInit_DLLs` changes are also suspicious. Monitor Sysmon 13 on these values; Autoruns lists them under AppInit.
>

# purpose

Hosts the AppInit_DLLs infrastructure, which provides a way to hook system APIs by loading custom DLLs into the address space of every interactive application.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | Software (`%SystemRoot%\System32\Config`) |

# values

| value name | type | description |
| --- | --- | --- |
| `AppInit_DLLs` | _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_ | DLLs loaded into every interactive application; disabled when Secure Boot is enabled. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows" /v AppInit_DLLs` | Show the configured AppInit DLLs. |
