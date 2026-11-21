---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Silverlight\5.1.50918.0\coregen.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - silverlight
aliases:
  - coregen.exe
url:
  - https://learn.microsoft.com/lifecycle/announcements/silverlight-end-of-support
---

**fullpath**:C:\Program Files\Microsoft Silverlight\5.1.50918.0\coregen.exe

# description

`coregen.exe` is a binary shipped with Microsoft Silverlight 5.1 (build 5.1.50918.0). Microsoft Learn documents only that Silverlight reached end of support on October 12, 2021; coregen.exe itself is not described.

## simple description

> ### 2026-11-21 Claude said
> coregen.exe is part of Microsoft Silverlight, the retired browser plug-in. It generates native images (precompiled code) for Silverlight's core .NET assemblies, similar to ngen for the .NET Framework, to speed up Silverlight app startup. Silverlight is end of life, so this file usually indicates an old install that should be removed.
>
> **SOC NOTE**: coregen.exe is a signed Microsoft LOLBin that can load an arbitrary DLL via its `/L` parameter (MITRE T1218 System Binary Proxy Execution). Alert on coregen.exe running with `/L` or loading DLLs from user-writable paths. Silverlight itself is unsupported and has known vulnerabilities, so its presence is a hygiene finding.
>

# purpose

Silverlight is supported only on Internet Explorer 10 and 11 and reached end of support on October 12, 2021. The specific purpose of coregen.exe is _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
