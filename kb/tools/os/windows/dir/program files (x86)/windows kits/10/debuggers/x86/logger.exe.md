---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\logger.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - debugging
  - windows-sdk
aliases:
  - logger.exe
  - Logger
url:
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/using-logger-exe
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/logger
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/using-the-debugger-and-logexts-dll
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\logger.exe

# description

Logger.exe is the stand-alone vehicle for the Logger API-logging tool in Debugging Tools for Windows (Windows Kits 10, x86 build). It is essentially a very small debugger that takes a single target and injects Logexts.dll into it; the same logging can be done from CDB or WinDbg with the Logexts.dll extension commands, and output .lgv files are read with LogViewer.

## simple description

> ### 2026-11-21 Claude said
> logger.exe is an old debugging utility from the Windows Debugging Tools that launches a program and records every Windows API call it makes (file, registry, COM, etc.). It works by injecting logexts.dll into the target process. Results go to a LogExts folder on the Desktop and are viewed with LogViewer. This is the 32-bit (x86) copy from the Windows 10 SDK/WDK.
>
> **SOC NOTE**: Microsoft-signed launcher that starts an arbitrary process and injects a DLL into it, so it can serve as a proxy execution/DLL injection LOLBin (MITRE ATT&CK T1218, T1055.001). Rare on non-developer machines; investigate its execution, the child process it launched, and LogExts\*.lgv/.txt files on the Desktop, which can reveal the target's API activity.
>

# purpose

Loads the specified application and injects code that loads and initializes Logexts.dll in the target process, then logs API calls by category. A Change Settings dialog lets you choose API categories, enable or disable logging, set a module inclusion/exclusion list, flush the buffer (default 2144 bytes) and start the target with Go; pressing F12 in the target's window reopens the dialog. When run through Logger.exe only an .lgv file is written (plus a zero-size .txt file), always in the LogExts subdirectory of the desktop.

# typical use cases

| usage | description |
| --- | --- |
| `logger Target` | Loads the target application and injects Logger into it. |

# options

| option | description |
| --- | --- |
| `Target` | Name of the target application to load and log. |
