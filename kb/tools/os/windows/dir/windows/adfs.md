---
created: 2026-11-21
fullpath: 'C:\Windows\ADFS'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - adfs
  - identity
aliases:
  - ADFS
  - AD FS installation folder
url:
  - https://learn.microsoft.com/windows-server/identity/ad-fs/troubleshooting/ad-fs-tshoot-logging
  - https://learn.microsoft.com/windows-server/identity/ad-fs/development/ad-fs-risk-assessment-model
  - https://learn.microsoft.com/windows-server/identity/ad-fs/technical-reference/the-role-of-the-ad-fs-configuration-database
---

**fullpath**:C:\Windows\ADFS

# description

`%windir%\ADFS` is the installation folder of Active Directory Federation Services (AD FS) on Windows Server (2012 R2 and later), the role that provides single sign-on and claims-based federation. It contains the AD FS service binaries and configuration such as `Microsoft.IdentityServer.ServiceHost.Exe.Config` and `Microsoft.IdentityServer.dll`.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the program files for AD FS, the Windows Server role that lets users sign in once and access cloud apps like Microsoft 365. It contains the AD FS service executable, its DLLs and its main configuration file. It only exists on servers where the AD FS role is installed.
>
> **SOC NOTE**: AD FS servers are Tier 0: attackers target them for Golden SAML (MITRE T1606.002) by stealing the token-signing certificate/DKM key and for backdoors via malicious DLLs or modified config (e.g. FoggyWeb loaded through the ServiceHost config). Monitor file changes in this folder, unexpected DLLs, and tracing switches in the .config file.
>

# purpose

Contains the AD FS service host and libraries. Editing `Microsoft.IdentityServer.ServiceHost.Exe.Config` enables WIF and WCF tracing (switchValue Verbose/Information/Warning/Error/Critical), which then appears in the AD FS Tracelog after restarting the service. Developers reference `Microsoft.IdentityServer.dll` from this folder when building risk assessment plug-ins.

# common files found

| file | description |
| --- | --- |
| `Microsoft.IdentityServer.ServiceHost.Exe.Config` | AD FS service XML configuration; WIF/WCF tracing switches. |
| `Microsoft.IdentityServer.dll` | AD FS library referenced by plug-ins such as risk assessment modules. |
