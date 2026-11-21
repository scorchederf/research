---
created: 2026-11-21
fullpath: 'c:\windows\system32\shdocvw.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - dll
aliases:
  - shdocvw.dll
  - SHDocVw
  - Microsoft Internet Controls
url:
  - https://learn.microsoft.com/windows/win32/shell/dshellwindowsevents
  - https://learn.microsoft.com/windows/win32/shell/scriptable-shell-objects-roadmap
---

**fullpath**:c:\windows\system32\shdocvw.dll

# description

`Shdocvw.dll` is the Windows Shell library that implements Internet Explorer and Shell window automation objects, exposed to Visual Basic as the **Microsoft Internet Controls (SHDocVw)** type library. Learn lists it as the DLL for the `DShellWindowsEvents` object (Shdocvw.dll version 5.00.2014.0216 or later, Internet Explorer 5, header Exdisp.h). It is used together with Shell32 (Microsoft Shell Controls and Automation).

## simple description

> ### 2026-11-21 Claude said
> shdocvw.dll is a long-standing Windows system library, originally the "Shell Doc Object and Control Library", that provides the Internet Explorer web browser control and Shell window objects to other programs. Applications and scripts use it to embed a browser, enumerate open Explorer/IE windows, or automate them. In modern Windows much of its code moved to ieframe.dll, but the file remains for compatibility. It is a normal, Microsoft-signed file.
>
> **SOC NOTE**: Its COM objects (ShellWindows, ShellBrowserWindow, InternetExplorer.Application) are abused for lateral movement via DCOM (MITRE ATT&CK T1021.003) and for script-based execution or proxy downloads. A shdocvw.dll outside System32/SysWOW64, or an unsigned copy, suggests DLL search-order hijacking (T1574.001). The ShellBags artifacts often discussed in forensics were historically stored under Software\Microsoft\Windows\Shell(NoRoam) keys tied to this component.
>

# purpose

To instantiate the scriptable Shell objects with early binding in Visual Basic applications, a project references Microsoft Internet Controls (SHDocVw) and Microsoft Shell Controls and Automation (Shell32). Shdocvw.dll provides the `DShellWindowsEvents` object, which receives `IShellWindows` window registration events through its `WindowRegistered` and `WindowRevoked` methods, so a caller can monitor when a Shell window is registered or revoked.
