---
created: 2026-11-21
fullpath: 'C:\Users\<username>\Documents\WindowsPowerShell'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - powershell
aliases:
  - WindowsPowerShell
  - $HOME\Documents\WindowsPowerShell
url:
  - https://learn.microsoft.com/powershell/scripting/whats-new/migrating-from-windows-powershell-51-to-powershell-7
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_psmodulepath
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles
---

**fullpath**:C:\Users\<username>\Documents\WindowsPowerShell

# description

Per-user folder used by Windows PowerShell 5.1 for the current user's profile scripts and CurrentUser-scope modules. PowerShell 7 uses the separate `$HOME\Documents\PowerShell` folder instead. The Documents location can be redirected by folder redirection or OneDrive.

## simple description

> ### 2026-11-21 Claude said
> This is the personal settings folder for Windows PowerShell 5.1. Scripts called profiles in here run automatically every time the user starts PowerShell. The Modules subfolder holds PowerShell modules the user installed only for themselves. It is created on demand, so it may not exist on every machine.
>
> **SOC NOTE**: Profile scripts (profile.ps1, Microsoft.PowerShell_profile.ps1) are a persistence location (MITRE ATT&CK T1546.013 PowerShell Profile); check for unexpected code, encoded commands or downloads. Rogue modules in Modules\ can hijack commands. Review file creation/modification times and Sysmon Event ID 11.
>

# purpose

Holds the CurrentUser profile location for Windows PowerShell 5.1 and the CurrentUser module scope `$HOME\Documents\WindowsPowerShell\Modules`, which is included in `$Env:PSModulePath`.

# common files found

- `profile.ps1` / `Microsoft.PowerShell_profile.ps1` - current-user profile scripts
- `Modules\` - CurrentUser-scope modules (e.g. modules installed with `Install-Module -Scope CurrentUser`)
