---
created: 2026-11-21
fullpath: 'C:\Windows\System32\verclsid.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - verclsid.exe
  - Verclsid
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/2006/ms06-015
---

**fullpath**:C:\Windows\System32\verclsid.exe

# description

Verclsid.exe was introduced by security update MS06-015 and is used to verify a COM object before it is instantiated by Windows Explorer. It ships with Windows alongside shell32.dll.

## simple description

> ### 2026-11-21 Claude said
> verclsid.exe is a small helper that Explorer runs to test-load a shell extension (COM object) in a separate process before trusting it, so a broken or malicious extension cannot crash Explorer. You will see it briefly run with /S /C {CLSID} arguments. It is a normal Windows binary.
>
> **SOC NOTE**: Known LOLBin (T1218.012 Verclsid): `verclsid.exe /S /C {CLSID}` can load an attacker-registered COM object, for example one registered under HKCU (T1546.015 COM hijacking), to execute a DLL or scriptlet. Alert when its parent isn't explorer.exe or the CLSID resolves to a user-writable path.
>

# purpose

Verify a COM object before Windows Explorer instantiates it.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
