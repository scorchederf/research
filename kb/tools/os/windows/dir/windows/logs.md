---
created: 2026-11-21
fullpath: 'C:\Windows\Logs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - logs
aliases:
  - "%windir%\\Logs"
  - "%SystemRoot%\\Logs"
url:
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/deployment-troubleshooting-and-log-files?view=windows-11
  - https://learn.microsoft.com/troubleshoot/windows-server/installing-updates-features-roles/fix-windows-update-errors
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/troubleshoot-cbs-component-store-corruption-azure-vm
---

**fullpath**: C:\Windows\Logs

# description

Windows directory (`%windir%\Logs`) that holds text log files written by operating-system servicing components. Microsoft Learn documents its `CBS` subfolder (Component Based Servicing, also used by SFC and DISM repair) and `DISM` subfolder (Deployment Image Servicing and Management). Related servicing logs live elsewhere, such as `%windir%\servicing\sessions\Sessions.xml` and `%windir%\panther`.

## simple description

> ### 2026-11-21 Claude said
> C:\Windows\Logs is where Windows keeps plain-text logs from built-in maintenance tools. The best known are CBS\CBS.log (Windows Update, roles/features, sfc /scannow) and DISM\dism.log; other subfolders can include WindowsUpdate, MoSetup, SIH, waasmedic, NetSetup and SystemRestore depending on the Windows version. Administrators read these when updates or repairs fail.
>
> **SOC NOTE**: Useful timeline source: CBS/DISM logs record when features or packages were added or removed (e.g. enabling Telnet, SMBv1 or RSAT, or tampering with Defender components), which attackers sometimes do (T1562.001). Deleting or truncating these logs is an anti-forensics signal (T1070). Some malware drops files in this directory because it is writable by SYSTEM and rarely inspected.
>

# purpose

Central location for servicing logs. DISM.log is the primary log for all online and offline DISM actions and points to CBS.log for details; CBS.log records servicing failures related to Windows Updates or roles and features, plus the results of DISM integrity scans and SFC repairs.

# common files found

| file | description |
| --- | --- |
| `CBS\CBS.log` | Current Component Based Servicing log; secondary log for online servicing failures, DISM repair results and SFC (`[SR]`) entries. |
| `CBS\CBS.persist.log` | Persisted CBS log written by the DISM tool. |
| `CBS\CbsPersist_*.log` / `CbsPersist_*.cab` | Archived CBS logs. |
| `DISM\dism.log` | Primary log for all DISM actions; location can be changed with `/LogPath` and detail with `/LogLevel`. |
