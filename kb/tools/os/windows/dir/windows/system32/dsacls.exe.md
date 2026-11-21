---
created: 2026-11-21
fullpath: 'C:\Windows\System32\dsacls.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - active-directory
aliases:
  - "dsacls.exe"
  - "Dsacls"
url:
  - https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771151(v=ws.11)
---

**fullpath**:C:\Windows\System32\dsacls.exe

# description

Dsacls displays and changes permissions (access control entries) in the ACL of objects in Active Directory Domain Services. It is built into Windows Server when the AD DS role is installed and is the command-line equivalent of the Security tab in tools such as Active Directory Users and Computers.

## simple description

> ### 2026-11-21 Claude said
> Dsacls is a built-in Windows Server tool that shows or edits who has which permissions on an Active Directory object, such as a user, group or OU. It works on the object's distinguished name and can grant, deny, remove or reset permissions and change inheritance. It must be run from an elevated prompt and needs Read rights to view or Write rights to change an ACL.
>
> **SOC NOTE**: Attackers use dsacls for AD reconnaissance and ACL abuse, e.g. granting themselves `GA`, `WP` on `member`, or `CA` for DCSync extended rights (MITRE ATT&CK T1222 / T1098 / T1003.006). Look for process creation of dsacls.exe with `/G` or `/D`, and Directory Service Changes event 5136 (nTSecurityDescriptor modified) on domain controllers.
>

# purpose

View and modify ACEs on Active Directory objects, add ownership and auditing information to output, restore default schema security on an object or tree, and control ACE inheritance and protection.

# typical use cases

| usage | description |
| --- | --- |
| `dsacls "CN=Jeff Akers,CN=Users,DC=domain,DC=test,DC=contoso,DC=com"` | Displays the ACEs in the ACL of the specified object. |
| `dsacls "\\Server01\CN=Jeff Akers,CN=Users,DC=domain,DC=test,DC=contoso,DC=com"` | Displays the ACL of an object on a remote computer. |
| `dsacls "<ObjectDN>" /G Domain1\User1:CCDC Domain1\User2:DC;computer` | Grants create/delete child permissions to multiple users. |
| `dsacls "<ObjectDN>" /G Domain\User:CC;computer` | Permits the user to create only child computer objects. |
| `dsacls "<ObjectDN>" /G Domain\User:RPWP;telephonenumber;` | Grants read and write property permissions on the Telephonenumber property. |

# options

| option | description |
| --- | --- |
| `"[\\<Computer>\]<ObjectDN>"` | Distinguished name of the Active Directory object (optionally on a remote computer); must be quoted. Without other parameters the ACEs are displayed. |
| `/A` | Adds ownership and auditing information to the results. |
| `/D <PermissionStatement>` | Denies the specified permissions to the user or group. |
| `/G <PermissionStatement>` | Grants the specified permissions to the user or group. |
| `/I:{T \| S \| P}` | Sets inheritance: T object and child objects (default), S child objects only, P object and children one level only. |
| `/N` | Replaces the current ACEs in the ACL with the specified ACE instead of adding it. |
| `/P:{Y \| N}` | Sets whether the object is protected (Y, cannot inherit) or not protected (N) from parent permissions. |
| `/R {<User> \| <Group>}` | Deletes all ACEs for the specified users or groups. |
| `/S` | Restores security on the object to the schema default for that object class. |
| `/T` | Restores security on the tree of objects to the default; valid only with /S. |
| `/?` | Displays help at the command prompt. |
| `<Permissions>` | Generic: GR, GE, GW, GA. Specific: SD, DT, RC, WD, WO, LC, CC, DC, WS, RP, WP, CA, LO. |
