---
created: 2026-11-21
fullpath: 'c:\windows\system32\mshtml.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - dll
  - internet-explorer
  - browser
aliases:
  - mshtml.dll
  - MSHTML
  - Trident
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/1999/ms99-012
  - https://learn.microsoft.com/windows/win32/dataxchg/html-clipboard-format
---

**fullpath**:c:\windows\system32\mshtml.dll

# description

`MSHTML.DLL` is the HTML parsing engine of Internet Explorer; MSHTML (also known as Trident) was Internet Explorer's engine, and MSHTML-based applications use it for HTML rendering and editing, including HTML cut and paste via the clipboard. It has been serviced through many Internet Explorer security bulletins.

## simple description

> ### 2026-11-21 Claude said
> mshtml.dll is the old Internet Explorer rendering engine (Trident). Even with IE retired, it stays in Windows because many apps, Office, help files (.chm), HTA files and the IE mode in Edge still use it to display HTML. It is a core, Microsoft-signed system DLL.
>
> **SOC NOTE**: Frequent exploitation target (e.g. CVE-2021-40444 via Office documents, MITRE T1203). mshtml.dll is also abused as a LOLBin entry point: `rundll32.exe javascript:"\..\mshtml,RunHTMLApplication"` (T1218.011) and mshta.exe (T1218.005). Look for rundll32/mshta command lines referencing mshtml and Office processes loading it followed by suspicious child processes.
>

# purpose

Parses and renders HTML for Internet Explorer and other MSHTML-based applications, and handles HTML clipboard cut and paste in the IE4/MSHTML HTML editor.
