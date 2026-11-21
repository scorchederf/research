---
created: 2026-11-21
fullpath: 'c:\windows\system32\ieframe.dll'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - ieframe.dll
  - Ieframe.dll
url:
  - https://learn.microsoft.com/answers/a/12567392
  - https://learn.microsoft.com/security-updates/securitybulletins/2007/ms07-027
---

**fullpath**:c:\windows\system32\ieframe.dll

# description

Ieframe.dll is an Internet Explorer component listed among the files updated by IE cumulative security updates (e.g. MS07-027). On modern Windows it is a system-owned, retired Internet Explorer component protected by TrustedInstaller; VBA references such as Microsoft Internet Controls depend on it, and Microsoft recommends moving to the Edge WebView2 control.

## simple description

> ### 2026-11-21 Claude said
> Ieframe.dll is the Internet Explorer "browser frame" library: it holds IE's window frame, the WebBrowser ActiveX control (Shell.Explorer / "Microsoft Internet Controls"), and many IE resources and dialogs. Even with IE retired, Windows keeps it because older apps and Office macros embed the browser control. It lives in System32 (64-bit) and SysWOW64 (32-bit). It is protected by Windows Resource Protection.
>
> **SOC NOTE**: Ieframe.dll has been involved in many IE vulnerabilities, and its exported `OpenURL` function can be invoked via `rundll32.exe ieframe.dll,OpenURL <file.url>` to proxy execution (MITRE ATT&CK T1218.011). Watch for rundll32 loading ieframe.dll with .url arguments, and macros/scripts creating InternetExplorer.Application or WebBrowser objects. A non-Microsoft-signed or modified ieframe.dll is suspicious.
>

# purpose

Provides Internet Explorer frame and browser-control functionality used by IE and by applications (e.g. Office VBA via Microsoft Internet Controls) that embed the legacy IE engine.
