---
created: 2026-11-21
fullpath: 'C:\Windows\WinSxS\amd64_microsoft-windows-u..ed-telemetry-client_31bf3856ad364e35_10.0.16299.15_none_c2df1bba78111118\Runscripthelper.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lolbin
  - telemetry
  - appcontrol
aliases:
  - Runscripthelper.exe
  - runscripthelper.exe
url:
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/design/applications-that-can-bypass-appcontrol
---

**fullpath**:C:\Windows\WinSxS\amd64_microsoft-windows-u..ed-telemetry-client_31bf3856ad364e35_10.0.16299.15_none_c2df1bba78111118\Runscripthelper.exe

# description

`runscripthelper.exe` is a Windows binary in the WinSxS component store of the unified telemetry client. Microsoft lists it among applications that attackers can use to bypass App Control for Business and recommends blocking it unless explicitly required.

## simple description

> ### 2026-11-21 Claude said
> Runscripthelper.exe is a Microsoft-signed helper from the Windows telemetry (diagnostics) client, shipped in some Windows 10 builds such as 1709 (10.0.16299). It was meant to run PowerShell diagnostic scripts for telemetry. Because it is signed by Microsoft, it can be abused to run arbitrary PowerShell. Normal users never run it directly.
>
> **SOC NOTE**: LOLBin (T1218 / T1059.001): `runscripthelper.exe surfacecheck \\?\C:\path\script.txt C:\path` runs an attacker's PowerShell script while bypassing constrained language mode / App Control. Any execution is suspicious; hunt for process creation (4688/Sysmon 1) of runscripthelper.exe and child PowerShell activity. Block it via App Control deny rules.
>

# purpose

Listed by Microsoft as an application that can be used to circumvent application allow policies, including App Control; Microsoft recommends blocking it unless your scenarios require it.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
