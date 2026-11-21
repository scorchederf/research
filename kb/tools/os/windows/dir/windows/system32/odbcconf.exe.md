---
created: 2026-11-21
fullpath: 'C:\Windows\System32\odbcconf.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
aliases:
  - "odbcconf.exe"
  - "ODBCCONF.EXE"
url:
  - https://learn.microsoft.com/sql/odbc/odbcconf-exe
---

**fullpath**:C:\Windows\System32\odbcconf.exe

# description

ODBCCONF.exe is a command-line tool that configures ODBC drivers and data source names. It is part of Windows Data Access Components and is deprecated; Microsoft recommends the Windows Data Access Components (WDAC) PowerShell cmdlets instead.

## simple description

> ### 2026-11-21 Claude said
> Odbcconf.exe is a built-in tool for installing and configuring ODBC database drivers and data sources from the command line or a response file. It can also register a DLL, similar to regsvr32. It is deprecated but still present on modern Windows.
>
> **SOC NOTE**: Classic LOLBin (MITRE ATT&CK T1218.008 Odbcconf): `odbcconf /a {REGSVR evil.dll}` or a `.rsp` response file with `/F` loads an attacker DLL via a signed binary. Alert on odbcconf.exe with REGSVR, INSTALLDRIVER pointing at user-writable paths, or `/F` response files.
>

# purpose

Configure ODBC drivers, translators and user/system DSNs, register DLLs, and set the default file DSN directory, optionally from a response file.

# typical use cases

| usage | description |
| --- | --- |
| `odbcconf /F my.rsp` | Runs actions from a response file (e.g. a line `REGSVR c:\my.dll`). |
| `odbcconf /A {CONFIGSYSDSN "SQL Server" "DSN=name \| Server=srv"}` | Adds or modifies a system data source. |
| `odbcconf /A {REGSVR c:\my.dll}` | Registers a DLL, equivalent to regsvr32.exe. |
| `odbcconf /A {SETFILEDSNDIR}` | Creates the DefaultDSNDir value if it does not exist. |

# options

| option | description |
| --- | --- |
| `/A {action}` | Specifies an action; optional if only one action is given. |
| `/?` | Displays usage. |
| `/C` | Continues processing if an action fails. |
| `/E` | Erases the response file specified with /F when finished. |
| `/F` | Uses a response file; /A is not used inside it. |
| `/H` | Displays usage (same as /?). |
| `/L[mode] filename` | Logs output in normal (n), verbose (v) or debug (d) mode; debug records loaded DLLs. |
| `/R` | Performs the action after a restart. |
| `/S` | Silent mode; no error messages. |
| `CONFIGDRIVER` | Loads the driver setup DLL and calls ConfigDriver (SQLConfigDriver). |
| `CONFIGDSN` | Adds or modifies a user data source (SQLConfigDataSource). |
| `CONFIGSYSDSN` | Adds or modifies a system data source (SQLConfigDataSource). |
| `INSTALLDRIVER` | Installs a driver (SQLInstallDriverEx). |
| `INSTALLTRANSLATOR` | Adds a translator under HKLM\SOFTWARE\ODBC\ODBCINST.INI\ODBC Translators (SQLInstallTranslatorEx). |
| `REGSVR dll` | Registers a DLL; equivalent to regsvr32.exe. |
| `SETFILEDSNDIR` | Creates HKLM\SOFTWARE\ODBC\ODBC.INI\ODBC File DSN\DefaultDSNDir from CommonFilesDir plus \ODBC\Data Sources. |
