---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft\Edge\Application\114.0.1823.43\msedgewebview2.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - edge
  - webview2
aliases:
  - msedgewebview2.exe
  - WebView2 Runtime
url:
  - https://learn.microsoft.com/microsoft-edge/webview2/concepts/distribution
---

**fullpath**:C:\Program Files (x86)\Microsoft\Edge\Application\114.0.1823.43\msedgewebview2.exe

# description

`msedgewebview2.exe` is the Microsoft Edge WebView2 Runtime executable that hosts web content inside native Windows apps. With the Fixed Version distribution mode, apps point `browserExecutableFolder` to the folder that contains `msedgewebview2.exe`; with Evergreen it is updated automatically. This path is a version folder under the Edge application directory.

## simple description

> ### 2026-11-21 Claude said
> WebView2 lets desktop apps (Teams, Outlook, Widgets, etc.) show web pages using the Edge (Chromium) engine. Each app that uses WebView2 spawns several `msedgewebview2.exe` processes (browser, renderer, GPU, utility), so many instances are normal. It runs under the user account of the host app.
>
> **SOC NOTE**: Usually benign, but often seen in process trees of Office/Teams. Abuse cases include malicious apps or injected code using WebView2 for credential phishing/cookie theft and launching with `--remote-debugging-port` to hijack sessions (MITRE ATT&CK T1185, T1539). Check the parent process and unusual command-line flags; a copy running from a non-standard path is suspicious.
>

# purpose

Hosts web content for WebView2-based apps. Fixed Version binaries are packaged with an app and not updated automatically; on Windows 10 from Fixed Version 120, the renderer runs inside an App Container, requiring ACL grants on the runtime folder.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_
