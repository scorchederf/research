---
created: 2026-11-21
fullpath: 'C:\Windows\System32\userinit.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - logon
aliases:
  - userinit.exe
  - Userinit
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/user-profiles-and-logon/cannot-log-on-windows
---

**fullpath**:C:\Windows\System32\userinit.exe

# description

`userinit.exe` is the user shell program that the Winlogon service loads from the registry during logon, alongside the default shell `explorer.exe`. Winlogon reads its path from the `Userinit` value under `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon`, whose correct value is `C:\windows\system32\userinit.exe`. It is part of Windows.

## simple description

> ### 2026-11-21 Claude said
> userinit.exe is a small Windows program that Winlogon starts right after a user signs in. It sets up the user's session, runs logon scripts and Group Policy user settings, and then launches the desktop shell (normally explorer.exe) before exiting. Seeing it briefly at each logon is normal. If it is missing or the registry points elsewhere, users get logged off immediately.
>
> **SOC NOTE**: The Winlogon `Userinit` value is a classic persistence spot (MITRE ATT&CK T1547.004): attackers append a comma and their own binary so it runs at every logon. Also check `UserInitMprLogonScript` under `HKCU\Environment` (T1037.001). userinit.exe should run from System32, have winlogon.exe as parent, and spawn explorer.exe; any other location, parent or children like powershell.exe deserve investigation.
>

# purpose

When a user logs on, the Winlogon service loads the Windows default shell (explorer.exe) and the user shell (userinit.exe) from the registry path `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon`. If the `Userinit` value is wrong or the file has been deleted (for example by spyware), Windows logs on and logs off immediately in both normal and Safe Mode. The fix is to set `Userinit = C:\windows\system32\userinit.exe` (and `Shell = explorer.exe`) through remote registry and restart; if that doesn't help, the machine should be considered compromised.

# typical use cases

| usage | description |
| --- | --- |
| `reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit` | Check which user shell program Winlogon starts at logon. |

# options

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
