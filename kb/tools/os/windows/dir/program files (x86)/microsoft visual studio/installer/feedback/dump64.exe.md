---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Visual Studio\Installer\Feedback\dump64.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "dump64.exe"
url: []
---

**fullpath**:C:\Program Files (x86)\Microsoft Visual Studio\Installer\Feedback\dump64.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> dump64.exe is a Microsoft-signed helper shipped with the Visual Studio Installer feedback component. It creates memory dump files of processes so they can be attached to problem reports. It is normally only run by the Visual Studio feedback tool.
>
> **SOC NOTE**: Known LOLBin: `dump64.exe <pid> out.dmp` can dump any process memory, including lsass.exe, for offline credential extraction (MITRE ATT&CK T1003.001 LSASS Memory). Because it is signed by Microsoft, it may evade simple allow-listing. Alert on dump64.exe accessing lsass or writing .dmp files outside Visual Studio feedback activity.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
