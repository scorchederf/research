---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - usb
  - pnp
  - forensics
aliases:
  - USBSTOR
url:
  - https://learn.microsoft.com/windows-hardware/drivers/install/identifiers-generated-by-usbstor-sys
  - https://learn.microsoft.com/windows-hardware/drivers/usbcon/supported-usb-classes
  - https://learn.microsoft.com/windows-hardware/drivers/storage/device-object-example-for-a-usb-mass-storage-device
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR

# description

Plug and Play enumeration key for devices enumerated by the USB storage port driver `Usbstor.sys`. Subkeys are named after the device IDs `USBSTOR\v(8)p(16)r(4)` that Usbstor.sys builds from the device's SCSI inquiry data.

## simple description

> ### 2026-11-21 Claude said
> Every USB flash drive or external disk plugged into the PC gets an entry here, named after its vendor, product and revision, with a subkey per device instance (usually the serial number). Windows creates these entries when the USB storage driver sets up the device. The entries usually stay even after the device is removed.
>
> **SOC NOTE**: Core artifact for removable-media investigations (MITRE T1052.001 Exfiltration over USB, T1091 Replication Through Removable Media). Instance subkeys give serial numbers, FriendlyName and first/last connection times (via Properties); correlate with MountedDevices, SetupAPI.dev.log and Partition/Diagnostic Event 1006.
>

# purpose

Holds device instances for USB mass storage logical units. Usbstor.sys creates a PDO for each logical unit (up to 16) and reports device IDs like `USBSTOR\SEAGATE_ST39102LW_______0004`, hardware IDs such as `USBSTOR\DiskSEAGATE_ST39102LW_______0004` and `USBSTOR\GenDisk`, and compatible IDs `USBSTOR\Disk` and `USBSTOR\RAW`.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# subkeys

| subkey | description |
| --- | --- |
| `<t*><v(8)><p(16)><r(4)>` | Device ID built from SCSI device type, 8-character vendor, 16-character product and 4-character revision. |

## SCSI device types

| SCSI type code | device type | generic type |
| --- | --- | --- |
| DIRECT_ACCESS_DEVICE (0) | Disk or SFloppy | GenDisk or GenSFloppy |
| SEQUENTIAL_ACCESS_DEVICE (1) | Sequential | GenSequential |
| WRITE_ONCE_READ_MULTIPLE_DEVICE (4) | Worm | GenWorm |
| READ_ONLY_DIRECT_ACCESS_DEVICE (5) | CdRom | GenCdRom |
| OPTICAL_DEVICE (7) | Optical | GenOptical |
| MEDIUM_CHANGER (8) | Changer | GenChanger |
| Default | Other | UsbstorOther |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR" /s` | List all USB storage devices and instance values recursively. |
