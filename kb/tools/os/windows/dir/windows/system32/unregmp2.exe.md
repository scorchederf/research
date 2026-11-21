---
created: 2026-11-21
fullpath: 'C:\Windows\System32\unregmp2.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-media-player
aliases:
  - unregmp2.exe
  - Microsoft Windows Media Player Setup Utility
url: []
---

**fullpath**:C:\Windows\System32\unregmp2.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_

## simple description

> ### 2026-11-21 Claude said
> unregmp2.exe is the Windows Media Player setup utility. Windows runs it to register, reset and configure Windows Media Player for each user (first-run setup, file associations, shortcuts) and during feature removal. Users rarely run it directly.
>
> **SOC NOTE**: Known LOLBin (MITRE ATT&CK T1218): with `/HideWMP` it launches wmpnscfg.exe from the folder in %ProgramW6432%, so pointing that variable to an attacker folder runs a payload via a signed binary. Alert on unregmp2.exe with modified environment variables or spawning children outside Program Files. It runs routinely at user logon via Active Setup, so baseline it.
>
> _Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_
