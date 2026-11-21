---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbadmin.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - backup
aliases:
  - wbadmin.exe
  - wbadmin
  - Windows Server Backup
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/wbadmin
---

**fullpath**:C:\Windows\System32\wbadmin.exe

# description

`wbadmin.exe` backs up and restores the operating system, volumes, files, folders and applications from a command prompt. It is the command-line interface of Windows Server Backup; PowerShell equivalents are the WindowsServerBackup cmdlets. Must run elevated; scheduling requires Administrators membership.

## simple description

> ### 2026-11-21 Claude said
> wbadmin is Windows' built-in backup tool. Admins use it to create system state or full backups, list backup versions and restore data. It can also delete backups and the backup catalog. Most commands require Backup Operators or Administrators.
>
> **SOC NOTE**: Ransomware commonly runs `wbadmin delete catalog -quiet` and `wbadmin delete systemstatebackup` to inhibit recovery (MITRE T1490). It can also back up NTDS.dit on DCs for offline credential theft (T1003.003). Alert on delete subcommands and on backups of system state to unusual targets.
>

# purpose

Command-line backup and recovery for Windows.

# typical use cases

| usage | description |
| --- | --- |
| `wbadmin start backup` | Runs a one-time backup; without parameters uses the daily backup schedule settings. |
| `wbadmin get versions` | Lists backups recoverable from the local computer or another location. |
| `wbadmin start systemstatebackup` | Runs a system state backup. |

# options

| option | description |
| --- | --- |
| `wbadmin delete catalog` | Deletes the backup catalog on the local computer; use only if the catalog is corrupted. |
| `wbadmin delete systemstatebackup` | Deletes one or more system state backups. |
| `wbadmin disable backup` | Disables your daily backups. |
| `wbadmin enable backup` | Configures and enables a regularly scheduled backup. |
| `wbadmin get disks` | Lists disks that are currently online. |
| `wbadmin get items` | Lists the items included in a backup. |
| `wbadmin get status` | Shows status of the currently running backup or recovery. |
| `wbadmin get versions` | Lists details of recoverable backups. |
| `wbadmin restore catalog` | Recovers a backup catalog from a storage location if the local catalog is corrupted. |
| `wbadmin start backup` | Runs a one-time backup. |
| `wbadmin start recovery` | Recovers volumes, applications, files or folders. |
| `wbadmin start sysrecovery` | Recovers the full system; only in Windows Recovery Environment. |
| `wbadmin start systemstatebackup` | Runs a system state backup. |
| `wbadmin start systemstaterecovery` | Runs a system state recovery. |
| `wbadmin stop job` | Stops the currently running backup or recovery operation. |
