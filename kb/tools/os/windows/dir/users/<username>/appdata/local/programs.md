---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Programs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - per-user
  - installation
aliases:
  - Programs
  - %LOCALAPPDATA%\Programs
  - FOLDERID_UserProgramFiles
url:
  - https://learn.microsoft.com/windows/win32/msi/installation-context
  - https://learn.microsoft.com/windows/win32/msi/single-package-authoring
  - https://learn.microsoft.com/windows/win32/msi/single-package-authoring-example
---

**fullpath**:C:\Users\<username>\AppData\Local\Programs

# description

`%LOCALAPPDATA%\Programs` is the per-user Programs folder (`FOLDERID_UserProgramFiles`), introduced with Windows 7 / Windows Server 2008 R2. Windows Installer redirects `ProgramFilesFolder`/`ProgramFiles64Folder` here for per-user installs (ALLUSERS=""); shared components go to `Programs\Common`.

## simple description

> ### 2026-11-21 Claude said
> This is the per-user version of Program Files. Apps that install without admin rights (for example VS Code user installer, many Electron apps) put their files here. Only the user who installed the app can use it. Each app normally sits in its own subfolder named after the vendor or product.
>
> **SOC NOTE**: Because it is user-writable and needs no elevation, attackers and malware install payloads here and register persistence via HKCU Run keys or Startup (T1547.001). Binaries here are not protected by admin ACLs, enabling DLL hijacking/replacement (T1574). Review unsigned or recently created executables and compare with installed-apps inventory.
>

# purpose

Holds applications installed in the per-user installation context; files are accessible only to the installing user.

# common files found

| file | description |
| --- | --- |
| `<ISV name>\<AppName>\` | Typical per-user application folder layout. |
| `Common\` | Per-user Common folder (`FOLDERID_UserProgramFilesCommon`) for shared components. |

