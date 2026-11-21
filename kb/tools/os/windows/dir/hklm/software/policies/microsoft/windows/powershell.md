---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - powershell
  - group-policy
aliases:
  - PowerShell
  - Windows PowerShell policy key
url:
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-powershellexecutionpolicy
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-windowspowershell
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_group_policy_settings
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_logging
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/debug-customscriptextension-runcommand-scripts
  - https://learn.microsoft.com/exchange/executionpolicy-gpo-is-defined-exchange-2013-help
---

**fullpath**:HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell

# description

Registry key that stores the Windows PowerShell Group Policy settings defined in `PowerShellExecutionPolicy.admx` (Computer Configuration > Administrative Templates > Windows Components > Windows PowerShell). It holds the "Turn on Script Execution" setting and parent subkeys for module logging and script block logging. The same settings can also be delivered through the Policy CSP (`ADMX_PowerShellExecutionPolicy`, `WindowsPowerShell`).

## simple description

> ### 2026-11-21 Claude said
> This key is where Group Policy writes machine-wide rules for Windows PowerShell. It decides which scripts are allowed to run (the execution policy) and whether PowerShell activity is logged. Subkeys such as ScriptBlockLogging, ModuleLogging and Transcription turn on detailed logging of what PowerShell actually executes. Because it lives under Policies, values here override settings users or admins set with `Set-ExecutionPolicy`.
>
> **SOC NOTE**: Attackers often disable or weaken these settings (e.g. set `EnableScriptBlockLogging` to 0, delete the key, or set `ExecutionPolicy` to Unrestricted/Bypass) to evade detection (MITRE ATT&CK T1562.002/T1562.001, T1059.001). Monitor registry changes to this key (Sysmon Event ID 13, Security 4657). When enabled, script block logging writes Event ID 4104 to Microsoft-Windows-PowerShell/Operational, and module logging writes Event ID 4103 - prime sources for decoding obfuscated PowerShell.
>

# purpose

Holds the computer-scope Windows PowerShell Group Policy settings. "Turn on Script Execution" maps to the `EnableScripts` value in this key; if enabled, the chosen option (Allow only signed scripts = `AllSigned`, Allow local scripts and remote signed scripts = `RemoteSigned`, Allow all scripts = `Unrestricted`) applies, and if disabled no scripts run (`Restricted`). The Computer Configuration setting takes precedence over User Configuration. Script block logging (subkey `ScriptBlockLogging`) logs all PowerShell script input to the Microsoft-Windows-PowerShell/Operational event log, and module logging (subkey `ModuleLogging`) records pipeline execution events for the specified modules.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide (Computer Configuration policy) |

# values

| value name | type | description |
| --- | --- | --- |
| `EnableScripts` | string (policy) | Set by "Turn on Script Execution"; controls whether scripts are allowed to run. |
| `ExecutionPolicy` | string | Execution policy selected by the policy (MachinePolicy scope). Exchange 2013 Setup fails if it is defined; it can be cleared with `Set-ItemProperty ... -Name ExecutionPolicy -Value ""`. |

# subkeys

| subkey | description |
| --- | --- |
| `ScriptBlockLogging` | Holds `EnableScriptBlockLogging` (REG_DWORD 1 = on); "Turn on PowerShell Script Block Logging", logs to Microsoft-Windows-PowerShell/Operational. |
| `ModuleLogging` | Holds `EnableModuleLogging` (REG_DWORD); "Turn on Module Logging". |
| `ModuleLogging\ModuleNames` | REG_SZ values naming the modules to log (`*` = all modules). |
| `Transcription` | "Turn on PowerShell Transcription"; captures input and output of PowerShell commands into text transcripts. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell" /s` | List the key, its subkeys (logging settings) and values. |
| `reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" /v "EnableScriptBlockLogging" /t REG_DWORD /d 1 /f` | Turn on script block logging. |
| `reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging" /v "EnableModuleLogging" /t REG_DWORD /d 1 /f` | Turn on module logging. |
| `Get-ExecutionPolicy -List` | Show the effective execution policy per scope, including MachinePolicy set from this key. |
