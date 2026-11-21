---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\IntuneManagementExtension'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - intune
aliases:
  - "IntuneManagementExtension"
  - "Intune management extension (IME)"
  - "SideCar"
url:
  - https://learn.microsoft.com/intune/device-management/tools/management-extension-windows
  - https://learn.microsoft.com/intune/app-management/deployment/troubleshoot-win32
---

**fullpath**: HKLM\SOFTWARE\Microsoft\IntuneManagementExtension

# description

Registry key of the Microsoft Intune management extension (IME), the agent that gives Intune its Win32 app, PowerShell script, remediation, custom compliance discovery, Endpoint analytics, Remote Help and managed installer capabilities on Windows. The IME installs automatically when one of those features is assigned to a user or device and runs as the **IntuneManagementExtension** service. Microsoft Learn documents the agent, its logs (`C:\ProgramData\Microsoft\IntuneManagementExtension\Logs`) and content folders, but not the contents of this registry key.

## simple description

> ### 2026-11-21 Claude said
> This key holds the local state of the Intune Management Extension, the agent Intune uses to install Win32 apps and run PowerShell scripts and remediations on Windows. Subkeys such as Win32Apps, Policies and SideCarPolicies track which apps and scripts were received and their install/detection results and retry state. Admins sometimes delete parts of it to force an app or script to re-run.
>
> **SOC NOTE**: The IME runs scripts and installers as SYSTEM, so a compromised Intune tenant is a powerful lateral-movement/execution channel (T1072 Software Deployment Tools). This key and the IME logs (AgentExecutor.log, AppWorkload.log, HealthScripts.log) show which scripts/apps were delivered and when - useful to confirm or rule out malicious deployments. Deleting entries here to re-trigger or hide deployments is suspicious.
>

# purpose

Supports the IME agent, which silently authenticates to Intune, checks for new or updated installations every 8 hours (independent of the MDM check-in), checks immediately after ESP or Autopilot device preparation completes, and performs periodic health checks. A manual check-in can be triggered from Company Portal > Settings > Sync.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\IntuneManagementExtension"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\IntuneManagementExtension" /s` | Recursively list all IME state subkeys and values. |
