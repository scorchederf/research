---
created: 2026-11-21
fullpath: 'C:\Windows\Sysmon64.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - sysmon
  - sysinternals
  - logging
aliases:
  - "Sysmon64.exe"
  - "Sysmon"
  - "System Monitor"
url:
  - https://learn.microsoft.com/sysinternals/downloads/sysmon
  - https://learn.microsoft.com/windows-server/administration/windows-commands/sysmon
  - https://learn.microsoft.com/windows/security/operating-system-security/sysmon/how-to-enable-sysmon
---

**fullpath**:C:\Windows\Sysmon64.exe

# description

System Monitor (Sysmon) is a Windows system service and device driver that, once installed, stays resident across reboots to monitor and log system activity such as process creations, network connections and file creation time changes to the Windows event log. It is a Sysinternals tool (Sysmon64.exe is the 64-bit build) and, starting February 2026, is also available as a built-in optional Windows 11 feature.

## simple description

> ### 2026-11-21 Claude said
> Sysmon is a free Microsoft Sysinternals tool that adds detailed security telemetry to Windows. When installed with `-i`, Sysmon64.exe copies itself to C:\Windows and runs as the Sysmon64 service with the SysmonDrv driver. Events go to Applications and Services Logs/Microsoft/Windows/Sysmon/Operational and are filtered by an XML configuration file.
>
> **SOC NOTE**: Sysmon is a primary data source for detection (process create 1, network 3, driver load 6, image load 7, registry 12-14, DNS 22, etc.). Attackers try to unload or reconfigure it (`sysmon -u`, `fltmc unload SysmonDrv`, config tampering) to blind defenders (T1562.001/T1562.006); alert on Sysmon event 16 (config change), service stop, and gaps in Sysmon logs.
>

# purpose

Installs, configures, and uninstalls the Sysmon service and driver, and prints its configuration schema. The driver installs as a boot-start driver to capture early-boot activity; install and uninstall do not require a reboot.

# typical use cases

| usage | description |
| --- | --- |
| `sysmon -accepteula -i` | Install with default settings (SHA1 image hashing, no network monitoring). |
| `sysmon -accepteula -i c:\windows\config.xml` | Install with a configuration file. |
| `sysmon -c` | Dump the current configuration. |
| `sysmon -c c:\windows\config.xml` | Reconfigure an active Sysmon with a configuration file. |
| `sysmon -c --` | Reset the configuration to default settings. |
| `sysmon -s all` | Display all configuration schema versions. |
| `sysmon -u` | Uninstall Sysmon. |

# options

| option | description |
| --- | --- |
| `-i [<configfile>]` | Installs the service and driver, optionally with a configuration file. |
| `-c [<configfile>]` | Updates the configuration of an installed Sysmon driver, or dumps the current configuration if no argument is given. |
| `-m` | Installs the event manifest (also done implicitly on service install). |
| `-s [<schemaversion>]` | Prints the configuration schema definition; `all` dumps all versions, default is latest. |
| `-u [force]` | Uninstalls the service and driver; `force` proceeds even when some components are not installed. |
| `-accepteula` | Automatically accepts the EULA on installation. |
| `-? config` | Displays more information on configuration files. |
