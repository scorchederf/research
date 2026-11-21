---
created: 2026-11-21
fullpath: 'C:\Windows\System32\SyncAppvPublishingServer.vbs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - app-v
  - lolbin
aliases:
  - SyncAppvPublishingServer.vbs
  - Sync-AppvPublishingServer
url:
  - https://learn.microsoft.com/powershell/module/appvclient/sync-appvpublishingserver?view=windowsserver2025-ps
---

**fullpath**:C:\Windows\System32\SyncAppvPublishingServer.vbs

# description

SyncAppvPublishingServer.vbs is a VBScript wrapper shipped with the built-in App-V client that triggers an App-V publishing refresh. Learn documents the underlying `Sync-AppvPublishingServer` cmdlet (AppvClient module), which connects to all added publishing servers and exposes new App-V packages and their extension points to the current user. Related: SyncAppvPublishingServer.exe, AppvClient PowerShell module.

## simple description

> ### 2026-11-21 Claude said
> This VBScript is part of Microsoft Application Virtualization (App-V) built into Windows 10/11 Enterprise. It refreshes which virtual applications are published to the user by calling the Sync-AppvPublishingServer PowerShell cmdlet. It is normally triggered by App-V at logon or on schedule. Most organisations that do not use App-V never run it.
>
> **SOC NOTE**: LOLBAS: the script builds a PowerShell command line from its argument, so `SyncAppvPublishingServer.vbs "n; <powershell code>"` executes arbitrary PowerShell via wscript (T1216 System Script Proxy Execution), bypassing some PowerShell restrictions. Alert on wscript/cscript running this script with `;` or encoded content, and on resulting powershell.exe children.
>

# purpose

Initiate an App-V publishing refresh for the current user against configured publishing servers; cmdlet parameters include `-ServerId`, `-Name`, `-URL`, `-Global`, `-Force`, `-NetworkCostAware` and `-HidePublishingRefreshUI`.


