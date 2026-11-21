---
created: 2026-11-21
fullpath: 'C:\Windows\System32\vaultcmd.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - credentials
aliases:
  - vaultcmd.exe
  - vaultcmd
url:
---

**fullpath**:C:\Windows\System32\vaultcmd.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> `vaultcmd.exe` is a built-in command-line tool for the Windows Credential Manager "vaults" (Web Credentials and Windows Credentials). It can list the vaults, show their properties and list or create/delete stored credentials. It is the command-line counterpart of the Credential Manager control panel, related to `cmdkey.exe`.
>
> **SOC NOTE**: Used for credential discovery (T1555.004 Credentials from Windows Credential Manager): `vaultcmd /listcreds:"Windows Credentials" /all` reveals stored targets and user names (not plaintext passwords). Execution by unusual parents or right after initial access is a reconnaissance indicator. Vault files live in `%LOCALAPPDATA%\Microsoft\Vault` and `%ProgramData%\Microsoft\Vault`, protected with DPAPI.
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
