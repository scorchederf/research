---
created: 2026-11-21
fullpath: 'C:\Windows\System32\dsquery.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - active-directory
  - lolbin
aliases:
  - dsquery.exe
  - Dsquery
url:
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc732952(v=ws.11)
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/directory-service-manage-objects
---

**fullpath**:C:\Windows\System32\dsquery.exe

# description

`dsquery` is an Active Directory Directory Service command-line tool that queries the directory using search criteria you specify. It is built into Windows Server and available when the Active Directory Domain Services (AD DS) role (or the AD DS tools) is installed, alongside related tools such as `dsget`, `dsadd`, `dsmod` and `dsrm`.

## simple description

> ### 2026-11-21 Claude said
> dsquery is a command-line tool for searching Active Directory. You can ask it to list users, computers, groups, OUs, domain controllers or any object using an LDAP filter. Admins use it for reports and scripts. It is installed with RSAT AD DS tools or on domain controllers.
>
> **SOC NOTE**: Frequently used by attackers for domain discovery (MITRE ATT&CK T1087.002 Domain Account, T1069.002 Domain Groups, T1018 Remote System Discovery, T1482 Domain Trust Discovery), e.g., `dsquery * -filter "(objectClass=trustedDomain)"` or `dsquery user -limit 0`. Its presence on a workstation without RSAT is suspicious; hunt for process creation (4688 / Sysmon 1) with dsquery from non-admin hosts or launched by scripts/LOLBins.

# purpose

Each `dsquery` command finds objects of a specific object type, with the exception of `dsquery *`, which can query for any type of object. It must be run from an elevated command prompt.

# typical use cases

| usage | description |
| --- | --- |
| `dsquery user <parameter>` | Find user accounts. |
| `dsquery computer -name <name>` | Find computer accounts whose name (CN) matches. |
| `dsquery group <parameter>` | Find groups. |
| `dsquery ou <parameter>` | Find organizational units. |
| `dsquery server <parameter>` | Find domain controllers. |
| `dsquery * <parameter>` | Perform a custom LDAP search for any object type. |
| `dsquery user /?` | View the complete syntax for a subcommand. |

# options

| option | description |
| --- | --- |
| `computer` | Finds computers in the directory that match search criteria that you specify. |
| `contact` | Finds contacts in the directory that match search criteria that you specify. |
| `group` | Finds groups in the directory that match search criteria that you specify. |
| `ou` | Finds organizational units (OUs) in the directory that match search criteria that you specify. |
| `site` | Finds sites in the directory that match search criteria that you specify. |
| `server` | Finds domain controllers according to specified search criteria. |
| `user` | Finds users in the directory that match search criteria that you specify. |
| `quota` | Finds quota specifications (maximum number of objects a security principal can own in a partition). |
| `partition` | Finds partition objects in the directory that match search criteria that you specify. |
| `*` | Finds any objects in the directory according to criteria using an LDAP query. |
