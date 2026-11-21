---
created: 2026-11-21
fullpath: 'C:\Windows\System32\CertLog'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - adcs
aliases:
  - CertLog
  - certificate database
url:
  - https://learn.microsoft.com/windows/win32/seccertenroll/about-certificate-directory
  - https://learn.microsoft.com/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/move-certificate-server-database-log-files
  - https://learn.microsoft.com/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/decommission-enterprise-certification-authority-and-remove-objects
  - https://learn.microsoft.com/windows-server/identity/ad-cs/migrate-certification-authority
---

**fullpath**:C:\Windows\System32\CertLog

# description

`%SystemRoot%\System32\CertLog` is the default location of the Active Directory Certificate Services (AD CS) certification authority database and its logs. It is created when a CA is configured and is left in place when Certificate Services is uninstalled.

## simple description

> ### 2026-11-21 Claude said
> CertLog holds the database of a Windows certification authority (CA): every certificate it issued or revoked, pending requests and, if enabled, archived private keys. It only exists on servers running the AD CS CA role. The database is an ESE (.edb) file with transaction logs next to it.
>
> **SOC NOTE**: The CA database records every issued certificate with requester and template, which is central when investigating AD CS abuse such as ESC1-style certificate requests (T1649 Steal or Forge Authentication Certificates). Copying the .edb or archived keys from this folder is high-value theft. Pair with Security events 4886/4887 (request/issue) and `certutil -view` queries.
>

# purpose

Stores the CA certificate database, named after the CA with an `.edb` extension, containing issued certificates, revoked certificates, archived private keys and certificate requests. The location is set by the `DBDirectory`, `DBLogDirectory`, `DBSystemDirectory` and `DBTempDirectory` values under `HKLM\SYSTEM\CurrentControlSet\Services\CertSvc\Configuration`. By default SYSTEM, Administrators and Enterprise Administrators have Full Control on the folder. To fully remove a decommissioned CA, delete the CertLog folder.

# common files found

| file | description |
| --- | --- |
| `<CAName>.edb` | CA certificate database. |
| `edb#####.log` | Database transaction logs (also present in CA backups). |
| `certbkxp.dat` | Found in the Database folder of CA backups. |
