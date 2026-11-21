---
created: 2026-11-21
fullpath: 'C:\Windows\System32\lsass.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lsass
  - authentication
  - credentials
aliases:
  - lsass.exe
  - Lsass.exe
  - LSASS
  - Local Security Authority Subsystem Service
  - Local Security Authority Server Service
url:
  - https://learn.microsoft.com/windows-server/security/windows-authentication/credentials-processes-in-windows-authentication
  - https://learn.microsoft.com/windows-server/administration/performance-tuning/role/active-directory-server/memory-usage-considerations
  - https://learn.microsoft.com/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-lsa
  - https://learn.microsoft.com/windows/win32/secauthn/lsa-mode-initialization
---

**fullpath**:C:\Windows\System32\lsass.exe

# description

`Lsass.exe` is the Local Security Authority Subsystem Service (LSASS), the protected Windows system process that authenticates and logs users on to the local computer and enforces local security policy. It hosts the LSA, NetLogon, SAM service, Kerberos, NTLM, SSL and other authentication packages, and on domain controllers also the Active Directory database services (NTDSAI.dll/ESE).

## simple description

> ### 2026-11-21 Claude said
> lsass.exe is the core Windows process that checks passwords and logs users on. It talks to the local SAM database or a domain controller to validate accounts, and keeps logon credentials in memory so users can reach network resources without retyping passwords. There is exactly one instance, running as SYSTEM, started by wininit.exe from C:\Windows\System32. Killing it forces a reboot.
>
> **SOC NOTE**: Prime credential-theft target (MITRE ATT&CK T1003.001 LSASS Memory): Mimikatz, procdump/comsvcs.dll MiniDump, Task Manager dumps. Watch for non-standard processes opening handles to lsass (Sysmon Event 10 with GrantedAccess like 0x1010/0x1FFFFF), lsass.dmp files, malicious SSP/AP DLLs loaded into it (T1547.005), and fake lsass.exe outside System32 or with the wrong parent. Enable RunAsPPL and Credential Guard.
>

# purpose

LSA validates users either against the local Security Accounts Manager (SAM) database or by contacting the issuing domain authority. LSASS stores credentials in memory for active sessions (reversibly encrypted plaintext, Kerberos TGTs and service tickets, NT hash, LM hash) and manages LSA secrets persisted on disk. At startup it loads all registered security support provider/authentication package (SSP/AP) DLLs into its process space. Since Windows 8.1 it can run as a protected process (PPL) to block memory reads and code injection, configured via `HKLM\SYSTEM\CurrentControlSet\Control\Lsa` or the `ConfigureLsaProtectedProcess` policy (0 disabled, 1 enabled with UEFI lock, 2 enabled without UEFI lock). On DCs it handles AD lookups, authentication and replication, and its memory grows with AD usage.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
