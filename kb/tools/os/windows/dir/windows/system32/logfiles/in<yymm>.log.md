---
created: 2026-11-21
fullpath: 'C:\Windows\System32\LogFiles\IN<yymm>.log'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - iis
  - log
aliases:
  - IN<yymm>.log
  - inyymm.log
  - Microsoft IIS Log Format
url:
  - https://learn.microsoft.com/windows/win32/api/http/ne-http-http_logging_rollover_type
  - https://learn.microsoft.com/iis/configuration/system.applicationhost/sites/site/logfile/
  - https://learn.microsoft.com/iis/manage/provisioning-and-managing-iis/configure-logging-in-iis
---

**fullpath**:C:\Windows\System32\LogFiles\IN<yymm>.log

# description

`inyymm.log` is the file name pattern for a log in the Microsoft IIS log file format with monthly rollover (other patterns: `inetsvnn.log` by size, `inyymmddhh.log` hourly, `inyymmdd.log` daily, `inymmww.log` weekly). The IIS format is handled by HTTP.sys, is fixed (fields cannot be customized), comma-separated, and records time in local time.

## simple description

> ### 2026-11-21 Claude said
> IN<yymm>.log is a monthly IIS web server log in the older "IIS" log format (prefix `in`; W3C logs use `ex`). Each line records one HTTP request: client IP, user name, date/time, site, server, time taken, bytes, status codes, method, URL and parameters. This location is typical of older IIS / HTTP.sys logging configurations.
>
> **SOC NOTE**: Primary evidence for web attacks: webshell access (T1505.003), exploitation, brute force and scanning. Look for POSTs to unusual .asp/.aspx files, odd query parameters, bursts of 401/500 errors and rare client IPs. Times are local time in this format (W3C uses UTC). Attackers may delete or disable logs (T1070.004, T1562.002), so missing months or gaps are suspicious.
>

# purpose

Records HTTP requests in the fixed IIS format when monthly rollover is configured. Logged fields: client IP address, user name, date, time, service and instance, server name, server IP address, time taken, client bytes sent, server bytes sent, service status code, Windows status code, request type, target of operation, parameters. Empty fields show `-`; non-printable characters become `+`.
