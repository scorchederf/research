---
created: 2026-11-21
fullpath: 'c:\windows\system32\provlaunch.exe'
generator:
  - claude
tags:
  - windows
  - executable
  - provisioning
aliases:
  - provlaunch.exe
url:
---

**fullpath**:c:\windows\system32\provlaunch.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> provlaunch.exe is a Windows component tied to the provisioning engine, which applies provisioning packages (.ppkg) and runs provisioning commands during setup or at runtime. It launches commands that are configured as part of provisioning. Regular users rarely interact with it directly.
>
> **SOC NOTE**: provlaunch.exe is documented in LOLBAS as a proxy-execution binary: it runs commands stored under `HKLM\SOFTWARE\Microsoft\Provisioning\Commands\...` (MITRE ATT&CK T1218). Attackers with admin rights can plant a command there and execute it via provlaunch. Hunt for writes to that registry path and child processes of provlaunch.exe.
> _Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_

# options

| option    | description    |
| --- | --- |
| _Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_ |  |
