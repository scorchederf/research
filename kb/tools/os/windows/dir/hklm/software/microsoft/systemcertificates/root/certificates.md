---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\SystemCertificates\ROOT\Certificates'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Trusted Root Certification Authorities (local machine registry store)
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/valid-root-ca-certificates-untrusted
  - https://learn.microsoft.com/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores
  - https://learn.microsoft.com/windows-hardware/drivers/install/trusted-root-certification-authorities-certificate-store
  - https://learn.microsoft.com/windows/win32/seccrypto/system-store-locations
  - https://learn.microsoft.com/security/trusted-root/deprecation
---

**fullpath**:HKLM\SOFTWARE\Microsoft\SystemCertificates\ROOT\Certificates

# description

This key is the registry-backed physical store of the local machine Trusted Root Certification Authorities certificate store, which contains root certificates of CAs that Windows trusts. Certificates are added with `certutil -addstore root`, certlm.msc (Registry physical store), Group Policy Preferences registry items or other management tools; current-user root stores inherit its contents.

## simple description

> ### 2026-11-21 Claude said
> Each subkey under this key is named after a certificate's SHA-1 thumbprint and holds the certificate in a `Blob` value. Anything here is trusted machine-wide as a root CA for TLS, code signing and more. Admins normally manage it with certlm.msc or certutil rather than editing the registry.
>
> **SOC NOTE**: Installing a rogue root CA here (MITRE ATT&CK T1553.004 Subvert Trust Controls: Install Root Certificate) lets attackers intercept TLS or make malware look validly signed. Monitor new thumbprint subkeys (Sysmon 12/13), CAPI2 events, and compare against Microsoft's trusted root list; `Get-ChildItem Cert:\LocalMachine\Root` shows the merged view.
>

# purpose

Stores trusted root certificates for the local machine. Learn recommends distributing root CA certificates by writing them to this location rather than to the Group Policy store (`HKLM\SOFTWARE\Policies\Microsoft\SystemCertificates\Root\Certificates`), which can intermittently appear untrusted. Roots installed manually into the Registry physical store are not removed by automatic root update, unlike the Third-Party physical store.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\SystemCertificates\ROOT\Certificates"` | List the key's values and certificate subkeys. |
| `certutil -addstore root c:\tmp\rootca.cer` | Add a root CA certificate to the local machine root store (admin only). |
