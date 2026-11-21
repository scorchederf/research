---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - windows
aliases:
  - "ConsoleHost_history.txt"
  - "PSReadLine history"
  - "HistorySavePath"
url:
  - https://learn.microsoft.com/powershell/module/psreadline/about/about_psreadline
  - https://learn.microsoft.com/powershell/module/psreadline/get-psreadlineoption
  - https://learn.microsoft.com/powershell/module/psreadline/set-psreadlineoption
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_history
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

# description

ConsoleHost_history.txt is the PSReadLine command history file for the PowerShell console host. PSReadLine names the file `$($Host.Name)_history.txt` and stores it in `$Env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine`; the path is shown by `HistorySavePath` in `Get-PSReadLineOption`. Other hosts get their own file, e.g. `Visual Studio Code Host_history.txt`.

## simple description

> ### 2026-11-21 Claude said
> This plain-text file contains every command a user typed into an interactive PowerShell console, across all sessions, and it survives after the session ends. It is separate from the in-session history shown by Get-History. Lines containing words like password, token, apikey or secret are filtered out. Scripts run non-interactively do not appear here.
>
> **SOC NOTE**: One of the best quick-win artifacts in an investigation: it shows attacker hands-on-keyboard PowerShell activity (MITRE ATT&CK T1059.001) including download cradles, recon and lateral movement commands. Attackers may delete it, run `Set-PSReadLineOption -HistorySaveStyle SaveNothing` or `Remove-Module PSReadLine` (T1070.003 Clear Command History). Check every user profile, and correlate with Script Block Logging (Event 4104).
>

# purpose

Stores the PSReadLine history for the ConsoleHost. History is written to a central file per host, available to all sessions and not deleted when a session ends; it cannot be managed by the `*-History` cmdlets. The location and behaviour can be changed with `Set-PSReadLineOption -HistorySavePath`, `-HistorySaveStyle` (default SaveIncrementally), `-MaximumHistoryCount` (default 4096) and `-AddToHistoryHandler`. PSReadLine 2.2.0+ uses the AST to filter sensitive data and allows SecretManagement cmdlets such as `Get-Secret`.


