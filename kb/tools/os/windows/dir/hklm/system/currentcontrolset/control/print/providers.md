---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Print\Providers'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - print-spooler
aliases:
  - Providers
  - Print Providers
url:
  - https://learn.microsoft.com/windows-hardware/drivers/print/installing-a-network-print-provider
  - https://learn.microsoft.com/windows-hardware/drivers/print/print-provider-capabilities
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\Print\Providers

# description

This key holds the print spooler's list of installed print providers. Installing a network print provider means copying the provider DLL into System32 and calling `AddPrintProvidor`, which creates a registry entry for the provider and adds it to the end of the spooler's provider list, then loads the DLL and calls `InitializePrintProvidor`. Learn warns that third-party print provider APIs are deprecated starting with Windows 10.

## simple description

> ### 2026-11-21 Claude said
> This registry key tells the Print Spooler which print provider DLLs to load, such as the local and network (LanMan) print providers. Each provider gets a subkey naming its DLL. The spooler service (spoolsv.exe, running as SYSTEM) loads these DLLs at startup.
>
> **SOC NOTE**: Adding a subkey here with a malicious DLL is a known persistence technique that gets code loaded into spoolsv.exe as SYSTEM (MITRE ATT&CK T1547.012 Print Processors / spooler-based persistence). Baseline the expected providers (e.g. Internet Print Provider, LanMan Print Services) and alert on new subkeys or Name/DLL values pointing to unsigned or unusual DLLs.
>

# purpose

Registers print providers with the spooler. Print providers supply print queue management, printer driver management, print job creation and scheduling, forms, print processor, print monitor, port and registry management capabilities through a predefined set of API functions.

# hive

| property | value |
| --- | --- |
| hive | HKLM (HKEY_LOCAL_MACHINE\System) |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\Config\System` (supporting files System, System.alt, System.log, System.sav) |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Print\Providers"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Print\Providers" /s` | List all provider subkeys and their values. |
