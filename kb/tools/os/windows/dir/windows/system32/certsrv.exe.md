---
created: 2026-11-21
fullpath: 'C:\Windows\System32\certsrv.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - adcs
  - pki
aliases:
  - "certsrv.exe"
  - "Active Directory Certificate Services"
  - "certsvc"
url:
  - https://learn.microsoft.com/windows-server/identity/ad-cs/active-directory-certificate-services-overview
  - https://learn.microsoft.com/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/certificate-services-not-start
  - https://learn.microsoft.com/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/cs-cant-start-computer
---

**fullpath**:C:\Windows\System32\certsrv.exe

# description

Active Directory Certificate Services (AD CS) is a Windows Server role for issuing and managing PKI certificates used in secure communication and authentication; its CA runs as the Active Directory Certificate Services (certsvc) service. Related tools include certutil.exe and the Certification Authority snap-in.

## simple description

> ### 2026-11-21 Claude said
> certsrv.exe is the program behind the Active Directory Certificate Services (CertSvc) Windows service, i.e. the certification authority engine. It only exists on servers where the AD CS Certification Authority role is installed. It issues, renews and revokes certificates and publishes CRLs according to the CA's templates and policy.
>
> **SOC NOTE**: A compromised or misconfigured CA enables domain-wide persistence and privilege escalation (ESC1-ESC8, Golden Certificate via stolen CA key, T1649 Steal or Forge Authentication Certificates). Monitor certsrv.exe for unusual child processes or memory access (CA private key theft), Security events 4886/4887 (requests/issues), 4899/4900 (template changes) and CertSvc service stops.
>

# purpose

Hosts the certification authority that issues and manages certificates for encryption, digital signatures and authentication of users, computers and devices, including certificate enrollment and revocation. Before the service starts it enumerates all keys and certificates issued to the CA and does not start if one has been removed from the local computer Personal store (error 0x80090016 NTE_BAD_KEYSET).

# typical use cases

| usage | description |
| --- | --- |
| `certutil -ping` | Attempt to contact the AD CS Request interface of the CA. |
| `certutil -verifykeys` | Verify the CA keys and certificates before starting the service. |
| `certutil -repairstore my "<Key_Id_Hash>"` | Repair the CA certificate key association when the service fails to start. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
