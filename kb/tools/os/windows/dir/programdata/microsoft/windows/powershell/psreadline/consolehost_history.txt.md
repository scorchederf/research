---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - powershell
  - forensics
aliases:
  - ConsoleHost_history.txt
  - PSReadLine history file
url:
  - https://learn.microsoft.com/powershell/module/psreadline/about/about_psreadline?view=powershell-7.6
  - https://learn.microsoft.com/powershell/module/psreadline/get-psreadlineoption?view=powershell-7.6
  - https://learn.microsoft.com/powershell/module/psreadline/set-psreadlineoption?view=powershell-7.6
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_history?view=powershell-7.6
---

**fullpath**:C:\ProgramData\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

# description

PSReadLine command history file for the PowerShell console host. PSReadLine names the file `$($Host.Name)_history.txt` (one per host, so `ConsoleHost_history.txt` for the console). Microsoft Learn documents the default location as `$Env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine` (per user, under AppData\Roaming), changeable with `Set-PSReadLineOption -HistorySavePath`; a copy under ProgramData is not a documented default.

## simple description

> ### 2026-11-21 Claude said
> This text file contains every command typed into interactive PowerShell console sessions, saved by the PSReadLine module across sessions. It normally lives in each user's AppData\Roaming profile; a file under ProgramData is unusual and may indicate a SYSTEM-context profile, a custom HistorySavePath, or a copied file. It is plain text and survives after PowerShell closes.
>
> **SOC NOTE**: PSReadLine history is a top-tier forensic artifact showing attacker commands (MITRE ATT&CK T1059.001) and may leak credentials typed on the command line (T1552.001). Attackers delete it, run `Set-PSReadLineOption -HistorySaveStyle SaveNothing`, or unload PSReadLine to hide activity (T1070.003). It does not record commands run non-interactively (scripts, `-EncodedCommand`), so pair it with 4104 script block logs.
>

# purpose

Persists PSReadLine command history so it is available to all sessions of the host; it is not deleted when a session ends and cannot be managed with the `*-History` cmdlets. PSReadLine tries to filter sensitive data: command lines containing `password`, `asplaintext`, `token`, `apikey` or `secret` aren't written (PSReadLine 2.2.0 uses the AST and an allowlist of SecretManagement cmdlets). The history may still contain sensitive data. Use `Get-PSReadLineOption` to see the effective `HistorySavePath` and `HistorySaveStyle`.
