---
created: 2026-11-21
fullpath: 'C:\Windows\diagnostics\system\Audio\CL_LoadAssembly.ps1'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - troubleshooting-pack
aliases:
  - CL_LoadAssembly.ps1
url: []
---

**fullpath**:C:\Windows\diagnostics\system\Audio\CL_LoadAssembly.ps1

# description

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

## simple description

> ### 2026-11-21 Claude said
> CL_LoadAssembly.ps1 is a helper PowerShell script that ships inside the built-in Audio troubleshooting pack (Windows Troubleshooting Platform). Other scripts in the pack dot-source it to load .NET/C# helper code used during diagnosis. It is signed by Microsoft and normally runs only when the audio troubleshooter is started.
>
> **SOC NOTE**: Documented LOLBAS script: it exposes a `LoadAssemblyFromPath` function that can load an arbitrary .NET assembly from a Microsoft-signed script, used to proxy execution and bypass application control (MITRE ATT&CK T1216 System Script Proxy Execution). Alert when it is dot-sourced from an interactive PowerShell session or outside sdiagnhost.exe/msdt.exe, and review PowerShell 4104 script block logs.
> _Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
