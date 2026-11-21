---
created: 2026-11-21
fullpath: 'c:\windows\system32\setres.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - servercore
aliases:
  - setres.exe
  - Set-DisplayResolution
url:
  - https://learn.microsoft.com/powershell/module/servercore/set-displayresolution?view=windowsserver2025-ps
---

**fullpath**:c:\windows\system32\setres.exe

# description

setres.exe changes the display resolution on Windows Server Core. Learn documents it only indirectly: the ServerCore module cmdlet `Set-DisplayResolution` invokes setres, whose output reads "setres will now attempt to apply the following display settings". Related cmdlet: `Get-DisplayResolution`.

## simple description

> ### 2026-11-21 Claude said
> setres.exe is a small built-in utility for changing screen resolution, mainly used on Server Core where there is no Display settings UI. Administrators normally call it through the PowerShell cmdlet Set-DisplayResolution. It needs width and height in pixels. It has no network or security functionality.
>
> **SOC NOTE**: Low security relevance; it is a signed system binary with no known LOLBAS abuse. Its execution from an unusual parent (Office, script host) would be anomalous but not inherently malicious. Use it mainly as context in process timelines.
>

# purpose

Apply a new display width and height on Server Core installations.

# typical use cases

| usage | description |
| --- | --- |
| `Set-DisplayResolution -Width 1024 -Height 768 -Force` | Set the resolution to 1024x768 without a prompt; the cmdlet calls setres. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
