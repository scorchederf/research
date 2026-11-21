---
created: 2026-11-21
fullpath: 'C:\Windows\System32\config\RegBack'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - registry
  - backup
aliases:
  - RegBack
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/installing-updates-features-roles/system-registry-no-backed-up-regback-folder
  - https://learn.microsoft.com/troubleshoot/windows-client/performance/windows-boot-issues-troubleshooting
---

**fullpath**:C:\Windows\System32\config\RegBack

# description

`%SystemRoot%\System32\config\RegBack` is the folder where Windows kept automatic backup copies of the system registry hives. Starting with Windows 10, version 1803 the automatic backup is disabled by design and the hive files appear as 0 KB.

## simple description

> ### 2026-11-21 Claude said
> RegBack holds backup copies of the main registry hive files (SYSTEM, SOFTWARE, SAM, SECURITY, DEFAULT). It was used to recover a PC whose registry got corrupted. On modern Windows 10/11 the files are empty unless an admin turns the backup back on. A scheduled task called RegIdleBackup does the copying.
>
> **SOC NOTE**: If populated, RegBack hives are an older snapshot of the registry, useful for comparing persistence or configuration changes over time, and they include SAM/SECURITY copies attackers could steal for offline credential extraction (MITRE T1003.002). Check file sizes/timestamps and whether `EnablePeriodicBackup` was enabled.
>

# purpose

Stores registry hive backups that can be copied back to `C:\Windows\System32\config` from WinRE when the system hive can't load. To re-enable legacy behavior set `HKLM\System\CurrentControlSet\Control\Session Manager\Configuration Manager\EnablePeriodicBackup` (REG_DWORD) to 1 and restart; Windows then backs up at restart and creates the RegIdleBackup task under Microsoft\Windows\Registry. Microsoft recommends system restore points instead.

# common files found

| file | description |
| --- | --- |
| registry hive files | Each registry hive is still present; 0 KB in size on Windows 10, version 1803 and later unless periodic backup is re-enabled. |
