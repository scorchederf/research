---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Mail\wab.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
aliases:
  - wab.exe
  - Windows Address Book
  - WAB
url:
  - https://learn.microsoft.com/windows/win32/api/_wab/
  - https://learn.microsoft.com/windows/win32/api/wabapi/nf-wabapi-iwabobject-import
  - https://learn.microsoft.com/security-updates/securitybulletins/2006/ms06-076
---

**fullpath**:C:\Program Files\Windows Mail\wab.exe

# description

wab.exe is the Windows Address Book (WAB) application, shipped with Windows Mail (formerly Outlook Express). Learn documents the WAB programming technology (headers wabapi.h, wabdefs.h, wabiab.h, wabtags.h; Wab32.dll), most of whose interfaces are marked "Do not use", and `IWABObject::Import` for importing .wab files.

## simple description

> ### 2026-11-21 Claude said
> wab.exe is the legacy Windows Address Book / Contacts program left over from Outlook Express and Windows Mail. On modern Windows it opens the Contacts folder and is seldom used. It loads wab32.dll and related libraries from its directory and the system.
>
> **SOC NOTE**: Known DLL sideloading target: copying wab.exe elsewhere with a malicious `wab32.dll` beside it has been used for execution and defense evasion (MITRE ATT&CK T1574.002 DLL Side-Loading). Flag wab.exe running outside `C:\Program Files\Windows Mail` or making network connections. MS06-076 (CVE-2006-2386) showed crafted .wab files could achieve remote code execution.
>

# purpose

Displays and manages the Windows Address Book; .wab files can be imported into the user's Address Book. A crafted .wab file was the attack vector in MS06-076.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
