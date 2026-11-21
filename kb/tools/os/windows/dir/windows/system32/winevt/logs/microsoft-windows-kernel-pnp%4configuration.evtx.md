---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-PnP%4Configuration.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - pnp
  - forensics
aliases:
  - "Microsoft-Windows-Kernel-PnP%4Configuration.evtx"
  - "Microsoft-Windows-Kernel-PnP/Configuration"
url: []
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-PnP%4Configuration.evtx

# description

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> This is the event log file for the Microsoft-Windows-Kernel-PnP/Configuration channel, shown in Event Viewer under Applications and Services Logs > Microsoft > Windows > Kernel-PnP > Configuration. The Plug and Play manager writes an entry each time a device is configured or a driver is installed or started for it (for example event IDs 400, 410 and 420). Events include the device instance ID (e.g., USB\VID_xxxx&PID_xxxx\serial), the driver name and INF used.
>
> **SOC NOTE**: Useful for USB/removable media forensics (T1052 / T1091) and rogue hardware: event 400/410 show when a device was first configured and which driver loaded, including the device serial number. It complements setupapi.dev.log and the USBSTOR/Enum registry keys, and it can reveal malicious or vulnerable driver installs (BYOVD).
>
> _Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
