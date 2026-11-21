---
created: 2026-11-21
fullpath: 'C:\Windows\System32\dsregcmd.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - entra
  - device-registration
aliases:
  - dsregcmd.exe
  - dsregcmd
url:
  - https://learn.microsoft.com/entra/identity/devices/troubleshoot-device-dsregcmd
  - https://learn.microsoft.com/troubleshoot/entra/entra-id/dir-dmns-obj/no-local-admin-privileges-azure-ad-joined-device
  - https://learn.microsoft.com/entra/identity/devices/troubleshoot-hybrid-join-windows-current
---

**fullpath**:C:\Windows\System32\dsregcmd.exe

# description

dsregcmd is the Windows device registration command. Its `/status` output shows the Microsoft Entra join state of the device, device and tenant details, user state, SSO (PRT) state and diagnostic data, and is the main tool for troubleshooting Microsoft Entra joined, hybrid joined and registered devices.

## simple description

> ### 2026-11-21 Claude said
> dsregcmd.exe is built into Windows 10/11 and reports how a device is joined to Microsoft Entra ID (Azure AD) and on-prem AD. `dsregcmd /status` shows join state, device ID, tenant, whether the user has a Primary Refresh Token (PRT), Windows Hello status and diagnostic errors. Other switches can leave or rejoin, or refresh the PRT.
>
> **SOC NOTE**: Useful to responders for device ID, tenant and PRT timestamps when investigating token theft (T1528/T1550.001 PRT abuse). Attackers run `dsregcmd /status` for discovery of cloud join state and tenant info (T1082/T1087.004); `/leave` can break device trust. Related events are in the AAD and User Device Registration logs (e.g. 304, 305, 307, 1006, 1007).
>

# purpose

Troubleshoot device state in Microsoft Entra ID. Run `/status` as a domain user to get user/SSO state; from an elevated prompt the pre-join diagnostics run in SYSTEM context. Device states: AzureAdJoined+DomainJoined = Microsoft Entra hybrid joined; AzureAdJoined only = Microsoft Entra joined; DomainJoined only = Domain joined; EnterpriseJoined+DomainJoined = On-premises DRS joined.

# typical use cases

| usage | description |
| --- | --- |
| `dsregcmd /status` | Show device join, tenant, user, SSO/PRT and diagnostic status. |
| `dsregcmd /refreshprt` | Schedule a refresh of the Primary Refresh Token; check AAD event logs for details. |

# options

| option | description |
| --- | --- |
| `/status` | Displays device state, device details, tenant details, user state, SSO state and diagnostic data. |
| `/refreshprt` | Schedules a PRT refresh. |

