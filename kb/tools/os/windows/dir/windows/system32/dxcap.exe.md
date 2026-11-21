---
created: 2026-11-21
fullpath: 'C:\Windows\System32\dxcap.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - directx
  - lolbin
aliases:
  - dxcap.exe
  - DXCap
url:
  - https://learn.microsoft.com/windows/uwp/gaming/handling-device-lost-scenarios
  - https://learn.microsoft.com/windows/uwp/gaming/use-the-directx-runtime-and-visual-studio-graphics-diagnostic-features
---

**fullpath**:C:\Windows\System32\dxcap.exe

# description

DXCap is a command-line tool for Direct3D event capture and playback used by Visual Studio Graphics Diagnostics. It and its support DLLs are installed into System32/SysWOW64 by the Graphics Tools optional feature (Feature on Demand), no longer by the Windows SDK. Related: Visual Studio Graphics Debugging, PIX.

## simple description

> ### 2026-11-21 Claude said
> dxcap.exe records the DirectX graphics calls an app makes so that developers can replay and debug rendering problems. It is only present when the optional Windows feature "Graphics Tools" has been added. It is a developer tool, not something normal users run. It can also force a GPU timeout to test error handling.
>
> **SOC NOTE**: LOLBAS: `dxcap.exe -c <exe>` launches an arbitrary executable under capture (T1127/T1218 proxy execution) from a signed binary. On hosts without game/graphics development, any dxcap execution, or dxcap spawning unexpected children, is suspicious.
>

# purpose

Capture and play back Direct3D events for graphics debugging, and test device-removed handling.

# typical use cases

| usage | description |
| --- | --- |
| `dxcap -forcetdr` | Force a GPU Timeout Detection and Recovery event while the app runs, triggering DXGI_ERROR_DEVICE_REMOVED to test error handling. |

# options

| option | description |
| --- | --- |
| `-forcetdr` | Forces a GPU Timeout Detection and Recovery (TDR) event. |
