---
created: 2026-11-21
fullpath: 'C:\Windows\Temp'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Temp
  - "%WINDIR%\\Temp"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/shell-experience/temp-folder-with-logon-session-id-deleted
  - https://learn.microsoft.com/answers/a/2002602
  - https://learn.microsoft.com/answers/a/8074735
---

**fullpath**:C:\Windows\Temp

# description

C:\Windows\Temp (`%WINDIR%\Temp`) is the system-wide temporary folder. It is one of the folders cleaned by Disk Cleanup (cleanmgr.exe) via the `Temporary Files` VolumeCaches handler, whose default `Folder` value is `%TEMP%|%WINDIR%\Temp|%WINDIR%\Logs|%WINDIR%\System32\LogFiles`, governed by the `LastAccess` value (default 7 days).

## simple description

> ### 2026-11-21 Claude said
> C:\Windows\Temp is the temporary folder used by Windows itself, services and programs running as SYSTEM, installers and updates (each user has a separate %TEMP% in their profile). It fills with logs, extracted setup files and leftovers that are usually safe to delete. Normal users can create files there but generally can't read others' files. Disk Cleanup and Storage Sense clean it periodically.
>
> **SOC NOTE**: Because SYSTEM-level tools and services write here, attackers stage payloads, scripts and dumps in C:\Windows\Temp, e.g. PsExec-style service binaries, lsass dumps and ransomware tools (MITRE ATT&CK T1074.001 Local Data Staging, T1036). Executables or DLLs created or run from this folder, particularly by services.exe or remote admin tools, deserve attention; MFT and $UsnJrnl timestamps help even after cleanup.
>

# purpose

Holds temporary files created by the operating system, services and installers running in system context; cleaned by Disk Cleanup and Storage Sense.

# common files found

- tmpxxxxxxx folders created by system processes (often only accessible to SYSTEM)
- Installer and update logs and extracted setup files
- Files in use by running processes that cannot be deleted
