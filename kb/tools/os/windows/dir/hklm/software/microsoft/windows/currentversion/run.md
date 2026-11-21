---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - persistence
aliases:
  - "Run"
  - "Run key"
url:
  - https://learn.microsoft.com/windows/win32/setupapi/run-and-runonce-registry-keys
  - https://learn.microsoft.com/azure/defender-for-cloud/file-integrity-monitoring-overview
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

# description

The machine-wide Run key makes the programs it lists run every time a user logs on. It is one of four Run/RunOnce keys (HKLM and HKCU) documented in the Windows Setup API reference.

## simple description

> ### 2026-11-21 Claude said
> This registry key lists programs that Windows starts automatically whenever any user logs on. Each value is a name and a command line. Installers use it for tray apps and updaters, and it requires administrator rights to change.
>
> **SOC NOTE**: One of the most common persistence locations (MITRE ATT&CK T1547.001 Registry Run Keys). Review every value for paths in user-writable folders, script hosts or LOLBins; changes appear in Sysmon events 12/13 and Autoruns. Also check the WOW6432Node counterpart, which Defender for Cloud file integrity monitoring recommends watching.
>

# purpose

Registers programs to run at every user logon. Entries take the form description-string=commandline, with the command line no longer than 260 characters. Run order between multiple entries is indeterminate, entries are ignored in Safe Mode, and the system may delay execution so it does not interfere with the foreground user experience. A program run from the key should not write to the key during execution.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `<description-string>` | string | Command line (max 260 characters) run every time a user logs on. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"` | List the key's values. |
