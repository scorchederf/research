---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft\Copilot\Application\mscopilot.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - copilot
aliases:
  - "mscopilot.exe"
  - "Microsoft Copilot app"
url:
  - https://learn.microsoft.com/copilot/plan/copilot-app-overview
  - https://learn.microsoft.com/copilot/implement/faq-deploy-microsoft-365-copilot-app
---

**fullpath**:C:\Program Files (x86)\Microsoft\Copilot\Application\mscopilot.exe

# description

`mscopilot.exe` is the executable of the Microsoft Copilot desktop app for Windows. Learn describes the Microsoft Copilot client app (web, desktop and mobile), supporting both personal Microsoft accounts and work/school Entra ID accounts; the specific executable name is not documented.

## simple description

> ### 2026-11-21 Claude said
> mscopilot.exe is Microsoft's Copilot AI assistant desktop app.
> It is a browser-based (Edge WebView) app installed under Program Files (x86)\Microsoft\Copilot, similar to how Edge is installed.
> Users sign in with a personal or work account to chat with Copilot.
>
> **SOC NOTE**: Mostly benign; relevant for data-loss reviews (users pasting sensitive data into AI tools) and for checking unexpected installs. Network traffic goes to *.cloud.microsoft / copilot endpoints.
>

# purpose

Provides the Microsoft Copilot experience on the Windows desktop. Visual indicators show which account is in use; data from the personal experience does not flow into the work/school experience and vice versa. Admins can restrict personal-account sign-in with tenant restrictions.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
