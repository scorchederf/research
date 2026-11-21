---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - ue-v
  - windows-adk
aliases:
  - "AppLauncher.exe"
url: []
---

**fullpath**: C:\Program Files\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

## simple description

> ### 2026-11-21 Claude said
> AppLauncher.exe is a small helper that ships with the User Experience Virtualization (UE-V) management tools in the Windows Kits (Windows ADK). It is used together with the UE-V template generator to launch an application so its settings locations can be captured into a settings location template. Administrators use it while building custom UE-V templates; it is not part of a normal end-user workflow. Its presence simply indicates the Windows ADK UE-V tools were installed.
>
> **SOC NOTE**: AppLauncher.exe is Microsoft-signed and launches arbitrary programs, so it could be used as a proxy-execution binary to hide the real parent of a payload (T1218 System Binary Proxy Execution). On machines that are not admin/packaging workstations its execution is unusual; review the child process and command line. Process creation events (Sysmon 1 / Security 4688) show it as parent of the launched app.
>
> _Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_
