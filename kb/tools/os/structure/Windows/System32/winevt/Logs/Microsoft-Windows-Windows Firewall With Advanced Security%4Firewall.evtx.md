---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx
  - Windows Firewall With Advanced Security/Firewall
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/troubleshoot-windows-firewall-with-advanced-security-guidance
  - https://learn.microsoft.com/windows/security/operating-system-security/network-security/windows-firewall/
  - https://learn.microsoft.com/windows/security/operating-system-security/network-security/windows-firewall/configure-logging
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx

# description

_Not documented on Microsoft Learn at 2026/11/21 05:17 UTC_ - Learn has no page describing this specific event log file. Related Learn content: Windows Firewall with Advanced Security events can be viewed in Event Viewer, and Windows 11 enhanced the firewall event logs so an audit can identify the specific filter responsible for an event. Separately, the firewall's packet log is a text file at `%windir%\system32\logfiles\firewall\pfirewall.log` (not this .evtx).

## simple description

> ### 2026-11-21 Claude said
> This file is the event log where Windows Defender Firewall records changes to its own configuration, such as rules being added, changed or deleted, and profile or setting changes. In Event Viewer it appears under Applications and Services Logs > Microsoft > Windows > Windows Firewall With Advanced Security > Firewall. It does not log individual network connections; those go to the firewall text log (`pfirewall.log`) or to Security log audit events. It's useful for seeing who or what changed the firewall and when.
>
> **SOC NOTE**: Firewall rule changes are a common attacker step to open remote access (RDP, WinRM) or block security tools (MITRE ATT&CK T1562.004). Classic event IDs are 2004 (rule added), 2005 (rule modified), 2006 (rule deleted) and 2033 (all rules deleted). Newer Windows 11 builds may log rule changes under different IDs, so check your OS version. The events usually show the rule details and the modifying application, so look for netsh.exe, PowerShell or unusual processes changing rules.
>
> _Not documented on Microsoft Learn at 2026/11/21 05:17 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 05:17 UTC_
