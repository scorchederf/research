---
created: 2026-11-21
fullpath: 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - autostart
aliases:
  - RunOnce
  - HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
url:
  - https://learn.microsoft.com/windows/win32/setupapi/run-and-runonce-registry-keys
  - https://learn.microsoft.com/windows-hardware/drivers/install/runonce-registry-key
  - https://learn.microsoft.com/troubleshoot/windows-client/shell-experience/standard-user-cannot-run-commnad-via-runonce
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-logon
  - https://learn.microsoft.com/windows/win32/shell/about-user-profiles
---

**fullpath**:HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

# description

The per-user `RunOnce` key makes a program run one time when the user logs on, after which the entry is deleted. It is one of four Run/RunOnce keys (HKLM and HKCU, Run and RunOnce); the related `RunOnceEx` key exists alongside it.

## simple description

> ### 2026-11-21 Claude said
> RunOnce under HKCU is a list of commands Windows runs a single time the next time this user logs on, then removes. Installers use it to finish setup after a reboot. Because it lives in the user's hive, a normal user (or malware running as that user) can write to it without admin rights.
>
> **SOC NOTE**: A common persistence/staging location (MITRE ATT&CK T1547.001 Registry Run Keys / Startup Folder). Entries self-delete, so evidence may only survive in registry transaction logs, NTUSER.DAT snapshots, Sysmon event 13 (registry value set) or process creation logs at logon. Watch for `!` or `*` prefixed value names (defer deletion / run in Safe Mode) and commands pointing to user-writable paths.
>

# purpose

Registers programs to run once at user logon. The data value is a command line no longer than 260 characters, written as entries of the form *description-string*=*commandline*; when several programs are registered, their order is indeterminate. By default the value is deleted before the command runs; prefix the value name with `!` to defer deletion until after the command runs, and with `*` to force it to run even in Safe Mode (RunOnce keys are otherwise ignored in Safe Mode). Applications should use RunOnce only for transient conditions such as completing setup. Commands under RunOnce/RunOnceEx are not executed when a Standard User logs on; an administrator or split-token account is required.

# hive

| property | value |
| --- | --- |
| hive | HKCU |
| scope | per-user |
| backing file | NTuser.dat |

# values

| value name | type | description |
| --- | --- | --- |
| `<description-string>` | REG_SZ or REG_EXPAND_SZ | Command line (max 260 characters) to run once at next logon. |
| `!<description-string>` | REG_SZ or REG_EXPAND_SZ | Deletion of the value is deferred until after the command runs. |
| `*<description-string>` | REG_SZ or REG_EXPAND_SZ | Command runs even when the computer starts in Safe Mode. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"` | List the key's values. |
| `reg query "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v DisableCurrentUserRunOnce` | Check the "Do not process the run once list" policy value. |
