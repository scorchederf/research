---
created: 2026-11-21
fullpath: 'c:\windows\system32\comsvcs.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - dll
  - com+
  - lolbin
aliases:
  - comsvcs.dll
  - COM+ Services
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/2005/ms05-051
  - https://learn.microsoft.com/security-updates/securitybulletins/2005/ms05-052
  - https://learn.microsoft.com/security-updates/securitybulletins/2006/ms06-018
---

**fullpath**:c:\windows\system32\comsvcs.dll

# description

comsvcs.dll is a COM+ Services system library. Learn references it only in security bulletins: it was updated by MS05-051 and MS06-018 (COM+/MSDTC fixes, alongside Comadmin.dll, Comrepl.dll, Comuid.dll, Es.dll and Msdtc*.dll), and MS05-052 set the Internet Explorer kill bit for its COM object CLSID `ECABAFC2-7F19-11D2-978E-0000F8757E2A`.

## simple description

> ### 2026-11-21 Claude said
> comsvcs.dll implements COM+ services, the Windows framework for running and managing component-based applications and transactions. It is loaded by many system processes and is a legitimate, signed Microsoft DLL. Users never interact with it directly.
>
> **SOC NOTE**: Infamous LOLBin for LSASS dumping (MITRE T1003.001 OS Credential Dumping: LSASS Memory): `rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump <lsass PID> C:\temp\out.dmp full`. Attackers obfuscate the export as `#24`. Alert on rundll32 command lines referencing comsvcs and MiniDump/#24, on handles to lsass with PROCESS_VM_READ from rundll32, and on new .dmp files.
>

# purpose

Provides COM+ services functionality. Learn documents only its inclusion in COM+ security updates and that one of its COM objects was kill-bitted in Internet Explorer.
