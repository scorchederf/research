---
created: 2026-11-21
fullpath: 'C:\Windows\System32\ntdsutil.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - active-directory
aliases:
  - "ntdsutil.exe"
  - "Ntdsutil"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/use-ntdsutil-manage-ad-files
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/transfer-or-seize-operation-master-roles-in-ad-ds
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/find-servers-holding-fsmo-role
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/ad-database-offline-defragmentation
  - https://learn.microsoft.com/windows-server/identity/ad-ds/deploy/simplified-administration-appendix
---

**fullpath**:C:\Windows\System32\ntdsutil.exe

# description

Ntdsutil.exe is a command-line tool for managing the Active Directory database file (Ntds.dit), its log files and paths, and for viewing, transferring and seizing FSMO (operations master) roles. It is available on domain controllers and with the AD RSAT tools, and it is related to Esentutl.exe (database recovery) and the IFM (Install from Media) feature.

## simple description

> ### 2026-11-21 Claude said
> Ntdsutil is an interactive menu-driven tool that administrators use to maintain the Active Directory database on domain controllers. It can move, compact, check and recover the Ntds.dit database, manage FSMO roles, clean up metadata and create Install-From-Media (IFM) snapshots. Commands can be typed in its menus or chained on a single command line.
>
> **SOC NOTE**: Attackers abuse `ntdsutil "ac i ntds" "ifm" "create full C:\temp" q q` to dump a copy of Ntds.dit and the SYSTEM hive for offline credential extraction (MITRE ATT&CK T1003.003 NTDS). Watch for ntdsutil process creation (Sysmon 1 / 4688) with `ifm` or `snapshot` arguments, ESENT application log events 325/326/327/216, and new folders containing `Active Directory\ntds.dit` and `registry\SYSTEM`.
>

# purpose

Manage the AD DS database (Ntds.dit) and log files from the command line, perform offline defragmentation (`compact to`), recover the database, set database/log/backup/working-directory paths, view FSMO role holders, transfer or seize FSMO roles, and create IFM media for promoting new domain controllers.

# typical use cases

| usage | description |
| --- | --- |
| `ntdsutil` then `files` then `info` | Displays the current path and size of the AD database and log files. |
| `ntdsutil` then `files` then `recover` | Recovers the Active Directory database (run in Directory Services Restore mode). |
| `ntdsutil` then `files` then `move DB to <new location>` | Moves Ntds.dit to an existing folder and updates the registry; restart required. |
| `ntdsutil` then `files` then `move logs to <new location>` | Moves the directory service log files to another folder. |
| `ntdsutil` then `files` then `compact to <drive>:\<directory>` | Creates a defragmented (compacted) copy of the database in the specified folder. |
| `ntdsutil roles Connections "Connect to server %1" Quit "select Operation Target" "List roles for connected server" Quit Quit Quit` | Lists FSMO role owners on the specified domain controller in one command line (Dumpfsmos.cmd). |
| `ntdsutil` then `roles` then `connections` then `connect to server <servername>` then `q` then `transfer <role>` / `seize <role>` | Transfers or seizes an operations master role (e.g. `seize rid master`, `seize pdc`, `seize naming master`). |

# options

| option | description |
| --- | --- |
| `files` | Enters the file maintenance menu (info, recover, move DB to, move logs to, set path, compact to). |
| `set path {Backup \| Database \| Logs \| Working Directory} <location>` | At the file maintenance prompt, updates the registry location of the backup target, data file, log files or working folder. |
| `roles` | Enters the fsmo maintenance menu used to connect to a server and transfer or seize roles; increases the next RID pool by 10,000 when seizing the RID master. |
| `domain management` | Menu used with `connections` and `select operation target` to list roles for a connected server. |
| `Create Full NoDefrag %s` | IFM menu item: creates IFM media without defragmenting for a full AD DC or AD LDS instance into folder %s (Windows Server 2012+). |
| `Create Sysvol Full NoDefrag %s` | IFM menu item: creates IFM media with SYSVOL and without defragmenting into folder %s (Windows Server 2012+). |
| `?` | Lists the commands available at the current prompt. |
| `quit` / `q` | Leaves the current menu or the tool. |
