---
created: 2026-11-21
fullpath: 'C:\Windows\System32\desk.cpl'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - desk.cpl
  - Display Control Panel
  - Display Properties
url:
  - https://learn.microsoft.com/windows/win32/shell/executing-control-panel-items
  - https://learn.microsoft.com/windows/win32/shell/shell-controlpanelitem
  - https://learn.microsoft.com/windows/win32/shell/using-cplapplet
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-controlpaneldisplay
---

**fullpath**:C:\Windows\System32\desk.cpl

# description

desk.cpl is the Windows Display Control Panel item, a .cpl module (a DLL that exports the `CPlApplet` function) loaded by Control Panel. It can be opened with `control.exe desk.cpl,<tab>` or via `Shell.ControlPanelItem("desk.cpl")`, and can be disabled by the "Disable the Display Control Panel" policy (`NoDispCPL`).

## simple description

> ### 2026-11-21 Claude said
> desk.cpl is the classic Display settings applet. Opening it shows screen resolution, monitor and (on older Windows) theme and screensaver settings; on Windows 10/11 it mostly redirects to the Settings app display page. It's a DLL with a .cpl extension that Control Panel (control.exe / rundll32 shell32.dll,Control_RunDLL) loads. It is a normal, signed Windows file.
>
> **SOC NOTE**: .cpl files are DLLs, so attackers abuse Control Panel items to run code via control.exe or rundll32 (MITRE ATT&CK T1218.002 System Binary Proxy Execution: Control Panel). A legitimate desk.cpl lives only in System32/SysWOW64 and is Microsoft-signed; a desk.cpl elsewhere, unsigned, or registered under `HKCU\Software\Microsoft\Windows\CurrentVersion\Control Panel\Cpls` deserves investigation. Check process creation (4688/Sysmon 1) for `control.exe` / `rundll32.exe` loading unexpected .cpl paths.
>

# purpose

Provides the Display Control Panel item. On Windows Vista and later Learn lists these command lines for specific pages:

| usage | description |
| --- | --- |
| `%windir%\system32\control.exe desk.cpl,Settings,@Settings` | Screen resolution / display settings. |
| `%windir%\system32\control.exe desk.cpl,Themes,@Themes` | Themes. |
| `%windir%\system32\control.exe desk.cpl,screensaver,@screensaver` | Screensaver. |
| `%windir%\system32\control.exe desk.cpl,Monitor,@Monitor` | Multi-monitor settings. |

As a Control Panel module, Control Panel calls its `CPlApplet` function with messages such as `CPL_INIT`, `CPL_GETCOUNT`, `CPL_DBLCLK`, `CPL_STOP` and `CPL_EXIT`. The user policy "Disable the Display Control Panel" (`Software\Microsoft\Windows\CurrentVersion\Policies\System\NoDispCPL`) prevents it from running.
