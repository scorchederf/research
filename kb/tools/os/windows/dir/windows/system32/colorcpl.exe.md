---
created: 2026-11-21
fullpath: 'C:\Windows\System32\colorcpl.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - control-panel
  - color-management
aliases:
  - 'colorcpl.exe'
  - 'Color Management'
  - 'Microsoft.ColorManagement'
url:
  - https://learn.microsoft.com/windows/win32/shell/controlpanel-canonical-names
---

**fullpath**:C:\Windows\System32\colorcpl.exe

# description

`colorcpl.exe` is the **Color Management** Control Panel item (canonical name `Microsoft.ColorManagement`, GUID `{B2C761C6-29BC-4f19-9251-E6195265BAF1}`) for managing device color profiles in the Windows Color System.

## simple description

> ### 2026-11-21 Claude said
> Colorcpl opens the Color Management window where you assign ICC/ICM color profiles to monitors and printers and install new profiles. Installing a profile copies it into the system color folder (spool\drivers\color). It is a small, signed Windows program.
>
> **SOC NOTE**: Has been noted as a LOLBin because installing a "profile" copies an arbitrary file into `C:\Windows\System32\spool\drivers\color` (file staging, T1105/T1036). Investigate colorcpl launched with a file argument from scripts or unusual parents, and non-profile files (exe, dll, scripts) appearing in the color directory.
>

# purpose

Learn lists Color Management as a Control Panel item supported on Windows Vista through Windows 8.1, with module name `@%systemroot%\system32\colorcpl.exe,-6`. It can be opened with its canonical name (`control.exe /name Microsoft.ColorManagement`).

# typical use cases

| usage | description |
| --- | --- |
| `control.exe /name Microsoft.ColorManagement` | Open the Color Management Control Panel item by canonical name. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
