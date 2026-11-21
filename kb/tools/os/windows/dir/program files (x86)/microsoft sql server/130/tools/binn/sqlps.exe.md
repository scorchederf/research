---
created: 2026-11-21
fullpath: 'C:\Program files (x86)\Microsoft SQL Server\130\Tools\Binn\sqlps.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - sqlserver
  - lolbin
aliases:
  - sqlps.exe
  - sqlps utility
url:
  - https://learn.microsoft.com/sql/tools/sqlps-utility?view=sql-server-ver17
  - https://learn.microsoft.com/powershell/sql-server/run-windows-powershell-steps-in-sql-server-agent?view=sqlserver-ps
---

**fullpath**:C:\Program files (x86)\Microsoft SQL Server\130\Tools\Binn\sqlps.exe

# description

The sqlps utility starts a PowerShell session with the SQL Server PowerShell provider and cmdlets loaded (Invoke-Sqlcmd, Invoke-PolicyEvaluation, Encode/Decode-SqlName). Version 130 corresponds to SQL Server 2016. It is deprecated in favor of the SqlServer module and is used by SQL Server Agent PowerShell job steps.

## simple description

> ### 2026-11-21 Claude said
> sqlps.exe is a PowerShell launcher that comes with SQL Server and preloads the SQL Server cmdlets. DBAs use it to run scripts against SQL instances, and SQL Server Agent uses it for PowerShell job steps. It is deprecated but still installed with many SQL Server versions. It behaves like powershell.exe with extra modules.
>
> **SOC NOTE**: LOLBAS: sqlps.exe can run arbitrary PowerShell (T1059.001) and may evade rules that only look for powershell.exe; check for `-Command`/`-NoProfile` usage from unusual parents. SQL Agent job steps spawning sqlps.exe can indicate persistence via SQL Agent jobs.
>

# purpose

Run PowerShell interactively or run scripts and SQL Server cmdlets with the SQL Server provider.

# typical use cases

| usage | description |
| --- | --- |
| `sqlps -NoLogo` | Run interactively without the copyright banner. |
| `sqlps -Command "&{.\MyFolder.MyScript.ps1}"` | Run a SQL Server PowerShell script from the command prompt. |
| `sqlps -NoExit -Command "&{.\MyFolder.MyScript.ps1}"` | Run a script and keep the session open afterwards. |

# options

| option | description |
| --- | --- |
| `-NoLogo` | Hides the copyright banner. |
| `-NoExit` | Keeps running after startup commands complete. |
| `-NoProfile` | Does not load a user profile. |
| `-OutPutFormat { Text \| XML }` | Formats output as text or serialized CLIXML. |
| `-InPutFormat { Text \| XML }` | Treats input as text or serialized CLIXML. |
| `-Command` | Runs the command and exits unless `-NoExit`; switches after it are read as command parameters. |
| `-` | With `-Command`, reads input from standard input. |
| `script_block [ -args argument_array ]` | Block of PowerShell commands in braces; only when called from PowerShell or sqlps. |
| `string [ command_parameters ]` | String with PowerShell commands in the form `"{<command>}"`. |
| `-?` \| `-Help` | Shows the syntax summary. |
