---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-PowerShell%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - powershell
aliases:
  - Microsoft-Windows-PowerShell%4Operational.evtx
  - Microsoft-Windows-PowerShell/Operational
  - PowerShell Operational log
url:
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_logging?view=powershell-5.1
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_group_policy_settings
  - https://learn.microsoft.com/powershell/scripting/security/security-features
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-windowspowershell
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/debug-customscriptextension-runcommand-scripts
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-PowerShell%4Operational.evtx

# description

This is the on-disk file of the **Microsoft-Windows-PowerShell/Operational** event log channel used by Windows PowerShell 5.1 (provider GUID `{A0C1853B-5C40-4B15-8766-3CF1C58F985A}`). Script Block Logging writes event 4104 here; the log is viewed in Event Viewer under Applications and Services Logs and managed with `wevtutil`. PowerShell 7 logs to a separate PowerShellCore/Operational channel.

## simple description

> ### 2026-11-21 Claude said
> This .evtx file stores the PowerShell Operational event log. It records PowerShell engine activity and, when Script Block Logging is enabled, the actual text of scripts and commands that PowerShell runs, even if they were obfuscated or encoded. The %4 in the file name stands for the "/" in the channel name. It is one of the most useful logs on a Windows host for incident response.
>
> **SOC NOTE**: Key events: 4104 (script block text, auto-logged as Warning for suspicious content even without the policy), 4103 (module/pipeline execution), 4105/4106 (start/stop), 40961/40962 (console start). Detects T1059.001, encoded commands, AMSI bypasses, download cradles. Attackers clear it (T1070.001: `wevtutil cl`) or downgrade to PowerShell v2 to avoid it - watch for log clears (event 104 in System) and gaps. Enable Protected Event Logging since script blocks may contain secrets.
>

# purpose

Stores PowerShell events. When Script Block Logging is enabled (Group Policy "Turn on PowerShell Script Block Logging", registry `HKLM\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging\EnableScriptBlockLogging = 1`, or Policy CSP), PowerShell records the processing of commands, script blocks, functions and scripts - interactive or automated - as EventId 4104 (0x1008), Channel Operational, Level Verbose, Opcode Create, Task CommandStart, Keyword Runspace. Enabling Script Block Invocation Logging additionally logs start/stop of invocations and produces high volume. Microsoft recommends enabling Protected Event Logging when using Script Block Logging for anything other than diagnostics. The default maximum log size shown on Learn is 15728640 bytes and can be changed or cleared with `wevtutil set-log` / `wevtutil clear-log "Microsoft-Windows-PowerShell/Operational"`.
