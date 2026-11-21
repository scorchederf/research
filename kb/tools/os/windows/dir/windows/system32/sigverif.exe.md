---
created: 2026-11-21
fullpath: 'C:\Windows\System32\sigverif.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - code-signing
  - drivers
aliases:
  - sigverif.exe
  - File Signature Verification
url: []
---

**fullpath**:C:\Windows\System32\sigverif.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> sigverif.exe is the File Signature Verification tool, a small GUI built into Windows. It scans system files and drivers (by default in System32\drivers and related folders) and lists any that are not digitally signed. Results are saved to a log file, SIGVERIF.TXT, normally in the Public Documents or Windows folder. It is mostly used to troubleshoot driver problems.
>
> **SOC NOTE**: Handy for quick triage of unsigned drivers that could indicate rootkits or BYOVD activity (T1014, T1068); however it is a GUI tool rarely run by users, so execution by unusual parents is suspicious. For scripted, more complete checks prefer Sysinternals `sigcheck -u -e` or `signtool verify /kp`.
> _Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
