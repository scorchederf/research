---
created: 2026-11-21
fullpath: 'c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\Extensions\Microsoft\LiveShare\Agent\vsls-agent.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visual-studio
aliases:
  - "vsls-agent.exe"
  - "Live Share agent"
url:
  - https://learn.microsoft.com/visualstudio/liveshare/reference/connectivity
  - https://learn.microsoft.com/visualstudio/liveshare/use/share-project-join-session-visual-studio
  - https://learn.microsoft.com/visualstudio/liveshare/faq
---

**fullpath**:c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\Extensions\Microsoft\LiveShare\Agent\vsls-agent.exe

# description

vsls-agent.exe is the Visual Studio Live Share agent for Visual Studio. It lives under the IDE\Extensions subfolder of the Visual Studio install location and may move with each Live Share update. Live Share is deprecated in Visual Studio and in maintenance mode in VS Code.

## simple description

> ### 2026-11-21 Claude said
> vsls-agent.exe is the background agent behind Visual Studio Live Share, which lets developers share code, terminals and debugging sessions with others in real time. It talks to Microsoft cloud relays and can also accept direct local connections. Windows Firewall may prompt to allow it the first time a session is shared.
>
> **SOC NOTE**: Live Share gives remote guests access to source code and potentially shared terminals/servers, so it can be abused for remote access or data exfiltration via trusted Microsoft endpoints (MITRE ATT&CK T1219 / T1567). Watch for vsls-agent listening on ports 5990-5999 or connecting to `*.liveshare.vsengsaas.visualstudio.com` / `*.servicebus.windows.net` on hosts where Live Share is not expected.
>

# purpose

Hosts Live Share collaboration sessions. In direct mode the host opens a port in the range 5990-5999 to accept inbound local-network connections; all modes need outbound access to `*.liveshare.vsengsaas.visualstudio.com:443`, relay mode needs `*.servicebus.windows.net:443`, and `*.online.visualstudio.com` is also required.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
