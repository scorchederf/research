---
created: 2026-11-21
fullpath: 'c:\windows\system32\conhost.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - console
aliases:
  - "conhost.exe"
  - "Console Window Host"
  - "Windows Console Host"
  - "OpenConsole.exe"
url:
  - https://learn.microsoft.com/windows/console/definitions
  - https://learn.microsoft.com/windows/terminal/faq
  - https://learn.microsoft.com/windows/console/ecosystem-roadmap
  - https://learn.microsoft.com/windows-server/administration/windows-console-changes
---

**fullpath**:c:\windows\system32\conhost.exe

# description

`conhost.exe` is the Windows Console Host: the server for all Windows Console APIs and the classic UI for command-line applications. It was split out of `csrss.exe` for security and isolation, and its open-source form is `OpenConsole.exe` in the microsoft/terminal repository.

## simple description

> ### 2026-11-21 Claude said
> conhost.exe draws the console window and handles input/output for command-line programs like cmd.exe and PowerShell.
> A copy starts for almost every console program, so seeing many instances is normal.
> When Windows Terminal is used, conhost still runs in the background as the API server via the pseudoconsole.
>
> **SOC NOTE**: Normally a child of a console process (cmd, powershell, services). Suspicious: conhost from a non-System32 path, unusual parents, or `conhost.exe --headless <cmd>` used to hide windows / proxy execution (T1218, T1564.003 Hidden Window).
>

# purpose

Services console API calls and translation for attached command-line applications and, traditionally, renders their GUI window. With the pseudoconsole (ConPTY) terminals such as Windows Terminal take over the UI while conhost remains responsible for API servicing. New console features can be controlled with DWORD values under `HKEY_CURRENT_USER\Console` (e.g. ForceV2).

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
