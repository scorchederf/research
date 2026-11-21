---
created: 2026-11-21
fullpath: 'C:\Windows\System32\config\SECURITY'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - registry
  - hive
  - lsa
aliases:
  - SECURITY
  - Security hive
url:
  - https://learn.microsoft.com/windows/win32/sysinfo/registry-hives
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/remotely-edit-the-registry
---

**fullpath**:C:\Windows\System32\config\SECURITY

# description

`SECURITY` is the supporting file of the `HKEY_LOCAL_MACHINE\Security` registry hive, stored in `%SystemRoot%\System32\Config` with companion `Security.log` and `Security.sav` files. It uses the standard (older) hive format for compatibility.

## simple description

> ### 2026-11-21 Claude said
> This file is the on-disk copy of the HKLM\SECURITY registry hive. It holds the Local Security Authority's (LSA) secrets, cached domain logon credentials and security policy. Windows locks it while running and even admins can't read the live key without SYSTEM rights. It can be loaded into Registry Editor offline via Load Hive.
>
> **SOC NOTE**: Prime credential-theft target: together with SYSTEM (boot key), it yields LSA secrets (service account passwords, machine account key) and cached domain credentials (DCC2) - MITRE T1003.004 and T1003.005. Watch for `reg save HKLM\SECURITY`, shadow-copy access to `config\SECURITY`, or copies in temp/staging folders.
>

# purpose

Persistent storage for the Security hive, loaded into memory at startup. The `.log` file is a transaction log of changes and `.sav` is a backup copy; the hive can be loaded offline in Regedit via File > Load Hive.


