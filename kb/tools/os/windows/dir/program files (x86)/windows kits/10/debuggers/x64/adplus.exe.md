---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\adplus.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - debugging-tools
  - windows-kits
aliases:
  - adplus.exe
  - ADPlus
url:
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\adplus.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> ADPlus (AutoDump Plus) is a console tool from Debugging Tools for Windows that automates CDB to capture memory dumps of processes that hang or crash. It can run in hang mode (immediate dumps) or crash mode (attach and wait for exceptions). It has largely been replaced by ProcDump and DebugDiag. Output is written to a timestamped folder with dumps and logs.
>
> **SOC NOTE**: ADPlus can dump any process, including LSASS, to disk, enabling credential theft (T1003.001) with a Microsoft-signed tool; it is listed in LOLBAS. Alert on adplus.exe/cdb.exe targeting lsass.exe or writing .dmp files in unusual locations.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
