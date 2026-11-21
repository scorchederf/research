---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-CodeIntegrity%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - code-integrity
  - app-control
aliases:
  - 'Microsoft-Windows-CodeIntegrity%4Operational.evtx'
  - 'CodeIntegrity - Operational'
  - 'Microsoft-Windows-CodeIntegrity/Operational'
url:
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/operations/event-id-explanations
  - https://learn.microsoft.com/windows-hardware/drivers/install/viewing-code-integrity-events
  - https://learn.microsoft.com/windows-hardware/drivers/install/code-integrity-event-log-messages
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-CodeIntegrity%4Operational.evtx

# description

Event log file for the **CodeIntegrity - Operational** channel (Applications and Services Logs > Microsoft > Windows > CodeIntegrity). Code Integrity checks the signatures of drivers and, with App Control for Business (WDAC) policies, of executables, DLLs and scripts; a separate **CodeIntegrity - Verbose** channel is disabled by default.

## simple description

> ### 2026-11-21 Claude said
> This log records what Windows' code-signing enforcement (Code Integrity / App Control) blocked or would have blocked: unsigned drivers, files with bad or revoked signatures, and files not allowed by an App Control policy. It also logs when App Control policies are loaded or refreshed. You view it in Event Viewer under Microsoft > Windows > CodeIntegrity.
>
> **SOC NOTE**: Key for detecting blocked or audited malicious binaries and vulnerable/unsigned driver loads (BYOVD, T1068 / T1014). Event 3077 (enforced block) and 3076 (audit) show the file, hash and policy; 3033/3034 revoked or expired signatures; 3099 policy loaded. Policy tampering or removal (T1562.001) shows up as unexpected activation/refresh events. Forward this channel to the SIEM.
>

# purpose

Holds Code Integrity warning events (for example, unable to verify image integrity because the file hash could not be found, or unsigned driver detected) and App Control events. Learn documents block events such as 3004 (driver with invalid signature), 3033/3034 (revoked or expired Lifetime Signing signature, enforced/audit), 3076 (audit-mode block) and 3077 (enforcement block); policy activation events 3095-3105 including 3099 (policy loaded); and ISG/managed installer diagnostics 3090 (3091/3092 on older versions). Other IDs include 3001 (unsigned driver load attempt), 3002, 3010-3012 (catalog loading), 3023, 3024, 3026 and 3032.

