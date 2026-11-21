---
created: 2026-11-21
fullpath: 'C:\Windows\System32\LogFiles\HTTPERR'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - logs
  - http.sys
aliases:
  - HTTPERR
  - httperr.log
  - HTTP Server API error log
url:
  - https://learn.microsoft.com/windows/win32/http/configuring-http-server-api-error-logging
  - https://learn.microsoft.com/windows/win32/http/error-logging-in-windows-server-2003-sp1
  - https://learn.microsoft.com/troubleshoot/developer/webapps/iis/site-behavior-performance/troubleshoot-http-error-code
  - https://learn.microsoft.com/troubleshoot/developer/webapps/iis/site-behavior-performance/troubleshoot-http-400-errors-in-iis
---

**fullpath**:C:\Windows\System32\LogFiles\HTTPERR

# description

HTTPERR is the folder where the HTTP Server API kernel driver (HTTP.sys) writes its error logs. HTTP.sys handles incoming HTTP requests before they reach IIS, so errors it blocks are logged here rather than in the IIS logs (`C:\inetpub\logs\Logfiles`). The location is configured by the `ErrorLoggingDir` value under `HKLM\System\CurrentControlSet\Services\HTTP\Parameters`.

## simple description

> ### 2026-11-21 Claude said
> This folder holds error logs from HTTP.sys, the Windows kernel component that receives web traffic for IIS, WinRM, WSUS, ADFS and other HTTP listeners. When a request is malformed, times out, or is rejected before an application sees it, a line is written here. The logs are W3C-style text files readable with any log parser.
>
> **SOC NOTE**: Useful for spotting web scanning, exploit attempts with malformed requests (e.g. HTTP.sys bugs like CVE-2015-1635 / CVE-2022-21907), and connection floods, since these never appear in IIS logs. Records client IP, port, URI and reason (`s-reason`). Only Administrators and Local System can read the folder.
>

# purpose

Stores HTTP Server API error log files. Logging is controlled by `EnableErrorLogging` (default 1), `ErrorLogFileTruncateSize` (default 1 MB, minimum 1 MB) and `ErrorLoggingDir` (default `%SystemRoot%\System32\LogFiles`, under which an `HTTPERR` subfolder is created). Admin and Local System have full access; other users have none. Settings are read when the driver starts (`net stop http` / `net start http`). Logged fields are controlled by `ErrorLoggingFields`, and time-based rollover by `ErrorLoggingRolloverType` and `ErrorLoggingLocaltimeRollover`. If logging fails, HTTP Server API uses event logging to notify administrators.

# common files found

| file | description |
| --- | --- |
| `httperr<SequenceNumber>.log` | Size-based rollover log, e.g. httperr4.log. |
| `htYYMMDD.log` | Daily rollover log. |
| `htYYMMww.log` | Weekly rollover log (ww = week of month). |
| `htYYMM.log` | Monthly rollover log. |
| `htYYMMDDhh.log` | Hourly rollover log. |
