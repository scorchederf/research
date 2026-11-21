---
created: 2026-11-21
fullpath: 'c:\windows\system32\setupapi.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - dll
aliases:
  - setupapi.dll
  - SetupAPI
  - Setup API
url:
  - https://learn.microsoft.com/windows-hardware/drivers/install/setupapi
  - https://learn.microsoft.com/windows/win32/api/setupapi/
  - https://learn.microsoft.com/windows/win32/setupapi/overview
---

**fullpath**:c:\windows\system32\setupapi.dll

# description

Setupapi.dll implements the Setup Application Programming Interface (SetupAPI), a Windows system component that provides general setup functions (Setup*Xxx*) and device installation functions (SetupDi*Xxx*) used by class installers, co-installers and device installation applications. Microsoft recommends CfgMgr32.dll where possible, and Windows Installer for application setup.

## simple description

> ### 2026-11-21 Claude said
> setupapi.dll is a core Windows library used to install drivers and process INF files. Device Manager, Plug and Play and driver installers call it to copy files, write registry entries and register devices. It also exports InstallHinfSection, which can run an INF section via rundll32.
>
> **SOC NOTE**: `rundll32 setupapi.dll,InstallHinfSection DefaultInstall 128 <file.inf>` is a known LOLBin proxy execution path (T1218.011) that can run commands or register COM scriptlets from a malicious INF. Device install activity is logged in C:\Windows\INF\setupapi.dev.log, useful for USB device timelines.
>

# purpose

Provides functions that work with INF files to queue and install files, update registry entries, handle disk prompting and errors, log installed files and keep an MRU source list; and device installation functions (device information sets, interfaces, class/device registry keys, driver selection). `InstallHinfSection` is an entry point exported by Setupapi.dll that executes a section of an .inf file and can be invoked with Rundll32.exe.
