---
created: 2026-11-21
fullpath: 'C:\Windows\System32\diskshadow.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - diskshadow.exe
  - Diskshadow
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/diskshadow
  - https://learn.microsoft.com/windows-server/administration/windows-commands/exec
  - https://learn.microsoft.com/windows-server/administration/windows-commands/vssadmin-delete-shadows
---

**fullpath**:C:\Windows\System32\diskshadow.exe

# description

Diskshadow.exe is a tool that exposes the functionality offered by the Volume Shadow Copy Service (VSS). By default it uses an interactive command interpreter similar to Diskraid or Diskpart, and it also has a scriptable mode (`diskshadow -s script.txt`). Membership in the local Administrators group is the minimum required to run it; Microsoft points to it for shadow copies that `vssadmin` cannot delete.

## simple description

> ### 2026-11-21 Claude said
> Diskshadow is a built-in Windows Server command-line tool for creating, listing, exposing and deleting Volume Shadow Copies (point-in-time snapshots of a disk). Backup admins use it to script consistent backups, often together with VSS writers. It can run interactively or read a script file of commands with `/s`. Because it can mount a snapshot as a drive letter, it gives access to files that are normally locked while Windows is running.
>
> **SOC NOTE**: Attackers use diskshadow scripts to snapshot C: and expose it, then copy the locked `ntds.dit` and SYSTEM hive from a domain controller for offline credential extraction (MITRE ATT&CK T1003.003). Its `exec` command runs arbitrary files, making it a proxy-execution LOLBin (T1218), and `delete shadows all` is used by ransomware to destroy recovery points (T1490). Look for diskshadow.exe with `/s` and a script in a temp/user folder, VSS events (Event IDs 8222, 7036 for VSS service) and unexpected new drive letters.
>

# purpose

Provides command-line and scripted access to VSS: create persistent or non-persistent shadow copies, run backup and restore sessions with writer involvement, expose or revert shadow copies, and import transportable (hardware) shadow copies.

# typical use cases

- Run a saved backup script: `diskshadow /s script.dsh` (set context, add volumes, `create`, `expose` as drive letters, `exec` a backup .cmd, `end backup`).
- List all shadow copies: `list shadows all`
- Delete shadow copies that are not client-accessible to `vssadmin`.

# options

| option    | description    |
| --- | --- |
| `-s <script.txt>` | Runs Diskshadow in script mode using a script file of Diskshadow commands. With no argument, starts the interactive interpreter. |
| `set` | Sets the context, options, verbose mode, and metadata file for creating shadow copies. |
| `load metadata` | Loads a metadata .cab file prior to importing a transportable shadow copy, or loads writer metadata for a restore. |
| `writer` | Verifies that a writer or component is included, or excludes a writer or component from the backup or restore procedure. |
| `add` | Adds volumes to the set of volumes to be shadow copied, or adds aliases to the alias environment. |
| `create` | Starts the shadow copy creation process using the current context and option settings. |
| `exec` | Executes a file (e.g. a .cmd script) on the local computer; if it fails, DiskShadow quits. |
| `begin backup` | Starts a full backup session. |
| `end backup` | Ends a full backup session and issues a **backupcomplete** event with the appropriate writer state. |
| `begin restore` | Starts a restore session and issues a **prerestore** event to involved writers. |
| `end restore` | Ends a restore session and issues a **postrestore** event to involved writers. |
| `reset` | Resets Diskshadow to the default state. |
| `list` | Lists writers, shadow copies, or currently registered shadow copy providers. |
| `delete shadows` | Deletes shadow copies. |
| `import` | Imports a transportable shadow copy from a loaded metadata file into the system. |
| `mask` | Removes hardware shadow copies that were imported by using **import**. |
| `expose` | Exposes a persistent shadow copy as a drive letter, share, or mount point. |
| `unexpose` | Unexposes a shadow copy that was exposed by using **expose**. |
| `break` | Disassociates a shadow copy volume from VSS (hardware shadow copies after import). |
| `revert` | Reverts a volume back to a specified shadow copy. |
| `exit` | Exits the command interpreter or script. |
