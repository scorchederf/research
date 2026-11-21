---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft\Copilot\Application\mscopilot_proxy.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - copilot
aliases:
  - mscopilot_proxy.exe
url:
---

**fullpath**:C:\Program Files (x86)\Microsoft\Copilot\Application\mscopilot_proxy.exe

# description

mscopilot_proxy.exe is a helper executable of the Microsoft Copilot desktop app. _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> mscopilot_proxy.exe appears to be a launcher/proxy helper installed with the Microsoft Copilot desktop application, similar to the msedge_proxy.exe helper used by Edge-based web apps. It starts the Copilot app experience on behalf of shortcuts or protocol activations. It is installed in Program Files (x86) with the Copilot application. Users do not normally run it directly.
>
> **SOC NOTE**: Low inherent risk, but Edge-style `*_proxy.exe` helpers accept `--app`/URL style arguments and can be used to open arbitrary web content from a signed binary; review unusual command lines or parents. Verify the binary is Microsoft-signed and in the expected path to rule out masquerading (T1036.005).
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
