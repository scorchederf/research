---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - windows
aliases:
  - "Winlogon"
url: []
---

**fullpath**:HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This per-user Winlogon key holds user-specific Winlogon settings, mirroring part of the machine-wide HKLM Winlogon key. Values such as Shell can be set here to override the user's shell. It is loaded from the user's NTUSER.DAT at logon.
>
> **SOC NOTE**: Persistence location (MITRE ATT&CK T1547.004 Winlogon Helper DLL): a `Shell` value here (e.g. `explorer.exe, evil.exe`) runs the attacker program at each logon for that user without admin rights. Review this key in every NTUSER.DAT, and monitor registry set events (Sysmon 13) for Shell/Userinit values.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# hive

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# values

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon"` | List the key's values. |
