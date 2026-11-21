---
created: 2026-11-21
fullpath: 'C:\Windows\System32\fodhelper.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - uac-bypass
  - autoelevate
aliases:
  - 'fodhelper.exe'
  - 'Features On Demand Helper'
url: []
---

**fullpath**:C:\Windows\System32\fodhelper.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> Fodhelper ("Features On Demand Helper") is a small Windows program behind the Settings page for managing optional features. It is marked to auto-elevate, meaning an administrator account can run it at high integrity without seeing a UAC prompt. Users rarely run it directly.
>
> **SOC NOTE**: Well-known UAC bypass (T1548.002): attackers write a command to `HKCU\Software\Classes\ms-settings\Shell\Open\command` (plus an empty `DelegateExecute` value) and launch fodhelper.exe, which runs that command elevated without a prompt. Alert on registry writes to that key (Sysmon 12/13) and on fodhelper.exe spawning cmd/powershell or any child process.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
