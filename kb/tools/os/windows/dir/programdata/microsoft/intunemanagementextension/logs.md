---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\IntuneManagementExtension\Logs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - intune
  - logs
aliases:
  - IME logs
  - Intune Management Extension logs
url:
  - https://learn.microsoft.com/intune/device-management/tools/management-extension-windows
  - https://learn.microsoft.com/intune/app-management/deployment/troubleshoot-win32
  - https://learn.microsoft.com/troubleshoot/mem/intune/app-management/develop-deliver-working-win32-app-via-intune
---

**fullpath**:C:\ProgramData\Microsoft\IntuneManagementExtension\Logs

# description

Log folder of the Microsoft Intune Management Extension (IME), the agent that runs as the IntuneManagementExtension service and handles Win32 apps, PowerShell scripts, remediations, custom compliance and Endpoint analytics on Intune-managed Windows devices. Logs are viewed with CMTrace.exe.

## simple description

> ### 2026-11-21 Claude said
> The Intune agent writes its activity logs here: when it checks in, which apps and scripts it received, and how installs went. Admins use these files to troubleshoot why an app or script didn't deploy. Files roll over and old copies are kept with a leading underscore.
>
> **SOC NOTE**: Shows which PowerShell scripts and Win32 apps ran as SYSTEM via Intune (AgentExecutor.log, AppWorkload.log, HealthScripts.log), including command lines. A compromised Intune admin can push malicious scripts (T1072); these logs prove what was executed and when.
>

# purpose

Holds IME logs on the client. IME checks in with Intune every 8 hours, independently of the MDM check-in; content downloads go to `C:\Program Files (x86)\Microsoft Intune Management Extension\Content` and are unzipped to `C:\Windows\IMECache`.

# common files found

| file | description |
| --- | --- |
| `IntuneManagementExtension.log` | Main log: IME check-ins, policy requests, processing and reporting. |
| `_IntuneManagementExtension.log` | Saved copy of the main log after rollover. |
| `AgentExecutor.log` | PowerShell script executions deployed by Intune. |
| `AppActionProcessor.log` | Detection and applicability checks for assigned apps. |
| `AppWorkload.log` | Win32 app deployment: check-ins, installs, applicability and detection. |
| `ClientCertCheck.log` | Device client certificate checks. |
| `ClientHealth.log` | Health of the Intune management extension. |
| `DeviceHealthMonitoring.log` | Hardware readiness, device inventory and other data collectors. |
| `HealthScripts.log` | Remediation scripts, custom compliance, managed installer, hardware configuration. |
| `NotificationInfra.log` | Notifications through the Microsoft real-time communication channel. |
| `Sensor.log` | Endpoint analytics data collector health. |
| `Win32AppInventory.log` | App inventory collector health. |
