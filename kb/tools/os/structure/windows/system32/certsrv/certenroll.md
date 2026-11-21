---
created: 2026-11-21
fullpath: 'C:\Windows\System32\CertSrv\CertEnroll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - adcs
  - pki
aliases:
  - CertEnroll
url:
  - https://learn.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/copy-the-ca-certificate-and-crl-to-the-virtual-directory
  - https://learn.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/configure-the-cdp-and-aia-extensions-on-ca1
---

**fullpath**:C:\Windows\System32\CertSrv\CertEnroll

# description

CertEnroll is the local folder on an Active Directory Certificate Services (AD CS) certification authority where the CA publishes its CA certificate (.crt) and certificate revocation lists (.crl). It backs the default `file://\\<ServerDNSName>\CertEnroll\...` and `http://<ServerDNSName>/CertEnroll/...` CDP and AIA locations. Related tools include certutil and pkiview.msc.

## simple description

> ### 2026-11-21 Claude said
> This folder exists on Windows servers running a Certificate Authority (AD CS). The CA drops its own certificate and its revocation lists (CRLs) here so clients can check whether certificates are trusted or revoked. It's usually shared as the CertEnroll share and exposed through IIS for HTTP downloads.
>
> **SOC NOTE**: Its presence identifies a CA server, a tier-0 asset (AD CS abuse: ESC1-ESC8, MITRE ATT&CK T1649). Unexpected files, stale CRLs, or modified permissions can indicate tampering or broken revocation. The CA cert here is public, but the CA private key and database (CertLog) nearby are crown jewels.
>

# purpose

Default publication location for the CA certificate and CRLs. After `certutil -crl` publishes the CRL, administrators copy `C:\Windows\system32\certsrv\certenroll\*.crt` and `*.crl` to a web server virtual directory so CDP/AIA locations resolve. Default CDP entries (`file://\\<ServerDNSName>\CertEnroll\<CaName><CRLNameSuffix><DeltaCRLAllowed>.crl`) and AIA entries (`...\CertEnroll\<ServerDNSName>_<CaName><CertificateName>.crt`) point here.

# common files found

- `<ServerDNSName>_<CaName><CertificateName>.crt` - CA certificate.
- `<CaName><CRLNameSuffix>.crl` - base CRL.
- `<CaName><CRLNameSuffix>+.crl` - delta CRL (when delta CRLs are allowed).
