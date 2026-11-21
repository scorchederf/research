---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Parameters
  - Netlogon Parameters
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/performance-tuning-ntlm-authentication-maxconcurrentapi
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/issues-ad-replication-netlogon-rpcs-request-backlog-values-exceeded
  - https://learn.microsoft.com/troubleshoot/windows-client/windows-security/enable-debug-logging-netlogon-service
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters

# description

Registry key that holds configuration values for the Netlogon service. Values here tune NTLM authentication concurrency, the Netlogon RPC backlog and Netlogon debug logging (written to %windir%\debug\netlogon.log). Policy-based Netlogon settings live separately under Software\Policies\Microsoft\Netlogon\Parameters.

## simple description

> ### 2026-11-21 Claude said
> This key stores settings for the Netlogon service, which handles domain logon, the machine's secure channel with domain controllers and NTLM authentication forwarding. Admins change values here to tune performance or turn on Netlogon debug logs. On domain controllers it also controls security behaviour around the secure channel. Changes usually need a Netlogon service restart.
>
> **SOC NOTE**: Relevant to Zerologon (CVE-2020-1472) hardening: values such as FullSecureChannelProtection and VulnerableChannelAllowList control secure-RPC enforcement, and weakening them is a red flag (T1112, T1556). DBFlag enables netlogon.log, useful for tracing NTLM authentications and password-spray sources. Monitor changes with registry auditing (4657) or Sysmon 13.
>

# purpose

Configures Netlogon service behaviour such as NTLM authentication concurrency, RPC backlog limits and debug logging.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SYSTEM |

# values

| value name | type | description |
| --- | --- | --- |
| `MaxConcurrentApi` | REG_DWORD | Concurrent NTLM authentications Netlogon processes; restart Netlogon after changing. |
| `DcTcpipBacklogLimit` | REG_DWORD | RPC backlog limit for Netlogon (10-100); restart Netlogon, possibly the DC. |
| `DBFlag` | REG_DWORD | Netlogon debug logging; `2080FFFF` enables, `0x0` disables. Logs to %windir%\debug\netlogon.log. |
| `MaximumLogFileSize` | REG_DWORD | Maximum Netlogon.log size in bytes (default 20 MB; rolls to Netlogon.bak). |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters"` | List the key's values. |
| `net stop netlogon` | Stop Netlogon so changes take effect (then `net start netlogon`). |
