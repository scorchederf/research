---
created: 2026-11-21
fullpath: 'C:\Windows\System32\diskpart.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - diskpart.exe
  - diskpart
  - DiskPart
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart
  - https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart-scripts-and-examples
---

**fullpath**:C:\Windows\System32\diskpart.exe

# description

The diskpart command interpreter manages a computer's drives: disks, partitions, volumes and virtual hard disks (VHDs). You list and select an object to give it focus, and subsequent commands act on that object. It requires membership in the local Administrators group (or equivalent).

## simple description

> ### 2026-11-21 Claude said
> Diskpart is Windows' built-in command-line tool for managing disks, partitions and volumes. You select a disk, partition or volume first, then run commands against it, such as create, format, assign a drive letter, or clean (wipe) it. It can also mount virtual hard disk files (VHD/VHDX) and run a list of commands from a script file. It needs administrator rights and is mostly used during Windows installs and by admins.
>
> **SOC NOTE**: Ransomware and wiper malware sometimes use diskpart to destroy data or break recovery (MITRE ATT&CK T1561 disk wipe, T1490 inhibit system recovery), for example `clean` on a disk or deleting recovery partitions. Attackers may also mount hidden volumes or VHD files to stage tools. Diskpart running on servers or user workstations outside normal admin activity, especially with `/s` and a script file, should be investigated, and the script file contents preserved.
>

# purpose

- Create, delete, extend, shrink and format partitions and volumes.
- Assign or remove drive letters and mount points.
- Attach, detach, expand, compact and merge VHDs.
- Script disk setup for unattended deployment (`diskpart /s`); allow ~15 seconds between consecutive scripts.

# typical use cases

| usage | description |
| --- | --- |
| `list disk`, `select disk 1`, `create partition primary`, `format fs=ntfs label=Backup quick` | Interactive. |
| `diskpart /s scriptname.txt` | Run a script. |
| `diskpart /s scriptname.txt > logfile.txt` | Script with logging. |
| — | Example script: wipe disk 0, convert to GPT, create a 300 MB WinRE partition and assign letter T. |

# options

| option    | description    |
| --- | --- |
| `active` | Marks the disk's partition with focus as active. |
| `add` | Mirrors the simple volume with focus to the specified disk. |
| `assign` | Assigns a drive letter or mount point to the volume with focus. |
| `attach vdisk` | Attaches (mounts) a VHD so it appears as a local hard disk drive. |
| `attributes` | Displays, sets, or clears the attributes of a disk or volume. |
| `automount` | Enables or disables the automount feature. |
| `break` | Breaks the mirrored volume with focus into two simple volumes. |
| `clean` | Removes any and all partition or volume formatting from the disk with focus. |
| `compact vdisk` | Reduces the physical size of a dynamically expanding VHD file. |
| `convert` | Converts FAT and FAT32 volumes to NTFS, leaving files and directories intact. |
| `create` | Creates a partition on a disk, a volume on one or more disks, or a VHD. |
| `delete` | Deletes a partition or a volume. |
| `detach vdisk` | Stops the selected VHD from appearing as a local hard disk drive. |
| `detail` | Displays information about the selected disk, partition, volume, or VHD. |
| `exit` | Exits the diskpart command interpreter. |
| `expand vdisk` | Expands a VHD to the size you specify. |
| `extend` | Extends the volume or partition with focus, and its file system, into free space. |
| `filesystems` | Displays the current and supported file systems for the volume with focus. |
| `format` | Formats a disk to accept files. |
| `gpt` | Assigns gpt attribute(s) to the partition with focus on basic GPT disks. |
| `help` | Displays available commands or detailed help on a command. |
| `import` | Imports a foreign disk group into the local computer's disk group. |
| `inactive` | Marks the system or boot partition with focus as inactive on basic MBR disks. |
| `list` | Displays a list of disks, partitions, volumes, or VHDs. |
| `merge vdisk` | Merges a differencing VHD with its parent VHD. |
| `offline` | Takes an online disk or volume offline. |
| `online` | Takes an offline disk or volume online. |
| `recover` | Refreshes disk group state, recovers disks in an invalid group, and resyncs stale mirrored/RAID-5 volumes. |
| `rem` | Adds comments to a script. |
| `remove` | Removes a drive letter or mount point from a volume. |
| `repair` | Repairs the RAID-5 volume with focus by replacing the failed disk region. |
| `rescan` | Locates new disks added to the computer. |
| `retain` | Prepares a dynamic simple volume to be used as a boot or system volume. |
| `san` | Displays or sets the SAN policy for the operating system. |
| `select` | Shifts the focus to a disk, partition, volume, or VHD. |
| `set id` | Changes the partition type field for the partition with focus. |
| `shrink` | Reduces the size of the selected volume by the amount you specify. |
| `uniqueid` | Displays or sets the GPT identifier or MBR signature for the disk with focus. |
| `/s <scriptname>` | (Command line) Runs a diskpart script file; redirect output with `> logfile.txt`. |
