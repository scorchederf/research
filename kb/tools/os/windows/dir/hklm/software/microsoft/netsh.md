---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\NetSh'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - netsh
  - networking
aliases:
  - NetSh
  - Netsh helper registration
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/netsh-add
  - https://learn.microsoft.com/windows-server/administration/windows-commands/netsh-show
  - https://learn.microsoft.com/windows-server/administration/windows-commands/netsh-delete
  - https://learn.microsoft.com/windows/win32/api/netsh/nc-netsh-ns_dll_init_fn
---

**fullpath**:HKLM\SOFTWARE\Microsoft\NetSh

# description

Registry location associated with NetShell (`netsh.exe`) helper DLLs. Learn documents that `netsh add helper` installs helper DLLs, `netsh delete helper` removes them and `netsh show helper` lists the top-level helpers; each helper must export `InitHelperDll`, which NetShell calls when loading the helper.

## simple description

> ### 2026-11-21 Claude said
> This key lists the helper DLLs that netsh.exe loads every time it starts. Each value name is a helper and its data is the DLL path. Windows registers its own helpers here (for example for firewall, interface and WLAN contexts). Adding a value makes netsh load an extra DLL.
>
> **SOC NOTE**: Classic persistence/execution point: MITRE ATT&CK T1546.007 (Event Triggered Execution: Netsh Helper DLL). An attacker runs `netsh add helper evil.dll` or writes a value directly; the DLL runs inside netsh.exe whenever netsh is invoked (including by admin scripts and VPN tools). Hunt for values pointing outside System32, unsigned DLLs, and registry set events (Sysmon 13) on this key.
>

# purpose

Holds the registration of NetShell helper DLLs that provide netsh contexts. Helpers are added with `netsh add helper`, removed with `netsh delete helper`; on load NetShell calls the helper's exported `InitHelperDll`, which typically calls `RegisterHelper`.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\NetSh"` | List the key's values. |
| `netsh show helper` | List all top-level helper DLLs available. |
| `netsh add helper C:\dlls\HelperDLL.dll` | Install a helper DLL. |
| `netsh delete helper C:\dlls\HelperDLL.dll` | Remove a helper DLL. |
