---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\PowerShellCore%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - event-log
  - powershell
aliases:
  - "PowerShellCore%4Operational.evtx"
  - "PowerShellCore/Operational"
url:
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_logging_windows?view=powershell-7.6
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-7.6
---

**fullpath**: C:\Windows\System32\winevt\Logs\PowerShellCore%4Operational.evtx

# description

Event log file backing the **PowerShellCore/Operational** channel written by PowerShell 7 (PowerShell Core) on Windows. The log appears in Event Viewer under **Application and Services Logs > PowerShellCore**; its ETW provider GUID is `{f90714a8-5509-434a-bf6d-b1624c8a19a2}`. It is separate from the Windows PowerShell 5.1 log, Microsoft-Windows-PowerShell/Operational.

## simple description

> ### 2026-11-21 Claude said
> This file stores the operational event log of PowerShell 7 (pwsh.exe). The `%4` in the file name stands for the `/` in the channel name PowerShellCore/Operational. It records engine start-up, runspace activity and, when Script Block Logging is enabled, the text of scripts that ran. It only gets events after PowerShell 7's event manifest has been registered (RegisterManifest.ps1, done by the installer).
>
> **SOC NOTE**: Key evidence for T1059.001 (PowerShell). Event 4104 holds de-obfuscated script block text; 40961/40962 mark console start-up. Attackers who know defenders watch Microsoft-Windows-PowerShell/Operational may use pwsh.exe instead, so collect this log too. Clearing or unregistering the provider (RegisterManifest.ps1 -Unregister) is a defence-evasion signal (T1070.001 / T1562.002).
>

# purpose

Stores PowerShell 7 events. When Script Block Logging is enabled, PowerShell logs event ID 4104 (`0x1008`, Channel Operational, Level Verbose, Opcode Create, Task CommandStart, Keyword Runspace) to this log. Other events seen in it include 40961 (console is starting up), 40962 (console is ready for user input), 8195 (Opening RunspacePool) and 8197 (Runspace state changed). The provider must be unregistered with `$PSHOME\RegisterManifest.ps1 -Unregister` before updating PowerShell and re-registered afterwards. Archived copies can be read with `Get-WinEvent -Path`.
