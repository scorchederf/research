---
created: 2026-11-21
fullpath: 'C:\Windows\System32\SyncAppvPublishingServer.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - appv
  - lolbin
aliases:
  - SyncAppvPublishingServer.exe
url:
  - https://learn.microsoft.com/powershell/module/appvclient/sync-appvpublishingserver?view=windowsserver2025-ps
---

**fullpath**:C:\Windows\System32\SyncAppvPublishingServer.exe

# description

`SyncAppvPublishingServer.exe` belongs to the Microsoft Application Virtualization (App-V) client. Learn documents the matching PowerShell cmdlet `Sync-AppvPublishingServer` (AppvClient module), which starts the App-V publishing refresh in the current user's context: it connects to all publishing servers added on the client and exposes new App-V packages and their extension points. The executable itself has no Learn page.

## simple description

> ### 2026-11-21 Claude said
> This program triggers an App-V "publishing refresh", which makes the App-V client check its publishing servers for new virtual applications for the user. Internally it starts PowerShell and calls the `Sync-AppvPublishingServer` cmdlet with the arguments it was given. A matching `SyncAppvPublishingServer.vbs` script also exists.
>
> **SOC NOTE**: Known LOLBin for signed binary proxy execution (T1216 / T1218): because arguments are passed into a PowerShell command line, input like `SyncAppvPublishingServer.exe "n; Start-Process calc"` runs arbitrary PowerShell, which can bypass rules that only block `powershell.exe`. Any use on machines without App-V, or with `;` in the arguments, is highly suspicious.
>

# purpose

Starts an App-V publishing refresh for the current user (per the `Sync-AppvPublishingServer` cmdlet description).

# typical use cases

| usage | description |
| --- | --- |
| `Sync-AppvPublishingServer -Name "MyServer"` | PowerShell cmdlet equivalent: start publishing refresh for the current user for the server MyServer. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
