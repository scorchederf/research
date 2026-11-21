---
created: 2026-11-21
fullpath: 'C:\Windows\System32\dllhost.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - com
  - surrogate
aliases:
  - dllhost.exe
  - COM Surrogate
  - DLL surrogate
url:
  - https://learn.microsoft.com/windows/win32/com/dll-surrogates
  - https://learn.microsoft.com/windows/win32/com/dllsurrogate
  - https://learn.microsoft.com/windows/win32/com/using-the-system-supplied-surrogate
  - https://learn.microsoft.com/windows/win32/com/surrogate-sharing
  - https://learn.microsoft.com/troubleshoot/sql/database-engine/development/run-dll-based-com-object
---

**fullpath**:C:\Windows\System32\dllhost.exe

# description

`dllhost.exe` is the system-supplied COM DLL surrogate: the default executable that the DCOM Service Control Manager (rpcss) launches to load an in-process COM DLL server out of process. A class is hosted in it when its AppID has an empty `DllSurrogate` value.

## simple description

> ### 2026-11-21 Claude said
> dllhost.exe, shown as 'COM Surrogate' in Task Manager, is a generic host process that loads COM DLLs so they run in their own process instead of inside the calling application. Windows uses it for things like thumbnail generation in Explorer, so if a buggy codec crashes, Explorer survives. Several instances are normal, each launched with a /Processid:{CLSID} argument.
>
> **SOC NOTE**: Frequently abused for masquerading and injection: malware names itself dllhost.exe outside System32, injects into it (T1055), or uses COM elevation monikers/UAC bypasses (T1548.002, e.g. CMSTPLUA {3E5FC7F9-9A51-4367-9063-A120244FBEC7}) that run under dllhost.exe. Check parent (should be svchost/DcomLaunch), the /Processid CLSID, network connections and loaded modules. COM hijacking (T1546.015) can make dllhost load attacker DLLs.
>

# purpose

Runs DLL servers in a surrogate process, giving fault isolation, the ability to serve multiple clients, remote clients in a distributed environment, protection of clients from untrusted server code, and the surrogate's security context. COM launches the surrogate together with the requested CLSID; it is a mixed-threading pseudo-COM server, and COM handles unloading DLLs and terminating the process based on marshaled object count. DLL servers with the same AppID and security identity share one surrogate. `DllSurrogate` must be present under `HKLM\SOFTWARE\Classes\AppID\{AppID_GUID}`; empty means use dllhost.exe, a path names a custom surrogate (see also `DllSurrogateExecutable`).

# typical use cases

| usage | description |
| --- | --- |
| `reg add "HKCR\AppID\{GUID}" /v DllSurrogate /t REG_SZ /d ""` | Configure a COM class's AppID to use the system surrogate (dllhost.exe), so the DLL runs out of process. |

# options

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
