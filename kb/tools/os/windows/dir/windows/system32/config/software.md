---
created: 2026-11-21
fullpath: 'C:\Windows\System32\config\SOFTWARE'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - SOFTWARE
  - SOFTWARE hive
url:
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
  - https://learn.microsoft.com/windows/win32/vss/registry-backup-and-restore-operations-under-vss
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/remotely-edit-the-registry
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/registry-troubleshooting-advanced-users
---

**fullpath**:C:\Windows\System32\config\SOFTWARE

# description

`SOFTWARE` is the supporting hive file for `HKEY_LOCAL_MACHINE\Software`, stored with the other system hives in `%SystemRoot%\System32\Config`. Its companions are `Software.log` (transaction log) and `Software.sav` (backup copy); the mapping is listed under `HKLM\System\CurrentControlSet\Control\hivelist`.

## simple description

> ### 2026-11-21 Claude said
> This file is the on-disk database behind `HKLM\SOFTWARE` in the registry: machine-wide settings for Windows and installed programs. Windows keeps it locked while running, so it cannot simply be copied. Tools load it offline (Registry Editor "Load Hive", forensic tools) or copy it via Volume Shadow Copy. If it is corrupt, Windows may fail to boot.
>
> **SOC NOTE**: The SOFTWARE hive holds many forensic artifacts: installed programs, `HKLM\...\Run` persistence, Image File Execution Options, Winlogon, network profiles, OS install info, AppCompat data. Attackers may dump hives via `reg save` or shadow copies (MITRE ATT&CK T1003.002 focuses on SAM/SECURITY/SYSTEM, but SOFTWARE is often taken alongside). Monitor `reg save HKLM\SOFTWARE`, VSS creation and access to `config\` from unusual processes.
>

# purpose

Supporting file holding a complete copy of the `HKEY_LOCAL_MACHINE\Software` hive data (file with no extension). The registry writer of VSS saves active hive files listed in `hivelist` before shadow copy. Offline, the file can be loaded into another machine's registry with Registry Editor **File > Load Hive** under `HKEY_LOCAL_MACHINE`. A corrupt or missing file produces boot errors such as "Windows could not start because the following file is missing or corrupt: \WINNT\SYSTEM32\CONFIG\SOFTWARE".


