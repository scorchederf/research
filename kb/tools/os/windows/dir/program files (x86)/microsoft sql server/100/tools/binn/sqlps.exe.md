---
created: 2026-11-21
fullpath: 'C:\Program files (x86)\Microsoft SQL Server\100\Tools\Binn\sqlps.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - sql-server
  - powershell
aliases:
  - sqlps.exe
  - sqlps utility
url:
  - https://learn.microsoft.com/sql/tools/sqlps-utility
---

**fullpath**:C:\Program files (x86)\Microsoft SQL Server\100\Tools\Binn\sqlps.exe

# description

The **sqlps** utility starts a Windows PowerShell session with the SQL Server PowerShell provider and cmdlets loaded. The SQL Server 2008 (version 100) build is a Windows PowerShell 1.0 mini-shell; the feature is deprecated in favor of the `sqlps`/SqlServer PowerShell module.

## simple description

> ### 2026-11-21 Claude said
> sqlps.exe is a SQL Server 2008-era PowerShell host with the SQL Server cmdlets (like Invoke-Sqlcmd) preloaded. Database admins use it to script and manage SQL Server. It is signed by Microsoft and lives in the SQL Server Tools\Binn folder.
>
> **SOC NOTE**: Known LOLBin (LOLBAS): it can run PowerShell commands while not being named powershell.exe, which can bypass naive detections or app-control rules targeting powershell.exe (T1059.001, T1218). Alert on sqlps.exe spawned by unusual parents or with -Command content like download cradles; PowerShell logging (4104) still applies.
>

# purpose

Interactively run PowerShell commands, run script files, run SQL Server cmdlets, and navigate SQL Server objects through provider paths. Runs with the execution policy set to Restricted by default. Loads `Microsoft.SqlServer.Management.PSProvider.dll` (provider, `Encode-SqlName`, `Decode-SqlName`) and `Microsoft.SqlServer.Management.PSSnapin.dll` (`Invoke-Sqlcmd`, `Invoke-PolicyEvaluation`).

# typical use cases

| usage | description |
| --- | --- |
| `sqlps -NoLogo` | Run sqlps interactively without the copyright banner. |
| `sqlps -Command "&{.\MyFolder.MyScript.ps1}"` | Run a SQL Server PowerShell script from the command prompt. |
| `sqlps -NoExit -Command "&{.\MyFolder.MyScript.ps1}"` | Run a script and keep running after it completes. |

# options

| option | description |
| --- | --- |
| `-NoLogo` | Hides the copyright banner at startup. |
| `-NoExit` | Keeps running after the startup commands complete. |
| `-NoProfile` | Does not load a user profile. |
| `-OutPutFormat { Text \| XML }` | Formats output as text strings or serialized CLIXML. |
| `-InPutFormat { Text \| XML }` | Treats input as text strings or serialized CLIXML. |
| `-Command` | Command to run, then exit unless `-NoExit` is given; switches after it are read as command parameters. |
| `-` | With `-Command`, reads input from standard input. |
| `script_block [ -args argument_array ]` | Block of PowerShell commands in braces; only when called from PowerShell or another sqlps session. |
| `string [ command_parameters ]` | String of PowerShell commands in the format `"&{<command>}"`. |
| `-? \| -Help` | Shows the syntax summary. |
