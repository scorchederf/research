---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - appcompat
  - persistence
aliases:
  - InstalledSDB
url:
  - https://learn.microsoft.com/windows/win32/devnotes/application-compatibility-database
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB

# description

Registry key under AppCompatFlags that registers custom application compatibility (shim) databases installed on the machine. Learn describes the compatibility infrastructure's .sdb databases (Apphelp and Appfix/shims) but not this key itself. Related: sdbinst.exe, `AppCompatFlags\Custom`, `%WINDIR%\AppPatch\Custom`.

## simple description

> ### 2026-11-21 Claude said
> This key lists custom shim databases (.sdb files) that have been installed on the computer, one GUID subkey per database. Shim databases tell Windows to apply compatibility fixes to specific programs when they start. They are normally installed by sdbinst.exe for legacy enterprise apps. Most systems have few or no entries here.
>
> **SOC NOTE**: Application shimming is a persistence/privilege technique (T1546.011): attackers install a malicious .sdb (e.g. InjectDll or RedirectEXE shims) with sdbinst, creating a GUID subkey here plus entries under `AppCompatFlags\Custom`. Investigate any InstalledSDB entry whose DatabasePath points outside `C:\Windows\AppPatch\Custom`, and sdbinst.exe executions (4688/Sysmon 1, Sysmon 12/13).
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | Software (`%SystemRoot%\System32\Config`) |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB" /s` | List all installed shim database subkeys and their values. |
