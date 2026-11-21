---
created: 2026-11-21
fullpath: 'C:\inetpub\logs\LogFiles\W3SVC<n>'
generator:
  - claude
  - microsoftlearn
tags:
  - iis
  - directory
  - logs
aliases:
  - W3SVC<n>
  - W3SVC1
  - IIS web logs
url:
  - https://learn.microsoft.com/iis/configuration/system.applicationhost/sites/site/logfile/
  - https://learn.microsoft.com/iis/manage/provisioning-and-managing-iis/configure-logging-in-iis
  - https://learn.microsoft.com/troubleshoot/developer/webapps/iis/site-behavior-performance/slow-page-response-hangs
  - https://learn.microsoft.com/troubleshoot/developer/webapps/iis/health-diagnostic-performance/troubleshoot-iis-perf-issues-or-app-errors
  - https://learn.microsoft.com/azure/azure-monitor/vm/data-collection-iis
---

**fullpath**:C:\inetpub\logs\LogFiles\W3SVC<n>

# description

Per-site IIS web (W3SVC) log directory, where `<n>` is the site ID shown in IIS Manager (Default Web Site is W3SVC1). IIS 7 and later log by default to `%SystemDrive%\inetpub\logs\LogFiles`; the location is configurable through the `logFile` `directory` attribute in applicationhost.config.

## simple description

> ### 2026-11-21 Claude said
> Each website hosted in IIS writes its access logs into its own W3SVC folder, numbered by site ID. Every line records one HTTP request: date/time (UTC), client IP, method, URL, query string, status code, user agent, time taken and more (W3C format). Files are usually named `u_exYYMMDD.log` and roll over daily by default. These are the primary record of who accessed the web server and what they requested.
>
> **SOC NOTE**: Essential for investigating web attacks: web shell access (T1505.003), exploitation of public-facing apps (T1190, e.g. Exchange/SharePoint), brute force, scanning and exfiltration. Look for POSTs to unusual .aspx/.ashx files, 200 responses to odd paths, encoded commands in query strings, and spikes in time-taken or bytes. Attackers may delete or clear these logs (T1070.004) - gaps in the daily files are a red flag. Times are in UTC.
>

# purpose

Stores IIS W3C log files for a single site; each site has its own directory named W3SVC# where # is the SiteID. You need the site ID from IIS Manager (Sites) to know which W3SVC directory to analyze. Log format and fields are set on the IIS Logging page (W3C fields separated by spaces, time recorded in UTC), and Log File Rollover can be Hourly, Daily, Weekly, Monthly or by maximum file size. Logs can be analyzed with LogParser or collected by Azure Monitor.

# common files found

- u_exYYMMDDHH.log / u_exYYMMDD.log - W3C log files (e.g. `u_ex12101858.log`), created according to the rollover schedule.
