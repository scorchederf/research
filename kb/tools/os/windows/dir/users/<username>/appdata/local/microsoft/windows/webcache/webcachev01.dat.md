---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Windows\WebCache\WebCacheV01.dat'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - forensics
  - browser
aliases:
  - "WebCacheV01.dat"
  - "WebCache"
url: []
---

**fullpath**: C:\Users\<username>\AppData\Local\Microsoft\Windows\WebCache\WebCacheV01.dat

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> WebCacheV01.dat is an ESE (Extensible Storage Engine) database in each user's profile. It stores Internet Explorer / legacy Edge and WinINet history, cache index, cookies and download records, and also records local file access via file:/// entries. It is locked while the user is logged on because taskhostw/dllhost keep it open. Forensic tools such as ESEDatabaseView or KAPE parse it.
>
> **SOC NOTE**: High forensic value: browsing history with timestamps, downloads (including source URLs), and file:/// entries proving a user opened local or network files, even when IE is not used directly. Attackers may delete or tamper with it to hide activity (T1070.004). Collect it with the accompanying .jfm/.log files via VSS or raw copy and run esentutl /r before parsing.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
