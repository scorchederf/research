---
created: 2026-11-21
fullpath: 'C:\Windows\Logs\CBS\CBS.log'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - log
  - servicing
aliases:
  - 'CBS.log'
  - 'Component-Based Servicing log'
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/installing-updates-features-roles/cbs-log-file-record-entries-not-repaired-run-sfc
  - https://learn.microsoft.com/troubleshoot/windows-client/installing-updates-features-roles/common-windows-update-errors
  - https://learn.microsoft.com/troubleshoot/windows-server/installing-updates-features-roles/fix-windows-update-errors
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/troubleshoot-windows-update-azure-vm
---

**fullpath**: C:\Windows\Logs\CBS\CBS.log

# description

The Component-Based Servicing (CBS) log. The Windows Modules Installer service (TrustedInstaller) writes to it when installing optional features, updates and service packs, and Sfc.exe writes details of each verify and repair operation (tagged `[SR]`). Archived logs are kept as `CbsPersist_*.log` / `.cab` files in the same folder; DISM.log points to it for details.

## simple description

> ### 2026-11-21 Claude said
> CBS.log is the main log for Windows servicing: installing updates, adding or removing Windows features, and repairing system files with SFC or DISM. It is a plain text file that grows and is periodically compressed into CbsPersist archives. Administrators read it to find why an update failed or which system file is corrupt.
>
> **SOC NOTE**: Useful timeline evidence for update/feature changes: shows when features (e.g., Telnet, SMB1, OpenSSH, RSAT) were enabled or packages removed, which attackers may do to enable tooling or weaken defenses (T1562). SFC [SR] lines reveal tampered/replaced protected system binaries (possible T1036/T1574). Old entries roll into CbsPersist_*.cab.
>

# purpose

Records servicing operations and failures related to Windows Updates, roles and features, and System File Checker scans.

# typical use cases

| usage | description |
| --- | --- |
| `findstr /c:"[SR]" %windir%\logs\cbs\cbs.log >sfcdetails.txt` | Extract System File Checker entries. |
| `Get-Content "C:\Windows\Logs\CBS\CBS.log" -Tail 200 \| Select-String "Error\|CORRUPT\|MISSING"` | Find recent errors and corruption entries. |
| `Dism.exe /Online /Cleanup-Image /Restorehealth` | Repair component store; results are logged to CBS.log. |
