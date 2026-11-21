---
created: 2026-11-21
fullpath: 'C:\Windows\debug\netlogon.log'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - log
  - netlogon
  - active-directory
aliases:
  - "netlogon.log"
  - "Netlogon debug log"
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/windows-security/enable-debug-logging-netlogon-service
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-netlogon
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/windows-updates-add-new-ntlm-pass-through-authentication-protections
---

**fullpath**:C:\Windows\debug\netlogon.log

# description

netlogon.log is the debug log of the Netlogon service, written to `%windir%\debug\netlogon.log` when Netlogon debug logging is enabled. It is used to troubleshoot authentication, DC locator, account lockout and other domain communication issues; logging is controlled with `nltest /dbflag`, the `DBFlag` registry value, or Group Policy.

## simple description

> ### 2026-11-21 Claude said
> Netlogon is the Windows service that handles domain logons, secure channels to domain controllers and DC discovery. When debug logging is turned on, it records every pass-through authentication, DC lookup and secure channel event in this text file. Logging is off by default and is usually enabled temporarily for troubleshooting.
>
> **SOC NOTE**: Very useful on DCs for tracing NTLM pass-through authentications (source workstation, user, result codes such as 0xC000006A bad password, 0xC0000234 lockout) and for spotting Zerologon (CVE-2020-1472) attempts and password-spray sources (T1110). It rolls over to netlogon.bak at the size limit, so collect both.
>

# purpose

Records Netlogon debug output. Enable with `Nltest /DBFlag:2080FFFF` (or `HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\DBFlag` = 0x2080FFFF, or the Specify log file debug output level policy) and disable with `Nltest /DBFlag:0x0`. Default maximum size is 20 MB (configurable with `MaximumLogFileSize`); when full it is renamed to Netlogon.bak and a new log is created.
