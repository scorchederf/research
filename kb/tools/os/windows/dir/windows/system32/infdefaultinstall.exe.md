---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Infdefaultinstall.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - drivers
aliases:
  - Infdefaultinstall.exe
  - InfDefaultInstall
url: []
---

**fullpath**:C:\Windows\System32\Infdefaultinstall.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

## simple description

> ### 2026-11-21 Claude said
> InfDefaultInstall.exe is the small Windows program that runs when you right-click an .inf file and choose "Install". It processes the INF file's [DefaultInstall] section, which can copy files, add registry entries, register DLLs and create services. It is used for installing filter drivers and other non-device components from INF files.
>
> **SOC NOTE**: Listed as a LOLBin (T1218 System Binary Proxy Execution): a crafted INF with a DefaultInstall section can write registry Run keys, register COM scriptlets or execute commands, so `InfDefaultInstall.exe <path>.inf` with an INF in a temp or user folder is suspicious. Correlate with setupapi.app.log/dev.log entries, Sysmon 1 process creation and registry changes made right after execution.
>
> _Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
