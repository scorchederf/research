---
created: 2026-11-21
fullpath: 'c:\windows\system32\syssetup.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - dll
aliases:
  - syssetup.dll
url:
---

**fullpath**:c:\windows\system32\syssetup.dll

# description

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

## simple description

> ### 2026-11-21 Claude said
> syssetup.dll is the Windows "System Setup" library used during OS installation and out-of-box setup. It contains routines for setup stages, installing optional components and processing INF sections. Normal users and applications rarely load it directly.
>
> **SOC NOTE**: It exports `SetupInfObjectInstallAction`, which can be invoked via `rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 <file.inf>` to execute a malicious INF (LOLBin, MITRE T1218.011 / T1218). Flag rundll32 command lines referencing syssetup.dll with an INF outside system folders.
> _Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_
