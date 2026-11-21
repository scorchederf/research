---
created: 2026-11-21
fullpath: 'C:\Windows\diagnostics\system\WindowsUpdate\CL_Mutexverifiers.ps1'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - powershell
  - troubleshooter
aliases:
  - CL_Mutexverifiers.ps1
url:
---

**fullpath**:C:\Windows\diagnostics\system\WindowsUpdate\CL_Mutexverifiers.ps1

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> CL_Mutexverifiers.ps1 is a PowerShell helper script that belongs to the built-in Windows Update troubleshooter package in C:\Windows\diagnostics. Troubleshooter packs are run by the diagnostics framework (msdt/sdiagnhost) to check and fix common problems. This script contains helper functions used by the troubleshooter.
>
> **SOC NOTE**: Signed troubleshooting scripts in C:\Windows\diagnostics are known LOLBAS candidates: CL_Mutexverifiers.ps1 exposes a function (`runAfterCancelProcess`) that can be dot-sourced to launch an arbitrary process, enabling signed-script proxy execution (MITRE ATT&CK T1216 System Script Proxy Execution). Alert on powershell.exe importing or dot-sourcing scripts from this folder outside of sdiagnhost.exe.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
