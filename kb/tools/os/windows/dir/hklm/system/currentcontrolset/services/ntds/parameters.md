---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - active-directory
  - ntds
aliases:
  - NTDS Parameters
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/issues-ad-replication-netlogon-rpcs-request-backlog-values-exceeded
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/configure-ad-and-lds-event-logging
  - https://learn.microsoft.com/windows-server/identity/ad-ds/manage/component-updates/directory-services-component-updates
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/use-ntdsutil-manage-ad-files
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters

# description

Registry key holding configuration parameters for the Active Directory Domain Services directory service (NTDS) on a domain controller. Ntdsutil `files` commands update this part of the registry when database, log or working directory paths are changed.

## simple description

> ### 2026-11-21 Claude said
> This key holds the main settings for Active Directory on a domain controller, such as where the NTDS.dit database and its log files live and tuning values for LDAP and replication. It only exists on domain controllers. Admins change it for troubleshooting (e.g. logging expensive LDAP searches) or when moving the database.
>
> **SOC NOTE**: The database path values tell an investigator where NTDS.dit is, the main target for domain credential theft (MITRE T1003.003). Unexpected changes here can indicate tampering with DC logging or paths. Search-threshold values control Event ID 1644 LDAP query logging, valuable for detecting LDAP reconnaissance (T1087).
>

# purpose

Configures directory service behavior: database and log file locations (set via `ntdsutil files` `set path`, `move DB to`, `move logs to`), RPC backlog limits for DRSUAPI, and thresholds for diagnostic logging of expensive, inefficient and long-running LDAP searches (Event ID 1644).

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

| value name | type | description |
| --- | --- | --- |
| `TCP/IP Backlog Limit` | REG_DWORD | RPC backlog limit for DRSUAPI; any value between 10 and 100. Restart required. |
| `Expensive Search Results Threshold` | REG_DWORD | Threshold for logging expensive LDAP searches (Event 1644). |
| `Inefficient Search Results Threshold` | REG_DWORD | Threshold for logging inefficient LDAP searches. |
| `Search Time Threshold (msecs)` | REG_DWORD | Time-based threshold in milliseconds for logging long-running searches (Windows Server 2012 R2 and later). |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters"` | List the key's values. |
