---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Directory Service.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - eventlog
  - active-directory
aliases:
  - "Directory Service.evtx"
  - "Directory Service log"
  - "Directory Services log"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/configure-ad-and-lds-event-logging
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/active-directory-replication-event-id-2042
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/active-directory-replication-event-id-2087
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/detect-and-recover-from-usn-rollback
---

**fullpath**: C:\Windows\System32\winevt\Logs\Directory Service.evtx

# description

Event log file for the Directory Service log on Active Directory domain controllers, where Active Directory Domain Services (source Microsoft-Windows-ActiveDirectory_DomainService / NTDS) records events. Diagnostic verbosity is controlled under `HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Diagnostics`; AD LDS instances use their own log.

## simple description

> ### 2026-11-21 Claude said
> This is the main AD log on a domain controller. It records replication problems, database issues, LDAP and security-related directory events. By default only critical and error events are logged; admins can raise logging levels per component in the registry. It only exists on domain controllers.
>
> **SOC NOTE**: Useful for detecting DCSync/DCShadow side effects, replication anomalies and LDAP abuse: event 2889 (unsigned/cleartext LDAP binds), 1644 (expensive/inefficient LDAP queries, e.g. recon tools when field engineering logging is enabled), 2095 (USN rollback), 2042/2087 replication failures. Clearing or a sudden gap in this log on a DC deserves investigation.
>

# purpose

Active Directory records events to the Directory Services log. By default only critical and error events are recorded; other events require increasing the logging level of the REG_DWORD values (e.g. Replication Events, Security Events, Field Engineering, LDAP Interface Events) under the NTDS\Diagnostics key. Examples: event 2042 (too long since last replication, tombstone lifetime exceeded), 2087 (DNS lookup failure caused replication to fail), 2095 (USN rollback detected).
