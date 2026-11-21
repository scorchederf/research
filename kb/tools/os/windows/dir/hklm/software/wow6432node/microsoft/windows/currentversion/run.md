---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - persistence
  - autorun
aliases:
  - Run
  - WOW6432Node Run key
url:
  - https://learn.microsoft.com/windows/win32/setupapi/run-and-runonce-registry-keys
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/registry-changes-in-x64-based-windows
  - https://learn.microsoft.com/windows/win32/winprog64/registry-redirector
---

**fullpath**:HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run

# description

The 32-bit (WOW64) view of the machine-wide `Run` key. On x64 Windows, registry calls by 32-bit programs to `HKLM\Software` are redirected by WOW64 to `HKLM\Software\WOW6432Node`, so a 32-bit installer writing `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` lands here. `Run` entries make a program run every time a user logs on.

## simple description

> ### 2026-11-21 Claude said
> This key lists programs that start automatically whenever any user logs on, for 32-bit software on 64-bit Windows. Each value is a name and a command line. Many legitimate apps (updaters, tray tools) register here. It is the 32-bit twin of the normal HKLM Run key, and both are processed at logon.
>
> **SOC NOTE**: Classic persistence location (MITRE T1547.001). Attackers may pick the WOW6432Node view because analysts often check only the 64-bit Run key. Review values pointing to user-writable paths, script hosts, rundll32 or encoded PowerShell. Changes appear in Sysmon event 13 and autoruns output.
>

# purpose

Registers command lines that run at every user logon for 32-bit applications on 64-bit Windows. The data value is a command line no longer than 260 characters; entry order is indeterminate, entries are ignored in Safe Mode, and the system may delay their execution.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `<description-string>` | REG_SZ | Command line (max 260 characters) to run at every logon, in the form description-string=commandline. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"` | List the key's values. |
