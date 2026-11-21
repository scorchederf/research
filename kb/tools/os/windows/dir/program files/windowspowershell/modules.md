---
created: 2026-11-21
fullpath: 'C:\Program Files\WindowsPowerShell\Modules'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - powershell
  - modules
aliases:
  - 'Modules'
  - '$Env:ProgramFiles\WindowsPowerShell\Modules'
  - 'AllUsers module scope'
url:
  - https://learn.microsoft.com/powershell/scripting/developer/module/installing-a-powershell-module?view=powershell-7.6
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_psmodulepath?view=powershell-7.6
---

**fullpath**:C:\Program Files\WindowsPowerShell\Modules

# description

All-users module location for Windows PowerShell 5.1 (`$Env:ProgramFiles\WindowsPowerShell\Modules`), included in `$Env:PSModulePath` by default in Windows PowerShell 4.0 and later. PowerShell 7 uses `$Env:ProgramFiles\PowerShell\Modules` instead.

## simple description

> ### 2026-11-21 Claude said
> This is where PowerShell modules installed for every user on the machine live, for example modules from the PowerShell Gallery installed with `Install-Module -Scope AllUsers`. Because it's on PSModulePath, PowerShell auto-loads a module from here the first time you run one of its commands. Writing here needs admin rights.
>
> **SOC NOTE**: Persistence and hijack point: a malicious module, or a module that shadows a common command name, is auto-imported in every user's session (T1546.013 / T1059.001). Monitor file creation of .psm1/.psd1/.dll here, unsigned or recently added modules, and Install-Module activity. Useful in forensics to list third-party tooling (e.g. offensive frameworks) installed on a host.
>

# purpose

Install a module here to make it available to all user accounts on the computer. Each module must be in a subfolder whose name matches the base name of at least one file in the module (well-formed module) so PowerShell discovery and autoloading find it. Do not use `$PSHOME\Modules` (`%windir%\System32\WindowsPowerShell\v1.0\Modules`), which is reserved for modules that ship with Windows.

# common files found

| item | description |
| --- | --- |
| `<ModuleName>\` | One folder per module (optionally with version subfolders). |
| `<ModuleName>.psd1` | Module manifest. |
| `<ModuleName>.psm1` / `<ModuleName>.dll` | Script module or binary module assembly. |

