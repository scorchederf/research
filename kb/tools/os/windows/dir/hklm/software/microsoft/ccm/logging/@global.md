---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\CCM\Logging\@Global'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - configmgr
  - logging
aliases:
  - "@Global"
  - "CCM global logging settings"
url:
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files
  - https://learn.microsoft.com/troubleshoot/mem/configmgr/update-management/enable-verbose-logging
  - https://learn.microsoft.com/intune/configmgr/develop/reference/core/clients/client-classes/setgloballoggingconfiguration-method-in-class-sms_client
---

**fullpath**:HKLM\SOFTWARE\Microsoft\CCM\Logging\@Global

# description

Registry key holding the global logging configuration for the Configuration Manager (ConfigMgr/SCCM) client and management point components (the CCM component). It controls log verbosity, maximum log size and number of history files for logs under %WinDir%\CCM\Logs. It can also be set via the SMS_Client SetGlobalLoggingConfiguration method, client installation properties, or Client Diagnostics in the console.

## simple description

> ### 2026-11-21 Claude said
> This key controls how much the Configuration Manager client writes to its log files (C:\Windows\CCM\Logs). LogLevel 0 means verbose, 1 default; LogMaxSize and LogMaxHistory control how big the logs get and how many old copies are kept. Admins change it temporarily when troubleshooting.
>
> **SOC NOTE**: CCM logs are valuable forensic sources (software deployment, scripts run, inventory). An attacker reducing LogLevel to 3, shrinking LogMaxSize or setting LogMaxHistory to 0 can cut evidence (T1562.002 Impair Defenses: Disable Windows Event Logging, analogous). Monitor writes to this key.
>

# purpose

Configures logging options for all components on a Configuration Manager client or management point. Changes take effect after restarting the SMS Agent Host service (CcmExec). Microsoft notes the keys shouldn't normally be manipulated directly, and other values that may exist in the key shouldn't be changed. Debug logging is configured separately under HKLM\SOFTWARE\Microsoft\CCM\Logging\DebugLogging (Enabled = True).

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `LogLevel` | REG_DWORD | Level of detail written to log files: 0 Verbose, 1 Default, 2 Warnings and errors, 3 Errors only. |
| `LogMaxHistory` | REG_DWORD | Number of previous log versions to keep when a log reaches maximum size; 0 no history, 1 default. |
| `LogMaxSize` | REG_DWORD | Maximum log file size in bytes (at least 10,000); default 250,000. 5242880 increases logs to 5 MB. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\CCM\Logging\@Global"` | List the key's values. |
