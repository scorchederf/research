---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Intune Management Extension'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - intune
  - mdm
aliases:
  - Microsoft Intune Management Extension
  - IME
  - Sidecar
url:
  - https://learn.microsoft.com/intune/app-management/deployment/troubleshoot-win32
  - https://learn.microsoft.com/troubleshoot/mem/intune/app-management/develop-deliver-working-win32-app-via-intune
  - https://learn.microsoft.com/intune/device-management/tools/management-extension-windows
---

**fullpath**:C:\Program Files (x86)\Microsoft Intune Management Extension

# description

Install folder of the Microsoft Intune Management Extension (IME, also called the SideCar agent), installed automatically on Intune-managed Windows devices when PowerShell scripts, Remediations, Win32 apps, custom compliance, Endpoint analytics, Remote Help or managed installer features are assigned. It runs as the **IntuneManagementExtension** service; its logs are in `C:\ProgramData\Microsoft\IntuneManagementExtension\Logs`.

## simple description

> ### 2026-11-21 Claude said
> This folder contains the Intune agent that installs Win32 apps and runs PowerShell scripts that IT pushes from Microsoft Intune. Its main program, `Microsoft.Management.Services.IntuneWindowsAgent.exe`, runs as a service with SYSTEM rights. On 64-bit Windows it is under Program Files (x86); on 32-bit Windows under Program Files. It checks in with Intune about every 8 hours.
>
> **SOC NOTE**: Scripts and installers run by the IME execute as SYSTEM, so a compromised Intune admin can deploy malware fleet-wide (MITRE T1072 Software Deployment Tools). Investigate `Content\Staging` and `Content\Incoming` for unexpected payloads, and AgentExecutor.log, IntuneManagementExtension.log and AppWorkload.log for what ran. The folder is commonly excluded from AV scanning, which attackers may abuse to stage files.
>

# purpose

Hosts the IME agent binaries and its working content. Learn documents that Win32 app content is downloaded to `Content\Incoming` (as `<appid>_1.bin`), decrypted and unzipped from `Content\Staging` to `C:\Windows\IMECache`, then installed; PowerShell and remediation scripts are also staged under `Content\Staging`. Microsoft recommends excluding `Content` (and `C:\windows\IMECache`) from antimalware scanning. The agent can be forced to check in through Company Portal **Settings > Sync**.

# common files found

| file | description |
| --- | --- |
| `Content\Incoming\` | Encrypted Win32 app content being downloaded (`<appid>_1.bin`). |
| `Content\Staging\` | Staging area for decrypted content and deployed PowerShell, detection and remediation scripts. |
| `Microsoft.Management.Services.IntuneWindowsAgent.exe` | IME agent executable, also set as an AppLocker managed installer. |
