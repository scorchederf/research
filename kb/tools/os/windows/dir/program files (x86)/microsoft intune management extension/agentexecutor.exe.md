---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Intune Management Extension\AgentExecutor.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - intune
aliases:
  - "AgentExecutor.exe"
  - "Intune Management Extension"
  - "IME"
url:
  - https://learn.microsoft.com/intune/device-management/tools/run-powershell-scripts-windows
  - https://learn.microsoft.com/intune/device-management/tools/management-extension-windows
---

**fullpath**: C:\Program Files (x86)\Microsoft Intune Management Extension\AgentExecutor.exe

# description

AgentExecutor.exe is part of the Microsoft Intune Management Extension (IME), the agent that supplements Windows MDM to run PowerShell platform scripts, Win32 apps, remediations and custom compliance scripts. It executes Intune-deployed PowerShell scripts and its activity is logged to AgentExecutor.log.

## simple description

> ### 2026-11-21 Claude said
> AgentExecutor.exe is the Intune helper that actually launches PowerShell scripts that admins push from the Intune portal. It runs scripts either as SYSTEM or as the logged-on user, in a 32-bit or 64-bit PowerShell host. It is installed automatically when a script or Win32 app is assigned. Logs are in C:\ProgramData\Microsoft\IntuneManagementExtension\Logs.
>
> **SOC NOTE**: A compromised Intune admin account can push scripts that run as SYSTEM fleet-wide through AgentExecutor (T1072 Software Deployment Tools). Review AgentExecutor.log and IntuneManagementExtension.log, and the script cache under ProgramData\Microsoft\IntuneManagementExtension, when investigating suspicious PowerShell whose parent is AgentExecutor.exe. It is also a LOLBin that can launch PowerShell with an arbitrary script path.
>

# purpose

Executes PowerShell scripts deployed by Intune. Scripts time out after 30 minutes, are retried three times on failure, and run in a 32-bit host unless configured for 64-bit. AgentExecutor.log tracks PowerShell script executions; antivirus sandboxing AgentExecutor can cause scripts to falsely report success.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
