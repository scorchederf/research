---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\MountedDevices'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - storage
  - mount-manager
aliases:
  - 'MountedDevices'
  - 'Mount manager persistent name database'
url:
  - https://learn.microsoft.com/windows-hardware/drivers/storage/supporting-mount-manager-requests-in-a-storage-class-driver
  - https://learn.microsoft.com/troubleshoot/windows-server/backup-and-storage/restore-system-boot-drive-letter
---

**fullpath**: HKLM\SYSTEM\MountedDevices

# description

The mount manager's persistent name database in the SYSTEM hive. It stores unique volume names (`\??\Volume{GUID}`), drive letters (`\DosDevices\X:`) and mount point names, each as a registry value whose data is the volume's unique ID. Learn documents renaming `\DosDevices\` values to restore a system or boot drive letter.

## simple description

> ### 2026-11-21 Claude said
> MountedDevices remembers which drive letter and volume GUID belong to which disk or partition, so drive letters stay the same across reboots. Every volume ever attached (including USB sticks) gets an entry. The data of each value identifies the device, for example a disk signature plus offset or a device path string.
>
> **SOC NOTE**: Key USB/removable-media artifact (T1052.001, T1091): \DosDevices\ and Volume{GUID} values link drive letters and volume GUIDs to device IDs (data often contains `_??_USBSTOR#Disk&Ven_...` with serial). Correlate with USBSTOR, MountPoints2 in NTUSER.DAT, and Partition/Diagnostic event 1006 to show which user mounted which device.
>

# purpose

Maintains persistent symbolic link names (unique volume names, drive letters, mount points) for volumes so names persist across reboots.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

| value name | type | description |
| --- | --- | --- |
| `\??\Volume{GUID}` | REG_BINARY | Unique volume name; data is the volume's unique ID. |
| `\DosDevices\<letter>:` | REG_BINARY | Drive letter mount point; shares the unique ID of the volume it points to. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\MountedDevices"` | List the key's values. |
