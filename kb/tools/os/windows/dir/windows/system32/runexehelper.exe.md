---
created: 2026-11-21
fullpath: 'c:\windows\system32\runexehelper.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lolbin
aliases:
  - "runexehelper.exe"
url: []
---

**fullpath**: c:\windows\system32\runexehelper.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> runexehelper.exe is a small Windows helper used by the Windows test/diagnostic framework to launch a specified executable and write a log. It is not something users run directly. On most systems it sits idle in System32.
>
> **SOC NOTE**: Listed in LOLBAS as able to launch an arbitrary executable (proxy execution, T1218); when the environment variable that sets its log path is controlled by an attacker it can run a binary and hide the parent chain. Alert on runexehelper.exe spawning anything outside test/diagnostic contexts.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
