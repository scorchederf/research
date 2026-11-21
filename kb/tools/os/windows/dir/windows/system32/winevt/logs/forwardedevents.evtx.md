---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\ForwardedEvents.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - wef
aliases:
  - "ForwardedEvents.evtx"
  - "ForwardedEvents"
  - "Forwarded Events"
url:
  - https://learn.microsoft.com/windows/win32/wec/setting-up-a-source-initiated-subscription
  - https://learn.microsoft.com/windows/win32/wec/windows-event-collector
  - https://learn.microsoft.com/windows-server/administration/windows-commands/wecutil
  - https://learn.microsoft.com/defender-for-identity/deploy/configure-event-forwarding
  - https://learn.microsoft.com/troubleshoot/windows-server/admin-development/configure-eventlog-forwarding-performance
---

**fullpath**:C:\Windows\System32\winevt\Logs\ForwardedEvents.evtx

# description

`ForwardedEvents.evtx` is the file backing the ForwardedEvents channel, the default destination log on a Windows Event Collector computer for events received through Windows Event Forwarding subscriptions. It is part of Windows and is managed with Event Viewer and `wecutil.exe`; event sources are configured via WinRM and the Event Forwarding Group Policy (SubscriptionManager).

## simple description

> ### 2026-11-21 Claude said
> This file holds events that other computers have sent to this machine using Windows Event Forwarding (WEF).
> It is normally only populated on a central collector server, not on regular workstations.
> Each forwarded event keeps its original content plus information about the computer it came from.
> Analysts and SIEM agents (and Defender for Identity standalone sensors) read it to get centralised logs.
>
> **SOC NOTE**: High forensic value: it may hold Security/Sysmon/PowerShell events from many hosts, sometimes surviving after attackers clear logs on the source (T1070.001 Clear Windows Event Logs). Check collector gaps or subscription failures (wecutil gr) as signs of tampering; clearing this log on the collector raises event 104 (System) / 1102 only for Security.
>

# purpose

Stores events forwarded from remote event sources. `wecutil qc` enables the ForwardedEvents channel if disabled, sets the Windows Event Collector service to delayed start and starts it. Subscriptions write to the ForwardedEvents log or to the log specified in the subscription; Defender for Identity requires the destination log to be Forwarded Events. For performance, the ForwardedEvents log can be put onto another disk.
