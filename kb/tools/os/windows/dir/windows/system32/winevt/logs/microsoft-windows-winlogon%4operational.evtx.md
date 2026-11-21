---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Winlogon%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - windows
aliases:
  - "Microsoft-Windows-Winlogon%4Operational.evtx"
  - "Microsoft-Windows-Winlogon/Operational"
  - "Winlogon Operational log"
url:
  - https://learn.microsoft.com/windows-server/identity/ad-ds/manage/component-updates/winlogon-automatic-restart-sign-on--arso-
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-Winlogon%4Operational.evtx

# description

This is the event log file for the Winlogon Operational channel (Applications and Services Logs > Microsoft > Windows > Winlogon > Operational), stored with the other channels in `%SystemRoot%\System32\winevt\Logs`. Winlogon writes its sign-in state trace here; related LSA events appear in the LSA Operational log.

## simple description

> ### 2026-11-21 Claude said
> This log records what the Winlogon process does during sign-in and sign-out, such as authentication starting and stopping. Event IDs 1 and 2 bracket an authentication attempt. It also tracks notifications to subscribers such as Group Policy and profile loading. It is a supporting log, not a replacement for Security log logon events.
>
> **SOC NOTE**: Helps build a logon timeline and confirm interactive/RDP session activity when the Security log has been cleared or rolled over (MITRE ATT&CK T1070.001). Correlate with Security 4624/4634 and TerminalServices logs. Unusual subscriber or shell-start delays can point at Winlogon persistence (T1547.004 Winlogon Helper DLL).
>

# purpose

When Winlogon performs a sign-in, its state trace is stored in this log. Documented events: Event ID 1 `Authentication started.` and Event ID 2 `Authentication stopped. Result 0` (source Winlogon). It is used, for example, when troubleshooting Winlogon automatic restart sign-on (ARSO), together with LSA Operational events 320-322.


