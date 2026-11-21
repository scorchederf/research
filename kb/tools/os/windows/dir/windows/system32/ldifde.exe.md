---
created: 2026-11-21
fullpath: 'c:\windows\system32\ldifde.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - active-directory
  - ldap
aliases:
  - ldifde.exe
  - Ldifde
  - LDIFDE
url:
  - https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731033(v=ws.11)
---

**fullpath**:c:\windows\system32\ldifde.exe

# description

Ldifde is a command-line tool that creates, modifies and deletes directory objects using LDAP Data Interchange Format (LDIF) files. It is available when the AD DS or AD LDS server role (or RSAT) is installed; csvde is the CSV-based companion tool.

## simple description

> ### 2026-11-21 Claude said
> ldifde exports Active Directory objects to a text file, or imports changes from one. Administrators use it to bulk create users, extend the schema, or copy data between directories. It must run from an elevated prompt and talks LDAP (port 389) to a domain controller. Normally found on domain controllers and admin workstations.
>
> **SOC NOTE**: Used for AD reconnaissance (MITRE T1087.002 Domain Account, T1482 Domain Trust Discovery): `ldifde -f out.ldf -r (objectClass=user)` dumps all users and attributes, a pattern seen in ransomware pre-staging. Import mode (`-i`) can modify AD objects or schema (T1098 Account Manipulation). Flag ldifde on non-admin hosts, exports to temp folders, and large LDAP queries in DC events 1644.
>

# purpose

Exports AD DS objects (default mode) or imports changes from an LDIF file (`-i`). Import files use a **changeType** of **add**, **modify** or **delete**. Can extend the schema, export user and group information to other applications, and populate AD DS from other directory services.

# typical use cases

| usage | description |
| --- | --- |
| `Ldifde -d dc=fabrikam,dc=com -r (objectClass=User) -l distinguishedname,cn,givenname,sn,telephone -f ldifde.txt` | Export selected attributes of all user objects in fabrikam.com. |
| `Ldifde -d dc=fabrikam,dc=com -r (objectClass=User) -o whenCreated,objectGUID -f ldifde.txt` | Export users while omitting creation time and GUID. |
| `Ldifde -i -f import.ldf -k` | Import an LDIF file and continue past common errors. |

# options

| option | description |
| --- | --- |
| `-i` | Use import mode. The default mode is export. |
| `-f <FileName>` | Import or export file name. |
| `-s <ServerName>` | Domain controller to perform the operation against. |
| `-c <String1> <String2>` | Replace all occurrences of String1 with String2, e.g. when moving data between domains. |
| `-v` | Verbose mode. |
| `-j <Path>` | Log file location; default is the current path. |
| `-t <PortNumber>` | LDAP port; default 389, global catalog 3268. |
| `-d <BaseDN>` | Distinguished name of the search base for export. |
| `-r <LDAPFilter>` | LDAP search filter for export. |
| `-p <Scope>` | Search scope: Base, OneLevel or SubTree. |
| `-l <LDAPAttributeList>` | Attributes to return in an export. |
| `-o <LDAPAttributeList>` | Attributes to omit from an export. |
| `-g` | Omit paged searches. |
| `-m` | Omit Active Directory-only attributes such as ObjectGUID, objectSID, pwdLastSet, samAccountType. |
| `-n` | Omit export of binary values. |
| `-k` | Ignore common errors during import and continue. |
| `-a <UserDistinguishedName> <Password>` | Run with the supplied DN and password. |
| `-b <UserName> <Domain> <Password>` | Run with the supplied user name, domain and password. |
| `/?` | Display help. |
