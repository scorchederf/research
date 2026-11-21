---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wsmprovhost.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - winrm
  - powershell-remoting
aliases:
  - wsmprovhost.exe
  - Wsmprovhost.exe
  - PowerShell host process
url:
  - https://learn.microsoft.com/powershell/scripting/security/remoting/powershell-remoting-faq
  - https://learn.microsoft.com/windows/win32/winrm/winrm-application-hosting
  - https://learn.microsoft.com/windows/win32/winrm/windows-remote-management-architecture
---

**fullpath**:C:\Windows\System32\wsmprovhost.exe

# description

Wsmprovhost.exe is the PowerShell host process that WS-Management starts on a remote computer when a client opens a PowerShell remoting session. It is part of Windows Remote Management (WinRM), the Microsoft implementation of WS-Management; in the WinRM service hosting model, requests are routed either to plug-ins in the main service or through a host where third-party plug-ins run.

## simple description

> ### 2026-11-21 Claude said
> wsmprovhost.exe is the process that actually runs your commands on a machine when someone connects to it with PowerShell remoting (Enter-PSSession, Invoke-Command) over WinRM. It is started by the WinRM service (svchost) and runs as the connecting user. Each remote session normally gets its own wsmprovhost.exe process.
>
> **SOC NOTE**: A wsmprovhost.exe process means someone ran PowerShell remotely on this host (MITRE ATT&CK T1021.006 Windows Remote Management, T1059.001 PowerShell). Child processes of wsmprovhost.exe (cmd, net, whoami, etc.) are strong lateral-movement indicators. Correlate with Security 4624 logon type 3, the Microsoft-Windows-WinRM/Operational log (e.g. event 91 session creation) and PowerShell Operational 4103/4104 script block logging.
>

# purpose

For the fan-out configuration, when a local computer connects to a remote computer, WS-Management establishes a connection and uses a plug-in for PowerShell to start the PowerShell host process (Wsmprovhost.exe) on the remote computer. In the IIS-hosted fan-in configuration, all PowerShell sessions instead run in the same host process.

# typical use cases

| usage | description |
| --- | --- |
| `Enter-PSSession <ComputerName>` | Starts an interactive remote session, which runs in Wsmprovhost.exe on the remote computer. |
| `Invoke-Command -ComputerName ServerB -ScriptBlock {hostname}` | Runs a command remotely through WS-Management and the PowerShell host process. |

# options

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
