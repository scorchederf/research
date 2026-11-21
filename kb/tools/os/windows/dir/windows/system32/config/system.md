---
created: 2026-11-21
fullpath: 'C:\Windows\System32\config\SYSTEM'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - registry
aliases:
  - SYSTEM
  - System hive
url:
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
  - https://learn.microsoft.com/windows/win32/vss/registry-backup-and-restore-operations-under-vss
---

**fullpath**:C:\Windows\System32\config\SYSTEM

# description

The SYSTEM file is the supporting file (a complete copy of the hive data) for the `HKEY_LOCAL_MACHINE\System` registry hive, which also backs `HKEY_CURRENT_CONFIG`. It lives in `%SystemRoot%\System32\Config` with System.log (transaction log), System.alt (backup copy, only the System hive has one) and System.sav. Its file location is listed under `HKLM\System\CurrentControlSet\Control\hivelist`.

## simple description

> ### 2026-11-21 Claude said
> This file is the on-disk copy of the HKLM\SYSTEM registry hive. It stores machine configuration such as services and drivers, control sets, network interfaces, mounted devices, USB history and the boot key used to protect password hashes. Windows keeps it locked while running.
>
> **SOC NOTE**: Attackers copy SYSTEM together with SAM/SECURITY (e.g. `reg save HKLM\SYSTEM`, VSS shadow copies, or CVE-2021-36934 HiveNightmare) to extract the boot key and dump local hashes and LSA secrets offline (MITRE ATT&CK T1003.002 / T1003.004). Forensically it yields services, USB devices, ShimCache (AppCompatCache), timezone, computer name and network data.
>

# purpose

Persists the HKLM\System hive across boots. If it is missing or corrupt Windows may fail to start with errors such as "Windows could not start because the following file is missing or corrupt: \WINNT\SYSTEM32\CONFIG\SYSTEM". The VSS registry writer saves the active hive files listed under `hivelist` before shadow copy.
