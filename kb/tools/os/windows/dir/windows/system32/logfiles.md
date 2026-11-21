---
created: 2026-11-21
fullpath: 'C:\Windows\System32\LogFiles'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - logs
aliases:
  - LogFiles
  - %SystemRoot%\System32\LogFiles
url:
  - https://learn.microsoft.com/windows/security/operating-system-security/network-security/windows-firewall/configure-logging
  - https://learn.microsoft.com/windows/win32/http/configuring-http-server-api-error-logging
  - https://learn.microsoft.com/windows/win32/http/error-logging-in-windows-server-2003-sp1
---

**fullpath**:C:\Windows\System32\LogFiles

# description

System folder used as the default location for several Windows text logs, including Windows Firewall logs (`Firewall\pfirewall.log`) and HTTP Server API (http.sys) error logs (`HTTPERR`). Related tools: `netsh advfirewall`, Windows Defender Firewall Group Policy.

## simple description

> ### 2026-11-21 Claude said
> C:\Windows\System32\LogFiles is a common place where Windows components write plain-text logs. Typical subfolders are Firewall (Windows Firewall packet logs), HTTPERR (http.sys errors) and, on web servers, W3SVC folders for IIS logs. Other components such as SUM (User Access Logging) and WMI traces may also write here.
>
> **SOC NOTE**: Rich evidence source: pfirewall.log shows allowed/dropped connections, HTTPERR shows malformed requests and scanning against http.sys, and IIS W3SVC logs reveal web shell activity (T1505.003). Attackers may delete or truncate these (T1070.004 Indicator Removal: File Deletion), so gaps or missing files are notable.
>

# purpose

Default folder for component logs. Windows Firewall logs to `%windir%\system32\logfiles\firewall\pfirewall.log` by default (max 4,096 KB by default, 32,767 KB maximum); the `mpssvc` service needs FullControl on the folder. The HTTP Server API creates an `HTTPERR` subfolder under `%SystemRoot%\System32\LogFiles` (unless `ErrorLoggingDir` overrides it) with files named `httperr<n>.log`, accessible only to Administrators and Local System.

# common files found

| file | description |
| --- | --- |
| `Firewall\pfirewall.log` | Windows Defender Firewall log of dropped packets and successful connections. |
| `HTTPERR\httperr<n>.log` | HTTP Server API error log, cycled by size (default 1 MB). |
