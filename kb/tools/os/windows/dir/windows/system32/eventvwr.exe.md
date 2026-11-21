---
created: 2026-11-21
fullpath: 'C:\Windows\System32\eventvwr.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - event-log
  - mmc
aliases:
  - eventvwr.exe
  - Event Viewer
  - eventvwr.msc
url:
  - https://learn.microsoft.com/host-integration-server/core/msdrdaservice-event-logs
  - https://learn.microsoft.com/host-integration-server/core/how-to-select-computers-in-event-viewer1
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.management/show-eventlog?view=powershell-5.1
---

**fullpath**:C:\Windows\System32\eventvwr.exe

# description

`eventvwr.exe` is the command-line launcher for Event Viewer, the Microsoft Management Console (MMC) snap-in (`%SYSTEMROOT%\system32\Eventvwr.msc`) used to browse and manage event logs. Related tools are `wevtutil`, `Get-WinEvent` and `Show-EventLog`, which opens Event Viewer from PowerShell.

## simple description

> ### 2026-11-21 Claude said
> eventvwr.exe opens Event Viewer, the Windows tool for reading the System, Application, Security and many application/service logs. It is a small launcher that starts the eventvwr.msc console in MMC. Admins use it to troubleshoot errors and review security events, locally or on remote computers.
>
> **SOC NOTE**: Known UAC bypass (T1548.002): eventvwr.exe auto-elevates and looks up HKCU\Software\Classes\mscfile\shell\open\command before HKCR, so writing a command there runs it elevated without a prompt. Hunt for that registry key being set and for eventvwr.exe spawning anything other than mmc.exe. Also watch for Event Viewer used before log clearing (T1070.001).
>

# purpose

Starts Event Viewer, which lets you view events from multiple event logs, save event filters as reusable custom views, schedule a task to run in response to an event, and create and manage event subscriptions. Typing `eventvwr` at a command prompt starts it; the tool supports options that set the computer the snap-in connects to and the event logs it displays (ignored when connecting to previous Windows versions). In the console, right-click Event Viewer > **Connect to another computer** to view a remote machine's logs.

# typical use cases

| usage | description |
| --- | --- |
| `eventvwr` | Start Event Viewer from a command prompt. |
| `eventvwr /?` | Display help for the eventvwr command-line tool. |
| `Show-EventLog -ComputerName "Server01"` | Open Event Viewer showing the classic event logs of a remote computer from PowerShell. |

# options

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
