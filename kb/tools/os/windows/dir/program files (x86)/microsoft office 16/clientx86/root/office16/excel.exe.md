---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Excel.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - office
  - excel
aliases:
  - "Excel.exe"
  - "Microsoft Excel"
url:
  - https://learn.microsoft.com/troubleshoot/microsoft-365-apps/excel/files-open-automatically
---

**fullpath**: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Excel.exe

# description

Excel.exe is the Microsoft Excel desktop application, part of Microsoft 365 Apps / Office. This path is the Click-to-Run (32-bit, ClientX86 virtualized root) install location. Learn documents its safe-mode and automation startup switches and the XLStart startup folders.

## simple description

> ### 2026-11-21 Claude said
> Excel.exe is the spreadsheet program from Microsoft Office. Users open .xlsx/.xls/.csv files with it, and it can also run macros (VBA) and add-ins. This specific path comes from a 32-bit Click-to-Run Office install. It is a very common, legitimate program on corporate machines.
>
> **SOC NOTE**: Excel is a top phishing target: malicious workbooks with VBA/XLM 4.0 macros, DDE or embedded objects lead to Excel.exe spawning cmd.exe, powershell.exe, mshta.exe or rundll32.exe (T1204.002, T1137 Office Application Startup via XLStart/add-ins). Alert on unusual child processes, Excel writing executables, and files dropped in XLStart. Check Office Trust Center / MOTW and Office Alerts event logs.
>

# purpose

Starts Microsoft Excel. When it starts, Excel automatically opens all files in the XLStart folder and any alternative startup folder; it can be started in safe mode to prevent add-ins, toolbar customizations and startup folders from loading.

# typical use cases

| usage | description |
| --- | --- |
| `excel.exe /safe` | Start Excel in safe mode (no add-ins, toolbar customizations or startup folders). |
| `excel.exe /automation` | Start Excel with all automatically opened files and auto-run macros disabled. |

# options

| option | description |
| --- | --- |
| `/safe` | Starts Excel in safe mode. |
| `/automation` | Disables all automatically opened files and auto-run macros. |
