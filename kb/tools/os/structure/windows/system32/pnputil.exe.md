---
created: 2026-11-21
fullpath: 'C:\Windows\system32\pnputil.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - drivers
aliases:
  - pnputil.exe
  - PnPUtil
url:
  - https://learn.microsoft.com/windows-hardware/drivers/devtest/pnputil
  - https://learn.microsoft.com/windows-hardware/drivers/devtest/pnputil-command-syntax
  - https://learn.microsoft.com/windows-hardware/drivers/devtest/pnputil-examples
  - https://learn.microsoft.com/windows-server/administration/windows-commands/pnputil
---

**fullpath**:C:\Windows\system32\pnputil.exe

# description

PnPUtil is a command line tool for managing Windows driver packages and devices: add, install, delete, export and enumerate driver packages in the driver store, and enable/disable/restart/remove/scan devices. It is included in `%windir%\system32` in every version of Windows since Vista; there is no separate download.

## simple description

> ### 2026-11-21 Claude said
> PnPUtil is the built-in command-line tool to manage drivers and Plug and Play devices. Admins use it to add drivers to the driver store, install them, list them, or remove them. Newer versions can also enable, disable, restart and list devices. Most commands need an elevated prompt.
>
> **SOC NOTE**: Attackers can use it to stage a malicious or vulnerable signed driver (BYOVD, T1068/T1014) with `/add-driver ... /install`, or to disable security-related devices. Hunt for process creation (4688/Sysmon 1) with `/add-driver` or `/disable-device`, new oem#.inf files in C:\Windows\INF, and setupapi.dev.log entries.
>

# purpose

Manage driver packages in the driver store and Plug and Play devices from the command line or scripts.

# typical use cases

- Add and install a driver package: `pnputil /add-driver x:\driver.inf /install`
- Enumerate third-party drivers: `pnputil /enum-drivers`
- Export all drivers for backup: `pnputil /export-driver * c:\backup`
- Delete a driver: `pnputil /delete-driver oem0.inf /force`
- Enumerate devices with problems: `pnputil /enum-devices /problem`

# options

| option    | description    |
| --- | --- |
| `/add-driver <filename.inf \| *.inf> [/subdirs] [/install] [/reboot]` | Adds driver package(s) into the driver store; `/subdirs` traverses subfolders, `/install` installs on matching devices (Windows 10 1607+). |
| `/delete-driver <oem#.inf> [/uninstall] [/force] [/reboot]` | Deletes a driver package from the driver store; `/uninstall` removes it from devices, `/force` deletes even if in use. |
| `/export-driver <oem#.inf \| *> <target directory>` | Exports driver package(s) from the driver store into a target directory. |
| `/enum-drivers [/class <name \| GUID>] [/files]` | Enumerates all third-party driver packages in the driver store, optionally filtered by class or listing files. |
| `/disable-device [<instance ID> \| /deviceid <device ID>] [/class] [/bus] [/reboot] [/force]` | Disables devices on the system (Windows 10 2004+). |
| `/enable-device [<instance ID> \| /deviceid <device ID>] [/class] [/bus] [/reboot]` | Enables devices on the system (Windows 10 2004+). |
| `/restart-device [<instance ID> \| /deviceid <device ID>] [/class] [/bus] [/reboot]` | Restarts devices on the system (Windows 10 2004+). |
| `/remove-device [<instance ID> \| /deviceid <device ID>] [/class] [/bus] [/subtree] [/reboot] [/force]` | Attempts to remove a device from the system; `/subtree` removes child devices too. |
| `/scan-devices [/instanceid <instance ID>] [/async]` | Scans the system for device hardware changes. |
| `/enum-devices [filters and display flags]` | Enumerates all devices, with filters (`/connected`, `/disconnected`, `/class`, `/problem`, `/bus`, ...) and display flags (`/drivers`, `/stack`, `/properties`, `/resources`, ...). |
| `/enum-devicetree [root instance ID] [/connected] [/services] [/stack] [/drivers] [/interfaces]` | Enumerates the device tree (Windows 11 23H2+). |
| `/enum-interfaces [/enabled \| /disabled] [/class <GUID>] [/properties]` | Enumerates all device interfaces on the system. |
| `/enum-classes [/class <name \| GUID>] [/services]` | Enumerates all device classes (Windows 11 22H2+). |
| `/enum-containers [...] [/format <txt \| xml \| csv>] [/output-file [<filename>]]` | Enumerates all device containers (Windows 11 23H2+). |
| `/?` | Displays the command-line syntax. |
| `-a [-i] <filename.inf>` | Legacy; maps to `/add-driver <filename.inf> [/install]`. |
| `-d [-f] <oem#.inf>` | Legacy; maps to `/delete-driver <oem#.inf> [/force]`. |
| `-e` | Legacy; maps to `/enum-drivers`. |
