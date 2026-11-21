---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Vault'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - credentials
  - dpapi
  - vault
aliases:
  - "Vault"
  - "Windows Vault"
  - "Credential Manager vault"
url:
  - https://learn.microsoft.com/windows-server/security/windows-authentication/credentials-processes-in-windows-authentication
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\Vault

# description

Per-user storage location for the Windows Vault used by Credential Manager to keep saved credentials for websites, applications and other computers. Credential Manager is a Control Panel feature introduced in Windows 7 / Windows Server 2008 R2. Related: cmdkey.exe, VaultCmd.exe, Credential Manager APIs (CredWrite/CredRead).

## simple description

> ### 2026-11-21 Claude said
> This folder holds the user's Windows Vault: encrypted saved credentials such as web passwords from legacy IE/Edge and some Windows app sign-ins. Folders are named by GUID and contain a Policy.vpol file plus .vcrd credential records, protected with DPAPI. Credential Manager reads them to sign the user in automatically.
>
> **SOC NOTE**: Target for credential theft (T1555.004 Windows Credential Manager): tools like Mimikatz (vault::cred), SharpDPAPI or LaZagne decrypt .vcrd files with the user's DPAPI master keys. Access by non-standard processes, or copying this folder with the Protect folder, is a strong indicator.
>

# purpose

Credential Manager lets users store credentials relevant to other systems and websites in the secure Windows Vault. Credentials are saved in special encrypted folders on the computer under the user's profile; applications using the Credential Manager APIs present them automatically during logon to resources, and Credential Manager overwrites a stored credential when new ones are accepted.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
