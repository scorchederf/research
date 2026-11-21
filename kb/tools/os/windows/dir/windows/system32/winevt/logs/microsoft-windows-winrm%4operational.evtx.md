---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-WinRM%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - winrm
aliases:
  - Microsoft-Windows-WinRM%4Operational.evtx
  - Microsoft-Windows-WinRM/Operational
url:
  - https://learn.microsoft.com/windows/win32/winrm/portal
  - https://learn.microsoft.com/windows/win32/winrm/about-windows-remote-management
  - https://learn.microsoft.com/powershell/scripting/security/remoting/winrm-security?view=powershell-7.6
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-WinRM%4Operational.evtx

# description

This is the event log file for the WinRM Operational channel. Windows Remote Management (WinRM) is the Microsoft implementation of the SOAP-based WS-Management protocol and is used by PowerShell remoting, `winrs` and event forwarding. Learn notes that WinRM events can't be obtained through WinRM scripting but can be viewed with `wevtutil.exe`, and refers to external research on the event logs that PowerShell remoting sessions generate.

## simple description

> ### 2026-11-21 Claude said
> This file stores the "WinRM / Operational" event log, which records activity of the Windows Remote Management service: listeners starting, clients connecting, shells being created and authentication problems. WinRM is what PowerShell Remoting (`Enter-PSSession`, `Invoke-Command`) uses on ports 5985/5986. The `%4` in the name stands for the `/` in the channel name.
>
> **SOC NOTE**: Key lateral movement evidence (T1021.006 Windows Remote Management). On the source host, Event ID 6 (WSMan session created) shows the destination; on the target, Event IDs 91 (shell created) and 142/161 (errors/auth failures) show incoming use. Correlate with Security 4624 logon type 3 and `wsmprovhost.exe` process creation. Clearing it (T1070.001) is suspicious.
>

# purpose

Holds operational events from the WinRM service. _Event IDs for this channel are not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
