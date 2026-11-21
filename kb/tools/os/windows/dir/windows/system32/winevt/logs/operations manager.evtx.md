---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Operations Manager.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - scom
aliases:
  - "Operations Manager.evtx"
  - "Operations Manager log"
url:
  - https://learn.microsoft.com/troubleshoot/system-center/scom/troubleshoot-agent-connectivity-issues
  - https://learn.microsoft.com/troubleshoot/system-center/scom/monitoring-agent-service-freezes-during-startup
  - https://learn.microsoft.com/troubleshoot/system-center/scom/troubleshoot-gray-agent-states
  - https://learn.microsoft.com/troubleshoot/system-center/scom/event-4001-monitor-sql-server-2012
---

**fullpath**:C:\Windows\System32\winevt\Logs\Operations Manager.evtx

# description

Operations Manager.evtx is the event log file for the Operations Manager channel written by the System Center Operations Manager agent (Microsoft Monitoring Agent / HealthService) and management servers. Event sources include HealthService, OpsMgr Connector, Health Service Script and OpsMgr Management Configuration.

## simple description

> ### 2026-11-21 Claude said
> This is the Windows event log file used by System Center Operations Manager (SCOM) and the Microsoft Monitoring Agent. It records agent health, connectivity to management servers, script errors and configuration updates. Admins read it to troubleshoot why an agent is grey or not reporting.
>
> **SOC NOTE**: Useful to confirm whether SCOM monitoring was healthy during an incident, and to spot RunAs account distribution problems (event 1108). Script events (e.g. 4001) can reveal monitoring scripts that ran; attackers who compromise SCOM can push management packs that execute code on every agent, so unexpected management pack or script events deserve review.
>

# purpose

Stores the Operations Manager log. During startup the Microsoft Monitoring Agent service writes to this log; if the Windows Event Log service is not running, the agent service can hang in the Starting state. Events such as 20070, 21016, 21006, 20057, 21023, 2010, 2003, 1108, 4000 and 4001 are logged here for connectivity, authentication, configuration and script issues.
