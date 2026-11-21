---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v2.0.50727\Applaunch.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - dotnet
  - clickonce
  - exe
aliases:
  - "AppLaunch.exe"
  - "Microsoft .NET ClickOnce Launch Utility"
url: []
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v2.0.50727\Applaunch.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> AppLaunch.exe is the .NET Framework 2.0 'ClickOnce Launch Utility', used to start ClickOnce and partially trusted applications in the correct security context. It lives in the 32-bit v2.0.50727 Framework folder (also used by .NET 3.0/3.5). It takes the path of a .NET executable or manifest to launch.
>
> **SOC NOTE**: Frequently abused as a process-hollowing / injection host: malware families (e.g. AgentTesla, RedLine, AsyncRAT loaders) spawn AppLaunch.exe suspended and inject payloads (T1055.012) to blend with a signed Microsoft binary. Alert on AppLaunch.exe making network connections or running without a ClickOnce parent.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
