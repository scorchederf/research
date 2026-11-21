---
created: 2026-11-21
fullpath: 'c:\windows\system32\ie4uinit.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - ie4uinit.exe
  - IE per-user initialization utility
url:
  - https://learn.microsoft.com/answers/a/8192702
  - https://learn.microsoft.com/answers/a/8101559
  - https://learn.microsoft.com/security-updates/securitybulletins/2007/ms07-027
---

**fullpath**:c:\windows\system32\ie4uinit.exe

# description

ie4uinit.exe is a legitimate Internet Explorer executable located in `C:\Windows\System32` (with copies in WinSxS under the `microsoft-windows-ie-setup-support` component). It is serviced through Internet Explorer security updates (for example MS07-027 lists Ie4uinit.exe among updated files).

## simple description

> ### 2026-11-21 Claude said
> Ie4uinit.exe is the "IE per-user initialization utility", a Windows component left over from Internet Explorer setup that runs per-user setup tasks such as refreshing shell icons and IE settings at logon or after updates. A common admin use is `ie4uinit.exe -show` (or `-ClearIconCache`) to rebuild the icon cache. It is Microsoft-signed and normally runs briefly with no visible window.
>
> **SOC NOTE**: ie4uinit.exe is a LOLBin: it reads `ieuinit.inf` from its current directory, so copying it with a malicious `ieuinit.inf` to a writable folder and running `ie4uinit.exe -BaseSettings` executes commands from the INF (MITRE ATT&CK T1218 System Binary Proxy Execution). Alert on ie4uinit.exe running outside System32/WinSxS or with an `ieuinit.inf` in an unusual directory, and on child processes it spawns.
>

# purpose

Legitimate Internet Explorer component. Learn (Q&A) confirms it may access user-profile folders after cumulative updates, which can trigger Controlled Folder Access notifications.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
