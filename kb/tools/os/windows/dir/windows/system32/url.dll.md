---
created: 2026-11-21
fullpath: 'c:\windows\system32\url.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - dll
  - lolbin
aliases:
  - url.dll
  - Internet Shortcut Shell Extension DLL
url:
  - https://learn.microsoft.com/windows/win32/api/intshcut/nf-intshcut-urlassociationdialogw
  - https://learn.microsoft.com/security-updates/securitybulletins/2004/ms04-043
---

**fullpath**:c:\windows\system32\url.dll

# description

url.dll is the Internet Shortcut shell extension library that implements URL/shortcut handling functions such as `URLAssociationDialog` (header intshcut.h). It ships with Windows; protocol handlers like telnet are registered as `rundll32.exe url.dll,TelnetProtocolHandler %l`. Related: rundll32.exe, ieframe.dll, shdocvw.dll.

## simple description

> ### 2026-11-21 Claude said
> url.dll is a Windows library that knows how to open URLs and internet shortcut (.url) files with the right program. Windows calls it through rundll32 for some protocol handlers. Users never run it directly. It is present on every Windows install.
>
> **SOC NOTE**: LOLBAS: `rundll32.exe url.dll,OpenURL <file.hta/.url>` and `url.dll,FileProtocolHandler <exe>` launch programs or files via a signed DLL (T1218.011 System Binary Proxy Execution: Rundll32), breaking parent-child lineage. Hunt for rundll32 command lines containing `url.dll` with FileProtocolHandler/OpenURL pointing to executables, HTA or script files.
>

# purpose

Provides internet shortcut and URL protocol handler functions, including the URL association dialog and the default `TelnetProtocolHandler` used for telnet: URLs.


