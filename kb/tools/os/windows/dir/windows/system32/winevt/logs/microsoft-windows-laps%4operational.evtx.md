---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-LAPS%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - laps
aliases:
  - Microsoft-Windows-LAPS%4Operational.evtx
  - Microsoft-Windows-LAPS/Operational
  - Windows LAPS event log
url:
  - https://learn.microsoft.com/windows-server/identity/laps/laps-management-event-log
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/windows-laps-troubleshooting-guidance
  - https://learn.microsoft.com/windows-server/identity/laps/laps-concepts-overview
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-LAPS%4Operational.evtx

# description

Dedicated event log channel for Windows Local Administrator Password Solution (Windows LAPS), viewed in Event Viewer under Applications and Services Logs > Microsoft > Windows > LAPS > Operational. All Windows LAPS operations are tracked with rich eventing.

## simple description

> ### 2026-11-21 Claude said
> This log records what Windows LAPS does: each hourly policy cycle, which policy is active, and when the managed local admin password is rotated and backed up to Active Directory or Entra ID. It is the first place to look when LAPS passwords aren't updating. On domain controllers it only covers the DSRM account.
>
> **SOC NOTE**: 10031 shows a blocked attempt to change the LAPS-managed account's password (possible tampering); 10041/10042 show the managed account authenticated and post-authentication rotation, i.e. someone used the LAPS password, useful for tracing lateral movement with local admin (T1078.003). Failed cycles (10005) or a missing log may indicate LAPS disabled for evasion.
>

# purpose

Tracks Windows LAPS client operations. Key events: 10003 policy processing starting; 10004 succeeded; 10005 failed (with error code); 10021/10022/10023 current policy configuration for AD, Entra ID or legacy LAPS; 10018 password updated in AD; 10029 password updated in Entra ID; 10020 local account password updated; 10031 external password modification blocked; 10041 authentication by the managed account detected; 10042 post-authentication grace period expired; 10043 password reset failed; 10044 reset and post-authentication actions succeeded; 10013 managed account not found; 10012 AD schema not extended; 10017 failed to update AD; 20000 CSP rejected MDM configuration on a non-joined device. `Invoke-LapsPolicyProcessing` starts a cycle immediately. On a domain controller the channel only contains DSRM account events.
