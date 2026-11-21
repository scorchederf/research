---
created: 2026-11-21
fullpath: 'c:\windows\system32\rdrleakdiag.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - diagnostics
  - lolbin
aliases:
  - rdrleakdiag.exe
  - Microsoft Windows Resource Leak Diagnostic
url: []
---

**fullpath**:c:\windows\system32\rdrleakdiag.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> rdrleakdiag.exe is the Microsoft Windows Resource Leak Diagnostic tool, part of the Windows Diagnostic Infrastructure. Windows uses it to collect information about processes that leak memory or handles, typically when the Memory Leak Diagnosis scenario fires. It can write memory snapshots of a target process to disk. Users rarely run it directly.
>
> **SOC NOTE**: Signed LOLBin abused to dump LSASS memory (MITRE T1003.001): `rdrleakdiag.exe /p <lsass PID> /o <outdir> /fullmemdmp /wait 1` writes `minidump_<pid>.dmp`, bypassing rules that only watch procdump/comsvcs. Alert on rdrleakdiag with `/fullmemdmp` or `/p` targeting lsass, and on new `.dmp`/`results_*.hlk` files in odd directories.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
