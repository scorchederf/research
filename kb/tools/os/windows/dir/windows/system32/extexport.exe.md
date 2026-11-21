---
created: 2026-11-21
fullpath: 'C:\Windows\System32\extexport.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - internet-explorer
  - lolbin
aliases:
  - "extexport.exe"
  - "ExtExport"
url: []
---

**fullpath**:C:\Windows\System32\extexport.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> ExtExport.exe is a legacy Internet Explorer helper used to export browser data (bookmarks/favorites) for other browsers such as Firefox. It normally lives in `C:\Program Files\Internet Explorer` and `C:\Program Files (x86)\Internet Explorer`; a copy in System32 is unusual. It is rarely used by legitimate users today.
>
> **SOC NOTE**: ExtExport is a documented LOLBin: `ExtExport.exe <folder> foo bar` loads `mozcrt19.dll`, `mozsqlite3.dll` or `sqlite3.dll` from the given folder, allowing DLL side-loading/proxy execution (T1218). A copy outside the Internet Explorer folder, or execution with a user-writable folder argument, should be treated as suspicious.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
