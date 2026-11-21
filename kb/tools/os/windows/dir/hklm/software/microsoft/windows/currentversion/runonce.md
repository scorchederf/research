---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - autostart
  - persistence
aliases:
  - 'RunOnce'
  - 'RunOnce registry key'
url:
  - https://learn.microsoft.com/windows/win32/setupapi/run-and-runonce-registry-keys
  - https://learn.microsoft.com/windows-hardware/drivers/install/runonce-registry-key
  - https://learn.microsoft.com/troubleshoot/windows-client/shell-experience/standard-user-cannot-run-commnad-via-runonce
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-logon
---

**fullpath**: HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

# description

One of the four Run/RunOnce keys used to make a program run when a user logs on; RunOnce entries run one time and are then deleted. The machine-wide RunOnce key only executes when members of the Administrators group log on. Driver packages can create entries through INF AddReg directives, and the "Do not process the run once list" policy (DisableCurrentUserRunOnce) can make Windows ignore it.

## simple description

> ### 2026-11-21 Claude said
> RunOnce holds commands that Windows runs a single time, usually at the next logon, and then removes. Installers use it to finish setup after a reboot. Each value is a name plus a command line. Because it is under HKLM, it affects the whole machine, but only runs when an administrator signs in.
>
> **SOC NOTE**: Classic persistence location (MITRE T1547.001 Registry Run Keys / Startup Folder). Because entries self-delete, check Sysmon event 13 / Security 4657 history, and value names prefixed with `!` (deletion deferred) or `*` (run in Safe Mode) - the `*` prefix is used by ransomware to survive Safe Mode boots. Also review RunOnceEx and HKCU equivalents and Autoruns output.
>

# purpose

Specifies commands that the system runs one time at logon and then deletes, typically to complete application setup.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide (executes only when an administrator logs on) |
| backing file | `%SystemRoot%\System32\config\SOFTWARE` |

# values

| value name | type | description |
| --- | --- | --- |
| `<description-string>` | REG_SZ / REG_EXPAND_SZ | Command line (up to 260 characters) to run once. By default the value is deleted before the command runs. |
| `!<name>` | REG_SZ | Prefixing the value name with `!` defers deletion until after the command runs (successfully, for driver installs). |
| `*<name>` | REG_SZ | Prefixing with `*` forces the command to run even in Safe Mode; otherwise RunOnce is ignored in Safe Mode. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"` | List pending run-once commands. |
| `reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce" /v Setup /t REG_SZ /d "C:\setup\finish.exe"` | Register a command to run once at next administrator logon. |
