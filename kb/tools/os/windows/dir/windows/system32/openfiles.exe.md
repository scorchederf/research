---
created: 2026-11-21
fullpath: 'C:\Windows\System32\openfiles.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - openfiles.exe
  - openfiles
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/openfiles
---

**fullpath**:C:\Windows\System32\openfiles.exe

# description

openfiles lets an administrator query, display or disconnect files and directories opened on a system, and enables or disables the system **Maintain Objects List** global flag. Related tools include Sysinternals Handle.

## simple description

> ### 2026-11-21 Claude said
> openfiles shows which files on a server are open through shared folders and who has them open, and can force them closed. With /local on it also tracks files opened locally, after a reboot. Admins use it when a shared file is locked. It can target remote systems with credentials.
>
> **SOC NOTE**: Attackers use `openfiles /query` for discovery of active users and files (T1083, T1033), or as a quick admin-rights check because it fails without elevation. `openfiles /disconnect` could disrupt users; remote use with /u /p may expose credentials on the command line in process logs.
>

# purpose

Query, display or disconnect open files and folders, and toggle the Maintain Objects List flag.

# typical use cases

| usage | description |
| --- | --- |
| `openfiles /query` | Query and display all open files. |
| `openfiles /query /fo table /nh` | Display open files as a table without headers. |
| `openfiles /query /fo list /v` | Display open files as a list with detailed information. |
| `openfiles /disconnect /id 26843578` | Disconnect the open file with that file ID. |
| `openfiles /disconnect /a hiropln` | Disconnect all files opened by user hiropln. |
| `openfiles /disconnect /o read/write` | Disconnect all files opened in read/write mode. |
| `openfiles /local on` | Enable the Maintain Objects List global flag (after restart). |

# options

| option    | description    |
| --- | --- |
| `/disconnect` | Disconnects files and folders opened remotely through a shared folder. |
| `/s <system>` | Remote system to connect to (name or IP, no backslashes); default local computer. |
| `/u [<domain>\]<username>` | Runs using the specified account's permissions; default system permissions. |
| `/p [<password>]` | Password for the `/u` account; prompts if omitted. |
| `/id <openfileID>` | Disconnects open files by file ID; wildcard allowed. |
| `/a <accessedby>` | Disconnects all open files for that user name; wildcard allowed. |
| `/o {read \| write \| read/write}` | Disconnects all open files with that open mode; wildcard allowed. |
| `/op <openfile>` | Disconnects connections created by a specific open file name; wildcard allowed. |
| `/query` | Queries and displays all open files. |
| `/fo {TABLE \| LIST \| CSV}` | Output format for `/query`. |
| `/nh` | Suppresses column headers; only with TABLE or CSV. |
| `/v` | Verbose output. |
| `/local [on \| off]` | Shows, enables or disables the Maintain Objects List global flag; changes need a restart. |
| `/?` | Displays help at the command prompt. |
