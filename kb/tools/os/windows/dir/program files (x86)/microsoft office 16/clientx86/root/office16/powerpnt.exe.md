---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Powerpnt.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - office
aliases:
  - Powerpnt.exe
  - PowerPoint
  - Microsoft PowerPoint
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/2006/ms06-058
  - https://learn.microsoft.com/security-updates/securitybulletins/2006/ms06-028
---

**fullpath**:C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Powerpnt.exe

# description

Powerpnt.exe is the Microsoft PowerPoint executable, listed in Microsoft security bulletins as the file replaced by PowerPoint security updates (for example MS06-028 for PowerPoint 2003 and MS06-058 for PowerPoint 2000). This path is the Click-to-Run location for 32-bit Office 16 on 64-bit Windows.

## simple description

> ### 2026-11-21 Claude said
> Powerpnt.exe is Microsoft PowerPoint, the presentation application in Microsoft Office / Microsoft 365. This path is a 32-bit Click-to-Run install (ClientX86\Root) of Office 16. It opens .ppt, .pptx, .pps/.ppsx and related files. It is a normal user application.
>
> **SOC NOTE**: Malicious presentations are a phishing vector (T1566.001): macros (.pptm/.ppsm), embedded OLE objects, action/mouse-over links that run programs, and exploits of parsing bugs. Alert on powerpnt.exe spawning cmd.exe, powershell.exe, mshta.exe, wscript.exe or rundll32.exe, or writing executables (T1204.002). Check Office trust records, MRU lists and the Office alerts log for opened documents.
>

# purpose

Creating, editing and presenting slide shows; it is also the binary that PowerPoint security updates patch.

# typical use cases

| usage | description |
| --- | --- |
| — | Open and edit presentations. |
| — | Run slide shows. |

# options

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_
