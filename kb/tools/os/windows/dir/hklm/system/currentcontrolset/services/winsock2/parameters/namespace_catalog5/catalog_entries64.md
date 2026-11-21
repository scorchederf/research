---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters\NameSpace_Catalog5\Catalog_Entries64'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Catalog_Entries64
  - Winsock namespace provider catalog
url:
  - https://learn.microsoft.com/windows/win32/api/sporder/nf-sporder-wscwritenamespaceorder32
  - https://learn.microsoft.com/windows/win32/winsock/name-space-provider-configuration-and-installation-2
  - https://learn.microsoft.com/windows-hardware/drivers/network/winsock-sections-in-a-network-inf-file
  - https://learn.microsoft.com/windows-server/administration/windows-commands/netsh-winsock
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters\NameSpace_Catalog5\Catalog_Entries64

# description

`Catalog_Entries64` holds the 64-bit Winsock 2 namespace provider (NSP) catalog under `NameSpace_Catalog5`, the registry location of the current namespace provider catalog. Entries are written by `WSCInstallNameSpace`/`WSCInstallNameSpaceEx` (and the `...32` variants for the 32-bit catalog) and read by Ws2_32.dll to route name resolution queries; `netsh winsock show catalog` displays them.

## simple description

> ### 2026-11-21 Claude said
> This key lists the 64-bit Winsock namespace providers: DLLs that Windows networking calls to resolve names (for example DNS, NLA, PNRP, or the hosts file). Each numbered subkey describes one provider, including the path to its DLL and the namespace it handles. Programs that do name lookups through Winsock load these DLLs. A matching `Catalog_Entries` key holds the 32-bit catalog.
>
> **SOC NOTE**: Registering a malicious namespace provider DLL here makes it load into every process that performs Winsock name resolution, giving persistence and DNS interception (MITRE ATT&CK T1547 / T1556-style hooking; similar to LSP abuse). Check each entry's `LibraryPath` for non-Microsoft or user-writable paths and compare against `netsh winsock show catalog`; note `netsh winsock reset` does not remove NSP entries.
>

# purpose

Stores the current namespace provider catalog. The order of providers in the catalog governs the order in which they are enumerated and considered when a client requests name resolution; it can be changed with `WSCWriteNameSpaceOrder` (native) or `WSCWriteNameSpaceOrder32` (32-bit catalog). Providers can be toggled active/inactive with `WSCEnableNSProvider`.

# hive

| property | value |
| --- | --- |
| hive | HKEY_LOCAL_MACHINE (SYSTEM) |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

| value name | type | description |
| --- | --- | --- |
| `ProviderId` | REG_SZ | GUID identifying the namespace provider (per-entry, as defined for Winsock INF sections). |
| `LibraryPath` | REG_EXPAND_SZ | Complete path to the namespace provider DLL. |
| `DisplayString` | string | Localizable name displayed for the namespace provider. |
| `SupportedNameSpace` | REG_DWORD | Namespace supported (e.g. `12` NS_DNS, `13` NS_NETBT, `14` NS_WINS). |
| `Version` | REG_DWORD | Optional provider version number; default 1. |

# subkeys

| subkey | description |
| --- | --- |
| `000000000001`, `000000000002`, ... | One numbered subkey per installed namespace provider (values as above). |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters\NameSpace_Catalog5\Catalog_Entries64" /s` | List all namespace provider entries and their values. |
| `netsh winsock show catalog` | Display the Winsock catalog, including namespace providers (64-bit first, then 32-bit). |
| `netsh winsock audit trail` | Display the audit trail of installed and uninstalled LSPs. |
