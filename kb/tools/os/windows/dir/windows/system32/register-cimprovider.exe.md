---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Register-cimprovider.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - wmi
  - lolbin
aliases:
  - "Register-CimProvider.exe"
url: []
---

**fullpath**: C:\Windows\System32\Register-cimprovider.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> Register-CimProvider.exe is a built-in Windows tool that registers a CIM/WMI (MI) provider DLL with the WMI service. Developers and installers use it to make a new WMI provider's classes available. It takes a path to the provider DLL and registers it in a namespace. Normal users rarely run it.
>
> **SOC NOTE**: Listed in LOLBAS: `Register-cimprovider -path <dll>` loads an arbitrary DLL, giving signed-binary proxy execution (T1218) and a path to WMI-provider persistence (T1546.003-adjacent). Alert on executions with DLLs in user-writable folders and check WMI provider registrations in root\cimv2.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
