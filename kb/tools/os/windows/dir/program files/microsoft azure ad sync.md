---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Azure AD Sync'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - entra-connect
  - identity
aliases:
  - Microsoft Azure AD Sync
  - ADSync
  - Microsoft Entra Connect Sync
url:
  - https://learn.microsoft.com/troubleshoot/entra/entra-id/user-prov-sync/troubleshoot-aad-connect-objects-attributes
  - https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-single-object-sync
  - https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-group-writeback-disable
  - https://learn.microsoft.com/entra/identity/hybrid/connect/concept-adsync-service-account
---

**fullpath**:C:\Program Files\Microsoft Azure AD Sync

# description

`C:\Program Files\Microsoft Azure AD Sync` is the installation folder of the Microsoft Entra Connect Sync engine (ADSync service, also known as MiiServer). It contains the `Bin` folder with the sync engine and the ADSync PowerShell modules. The ADSync service orchestrates synchronization between on-premises Active Directory and Microsoft Entra ID.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the synchronization engine behind Azure AD Connect / Microsoft Entra Connect. It runs as the ADSync service and copies users, groups and password hashes from on-prem AD to Entra ID. It also includes the Synchronization Service Manager and PowerShell modules for admins. Servers with this folder are Tier 0 assets.
>
> **SOC NOTE**: Entra Connect servers are high-value targets: attackers extract the AD DS connector (MSOL_) and Entra credentials from the ADSync database (AADInternals, adconnectdump; T1555, T1003.006 DCSync rights) or backdoor password hash sync / PTA. Monitor for unexpected processes loading mcrypt.dll, access to ADSync LocalDB, and changes to miiserver.exe.config.
>

# purpose

Holds the Entra Connect Sync engine binaries, configuration and PowerShell modules used to administer and troubleshoot synchronization.

# common files found

| file | description |
| --- | --- |
| `Bin\miiserver.exe.config` | Sync engine (MiiServer) config; ETW tracing of the sync rules pipeline can be enabled here. |
| `Bin\ADSync\ADSync.psd1` | ADSync PowerShell module (e.g. `Set-ADSyncAADCompanyFeature`). |
| `Bin\ADSyncDiagnostics\ADSyncDiagnostics.psm1` | Diagnostics module providing `Invoke-ADSyncSingleObjectSync`. |

