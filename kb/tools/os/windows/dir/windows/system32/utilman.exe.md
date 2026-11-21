---
created: 2026-11-21
fullpath: 'C:\Windows\System32\utilman.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - accessibility
aliases:
  - utilman.exe
  - Utility Manager
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/2004/ms04-019
  - https://learn.microsoft.com/security-updates/securitybulletins/2004/ms04-011
  - https://learn.microsoft.com/security-updates/securitybulletins/2003/ms03-025
  - https://learn.microsoft.com/answers/a/12823470
---

**fullpath**:C:\Windows\System32\utilman.exe

# description

Utilman.exe is the process name of Utility Manager, an accessibility utility that lets users check the status of accessibility programs such as Magnifier, Narrator and On-Screen Keyboard and start or stop them. Microsoft security bulletins MS03-025, MS04-011 and MS04-019 addressed Windows 2000 privilege elevation vulnerabilities in how Utility Manager launched applications with system privileges.

## simple description

> ### 2026-11-21 Claude said
> utilman.exe is the Ease of Access (Accessibility) launcher in Windows. It is started when someone clicks the accessibility button on the logon or lock screen or presses Windows+U, and it opens tools like Narrator, Magnifier and the On-Screen Keyboard. Because it can be launched from the logon screen before anyone signs in, it runs as SYSTEM in that context.
>
> **SOC NOTE**: Classic "accessibility features" backdoor (MITRE T1546.008): attackers replace utilman.exe with cmd.exe (or set an Image File Execution Options Debugger for utilman.exe) to get a SYSTEM shell from the logon screen, often via RDP without credentials. Check the file hash/signature and size against cmd.exe, look for `HKLM\...\Image File Execution Options\utilman.exe` Debugger values, and for utilman.exe spawning cmd.exe/powershell.exe from winlogon.exe.
>

# purpose

Provides access to the operating system's accessibility features. Microsoft's historical workaround for the Utility Manager vulnerabilities was to disable Utility Manager via Group Policy or software restriction policies, which makes those accessibility features unavailable until restrictions are removed. Learn Q&A notes that replacing utilman.exe with cmd.exe breaks the file and System File Checker can restore it.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
