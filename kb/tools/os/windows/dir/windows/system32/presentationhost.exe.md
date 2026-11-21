---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Presentationhost.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - wpf
  - lolbin
aliases:
  - PresentationHost.exe
  - WPF Host
url:
  - https://learn.microsoft.com/dotnet/desktop/wpf/app-development/wpf-host-presentationhost-exe
  - https://learn.microsoft.com/dotnet/desktop/wpf/app-development/hosting-wpf-applications
  - https://learn.microsoft.com/dotnet/desktop/wpf/app-development/configure-vs-to-debug-a-xaml-browser-to-call-a-web-service
---

**fullpath**:C:\Windows\System32\Presentationhost.exe

# description

Windows Presentation Foundation (WPF) Host, the application that hosts WPF content in compatible browsers. It is registered as the shell and MIME handler for loose XAML (.xaml) and XAML browser applications (.xbap), loads the correct CLR and WPF assemblies and enforces the deployment zone's permission level. XBAPs require legacy browsers such as Internet Explorer and are no longer supported by modern browsers.

## simple description

> ### 2026-11-21 Claude said
> PresentationHost.exe is part of the .NET Framework WPF stack and runs XBAP and loose XAML "web apps" that used to open inside Internet Explorer. The technology is obsolete, so on a modern system it should almost never run. It is signed by Microsoft.
>
> **SOC NOTE**: Listed LOLBAS binary: it can execute a local or remote .xbap (arbitrary .NET code) under a signed Microsoft process, bypassing application control (MITRE T1218). Any execution, especially with a URL or from Office/browser parents, deserves investigation.
>

# purpose

Activates browser-hosted WPF content: launches the registered HTML handler to host it, loads the required CLR and WPF assemblies and applies the zone permissions. Also used by Visual Studio for debugging XBAPs.

# typical use cases

| usage | description |
| --- | --- |
| `PresentationHost.exe example.xbap` | Shell handler: activate an XBAP. |
| `PresentationHost.exe -embedding example.xbap` | MIME handler activation. |
| `PresentationHost.exe -debug example.xbap` | Visual Studio debugging of a local XBAP. |
| `PresentationHost.exe -debug -debugSecurityZoneURL http://www.example.com c:\folderpath\example.xbap` | Debug an XBAP as if deployed from the given URL. |

# options

| option | description |
| --- | --- |
| `filename` | Path of the file to activate; can also be a URI. |
| `-debug` | Activates an application without committing it to or running it from the store. Only works for local files. |
| `-debugSecurityZoneURL <url>` | Debug the application as if deployed from the URL, setting deployment zone and site of origin. |
| `-embedding` | Required by OLE; set internally when `-event` or `-debug` is used. |
| `-event <eventname>` | Open the named event and signal it when ready to host WPF content; terminates if the event can't be opened. |
| `-launchApplication <url>` | Launches a standalone ClickOnce application from the URL, applying IE and WinINet security policy. |
