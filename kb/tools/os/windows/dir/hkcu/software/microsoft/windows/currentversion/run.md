---
created: 2026-11-21
fullpath: 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Run
  - Run key
url:
  - https://learn.microsoft.com/windows/win32/setupapi/run-and-runonce-registry-keys
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
  - https://learn.microsoft.com/windows/configuration/shell-launcher/configure
---

**fullpath**:HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

# description

The per-user `Run` key lists programs that start every time the current user logs on. It is one of four Run/RunOnce keys (HKLM and HKCU); Shell Launcher also processes Run and RunOnce before starting a custom shell.

## simple description

> ### 2026-11-21 Claude said
> Anything listed in this key starts automatically every time this user signs in to Windows. Each value is a name plus the command line to run. Because it is in HKCU, a normal user can add entries without admin rights, and it only affects that one user. Many legitimate apps (OneDrive, Teams, updaters) put themselves here.
>
> **SOC NOTE**: This is one of the most common persistence locations (MITRE ATT&CK T1547.001 Registry Run Keys / Startup Folder) because it needs no admin rights. Look for values pointing into `%AppData%`, `%Temp%`, `Public`, script hosts (`wscript`, `mshta`, `powershell -enc`), or LOLBins. Sysmon Event 13 / Autoruns capture changes; for offline forensics parse the user's `NTUSER.DAT`.
>

# purpose

Makes a program run every time the user logs on. Value data is a command line no longer than 260 characters, in the form *description-string*=*commandline*; when several entries exist, their run order is indeterminate. The keys are ignored in Safe Mode, programs should not write to the key while running, and the system may delay Run-key programs to reduce impact on the foreground experience.

# hive

| property | value |
| --- | --- |
| hive | HKEY_CURRENT_USER |
| scope | per-user |
| backing file | `Ntuser.dat` |

# values

| value name | type | description |
| --- | --- | --- |
| any name (description string) | string | Command line (max 260 characters) run at every logon of this user. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"` | List the key's values. |
| `reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Run"` | List the machine-wide Run key for comparison. |
