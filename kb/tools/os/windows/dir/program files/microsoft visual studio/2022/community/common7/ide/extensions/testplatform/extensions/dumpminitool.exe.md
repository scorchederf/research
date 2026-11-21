---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\Extensions\TestPlatform\Extensions\DumpMinitool.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visual-studio
aliases:
  - DumpMinitool.exe
url:
---

**fullpath**:C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\Extensions\TestPlatform\Extensions\DumpMinitool.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> DumpMinitool.exe is a small helper shipped with the Visual Studio Test Platform (VSTest). It is used by the blame data collector to write crash or hang memory dumps of test host processes. It is normally started automatically by vstest/dotnet test, not by users.
>
> **SOC NOTE**: DumpMinitool.exe is a signed Microsoft binary that can write a memory dump of an arbitrary process given its PID (e.g. `--file out.dmp --processId <pid> --dumpType Full`), so it is a documented LOLBin for dumping lsass.exe (MITRE ATT&CK T1003.001). Alert when it runs outside of test runs, targets lsass, or is copied out of its Visual Studio folder.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
