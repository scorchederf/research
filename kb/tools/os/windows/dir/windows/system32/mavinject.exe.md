---
created: 2026-11-21
fullpath: 'C:\Windows\System32\mavinject.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - app-v
aliases:
  - mavinject.exe
  - Microsoft Application Virtualization Injector
url:
---

**fullpath**:C:\Windows\System32\mavinject.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> mavinject.exe is the Microsoft Application Virtualization (App-V) injector. App-V uses it to inject its runtime DLL into processes so they run inside a virtual application environment. It is signed by Microsoft and present on Windows 10/11 even when App-V is not in use.
>
> **SOC NOTE**: mavinject.exe can inject any DLL into a running process: `mavinject.exe <PID> /INJECTRUNNING C:\path\evil.dll` (MITRE ATT&CK T1218.013 Mavinject, T1055.001 DLL injection). On hosts that don't use App-V, any execution is suspicious; look for /INJECTRUNNING or /HMODULE arguments and DLLs from user-writable paths, and correlate with Sysmon Event ID 8 (CreateRemoteThread) and 7 (image load).
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
