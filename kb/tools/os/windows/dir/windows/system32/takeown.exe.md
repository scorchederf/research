---
created: 2026-11-21
fullpath: 'C:\Windows\System32\takeown.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - takeown.exe
  - takeown
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/takeown
  - https://learn.microsoft.com/security-updates/securitybulletins/2015/ms15-106
---

**fullpath**:C:\Windows\System32\takeown.exe

# description

takeown is a built-in Windows command that enables an administrator to recover access to a file that was previously denied by making the administrator the owner of the file. It is part of the Windows Commands set and is often followed by permission changes with tools such as cacls/icacls.

## simple description

> ### 2026-11-21 Claude said
> takeown changes the owner of files or folders to the current user or to the Administrators group. Admins use it when they're locked out of a file or need to replace a protected system file. It can work recursively and against remote computers. After taking ownership, they usually grant themselves permissions with icacls.
>
> **SOC NOTE**: Attackers and ransomware use `takeown /f <file> /r /d y` followed by `icacls ... /grant` to seize protected files, replace accessibility binaries (sethc.exe, utilman.exe - T1546.008) or disable security tools; this maps to MITRE ATT&CK T1222.001 (Windows File and Directory Permissions Modification). Ownership changes generate Event 4670 (permissions changed) when object auditing is on; watch process creation for takeown against System32 or AV folders.
>

# purpose

Make the current user (or the Administrators group with `/a`) the owner of a file or directory so that access can be restored. Mixed wildcard patterns (`?` with `*`) aren't supported, and after taking ownership you may still need to grant yourself full permissions before deleting the files.

# typical use cases

| usage | description |
| --- | --- |
| `takeown /f lostfile` | Take ownership of a file named Lostfile. |
| `takeown /f %windir%\system32\vbscript.dll` | Take ownership of a system DLL before changing its ACL (MS15-106 workaround pattern). |

# options

| option    | description    |
| --- | --- |
| `/s <computer>` | Name or IP address of a remote computer (no backslashes); default is the local computer. |
| `/u [<domain>\]<username>` | Runs the command with the permissions of the specified user account; default is system permissions. |
| `/p [<password>]` | Password of the user account specified in `/u`. |
| `/f <filename>` | File or directory name pattern; `*` wildcard and `<sharename>\<filename>` syntax are allowed. |
| `/a` | Gives ownership to the Administrators group instead of the current user. |
| `/r` | Recursive operation on all files in the directory and subdirectories. |
| `/d {Y \| N}` | Suppresses the prompt when the user lacks List Folder/Read permission: Y takes ownership of the directory, N skips it. Must be used with `/r`. |
| `/?` | Displays help at the command prompt. |
