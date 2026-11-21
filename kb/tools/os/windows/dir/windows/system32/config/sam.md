---
created: 2026-11-21
fullpath: 'C:\Windows\System32\config\SAM'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - registry-hive
  - credentials
aliases:
  - SAM
  - Security Account Manager database
  - Security Accounts Manager
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/2011/ms11-054
  - https://learn.microsoft.com/windows-server/security/kerberos/system-key-utility-technical-overview
  - https://learn.microsoft.com/windows-server/security/windows-authentication/credentials-processes-in-windows-authentication
---

**fullpath**:C:\Windows\System32\config\SAM

# description

The Security Account Manager (SAM) database file, which stores local user accounts and groups and their password hashes on every Windows system. It is part of the registry; on domain controllers, domain account passwords are stored in directory services (Active Directory) instead. The legacy Syskey utility added encryption of SAM password data but is no longer supported from Windows 10 1607 / Windows Server 2016.

## simple description

> ### 2026-11-21 Claude said
> The SAM file is the registry hive that holds local Windows accounts (like the local Administrator) and their NTLM password hashes. Windows keeps it locked while running, so it can't simply be copied. It is loaded as `HKLM\SAM` and its secrets are encrypted with a key derived from the SYSTEM hive.
>
> **SOC NOTE**: Dumping SAM is credential access (MITRE ATT&CK T1003.002): look for `reg save HKLM\SAM`, `reg save HKLM\SYSTEM`, Volume Shadow Copy access (`\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy*\Windows\System32\config\SAM`), esentutl/ntdsutil abuse, or tools like Mimikatz/secretsdump. Recovered hashes enable pass-the-hash (T1550.002) and offline cracking. Event 4656/4663 (with SACLs), Sysmon 1/11, and CVE-2021-36934 (HiveNightmare) are relevant.
>

# purpose

Stores local user accounts and groups and the hashed form of their passwords. Microsoft notes that an attacker with a copy of the SAM database can mount an offline password-cracking attack by hashing candidate passwords and comparing them to the stored hashes. The SAM is present on every Windows OS; when a computer is joined to a domain, domain accounts are managed by Active Directory, while the SAM continues to hold local accounts.
