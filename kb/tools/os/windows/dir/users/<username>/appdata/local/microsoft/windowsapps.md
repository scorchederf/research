---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\WindowsApps'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - msix
  - app-execution-alias
aliases:
  - WindowsApps
  - '%LOCALAPPDATA%\Microsoft\WindowsApps'
  - App execution aliases
url:
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\WindowsApps

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> This per-user folder holds "app execution alias" stubs: tiny zero-byte-looking .exe reparse points (for example winget.exe, python.exe, wt.exe) that let you start Store/MSIX-packaged apps by name from a command prompt. The folder is on the user's PATH by default. Each alias can be turned on or off in Settings > Apps > Advanced app settings > App execution aliases. It is created per user under %LOCALAPPDATA%.
>
> **SOC NOTE**: Because it is user-writable and on PATH, attackers can drop executables here for search-order hijacking or persistence (MITRE ATT&CK T1574.007 Path Interception by PATH Environment Variable). The python.exe/python3.exe stubs that open the Store are a common source of confusion in script-based attacks. Look for real PE files (non-reparse points) or unexpected names here; legitimate entries are IO_REPARSE_TAG_APPEXECLINK reparse points.
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
