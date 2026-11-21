---
created: 2026-11-21
fullpath: 'C:\Windows\IMECache'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - intune
aliases:
  - IMECache
  - Intune Management Extension cache
url:
  - https://learn.microsoft.com/troubleshoot/mem/intune/app-management/develop-deliver-working-win32-app-via-intune
  - https://learn.microsoft.com/intune/app-management/deployment/troubleshoot-win32
  - https://learn.microsoft.com/intune/device-management/tools/management-extension-windows
---

**fullpath**:C:\Windows\IMECache

# description

Working folder used by the Microsoft Intune Management Extension (IME) when installing Win32 apps. Downloaded, decrypted content is unzipped from `Content\Staging` into `C:\Windows\IMECache\<appid>_<version>` before the installer runs. Microsoft recommends excluding it from antimalware scanning.

## simple description

> ### 2026-11-21 Claude said
> When Intune deploys a Win32 app, the Intune Management Extension downloads the package and extracts it into this folder. The installer command then runs from here, usually as SYSTEM. Subfolders are named after the app ID and version and are normally cleaned up after install.
>
> **SOC NOTE**: Because it is usually AV-excluded and its content runs as SYSTEM, it is attractive for hiding or executing payloads; unexpected files or processes launched from here are suspicious. Correlate with IntuneManagementExtension.log/AppWorkload.log in C:\ProgramData\Microsoft\IntuneManagementExtension\Logs.
>

# purpose

Staging/extraction location for Intune Win32 app content prior to installer execution.

# common files found

- `<appid>_<version>\` - extracted Win32 app content (e.g. `59f9a567-..._1`) containing installer files such as .msi/.exe
