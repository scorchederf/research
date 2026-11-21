---
created: 2026-11-21
fullpath: 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - powershell
aliases:
  - powershell_ise.exe
  - PowerShell_ISE
  - ISE
  - Windows PowerShell Integrated Scripting Environment
url:
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_powershell_ise_exe?view=powershell-5.1
  - https://learn.microsoft.com/windows-server/administration/windows-commands/powershell_ise
  - https://learn.microsoft.com/powershell/scripting/windows-powershell/ise/introducing-the-windows-powershell-ise?view=powershell-7.6
---

**fullpath**:C:\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe

# description

`powershell_ise.exe` starts the Windows PowerShell Integrated Scripting Environment (ISE), a graphical host for Windows PowerShell for writing, running, testing and debugging scripts. It ships with Windows and supports Windows PowerShell up to 5.1; it is no longer in feature development and isn't supported for PowerShell 6+, where Visual Studio Code with the PowerShell extension is recommended. It doesn't run on Server Core.

## simple description

> ### 2026-11-21 Claude said
> PowerShell ISE is the built-in graphical script editor for Windows PowerShell 5.1. It has a script pane, a console pane, IntelliSense and a debugger. Admins use it to write and test scripts.
>
> **SOC NOTE**: An alternative PowerShell host (T1059.001): commands run here are still captured by script block logging (4104) and AMSI, but some detections only look for `powershell.exe`. ISE on servers or user desktops where it isn't normally used, ISE launched with `-NoProfile` from unusual parents, or remote tabs to other hosts are worth checking. It has its own profile (`Microsoft.PowerShellISE_profile.ps1`), a persistence location (T1546.013).
>

# purpose

Provides a graphical environment with multiline editing, tab completion, syntax coloring, selective execution, context-sensitive help, visual debugging, snippets and Show-Command.

# typical use cases

| usage | description |
| --- | --- |
| `powershell_ise.exe` | Start a Windows PowerShell ISE session (also `powershell_ise` or `ISE`). |
| `powershell_ise.exe -File .\Get-Profile.ps1` | Open a script in ISE. |
| `ISE -File ".\Get-Backups.ps1,Get-BackupInstance.ps1"` | Open several files; separate names with commas inside one quoted string. |
| `ISE -NoProfile` | Start ISE without running PowerShell profiles. |
| `ISE -Help` | Show help for `powershell_ise.exe`. |

# options

| option | description |
| --- | --- |
| `-File <FilePath[]>` | Opens the specified files in ISE; the parameter name is optional. Any text file can be opened. |
| `-MTA` | Starts ISE in a multi-threaded apartment (STA is the default). Introduced in Windows PowerShell 3.0. |
| `-NoProfile` | Does not run Windows PowerShell profiles. |
| `-Help`, `-?`, `/?` | Displays the syntax and describes the command-line switches. |
