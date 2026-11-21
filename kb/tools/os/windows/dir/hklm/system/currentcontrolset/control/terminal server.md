---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - rdp
  - remote-desktop
aliases:
  - "Terminal Server"
  - "Terminal Server key"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/rdp-error-general-troubleshooting
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/serial-console-cmd-ps-commands
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/client-disconnected-group-policy-updates
  - https://learn.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-terminalservices-localsessionmanager-fdenytsconnections
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server

# description

Registry key holding machine-wide Remote Desktop Services / Terminal Server configuration, including whether RDP connections are allowed (`fDenyTSConnections`). Group Policy equivalents live under `HKLM\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services` and override it.

## simple description

> ### 2026-11-21 Claude said
> This registry key controls the Remote Desktop server on the machine.
> The most important value, fDenyTSConnections, decides whether people can connect with RDP (0 = allowed, 1 = blocked).
> Subkeys such as WinStations\RDP-Tcp hold listener settings like the port number.
>
> **SOC NOTE**: Attackers flip fDenyTSConnections to 0 to enable RDP for lateral movement/persistence (T1021.001, T1112 Modify Registry), change RDP-Tcp PortNumber, or set fSingleSessionPerUser / shadowing values. Monitor registry writes here (Sysmon 13) together with firewall rule changes.
>

# purpose

Stores Remote Desktop configuration for the computer. A Group Policy refresh can temporarily apply the local setting, so set `fDenyTSConnections` to 0 when the policy allows RDP to avoid disconnections.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SYSTEM |

# values

| value name | type | description |
| --- | --- | --- |
| `fDenyTSConnections` | REG_DWORD | 0 = Remote Desktop (RDP) enabled; 1 = RDP disabled / no connections allowed. Can be overridden by Group Policy. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server"` | List the key's values. |
| `get-itemproperty -path 'hklm:\system\curRentcontrolset\control\terminal server' -name 'fdenytsconNections'` | Verify whether RDP is enabled. |
| `set-itemproperty -path 'hklm:\system\curRentcontrolset\control\terminal server' -name 'fdenytsconNections' 0 -type dword` | Enable RDP. |
