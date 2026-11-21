---
created: 2026-11-21
fullpath: 'C:\Windows\System32\config\systemprofile'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - user-profile
  - localsystem
aliases:
  - systemprofile
  - LocalSystem profile
url: []
---

**fullpath**:C:\Windows\System32\config\systemprofile

# description

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> systemprofile is the user profile folder of the built-in SYSTEM (LocalSystem, S-1-5-18) account. Just like C:\Users\<name>, it contains AppData, Desktop and an NTUSER.DAT hive, but it is used by services and processes running as SYSTEM. Its registry hive is loaded as HKU\S-1-5-18. Normal users never log on with this profile.
>
> **SOC NOTE**: Anything running as SYSTEM writes here, so it is a common place for attacker tools, staging files and caches from SYSTEM-level malware (e.g. AppData\Local\Temp, AppData\Roaming, INetCache from downloads made by SYSTEM, PowerShell PSReadLine history of SYSTEM shells). Review its AppData and the NTUSER.DAT (Run keys, UserAssist) during investigations of privilege escalation (T1068) or service-based persistence (T1543.003).
> _Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
