---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\SystemCertificates\My\Certificates'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - certificates
  - pki
aliases:
  - SystemCertificates\My\Certificates
  - Current User Personal store
url:
  - https://learn.microsoft.com/windows/win32/seccrypto/certificate-store-migration
  - https://learn.microsoft.com/windows/security/identity-protection/hello-for-business/deploy/on-premises-cert-trust-adfs
  - https://learn.microsoft.com/windows/win32/seccrypto/managing-certificates-with-certificate-stores
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\SystemCertificates\My\Certificates

# description

File-based storage location of the Current User `MY` (Personal) certificate store (`%APPDATA%\Microsoft\SystemCertificates\My\Certificates`). Each file in this folder represents a certificate in the user's Personal store and is named by its thumbprint; `certutil -q` can display it. It is migrated during computer upgrades or migrations.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the user's personal certificates, the ones used to sign or decrypt that user's messages and authenticate (client auth, S/MIME, EFS). Each file is one certificate named by its SHA1 thumbprint. The matching private keys are stored separately (under Crypto/Protect, protected by DPAPI). The folder is hidden and roams with the profile.
>
> **SOC NOTE**: Attackers steal user certificates plus their DPAPI-protected private keys to authenticate as the user, e.g. AD CS client auth / PKINIT (MITRE ATT&CK T1649 Steal or Forge Authentication Certificates, T1552.004 Private Keys). New certificate files appearing here can indicate malicious enrollment (ESC1-style). Correlate with CertificateServicesClient events.
>

# purpose

Persists the Current User Personal (`MY`) certificate store. Each file is one certificate; the thumbprint matches the file name.

# common files found

| file | description |
| --- | --- |
| `<certificate thumbprint>` | One file per certificate in the user's Personal store; view with `Certutil -q <certificateThumbprintFileName>` (or `-v` for detail). |
