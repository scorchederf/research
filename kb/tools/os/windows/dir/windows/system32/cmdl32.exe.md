---
created: 2026-11-21
fullpath: 'C:\Windows\System32\cmdl32.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
aliases:
  - "cmdl32.exe"
  - "Connection Manager Auto-Download"
url:
  []
---

**fullpath**:C:\Windows\System32\cmdl32.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> Cmdl32.exe is the Microsoft Connection Manager Auto-Download utility. Connection Manager profiles (built with the Connection Manager Administration Kit) use it to download phonebook and VPN configuration updates from a server. It is a legacy component that most users never run directly.
>
> **SOC NOTE**: Listed in LOLBAS as a download utility: with a crafted profile/settings file and the `/vpn /lan` switches it can fetch an arbitrary file from a URL into %TMP% (MITRE ATT&CK T1105 Ingress Tool Transfer). Any cmdl32.exe execution outside managed VPN deployments, especially paired with an environment-variable change to TMP, should be investigated.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
