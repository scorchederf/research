---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - persistence
aliases:
  - "Active Setup"
  - "Installed Components"
url: []
---

**fullpath**: HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components

# description

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> Active Setup is an old Windows mechanism that runs a command once per user at logon, used to apply per-user settings for software installed machine-wide (Internet Explorer, Windows Mail, Office components, etc.). Each component is a subkey (usually a GUID) with a StubPath command and a Version. At logon, Explorer compares the HKLM entry with HKCU\Software\Microsoft\Active Setup\Installed Components; if the user's copy is missing or older, it runs StubPath and records the version in HKCU.
>
> **SOC NOTE**: Writing a new subkey with a malicious StubPath gives persistence that runs for every user at their next logon (MITRE T1547.014 Boot or Logon Autostart Execution: Active Setup). Needs admin rights to write HKLM. Review subkeys with unusual StubPath commands (powershell, rundll32, scripts in user-writable paths) and monitor Sysmon 12/13 on this key; Autoruns lists these entries.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components" /s /v StubPath` | List every component's StubPath command. |
