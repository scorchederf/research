---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - networking
  - nla
aliases:
  - 'Profiles'
  - 'NetworkList\Profiles'
  - 'Network List Manager profiles'
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/networking/domain-joined-machines-cannot-detect-domain-profile
---

**fullpath**: HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles

# description

Registry key under `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList` that holds the network profiles known to the machine. Information gathered by Network Location Awareness (NLA) is curated by the Network List Service and stored under the NetworkList key; starting with Windows 11 the Network List Manager detects the domain profile. Related keys are `NetworkList\Signatures\Managed` and `NetworkList\Signatures\Unmanaged`, and the current profile can be checked with `Get-NetConnectionProfile`.

## simple description

> ### 2026-11-21 Claude said
> This key keeps a record of every network the computer has connected to, one subkey (named with a GUID) per network. Each profile stores the network name, its category (Public, Private or Domain) and when it was first and last connected. Windows uses this to decide which firewall profile applies. Entries remain after the network is gone, so it is a history of networks the device has joined.
>
> **SOC NOTE**: High forensic value: each profile's ProfileName, DateCreated and DateLastConnected (SYSTEMTIME binary) values show which Wi-Fi/wired networks a host joined and when, useful for tracking a laptop's location or rogue network use. Pair with Signatures\Unmanaged (DefaultGatewayMac) to identify the gateway. Attackers may change Category to Private to loosen firewall rules (T1562.004); changing NLA state is logged in Microsoft-Windows-NetworkProfile/Operational (event 10000/10001).
>

# purpose

Stores per-network profile information and the current category of each network profile, which Windows uses to identify the network and its location type.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SOFTWARE` |

# values

| value name | type | description |
| --- | --- | --- |
| `Category` | REG_DWORD | Under `Profiles\{GUID}`: `0` = not an Active Directory network; `1` = Active Directory network, machine not authenticated; `2` = Active Directory network, machine authenticated. |

# subkeys

| subkey | description |
| --- | --- |
| `{GUID}` | One subkey per network profile (example on Learn: `{985EE69C-23B4-4D38-AC66-5F0D6AD8A128}`), containing information about the profile and its current category. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles"` | List the network profile subkeys. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles" /s` | List all profiles with their values, including Category. |
| `Get-NetConnectionProfile` | Show the currently applied network profile and NetworkCategory (for example DomainAuthenticated). |
