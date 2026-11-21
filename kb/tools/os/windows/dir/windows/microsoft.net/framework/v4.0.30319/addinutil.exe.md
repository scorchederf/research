---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
aliases:
  - AddinUtil.exe
  - addinutil.exe
url:
  - https://learn.microsoft.com/defender-endpoint/defender-endpoint-exclusions-common-mistakes
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe

# description

AddinUtil.exe is a .NET Framework utility in the Framework v4.0.30319 directory. Microsoft lists addinutil.exe (with addinprocess.exe and addinprocess32.exe) among the processes attackers can abuse and that you shouldn't exclude from Microsoft Defender Antivirus or Defender for Endpoint scanning.

## simple description

> ### 2026-11-21 Claude said
> AddinUtil.exe is the .NET Framework Add-in Utility, used to build and maintain the add-in pipeline store cache (AddIns.store) for the System.AddIn model. It ships with .NET Framework 4.x and is rarely used by modern software. Normal users never run it.
>
> **SOC NOTE**: LOLBAS documents AddinUtil.exe executing code by loading a crafted AddIns.store file from the working directory (`AddinUtil.exe -AddinRoot:.`), deserializing attacker-controlled data (MITRE ATT&CK T1218 System Binary Proxy Execution). Alert on any execution, especially with `-AddinRoot`/`-PipelineRoot` pointing at user-writable paths or with unusual parents.
>

# purpose

Manage the .NET Framework add-in pipeline; Microsoft recommends never excluding it from antivirus scanning.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
