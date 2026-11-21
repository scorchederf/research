---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - umdf
  - usb
aliases:
  - Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx
  - Microsoft-Windows-DriverFrameworks-UserMode/Operational
  - UMDF Operational log
url:
  - https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-security
  - https://learn.microsoft.com/troubleshoot/windows-client/setup-upgrade-and-drivers/event-id-219-when-device-plugged-in-windows-system
  - https://learn.microsoft.com/windows-hardware/drivers/wdf/how-umdf-handles-driver-failures
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx

# description

This is the on-disk file of the **Microsoft-Windows-DriverFrameworks-UserMode/Operational** event log channel, written by the User-Mode Driver Framework (UMDF), whose kernel component is the reflector WUDFRd.sys and whose drivers run in Wudfhost host processes. It is viewed in Event Viewer or queried with `wevtutil`.

## simple description

> ### 2026-11-21 Claude said
> This log records activity of user-mode drivers - drivers that run outside the kernel, commonly for USB devices such as phones, MTP media players, sensors and some smart card readers. When a device is plugged in or removed, UMDF logs events about loading the driver and the Plug and Play/power operations. It is disabled by default on many Windows versions and must be enabled to collect data.
>
> **SOC NOTE**: Useful for USB device history and removable-media investigations (T1052, T1091, BadUSB): event 2003/2004 (driver load for a device), 2100/2101 (PnP/power operations), 2102 and 2105/2106 (removal), with device instance IDs containing VID/PID and serial. Correlate with Kernel-PnP, Partition/Diagnostic and SetupAPI logs.
>

# purpose

Records UMDF driver host events for devices. Microsoft's Azure Local security reference uses the query `Microsoft-Windows-DriverFrameworks-UserMode/Operational!*[System[(EventID=2004)]]` to "Detect User-Mode drivers loaded - for potential BadUSB detection". Related DriverFrameworks-UserMode events documented on Learn: 10118 (UMDF reflector unable to connect to the Service Control Manager during boot, expected and retried), and when a UMDF driver fails the OS logs 10110 (host process at fault), 10111 (device went offline and was restarted) and 10112 (device went offline and was not restarted).
