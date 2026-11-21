---
created: 2026-11-21
fullpath: 'C:\Windows\System32\osk.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - accessibility
aliases:
  - osk.exe
  - On-Screen Keyboard
  - OSK
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/2014/ms14-039
  - https://learn.microsoft.com/globalization/input/keyboards
---

**fullpath**:C:\Windows\System32\osk.exe

# description

On-Screen Keyboard (OSK) is an Ease of Access tool in Microsoft Windows that lets users move around their PC and enter text without a physical keyboard. It displays a visual keyboard with all standard keys, usable with a touch screen, mouse, or other pointing device. It's related to the touch keyboard (TabTip.exe).

## simple description

> ### 2026-11-21 Claude said
> osk.exe is the Windows On-Screen Keyboard, an accessibility program that shows a clickable keyboard on screen. It's built into Windows and can be opened from the logon screen's Ease of Access menu or with Windows+Ctrl+O. People use it when they lack a working keyboard or need accessibility support.
>
> **SOC NOTE**: Because osk.exe can be launched from the logon screen as SYSTEM, attackers replace it or set an Image File Execution Options "Debugger" value to get a pre-logon SYSTEM shell (accessibility features backdoor, MITRE ATT&CK T1546.008). Check osk.exe hash/signature, IFEO registry keys for osk.exe, and cmd.exe spawned by winlogon/utilman. CVE-2014-2781 (MS14-039) was an OSK elevation of privilege.
>

# purpose

Provides a visual keyboard for text entry and navigation without a physical keyboard. Can improve accessibility, for example with text prediction, Hover over keys, and Scan through keys modes. Toggle with Windows logo key + Ctrl + O.

# typical use cases

| usage | description |
| --- | --- |
| — | Enter text on devices without a hardware keyboard or for users with accessibility needs. |
| — | Learn which language-specific characters map to which keys (e.g. Korean IME layout). |
| — | Security note from Learn: MS14-039 (CVE-2014-2781) fixed a local elevation of privilege when OSK was executed from a low-integrity process. |

# options

| option    | description    |
| --- | --- |
| _Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_ |  |
