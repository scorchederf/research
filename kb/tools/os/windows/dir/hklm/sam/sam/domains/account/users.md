---
created: 2026-11-21
fullpath: 'HKLM\SAM\SAM\Domains\Account\Users'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - sam
  - accounts
aliases:
  - Users
  - SAM Account domain users
  - Security Accounts Manager
url:
  - https://learn.microsoft.com/windows/win32/secmgmt/built-in-and-account-domains
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
  - https://learn.microsoft.com/windows-server/security/windows-authentication/credentials-processes-in-windows-authentication
---

**fullpath**:HKLM\SAM\SAM\Domains\Account\Users

# description

Registry location inside the Security Accounts Manager (SAM) hive that holds the local user accounts of the computer's account domain. The SAM database exists on every non-domain-controller computer and is used by the LSA to validate local accounts; domain controllers use Active Directory instead.

## simple description

> ### 2026-11-21 Claude said
> This key is where Windows stores local user accounts: each user has a subkey named by its RID in hex (for example 000001F4 for Administrator), with binary F and V values holding account flags, last logon times and the password hashes, plus a Names subkey mapping user names to RIDs. Normally only SYSTEM can read it; administrators see it empty in regedit. It is part of the SAM hive file at C:\Windows\System32\config\SAM.
>
> **SOC NOTE**: High forensic value: reveals local accounts, creation/last-logon/password-change times, logon counts and disabled state (tools: RegRipper samparse). Attackers dump it to extract NT hashes (T1003.002 Security Account Manager) via `reg save HKLM\SAM`, shadow copies or Mimikatz lsadump::sam. New RID subkeys indicate account creation (T1136.001); RID hijacking (T1098) modifies the F value. Alert on `reg save hklm\sam` and access to config\SAM.
>

# purpose

Holds the user accounts of the SAM account domain. The account domain can contain user, group and local group accounts, including the Administrator account; accounts there can access only resources on that computer. Its name is derived from the computer name. LSA validates local logons by checking this SAM database.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SAM` (with Sam.log, Sam.sav) |

# values

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SAM\SAM\Domains\Account\Users"` | List the key's values and subkeys (requires SYSTEM rights). |
