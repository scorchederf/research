---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v2.0.50727\Dfsvc.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - clickonce
aliases:
  - Dfsvc.exe
  - ClickOnce deployment service
url:
  - https://learn.microsoft.com/windows/win32/shell/appids
  - https://learn.microsoft.com/kusto/tools/kusto-explorer-troubleshooting?view=microsoft-fabric
  - https://learn.microsoft.com/visualstudio/deployment/clickonce-security-and-deployment?view=visualstudio
  - https://learn.microsoft.com/security-updates/securitybulletins/2007/ms07-040
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v2.0.50727\Dfsvc.exe

# description

Dfsvc.exe is the .NET Framework ClickOnce deployment service process that manages installation and updates of ClickOnce applications in the per-user ClickOnce store. It ships with the .NET Framework 2.0 runtime (v2.0.50727) and later. Learn lists it among programs excluded from taskbar pinning and recent lists, and advises terminating dfsvc.exe before clearing the ClickOnce store at `%userprofile%\appdata\local\apps\2.0`.

## simple description

> ### 2026-11-21 Claude said
> Dfsvc.exe is the background helper that installs and updates ClickOnce applications, which are .NET apps launched from a web page or file share without admin rights. It starts when a user opens a .application link and exits when idle. Installed apps are stored per user in AppData\Local\Apps\2.0. It is a normal part of the .NET Framework.
>
> **SOC NOTE**: ClickOnce is abused for initial access and persistence (T1127, T1204): malicious .application/.appref-ms deployments install via dfsvc.exe without admin rights. Look for dfsvc.exe spawning unknown children, new folders in `%LOCALAPPDATA%\Apps\2.0`, and network connections to untrusted deployment URLs.
>

# purpose

Install, update and roll back ClickOnce applications per user; ClickOnce apps are self-updating and run in an isolated per-user, per-application cache.

# typical use cases

| usage | description |
| --- | --- |
| `rd /q /s %userprofile%\appdata\local\apps\2.0` | Clear a corrupted ClickOnce store after terminating dfsvc.exe; apps reinstall on next launch. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
