---
created: 2026-11-21
fullpath: 'C:\Windows\System32\csvde.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "csvde.exe"
  - "Csvde"
  - "CSVDE"
url:
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc732101(v=ws.11)
  - https://learn.microsoft.com/windows/win32/ad/comma-separated-value-csv-scripts
---

**fullpath**:C:\Windows\System32\csvde.exe

# description

Csvde is a command-line tool that imports and exports Active Directory Domain Services (AD DS) data using comma-separated value (CSV) files. It is built into Windows Server in `%windir%\system32` and is available when the AD DS or AD LDS server role (or the AD DS tools) is installed. It is a sibling of `ldifde`, which uses LDIF instead of CSV.

## simple description

> ### 2026-11-21 Claude said
> Csvde is an administrator tool for bulk exporting Active Directory objects to a CSV file or creating objects from one. By default it exports, using the credentials of the logged-on user, and it can filter with LDAP queries. Admins use it for reporting or bulk user creation. It cannot set passwords.
>
> **SOC NOTE**: A single `csvde -f out.csv` dumps the whole directory (users, groups, computers, descriptions) for offline analysis, which is classic AD discovery (MITRE ATT&CK T1087.002 Domain Account, T1069.002 Domain Groups, T1482 Domain Trust Discovery). Execution on a non-admin workstation or by an unusual account, especially with `-r` filters for admins or with output to temp folders, is suspicious. Look for process creation events (4688/Sysmon 1) and large LDAP query volumes on DCs (Event 1644 if enabled).
>

# purpose

Imports and exports AD DS data in CSV format and supports batch operations. It must be run from an elevated command prompt. User passwords cannot be imported because csvde does not support SSL or encrypted LDAP; setting `userAccountControl` to 514 (disabled) is recommended for created users. The first line of a CSV file lists the attribute names.

# typical use cases

| usage | description |
| --- | --- |
| `csvde -f output.csv` | Exports data from the current domain to output.csv. |
| `csvde -i -f input.csv` | Imports data from input.csv into the current domain. |
| `csvde -d "ou=marketing,dc=contoso,dc=com" -f marketingobjects.csv` | Exports all objects in the Marketing OU. |
| `csvde -r objectClass=user -f usersonly.csv` | Exports only user objects. |
| `csvde -f search.txt -p subtree -l SamAccountName,CN,Distinguishname` | Exports selected attributes with subtree scope. |
| `csvde -r (&(objectClass=User)(sn=Surname))` | Exports all users with a particular surname. |

# options

| option | description |
| --- | --- |
| `-i` | Specifies import mode. If not specified, the default mode is export. |
| `-f <FileName>` | Identifies the import or export file name. |
| `-s <ServerName>` | Specifies the domain controller to perform the import or export operation. |
| `-c <String1> <String2>` | Replaces all occurrences of String1 with String2, e.g. to swap the export domain DN for the import domain DN. |
| `-v` | Sets verbose mode. |
| `-j <Path>` | Sets the log file location. The default is the current path. |
| `-t <PortNumber>` | Specifies an LDAP port. Default 389; global catalog port is 3268. |
| `-u` | Specifies Unicode format. |
| `-d <BaseDN>` | Sets the distinguished name of the search base for data export. |
| `-r <LDAPFilter>` | Creates an LDAP search filter for data export. |
| `-p <Scope>` | Sets the search scope: Base, OneLevel, or SubTree. |
| `-l <LDAPAttributeList>` | Sets the list of attributes to return in an export query; if omitted, all attributes are returned. |
| `-o <LDAPAttributeList>` | Specifies the list of attributes to omit from the results of an export query. |
| `-g` | Omits paged searches. |
| `-m` | Omits attributes that apply only to Active Directory objects, such as ObjectGUID, objectSID, pwdLastSet and samAccountType. |
| `-n` | Omits the export of binary values. |
| `-k` | Ignores errors (object already exists, constraint violation, attribute or value already exists) during import and continues. |
| `-a <UserDistinguishedName> {<Password> \| *}` | Performs a simple LDAP bind with the supplied user DN and password. |
| `-b <UserName> <Domain> {<Password> \| *}` | Performs a secure LDAP bind with the NEGOTIATE authentication method. |
| `/?` | Displays Help at the command prompt. |
