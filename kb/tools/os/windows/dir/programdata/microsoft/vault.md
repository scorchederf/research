---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Vault'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Vault
  - Windows Vault
  - Credential Manager
url:
  - https://learn.microsoft.com/windows-server/security/windows-authentication/credentials-processes-in-windows-authentication
  - https://learn.microsoft.com/windows/security/identity-protection/credential-guard/how-it-works
  - https://learn.microsoft.com/windows/win32/secbp/handling-passwords
---

**fullpath**:C:\ProgramData\Microsoft\Vault

# description

The Windows Vault is the secure store behind Credential Manager, a Control Panel feature introduced in Windows 7 and Windows Server 2008 R2 that stores user names and passwords for other systems and websites. Learn describes saved credentials as kept in special encrypted folders; it does not document this specific ProgramData path. Related: Credential Manager APIs (`CredWrite`, `CredRead`), DPAPI, Credential Guard.

## simple description

> ### 2026-11-21 Claude said
> This folder is the machine-wide part of the Windows Vault, where Windows keeps encrypted saved credentials that are not tied to a single user (per-user vaults live under each profile's AppData). Credential Manager uses the vault to remember passwords for websites, network shares and apps so users do not need to retype them. The files are encrypted with DPAPI and are not readable as plain text. Normal users rarely touch this folder directly.
>
> **SOC NOTE**: Attackers target vault contents to steal saved passwords (MITRE ATT&CK T1555.004 Windows Credential Manager), using tools such as Mimikatz `vault::cred` / `dpapi::` modules, `vaultcmd`, or SharpDPAPI. Unexpected processes reading `*.vcrd` / `Policy.vpol` files here, or copying the folder alongside DPAPI master keys, is a strong credential-access indicator. Credential Guard does not protect credentials stored in the Windows Vault.
>

# purpose

Credential Manager lets users store credentials for other systems and websites in the secure Windows Vault. When a service requests NTLM or Kerberos authentication and the user selects **Save Password**, Credential Manager records the user name, password and related information and supplies them automatically next time, overwriting them if new credentials are accepted. Credentials stored in the Windows Vault aren't protected by Credential Guard.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
