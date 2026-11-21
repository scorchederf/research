---
created: 2026-11-21
fullpath: 'c:\Program Files\WindowsPowerShell\Modules\Pester\<VERSION>\bin\Pester.bat'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - powershell
  - pester
aliases:
  - Pester.bat
  - Pester
url:
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_windows_powershell_5.1?view=powershell-5.1
---

**fullpath**:c:\Program Files\WindowsPowerShell\Modules\Pester\<VERSION>\bin\Pester.bat

# description

Pester.bat is a batch launcher inside the Pester PowerShell test framework module that ships in-box with Windows PowerShell. Microsoft Learn notes that WMF 5.1 ships with Pester v3.4.0; the batch file itself is not described on Learn.

## simple description

> ### 2026-11-21 Claude said
> Pester is the testing framework for PowerShell, and Windows ships an old copy (3.4.0) under the Windows PowerShell module folder. Pester.bat in its bin folder is a small wrapper that starts powershell.exe and runs Invoke-Pester so tests can be run from cmd. It is normal to find it on Windows 10/11 and Server. Most developers install a newer Pester from the PowerShell Gallery side by side.
>
> **SOC NOTE**: Pester.bat is a known LOLBAS entry: because it passes its arguments into a PowerShell invocation, it can be abused to execute arbitrary PowerShell commands via a signed-path batch file (T1216 System Script Proxy Execution / T1059.001). Look for cmd.exe or Pester.bat launching powershell.exe with unusual arguments in process creation logs (4688 / Sysmon 1).
>
> _Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_
