---
created: 2026-11-21
fullpath: 'C:\Windows\System32\auditpol.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - auditpol.exe
  - auditpol
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/auditpol
  - https://learn.microsoft.com/windows-server/administration/windows-commands/auditpol-get
  - https://learn.microsoft.com/windows-server/administration/windows-commands/auditpol-set
  - https://learn.microsoft.com/windows-server/administration/windows-commands/auditpol-list
  - https://learn.microsoft.com/windows-server/administration/windows-commands/auditpol-resourcesacl
---

**fullpath**:C:\Windows\System32\auditpol.exe

# description

auditpol displays information about and manipulates audit policies: system and per-user audit policy, auditing options, the security descriptor that delegates access to audit policy, CSV backup/restore and global resource SACLs. It is a built-in Windows command; get/set/list operations need the corresponding permission in the audit security descriptor or the Manage auditing and security log (SeSecurityPrivilege) right.

## simple description

> ### 2026-11-21 Claude said
> auditpol is the command-line tool for advanced audit policy - which Security log events (logons, process creation, object access, policy changes...) Windows records. Admins use `auditpol /get /category:*` to see what's enabled and `/set` to change it. It's also used to back up and restore audit settings.
>
> **SOC NOTE**: Attackers run `auditpol /clear`, `/remove` or `/set ... /success:disable /failure:disable` to blind defenders (MITRE ATT&CK T1562.002 Impair Defenses: Disable Windows Event Logging). Changes produce Event 4719 (system audit policy changed) and 4912 (per-user policy changed). Any auditpol execution outside known admin tooling should be investigated.
>

# purpose

Set and query system and per-user audit policy, auditing options (CrashOnAuditFail, FullprivilegeAuditing, AuditBaseObjects, AuditBasedirectories) and the audit security descriptor; back up, restore, clear and remove policy; configure global object access auditing (resource SACLs).

# typical use cases

| usage | description |
| --- | --- |
| `auditpol /get /option:AuditBaseObjects` | Show the state of the AuditBaseObjects option. |
| `auditpol /get /option:CrashOnAuditFail /r` | Show CrashOnAuditFail in CSV report format. |
| `auditpol /set /category:"detailed Tracking" /success:enable` | Audit successful events for all Detailed Tracking subcategories. |
| `auditpol /set /option:CrashOnAuditFail /value:enable` | Enable the CrashOnAuditFail option. |
| `auditpol /list /user /v` | List users with a per-user audit policy and their SIDs. |
| `auditpol /list /subcategory:* /r` | List all categories and subcategories as CSV. |

# options

| option    | description    |
| --- | --- |
| `/get` | Displays the current audit policy (`/user`, `/category`, `/subcategory`, `/option`, `/sd`, `/r`). |
| `/set` | Sets the audit policy (`/user`, `/include`, `/exclude`, `/category`, `/subcategory`, `/success`, `/failure`, `/option`, `/sd`). |
| `/list` | Displays selectable policy elements (`/user`, `/category`, `/subcategory`, `/v`, `/r`). |
| `/backup` | Saves the audit policy to a file. |
| `/restore` | Restores the audit policy from a file created by `auditpol /backup`. |
| `/clear` | Clears the audit policy. |
| `/remove` | Removes all per-user audit policy settings and disables all system audit policy settings. |
| `/resourceSACL` | Configures global resource SACLs (`/set`, `/remove`, `/clear`, `/view` with `/type:File\|Key`, `/user`, `/access`, `/success`, `/failure`). Windows 7 / Server 2008 R2. |
| `/?` | Displays help at the command prompt. |
