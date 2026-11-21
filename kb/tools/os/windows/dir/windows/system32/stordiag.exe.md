---
created: 2026-11-21
fullpath: 'c:\windows\system32\stordiag.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - storage
  - diagnostics
aliases:
  - stordiag.exe
  - Storage Diagnostic Tool
url: []
---

**fullpath**:c:\windows\system32\stordiag.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_

## simple description

> ### 2026-11-21 Claude said
> stordiag.exe is the Windows Storage Diagnostic Tool. It collects storage-related logs, event logs, registry data and output from tools like fsutil, chkdsk and systeminfo into a folder for troubleshooting disks and file systems. It is mainly used by support engineers.
>
> **SOC NOTE**: Listed as a LOLBin (MITRE ATT&CK T1218): it runs systeminfo.exe, fltmc.exe and schtasks.exe from the current directory, so a renamed payload in a writable folder can be executed under a signed parent. Alert on stordiag.exe run from a non-System32 working directory or spawning children not located in System32.
>
> _Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_
