---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Kerberos%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - evtx
  - kerberos
aliases:
  - Microsoft-Windows-Kerberos%4Operational.evtx
  - Microsoft-Windows-Kerberos/Operational
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/enable-kerberos-event-logging
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/kerberos-authentication-troubleshooting-guidance
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-Kerberos%4Operational.evtx

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This is the event log file for the Kerberos client's Operational channel (Microsoft-Windows-Kerberos/Operational). It records Kerberos client-side errors and activity on the machine, such as failed ticket requests and errors from the KDC. The channel is often disabled by default and must be enabled to collect data. Security-log events 4768/4769/4771 on domain controllers are the more common Kerberos sources.
>
> **SOC NOTE**: Client-side Kerberos errors (e.g. KDC_ERR_S_PRINCIPAL_UNKNOWN, KRB_AP_ERR_MODIFIED, clock skew) can reveal SPN misconfiguration, Kerberoasting or pass-the-ticket activity (T1558, T1550.003). Correlate with DC Security events 4768/4769 (RC4 etype 0x17 requests) and 4771.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
