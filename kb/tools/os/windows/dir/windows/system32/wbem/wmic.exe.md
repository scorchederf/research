---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbem\wmic.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - wmi
  - lolbin
  - deprecated
aliases:
  - "wmic.exe"
  - "WMIC"
  - "WMI command-line utility"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/wmic
  - https://learn.microsoft.com/windows/win32/wmisdk/wmic
  - https://learn.microsoft.com/windows/whats-new/deprecated-features
  - https://learn.microsoft.com/windows/whats-new/removed-features
  - https://learn.microsoft.com/windows-server/get-started/removed-deprecated-features-windows-server
---

**fullpath**:C:\Windows\System32\wbem\wmic.exe

# description

`wmic.exe` is the WMI command-line utility, providing a command-line interface for Windows Management Instrumentation. It is deprecated since Windows 10 21H1, removed from Windows 11 24H2+ (no longer available as a Feature on Demand from August 2026), and a Feature on Demand in Windows Server 2025; PowerShell CIM cmdlets replace it. WMI itself is not affected.

## simple description

> ### 2026-11-21 Claude said
> wmic.exe lets you query and manage Windows through WMI from a command prompt, e.g. list processes, disks or installed software, locally or on remote PCs.
> It is old and deprecated, and newer Windows 11 builds no longer include it.
> PowerShell (Get-CimInstance) is the replacement.
>
> **SOC NOTE**: Heavily abused (T1047 Windows Management Instrumentation): remote execution `wmic /node:x process call create`, recon, shadow-copy deletion `wmic shadowcopy delete` (T1490), and XSL script execution `wmic ... /format:evil.xsl` (T1220). Its presence on a 24H2+ host may itself indicate an attacker-supplied copy.
>

# purpose

Displays WMI information inside an interactive command shell or runs one-off WMI queries. On Windows Server 2025 it can be added with `DISM /Add-Capability`; Windows Server 2028 removes it.

# typical use cases

| usage | description |
| --- | --- |
| `wmic logicaldisk` | Displays properties of all logical disks on the computer. |
| `wmic context` | Displays the current values of all global switches. |

# options

| option | description |
| --- | --- |
| `logicaldisk` | Displays properties of all the logical disks on this computer. |
| `class` | Escapes from the default alias mode to access classes in the WMI schema directly. |
| `path` | Escapes from the default alias mode to access instances in the WMI schema directly. |
| `context` | Displays the current values of all global switches. |
| `quit` \| `exit` | Exits the WMIC command shell. |
