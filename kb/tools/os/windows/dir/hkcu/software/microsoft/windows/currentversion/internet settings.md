---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - proxy
  - wininet
aliases:
  - Internet Settings
  - WinINet proxy settings
url:
  - https://learn.microsoft.com/windows/win32/wininet/enabling-internet-functionality
  - https://learn.microsoft.com/troubleshoot/windows-client/networking/directaccess-clients-unable-connect-error-0x80092013
  - https://learn.microsoft.com/windows/win32/winhttp/setting-wininet-proxy-configurations-in-winhttp
  - https://learn.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-ie-clientnetworkprotocolimplementation-hklmproxyenable
---

**fullpath**:HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings

# description

Per-user registry key holding WinINet / Internet Options settings, notably the proxy configuration. Applications calling `InternetOpen` with INTERNET_OPEN_TYPE_PRECONFIG read `ProxyEnable`, `ProxyServer` and `ProxyOverride` from this key.

## simple description

> ### 2026-11-21 Claude said
> This key stores a user's Internet Options settings, the same ones you see in the Connections > LAN settings dialog: whether a proxy is used, which proxy server, the bypass list and an automatic configuration (PAC) script URL. Browsers and many applications that use WinINet read it. Each user has their own copy in their NTUSER.DAT.
>
> **SOC NOTE**: Attackers set ProxyServer/ProxyEnable or AutoConfigURL to route traffic through their proxy for interception or C2 (T1090, T1557), or change ZoneMap/zone settings to weaken security (T1112). Review ProxyServer, AutoConfigURL and ZoneMap during investigations; changes appear in NTUSER.DAT with key last-write times.
>

# purpose

Stores the current user's Internet (WinINet) configuration. `INTERNET_OPEN_TYPE_PRECONFIG` retrieves the proxy configuration from here. If `ProxyEnable` is 1, connections are made only through the proxy in `ProxyServer` or `AutoConfigURL`. Machine-wide proxy settings apply instead when the "Make proxy settings per-machine (rather than per-user)" policy is enabled (`ProxySettingsPerUser`). Services must load the user profile for WinHTTP to read these settings.

# hive

| property | value |
| --- | --- |
| hive | HKCU |
| scope | per-user |
| backing file | `Ntuser.dat` |

# values

| value name | type | description |
| --- | --- | --- |
| `ProxyEnable` | REG_DWORD | 1 means use the proxy defined in ProxyServer or AutoConfigURL. |
| `ProxyServer` | REG_SZ | Host name or IP address of the proxy server. |
| `ProxyOverride` | REG_SZ | Semicolon-separated hosts/addresses that bypass the proxy; `<local>` bypasses intranet addresses. |
| `AutoConfigURL` | REG_SZ | URL of the automatic proxy configuration script. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings"` | List the key's values. |
| `reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer` | Show the configured proxy server. |
