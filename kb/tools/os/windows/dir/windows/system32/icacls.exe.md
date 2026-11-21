---
created: 2026-11-21
fullpath: 'C:\Windows\System32\icacls.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - permissions
aliases:
  - icacls.exe
  - icacls
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/icacls
---

**fullpath**:C:\Windows\System32\icacls.exe

# description

`icacls` displays or modifies discretionary access control lists (DACLs) on files and folders and applies stored DACLs to files in a directory. It is a built-in Windows command that replaces the deprecated `cacls` command.

## simple description

> ### 2026-11-21 Claude said
> icacls is a command-line tool for viewing and changing NTFS permissions on files and folders. It can grant, deny or remove access for users, change ownership, reset inheritance and save or restore permissions to a file. Administrators use it to fix or audit access rights in bulk.
>
> **SOC NOTE**: Attackers use icacls to grant `Everyone` full control, take ownership of protected files, or hide payloads by denying access (T1222.001 File and Directory Permissions Modification). Ransomware often runs `icacls * /grant Everyone:F /T /C /Q` before encryption. Look for process creation events (4688 / Sysmon 1) with `/grant`, `/setowner`, `/reset` or `/deny`, and object-access event 4670 for permission changes.
>

# purpose

Displays, modifies, saves and restores DACLs, sets owners and integrity levels, and finds files with specific SIDs or non-canonical ACLs. ACEs are kept in canonical order: explicit denials, explicit grants, inherited denials, inherited grants.

# typical use cases

| usage | description |
| --- | --- |
| `icacls c:\windows\* /save aclfile /t` | Save DACLs for all files under C:\Windows and subdirectories to ACLFile. |
| `icacls c:\windows\ /restore aclfile` | Restore DACLs from ACLFile to files in C:\Windows. |
| `icacls test1 /grant User1:(d,wdac)` | Grant User1 Delete and Write DAC on Test1. |
| `icacls TestFile /grant *S-1-1-0:(d,wdac)` | Grant SID S-1-1-0 Delete and Write DAC on TestFile. |
| `icacls "myDirectory" /setintegritylevel (CI)(OI)H` | Apply a high integrity level inherited by files and subdirectories. |

# options

| option | description |
| --- | --- |
| `<name>` | File for which to display or modify DACLs. |
| `<directory>` | Directory for which to display or modify DACLs. |
| `/t` | Performs the operation on all specified files in the current directory and subdirectories. |
| `/c` | Continues even if file errors occur; errors are still shown. |
| `/l` | Operates on a symbolic link instead of its destination. |
| `/q` | Suppresses success messages. |
| `/save <ACLfile>` | Stores DACLs for matching files into an ACL file for later `/restore`. |
| `/setowner <user>` | Changes the owner of all matching files. |
| `/findsid <sid>` | Finds files whose DACL explicitly mentions the SID. |
| `/verify` | Finds files with non-canonical ACLs or lengths inconsistent with ACE counts. |
| `/reset` | Replaces ACLs with default inherited ACLs. |
| `/grant[:r] <sid>:<perm>` | Grants access rights; `:r` replaces previously granted explicit permissions, otherwise they are added. |
| `/deny <sid>:<perm>` | Adds an explicit deny ACE and removes the same permissions from any explicit grant. |
| `/remove[:g\|:d] <sid>` | Removes all occurrences of the SID; `g` only granted rights, `d` only denied rights. |
| `/setintegritylevel <perm><level>` | Adds an integrity ACE: `l` Low, `m` Medium, `h` High. |
| `/substitute <sidold> <sidnew>` | Replaces an existing SID with a new SID (with `<directory>`). |
| `/restore <ACLfile>` | Applies stored DACLs to files in the directory (with `<directory>`). |
| `/inheritancelevel:[e\|d\|r]` | `e` enables inheritance, `d` disables and copies ACEs, `r` disables and removes inherited ACEs. |
