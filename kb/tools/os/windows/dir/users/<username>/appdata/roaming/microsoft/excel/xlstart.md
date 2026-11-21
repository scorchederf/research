---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Excel\XLSTART'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - excel
  - office
aliases:
  - XLSTART
  - XLStart
  - User startup
url:
  - https://learn.microsoft.com/troubleshoot/microsoft-365-apps/excel/files-open-automatically
  - https://learn.microsoft.com/microsoft-365-apps/security/trusted-locations
  - https://learn.microsoft.com/office/vba/api/excel.application.startuppath
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Excel\XLSTART

# description

The per-user Excel startup folder (`%appdata%\Microsoft\Excel\XLSTART`). Every file in it is opened automatically when Microsoft Excel starts, and it is a default Office Trusted Location ("User startup", subfolders not trusted). The per-machine equivalent is `Program Files\Microsoft Office\Root\Office16\XLSTART`; the path is returned by the VBA `Application.StartupPath` property.

## simple description

> ### 2026-11-21 Claude said
> XLSTART is a folder that Excel checks every time it launches; any workbook, template or add-in placed there opens automatically. It is commonly used for `PERSONAL.XLSB`, the user's personal macro workbook, and for a default `Book.xltx` template. Each user has their own copy under their roaming profile. Because it is a trusted location, macros in files there run without the usual security prompt.
>
> **SOC NOTE**: Classic Office persistence (MITRE ATT&CK T1137 Office Application Startup / T1137.006 Add-ins): dropping a macro-enabled workbook (`.xlsm`/`.xlsb`/`.xlam`) here runs attacker VBA every time Excel starts, bypassing macro warnings because the folder is trusted. Monitor file creation in this folder (Sysmon 11) and review unexpected files, especially recently created `PERSONAL.XLSB` with auto-run macros.

# purpose

When Excel starts, all files located in the XLStart folder are opened automatically, regardless of file type. Excel can stop responding or start slowly if files in the startup folder aren't valid workbooks or are on a slow network drive. Starting Excel with `excel.exe /safe` or `excel.exe /automation`, holding CTRL, or pressing ESC prevents startup files from opening; removing files from the folder stops them permanently.

# common files found

| file | description |
| --- | --- |
| `PERSONAL.XLSB` | Personal macro workbook opened at Excel startup. |
| `Book.xltx` | Default workbook template used for new workbooks. |
