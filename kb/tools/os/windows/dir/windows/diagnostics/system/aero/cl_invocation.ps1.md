---
created: 2026-11-21
fullpath: 'C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - CL_Invocation.ps1
url:
---

**fullpath**:C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> CL_Invocation.ps1 is a PowerShell helper script shipped inside the built-in Aero troubleshooting pack under `C:\Windows\diagnostics\system\AERO`. Troubleshooting packs are collections of PowerShell scripts run by the Windows Troubleshooting Platform. This script defines helper functions, notably `SyncInvoke`, that start a process and wait for it. It is Microsoft-signed and normally only run by the troubleshooting engine.
>
> **SOC NOTE**: CL_Invocation.ps1 is a signed-script proxy LOLBAS: dot-sourcing it and calling `SyncInvoke <command>` executes arbitrary programs from a Microsoft-signed script, which can bypass script-signing or application control policies (MITRE ATT&CK T1216 System Script Proxy Execution). Hunt for PowerShell command lines or ScriptBlock logs (Event 4104) referencing `CL_Invocation.ps1` or `SyncInvoke` outside the troubleshooting engine (`sdiagnhost.exe`).
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
