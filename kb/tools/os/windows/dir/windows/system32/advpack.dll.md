---
created: 2026-11-21
fullpath: 'c:\windows\system32\advpack.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - dll
  - lolbin
aliases:
  - "advpack.dll"
  - "Advanced INF Setup"
url: []
---

**fullpath**:c:\windows\system32\advpack.dll

# description

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> advpack.dll is the legacy Windows Advanced INF installer library originally shipped with Internet Explorer setup. It exposes functions such as LaunchINFSection, LaunchINFSectionEx, RegisterOCX and RunSetupCommand that install software from INF files. These functions can be called from the command line through rundll32.exe.
>
> **SOC NOTE**: A well-known LOLBin DLL: `rundll32.exe advpack.dll,LaunchINFSection <file.inf>,DefaultInstall_SingleUser,1,` or `advpack.dll,RegisterOCX <payload>` executes attacker-supplied INF/DLL/EXE content, including scriptlet (.sct) downloads (T1218.011 Rundll32). Alert on rundll32 command lines referencing advpack with INF files in user-writable paths.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
