---
created: 2026-11-21
fullpath: 'c:\windows\system32\pcwutl.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - dll
  - compatibility
  - lolbin
aliases:
  - pcwutl.dll
  - Program Compatibility Wizard utility library
url: []
---

**fullpath**:c:\windows\system32\pcwutl.dll

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> pcwutl.dll is a Windows system library used by the Program Compatibility Troubleshooter (Program Compatibility Wizard), which helps run older applications with compatibility settings. It lives in System32 and is normally loaded by the compatibility troubleshooter components rather than run directly.
>
> **SOC NOTE**: Known LOLBin: it exports LaunchApplication, so `rundll32.exe pcwutl.dll,LaunchApplication <exe>` launches an arbitrary program through signed binaries (T1218.011 Rundll32). Hunt for rundll32 command lines referencing pcwutl.dll and the child process it spawns.
>
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_


