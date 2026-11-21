---
created: 2026-11-21
fullpath: 'C:\Windows\System32\whoami.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - whoami.exe
  - whoami
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/whoami
---

**fullpath**:C:\Windows\System32\whoami.exe

# description

whoami shows information about the user, groups and privileges for the account currently logged on to the local system; with no parameters it returns the domain and user name. It is a built-in Windows command.

## simple description

> ### 2026-11-21 Claude said
> whoami tells you which account you are running as. With switches it shows your SID, group memberships, privileges, claims and logon ID, all read from the current access token. Admins use it to check elevation or troubleshoot permissions. It only reports on the current user.
>
> **SOC NOTE**: Classic first command after compromise (T1033). whoami /priv reveals SeImpersonate/SeDebug for privilege escalation (potato attacks), and /groups shows integrity level. whoami spawned by w3wp.exe, sqlservr.exe, Office apps or java is a strong webshell/exploitation indicator. Hunt in 4688/Sysmon 1.
>

# purpose

Display the current user's identity, SID, groups, claims and privileges from the access token.

# typical use cases

| usage | description |
| --- | --- |
| `whoami` | Display the domain and user name of the person currently logged on. |
| `whoami /all` | Display all information in the current access token. |

# options

| option    | description    |
| --- | --- |
| `/upn` | Displays the user name in UPN format. |
| `/fqdn` | Displays the user name in FQDN format. |
| `/logonid` | Displays the logon ID of the current user. |
| `/user` | Displays the current domain and user name and the SID. |
| `/groups` | Displays the groups the current user belongs to. |
| `/claims` | Displays the current user's claims (name, flags, type, values). |
| `/priv` | Displays the security privileges of the current user. |
| `/fo <format>` | Output format: table (default), list or csv. |
| `/all` | Displays all information in the current access token. |
| `/nh` | Hides the column header; valid only for table and CSV formats. |
| `/?` | Displays help at the command prompt. |
