---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\vshadow.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-sdk
  - vss
  - shadow-copy
aliases:
  - vshadow.exe
  - VShadow
url:
  - https://learn.microsoft.com/windows/win32/vss/vshadow-tool-and-sample
  - https://learn.microsoft.com/windows/win32/vss/vshadow-tool-examples
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\vshadow.exe

# description

VShadow is a command-line tool from the Windows SDK (Windows Vista and later) for creating and managing Volume Shadow Copy Service (VSS) shadow copies. Without options it creates a new shadow copy set; related built-in tool is `vssadmin`.

## simple description

> ### 2026-11-21 Claude said
> vshadow.exe creates, lists, exposes and deletes volume shadow copies (point-in-time snapshots of a disk). Admins and developers use it to test backups and VSS writers. It ships with the Windows SDK, not with Windows itself. It needs administrator rights.
>
> **SOC NOTE**: High-value LOLBin-style tool: `vshadow -nw -p C:` plus `-el` or copying from `%VSHADOW_DEVICE_1%` lets attackers read locked files such as `NTDS.dit` and `SAM` (MITRE ATT&CK T1003.002/.003), and `-exec` runs arbitrary programs (T1218-style proxy execution). `-da`/`-do` delete shadow copies (T1490 Inhibit System Recovery, common in ransomware). Look for VSS event IDs and vshadow process creation.
>

# purpose

Creates and manages shadow copies: create, import, query, delete, break, expose, list writers, restore, revert and LUN resync.

# typical use cases

| usage | description |
| --- | --- |
| `vshadow -p -nw -script=SETVAR1.cmd c:` | Create a persistent shadow copy of C: without writers and write its device to a script. |
| `vshadow -nw -exec=c:\enum.cmd -script=setvar1.cmd c:` | Create a non-persistent shadow copy and run a script against it before exit. |
| `vshadow -q` | List all shadow copies. |
| `vshadow -el={GUID},x:` | Expose a persistent shadow copy as drive X:. |
| `vshadow -ws` | List VSS writer status. |
| `vshadow -da` | Delete all shadow copies. |

# options

| option | description |
| --- | --- |
| `-ad` | Differential hardware shadow copies; exclusive with `-ap` (server only). |
| `-ap` | Plex hardware shadow copies; exclusive with `-ad` (server only). |
| `-bc=File.xml` | Non-transportable shadow copies; stores the Backup Components Document in the file (server only). |
| `-exec=<Command>` | Runs a command or CMD file after shadow copies are created, before VShadow exits; no parameters allowed. |
| `-forcerevert` | Complete the operation only if all disk signatures can be reverted (server only). |
| `-mask` | Mask shadow copy LUNs from the computer when the set is broken (server only). |
| `-nar` | Shadow copies without auto-recovery. |
| `-norevert` | Do not revert disk signatures (server only). |
| `-nw` | Shadow copies without writer participation; exclusive with `-wi`/`-wx`. |
| `-p` | Persistent shadow copies (server only). |
| `-rw` | Make shadow copy LUNs read/write when the set is broken (server only). |
| `-scsf` | Client-accessible shadow copies (server only). |
| `-script=File.cmd` | Generate a CMD file with environment variables for shadow copy IDs and set IDs. |
| `-t=File.xml` | Transportable shadow copies; stores the Backup Components Document in the file. |
| `-tr` | Enforce TxF recovery during creation (server only). |
| `-tracing` | Verbose output for troubleshooting. |
| `-wait` | Wait for user confirmation before exiting. |
| `-wi=<Writer>` | Verify a writer or component is included. |
| `-wx=<Writer>` | Verify a writer or component is excluded. |
| `-i=File.xml` | Import a transportable shadow copy set (server only). |
| `-q` | List properties of all shadow copies. |
| `-qx=<ShadowCopySetId>` | List properties of all shadow copies in a set. |
| `-s=<ShadowCopyId>` | List properties of one shadow copy. |
| `-da` | Delete all shadow copies (requires confirmation). |
| `-do` | Delete the oldest shadow copy. |
| `-dx=<ShadowCopySetId>` | Delete all shadow copies in a set. |
| `-ds=<ShadowCopyId>` | Delete one shadow copy. |
| `-b=<ShadowCopySetId>` | Break a set into stand-alone read-only volumes (server only). |
| `-bw=<ShadowCopySetId>` | Break a set into stand-alone writable volumes (server only). |
| `-bex` | Break a set using BreakSnapshotSetEx with `-mask`, `-rw`, `-forcerevert`, `-norevert` (server only). |
| `-el=<ShadowCopyId>,<Dir or DriveLetter>` | Expose a persistent shadow copy locally as a mounted folder or drive letter. |
| `-er=<ShadowCopyId>,<ShareName>[,<Path>]` | Expose a shadow copy (or subtree) as a read-only share. |
| `-ws` | List VSS writers and their state. |
| `-wm` | Summary of writer metadata. |
| `-wm2` | All writer metadata. |
| `-wm3` | All writer metadata in raw XML. |
| `-r=File.xml` | Perform a restore. |
| `-rs=File.xml` | Perform a simulated restore. |
| `-revert=<ShadowCopyId>` | Revert a volume to a previous shadow copy (server only). |
| `-addresync=<ShadowCopyId>[,<Drive>]` | Add volumes to a LUN resynchronization (server only). |
| `-resync=<BCDFileName>` | Start LUN resynchronization (server only). |
| `-revertsig` | After resync, target LUN signatures match the original LUN (server only). |
| `-novolcheck` | Do not check for unselected volumes overwritten by resync (server only). |
