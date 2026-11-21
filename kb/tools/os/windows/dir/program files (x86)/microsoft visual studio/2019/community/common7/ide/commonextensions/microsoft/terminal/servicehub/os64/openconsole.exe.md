---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - console
  - visual-studio
aliases:
  - 'OpenConsole.exe'
  - 'Windows Console Host (open source)'
  - 'conhost.exe'
url:
  - https://learn.microsoft.com/windows/console/ecosystem-roadmap
  - https://learn.microsoft.com/windows/console/definitions
---

**fullpath**:C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe

# description

`OpenConsole.exe` is the open-source build of the Windows Console Host (`conhost.exe`) from the microsoft/terminal repository. This copy ships with Visual Studio 2019's integrated Terminal (ServiceHub) to provide an up-to-date pseudoconsole implementation.

## simple description

> ### 2026-11-21 Claude said
> OpenConsole is Microsoft's open-source version of conhost.exe, the program that sits between command-line apps (cmd, PowerShell) and the window that displays them. Visual Studio bundles its own copy so its built-in terminal pane can host shells via a pseudoconsole (ConPTY). It is normally started by Visual Studio's ServiceHub, not by users.
>
> **SOC NOTE**: Legitimate when parented by Visual Studio/ServiceHub processes; it will commonly spawn cmd.exe/powershell.exe for the developer terminal, so expect shell children. Suspicious if found outside Visual Studio or Windows Terminal install paths, unsigned, or launched by unrelated parents (masquerading, T1036.005). Treat shells under it like any developer-launched shell when hunting.
>

# purpose

Per Learn, the Windows Console Host is the server for all Windows Console APIs and the classic UI for command-line applications; it is found in the system directory as `conhost.exe`, or as `openconsole.exe` in its open-source form, and can be found in other Microsoft products built from the open-source repository for a more up-to-date implementation of the pseudoconsole infrastructure. It operates in a combined server-and-terminal role or a server-only role through the pseudoconsole.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
