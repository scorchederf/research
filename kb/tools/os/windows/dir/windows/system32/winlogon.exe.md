---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winlogon.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - logon
  - security
aliases:
  - winlogon.exe
  - Winlogon
  - WinLogon
url:
  - https://learn.microsoft.com/windows/win32/secauthn/winlogon-states
  - https://learn.microsoft.com/windows/win32/secauthn/initializing-winlogon
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/debugging-winlogon
  - https://learn.microsoft.com/security-updates/securitybulletins/2004/ms04-011
---

**fullpath**:C:\Windows\System32\winlogon.exe

# description

Winlogon.exe is the Windows logon process, the user-mode component that provides interactive logon support and manages security-related user interactions. It handles logon and logoff, locking and unlocking, password changes and all CTRL+ALT+DELETE (secure attention sequence) events. Related components are the GINA (pre-Vista) and Winlogon notification packages.

## simple description

> ### 2026-11-21 Claude said
> winlogon.exe is the core Windows process that handles signing in, signing out, locking the screen and Ctrl+Alt+Del. One instance runs per session, started by smss.exe, and it launches userinit.exe and the user's shell (explorer.exe) after logon. Killing it crashes or logs off the session.
>
> **SOC NOTE**: Frequent persistence target via HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon values Shell, Userinit and Notify (T1547.004) and via Image File Execution Options debugger on winlogon.exe. Credential dumpers and keyloggers may inject into it; LSASS-adjacent. Expected parent is smss.exe (which exits), path must be System32, and it runs as SYSTEM; anomalies indicate masquerading (T1036.005).
>

# purpose

Winlogon registers CTRL+ALT+DEL as the secure attention sequence at initialization and creates three desktops in the WinSta0 window station: the Winlogon (secure) desktop, the application desktop and the screen saver desktop. It maintains three states: logged-off (prompts for credentials and starts the shell on success), logged-on, and workstation-locked (secure desktop shown until the same user or an administrator authenticates). It also reads domain data during logon to configure the user's environment. For debugging, set `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\WinLogon.EXE\Debugger` to `ntsd -d -x -g` (requires reboot).

# typical use cases

| usage | description |
| --- | --- |
| `Debug-Process "Winlogon"` | Attach the registered debugger to Winlogon (protected process; requires administrator). |

# options

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
