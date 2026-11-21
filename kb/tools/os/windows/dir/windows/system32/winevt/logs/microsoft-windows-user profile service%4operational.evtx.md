---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-User Profile Service%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - user-profile
aliases:
  - Microsoft-Windows-User Profile Service%4Operational.evtx
  - User Profile Service Operational log
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/user-profiles-and-logon/troubleshoot-user-profiles-events
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-User Profile Service%4Operational.evtx

# description

The User Profile Service Operational event log, shown in Event Viewer under **Applications and Services Logs > Microsoft > Windows > User Profile Service > Operational**. It is enabled by default in all Windows installations and complements the User Profile Service events in the Application log and the optional Diagnostic (analytic/debug) log.

## simple description

> ### 2026-11-21 Claude said
> This event log file records what the User Profile Service does when a user's profile is loaded at logon and unloaded at logoff. It shows steps such as locating the profile, loading the user's registry hive and handling roaming profiles. Admins use it to troubleshoot slow logons or temporary profiles. The `%4` in the file name stands for the `/` in the channel name.
>
> **SOC NOTE**: Useful for building a logon timeline per user: events such as 1 (received logon notification), 2/3 (finished processing), 4 (logoff) and 5 (registry file loaded, showing `NTUSER.DAT` path and SID) show which accounts' profiles were loaded and when, including first-time logons that create new profiles (lateral movement or new local accounts, MITRE ATT&CK T1078 / T1136). Gaps or clearing support anti-forensics detection (T1070.001).

# purpose

Shows some of the inner workings of the User Profile Service and helps pinpoint where in the profile load or unload process a problem is occurring. Learn recommends examining it for events around the time of Error or Warning events from the User Profile Service in the Application log; for more detail, the Diagnostic log or an ETL trace (`logman`/`tracerpt`) can be used.
