---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - crypt32
  - certificates
  - crl
aliases:
  - CryptnetUrlCache
  - Cryptnet URL cache
url:
  - https://learn.microsoft.com/windows/win32/seccrypto/certificate-revocation-list-semantics
---

**fullpath**:C:\Users\<username>\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content

# description

The `Content` folder of the per-user Cryptnet URL cache, used by Crypt32 to cache objects retrieved from URLs during certificate chain validation. Crypt32's `CertGetCertificateChain` adds downloaded OCSP responses and CRLs to the user's Cryptnet URL cache.

## simple description

> ### 2026-11-21 Claude said
> This folder holds files Windows downloaded while checking digital certificates, such as certificate revocation lists (CRLs), OCSP responses and sometimes certificates. It saves Windows from re-downloading them every time a signed file or website is checked. A companion MetaData folder stores the URL each cached file came from. It sits in LocalLow, which is writable by low-integrity processes.
>
> **SOC NOTE**: `certutil -urlcache -f <url>` downloads arbitrary payloads into this cache, a well-known LOLBin technique (MITRE T1105, T1218), so files here can be attacker tools, not only CRLs. The paired `MetaData` entries record the original URL and download time, giving forensic evidence of downloads even after the payload is moved. Check for non-certificate content (PE files, scripts) in this folder.
>

# purpose

When online revocation checking is enabled, Crypt32 first checks for a time-valid OCSP response or CRL in the user's Cryptnet URL cache; when it downloads an OCSP response from the AIA URL or a CRL from the CDP, it adds it to the cache. CRLs with the Next CRL Publish extension (1.3.6.1.4.1.311.21.4) are pre-fetched before they expire.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
