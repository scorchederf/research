---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Credentials'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - credentials
  - dpapi
aliases:
  - "Credentials"
  - "Credential Manager store"
  - "Windows Vault"
url:
  - https://learn.microsoft.com/windows-server/security/windows-authentication/credentials-processes-in-windows-authentication
  - https://learn.microsoft.com/windows/security/identity-protection/credential-guard/considerations-known-issues
  - https://learn.microsoft.com/windows/win32/secbp/handling-passwords
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Credentials

# description

Per-user roaming folder where Windows Credential Manager persists saved credentials as encrypted files. Learn describes Credential Manager saving credentials "in special encrypted folders on the computer under the user's profile", written via `CredWrite` and protected with the user's logon session key.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the user's saved passwords from Credential Manager, such as saved RDP, network share and some app logins.
> Each file has a random-looking name and is encrypted with DPAPI, tied to the user's password.
> Because it is in the Roaming profile it can follow the user between machines with roaming profiles.
>
> **SOC NOTE**: Target for credential theft (T1555.004 Windows Credential Manager): tools like Mimikatz dpapi::cred / SharpDPAPI decrypt these blobs with the user's DPAPI master keys (AppData\Roaming\Microsoft\Protect). Watch for non-standard processes reading this folder or copying it with the Protect folder.
>

# purpose

Stores credentials saved through Credential Manager (Windows credentials, certificate-based credentials and generic credentials) so they can be supplied automatically on later logons. Domain credentials stored in Credential Manager are protected by Credential Guard; generic credentials are not.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
