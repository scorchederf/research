---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wuauclt.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-update
aliases:
  - wuauclt.exe
  - Windows Update Client
url:
  - https://learn.microsoft.com/windows-server/get-started/removed-deprecated-features-windows-server
  - https://learn.microsoft.com/troubleshoot/windows-server/installing-updates-features-roles/re-register-windows-clientserver-in-wsus
  - https://learn.microsoft.com/troubleshoot/windows-server/installing-updates-features-roles/troubleshoot-windows-update-error-0x80244007
  - https://learn.microsoft.com/defender-endpoint/defender-endpoint-exclusions-common-mistakes
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/symbols-windows-update
---

**fullpath**:C:\Windows\System32\wuauclt.exe

# description

wuauclt.exe is the Windows Update Client binary in System32 that manages update tasks alongside the Windows Update service (wuauserv). It ships with Windows as part of the Windows Update Agent, together with wuapi.dll and wuaueng.dll; the `/detectnow` switch is removed and no longer supported on Windows Server 2016, with the `Microsoft.Update.AutoUpdate` COM object `DetectNow()` as the replacement.

## simple description

> ### 2026-11-21 Claude said
> wuauclt.exe is the legacy Windows Update (Automatic Updates) client. Admins historically used it to force a check for updates or re-register a machine with WSUS. On modern Windows most of its switches were replaced by UsoClient.exe and the Update Session Orchestrator, but the binary still exists and runs as part of update activity. Seeing it occasionally on endpoints is normal.
>
> **SOC NOTE**: wuauclt.exe is a LOLBin: attackers run `wuauclt.exe /UpdateDeploymentProvider <dll> /RunHandlerComServer` to load an arbitrary DLL under a signed Microsoft process (MITRE ATT&CK T1218 System Binary Proxy Execution). Alert on wuauclt with `/UpdateDeploymentProvider` pointing outside System32, on unusual parent processes, or on network connections to non-Microsoft hosts. Microsoft lists wuauclt.exe as a process you should not exclude from Defender scanning.
>

# purpose

Client-side component of Windows Update that manages update tasks, including WSUS detection and client re-registration.

# typical use cases

| usage | description |
| --- | --- |
| `wuauclt /detectnow` | Triggers a detection cycle so a client re-registers with WSUS (removed and unsupported on Windows Server 2016 and later). |
| `wuauclt.exe /resetauthorization /detectnow` | Resets the WSUS client authorization cookie and starts detection; used when a client has WSUS registration issues. |

# options

| option | description |
| --- | --- |
| `/detectnow` | Starts an update detection cycle. Removed and no longer supported starting with Windows Server 2016. |
| `/resetauthorization` | Resets the client's WSUS authorization; used together with `/detectnow`. |
