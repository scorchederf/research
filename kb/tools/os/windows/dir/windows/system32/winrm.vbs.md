---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winrm.vbs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - vbscript
  - winrm
  - remote-management
aliases:
  - 'winrm.vbs'
  - 'Winrm.cmd'
  - 'winrm'
url:
  - https://learn.microsoft.com/windows/win32/winrm/about-windows-remote-management
  - https://learn.microsoft.com/windows/win32/winrm/scripting-in-windows-remote-management
  - https://learn.microsoft.com/windows/win32/winrm/installation-and-configuration-for-windows-remote-management
---

**fullpath**:C:\Windows\System32\winrm.vbs

# description

`winrm.vbs` is the VBScript implementation of the `winrm` command-line tool (invoked via `Winrm.cmd`) for Windows Remote Management. It is written using the WinRM Scripting API and ships with the operating system alongside `Winrs.exe` and the WinRM service; its output formatting uses the `WsmTxt.xsl` transform.

## simple description

> ### 2026-11-21 Claude said
> When you type `winrm` at a command prompt, Windows actually runs winrm.cmd, which calls this VBScript through cscript. It is the admin tool for configuring the WinRM (WS-Management) service, creating listeners, and querying or invoking WMI classes on local or remote machines. It talks over HTTP 5985 / HTTPS 5986.
>
> **SOC NOTE**: Used for remote execution and lateral movement via WinRM (T1021.006) and WMI queries/method calls (T1047), e.g. `winrm invoke Create wmicimv2/Win32_Process`. Also known for a proxy-execution trick where a copied winrm.vbs loads a malicious WsmPty.xsl/WsmTxt.xsl from its directory (T1216 / T1220). Watch for cscript.exe running winrm.vbs from a non-System32 path, `winrm quickconfig`/listener creation, and WinRM operational log events (Microsoft-Windows-WinRM/Operational).
>

# purpose

Learn describes Winrm.cmd as a command-line tool for system management implemented in a VBScript file (Winrm.vbs) written using the WinRM Scripting API; it enables an administrator to configure WinRM and to get data or manage resources (help via `winrm /?`). Winrm.vbs also serves as an example of how to use the WinRM Scripting API. Typical commands include `winrm quickconfig` (start the service, create a listener, add firewall exceptions), `winrm enumerate winrm/config/listener`, `winrm get winrm/config`, and `winrm quickconfig -transport:https`. The tool outputs ANSI text.

