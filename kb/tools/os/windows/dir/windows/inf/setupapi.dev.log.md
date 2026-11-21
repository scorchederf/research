---
created: 2026-11-21
fullpath: 'C:\Windows\inf\setupapi.dev.log'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - log
  - drivers
aliases:
  - setupapi.dev.log
  - SetupAPI.dev.log
  - device installation text log
url:
  - https://learn.microsoft.com/windows-hardware/drivers/install/setupapi-device-installation-log-entries
  - https://learn.microsoft.com/windows-hardware/drivers/install/setupapi-text-logs
  - https://learn.microsoft.com/windows-hardware/drivers/install/setupapi-logging--windows-vista-and-later-
  - https://learn.microsoft.com/windows-hardware/drivers/install/troubleshooting-driver-signing-installation
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-setup-log-files-and-event-logs?view=windows-11
  - https://learn.microsoft.com/windows-hardware/drivers/install/setting-setupapi-logging-levels
---

**fullpath**:C:\Windows\inf\setupapi.dev.log

# description

SetupAPI.dev.log is the SetupAPI device installation text log, used in Windows Vista and later. The Plug and Play (PnP) manager and SetupAPI write entries to it about device and driver installations; its companion SetupAPI.app.log records application installation operations. It is an ANSI plain-text file in English located by default in `%SystemRoot%\inf`.

## simple description

> ### 2026-11-21 Claude said
> setupapi.dev.log is a plain-text log where Windows records every device and driver installation. Each time a new device is plugged in or a driver is installed, Windows appends a section with timestamps, the device ID and the driver used. It is mainly used to troubleshoot driver problems, but it keeps a long history.
>
> **SOC NOTE**: It is a key forensic artifact for USB/removable media history (T1052, T1091): the first-install timestamp for a device (`Device Install (Hardware initiated) - USBSTOR\...`) shows when a USB drive was first connected, correlating with `SYSTEM\CurrentControlSet\Enum\USBSTOR`. It also reveals malicious or unsigned driver installs (BYOVD, T1068/T1543.003) via `!!!` failure lines and signer info.
>

# purpose

Provides information to verify the installation of a device and troubleshoot device installation problems, including driver signing problems. The log consists of a text log header (OS and architecture info) followed by text log sections, each recording the events of a single device installation. A single `!` in the left column is a warning; `!!!` indicates a failure. Driver installation information is appended to the file; if the file is renamed before an install, a new log file is generated. Logging levels are controlled by `HKLM\Software\Microsoft\Windows\CurrentVersion\Setup\LogLevel`.
