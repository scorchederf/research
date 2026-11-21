---
created: 2026-11-21
fullpath: 'C:\Windows\diagnostics\system\Networking\UtilityFunctions.ps1'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - powershell
  - troubleshooting-pack
aliases:
  - "UtilityFunctions.ps1"
url: []
---

**fullpath**: C:\Windows\diagnostics\system\Networking\UtilityFunctions.ps1

# description

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

## simple description

> ### 2026-11-21 Claude said
> UtilityFunctions.ps1 is a PowerShell helper script inside the built-in Windows Networking troubleshooting pack (the "Network and Internet" troubleshooter). It contains shared functions used by the pack's detection and resolution scripts, which are run by the Scripted Diagnostics host (sdiagnhost.exe) through msdt.exe. It is Microsoft-signed and ships with the operating system.
>
> **SOC NOTE**: Microsoft-signed scripts in C:\Windows\diagnostics have been abused for proxy execution and AMSI/signing bypasses, e.g. dot-sourcing a signed script to reach helper functions or abusing the msdt troubleshooting framework (CVE-2022-30190 "Follina", T1216 System Script Proxy Execution, T1218). Alert on powershell.exe or sdiagnhost.exe loading scripts from this folder outside normal troubleshooter use, especially from Office parents, and on any modification of files here.
>
> _Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_
