---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - network-provider
aliases:
  - "NetworkProvider\\Order"
  - "ProviderOrder"
url:
  - https://learn.microsoft.com/windows/win32/secauthn/authentication-registry-keys
  - https://learn.microsoft.com/windows-hardware/drivers/ifs/support-for-unc-naming-and-mup
  - https://learn.microsoft.com/windows-hardware/drivers/ifs/mup-changes-in-microsoft-windows-vista
  - https://learn.microsoft.com/troubleshoot/windows-client/setup-upgrade-and-drivers/network-provider-settings-removed-in-place-upgrade
---

**fullpath**: HKLM\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order

# description

Registry key whose `ProviderOrder` value lists the installed network providers and the order in which the Multiple Provider Router (MPR) and the Multiple UNC Provider (MUP) try them. Each name in the list maps to a service key under `HKLM\SYSTEM\CurrentControlSet\Services\<ProviderName>\NetworkProvider`. The list can also be viewed in `ncpa.cpl` > Advanced > Advanced Settings.

## simple description

> ### 2026-11-21 Claude said
> Windows can talk to network resources through several "network providers" such as the SMB client, Remote Desktop and WebDAV. This key holds the ordered list of those providers. When you open a UNC path like \\server\share, Windows asks each provider in this order until one claims it. Each provider is a DLL registered under its own service key.
>
> **SOC NOTE**: Adding a malicious provider to ProviderOrder (with a NetworkProvider\ProviderPath DLL) is a known credential-theft technique ("NPPSpy"): mpnotify passes cleartext logon passwords to every network provider's NPLogonNotify. Maps to T1556.008 (Modify Authentication Process: Network Provider DLL). Alert on changes to this value and on unexpected entries beyond RDPNP, LanmanWorkstation, webclient (plus known vendors such as VMware/Citrix).
>

# purpose

Lists the installed network providers and specifies the order in which they are tried during operations that cycle through providers until an accepting provider is found. MUP issues UNC prefix resolution requests serially in this order and stops at the first provider that claims the prefix; MPR honours the same order. Third-party provider entries can be removed during an in-place upgrade to Windows 10.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `ProviderOrder` | REG_SZ | Comma-separated list (no white space) of provider key names, e.g. `RDPNP,LanmanWorkstation,webclient` (default). Each name is the provider's key under `HKLM\SYSTEM\CurrentControlSet\Services`. Changes require a reboot to take effect in MUP. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\NetworkProvider\HwOrder" /v ProviderOrder` | Show the related HwOrder provider list. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\NetworkProvider"` | Show the settings of one provider named in the list. |
