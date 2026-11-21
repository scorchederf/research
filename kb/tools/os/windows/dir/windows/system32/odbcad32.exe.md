---
created: 2026-11-21
fullpath: 'c:\windows\system32\odbcad32.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - odbc
  - windows
aliases:
  - odbcad32.exe
  - ODBC Data Source Administrator
  - ODBC Data Sources (64-bit)
url:
  - https://learn.microsoft.com/sql/odbc/admin/viewing-drivers
  - https://learn.microsoft.com/sql/odbc/admin/managing-data-sources
  - https://learn.microsoft.com/troubleshoot/sql/connect/odbc-tool-displays-32-bit-64-bit
  - https://learn.microsoft.com/sql/relational-databases/native-client/odbc/data-source-names-and-64-bit-operating-systems
---

**fullpath**:c:\windows\system32\odbcad32.exe

# description

The ODBC Data Source Administrator (Odbcad32.exe) is the Windows tool used to add, modify and delete ODBC data sources (User, System and File DSNs) and to view installed ODBC drivers. On 64-bit Windows, `C:\Windows\System32\odbcad32.exe` is the 64-bit version and `C:\Windows\SysWOW64\odbcad32.exe` is the 32-bit version. It is also reachable from Control Panel > Administrative Tools > ODBC Data Sources.

## simple description

> ### 2026-11-21 Claude said
> odbcad32.exe is the built-in Windows GUI for managing ODBC database connections. Applications use ODBC data source names (DSNs) to know which driver and server to connect to. Admins use it to create, test and remove DSNs and to see which database drivers are installed. The System32 copy manages 64-bit drivers and DSNs, the SysWOW64 copy manages 32-bit ones.
>
> **SOC NOTE**: It is a signed Microsoft binary, so unusual launches (from scripts, Office, or remote sessions) deserve attention; DSN changes land in the registry (`HKLM\SOFTWARE\ODBC\ODBC.INI`, `HKCU\Software\ODBC\ODBC.INI`) and can reveal database servers, usernames and sometimes stored credentials useful for lateral movement (T1552 Unsecured Credentials). Malicious ODBC driver registration (pointing a driver DLL to an attacker DLL) is a known persistence/execution trick; review `ODBCINST.INI` driver paths during investigations.
>

# purpose

Create and maintain data source names for 64-bit applications (`%SystemRoot%\system32\odbcad32.exe`), view installed ODBC drivers on the **Drivers** tab, and manage User, System and File DSNs. Using the 64-bit tool against a DSN for a 32-bit driver returns `The specified DSN contains an architecture mismatch between the Driver and Application`; use the SysWOW64 copy instead. User DSNs are stored under `HKEY_CURRENT_USER\Software\ODBC\ODBC.INI`, which is not redirected, so both versions show them.

# typical use cases

| usage | description |
| --- | --- |
| `odbcad32.exe` | Open the 64-bit ODBC Data Source Administrator (Windows+R). |
| `C:\Windows\SysWOW64\odbcad32.exe` | Open the 32-bit ODBC Data Source Administrator to manage DSNs for 32-bit drivers. |

# options

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_
