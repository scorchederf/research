---
created: 2026-11-21
fullpath: 'c:\windows\system32\vsjitdebugger.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visualstudio
  - debugging
aliases:
  - vsjitdebugger.exe
  - Visual Studio Just-In-Time Debugger
url:
  - https://learn.microsoft.com/visualstudio/debugger/debug-using-the-just-in-time-debugger?view=visualstudio
  - https://learn.microsoft.com/visualstudio/debugger/just-in-time-debugging-in-visual-studio?view=visualstudio
---

**fullpath**:c:\windows\system32\vsjitdebugger.exe

# description

This is the Visual Studio Just-In-Time (JIT) debugger, which can launch Visual Studio automatically when an app running outside Visual Studio errors or crashes and shows the **Choose Just-In-Time Debugger** dialog. It is installed with Visual Studio (Individual components > Debugging and testing) and is registered through the `AeDebug\Debugger` and `.NETFramework\DbgManagedDebugger` registry values. Learn does not name the executable file itself.

## simple description

> ### 2026-11-21 Claude said
> `vsjitdebugger.exe` is the small program Windows starts when an application crashes on a machine with Visual Studio installed. It shows a dialog asking which debugger to use and then attaches Visual Studio to the crashing process. It is registered as the system's automatic crash debugger.
>
> **SOC NOTE**: The `AeDebug\Debugger` value it uses is a known persistence / execution hook: replacing it makes Windows run an attacker binary whenever any process crashes (T1546). It can also be used to attach to and inspect processes. Alert on changes to `HKLM\SOFTWARE\(Wow6432Node\)Microsoft\Windows NT\CurrentVersion\AeDebug` and on vsjitdebugger on hosts without Visual Studio.
>

# purpose

Lets a developer debug an unhandled exception or crash in a Windows desktop app in a new Visual Studio instance. It doesn't work for Universal Windows apps or for managed code hosted in a native application. Enabling or disabling JIT debugging in **Tools > Options > Debugging > General** sets the registry keys and may need administrator rights.

# typical use cases

| usage | description |
| --- | --- |
| `reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug" /v Debugger` | Disable JIT debugging when Visual Studio is no longer installed (also delete the `Wow6432Node` and `DbgManagedDebugger` entries). |
| `reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug" /v Auto /t REG_DWORD /d 1` | Fix for JIT debugging failing to start: add `Auto` = 1. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
