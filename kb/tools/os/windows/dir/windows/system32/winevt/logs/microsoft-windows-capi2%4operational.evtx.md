---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-CAPI2%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - event-log
  - pki
  - certificates
aliases:
  - Microsoft-Windows-CAPI2%4Operational.evtx
  - Microsoft-Windows-CAPI2/Operational
  - CAPI2 log
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/networking/802-1x-authentication-issues-troubleshooting
  - https://learn.microsoft.com/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/microsoft-trusted-root-store-removal-of-us-federal-common-policy
  - https://learn.microsoft.com/windows/security/operating-system-security/device-management/use-windows-event-forwarding-to-assist-in-intrusion-detection
  - https://learn.microsoft.com/troubleshoot/sharepoint/sites/site-slowness-because-of-sts-certificate-crl-checking
  - https://learn.microsoft.com/windows-server/remote/remote-access/how-to-always-on-vpn-block-clients-revoked-certificates
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-CAPI2%4Operational.evtx

# description

Event log file for the **Microsoft-Windows-CAPI2/Operational** channel (Applications and Services Logs > Microsoft > Windows > CAPI2 > Operational), which records CryptoAPI 2 certificate chain building, verification, revocation and store operations. The channel is disabled by default and is used for troubleshooting PKI, SSL/TLS, 802.1X and VPN certificate issues.

## simple description

> ### 2026-11-21 Claude said
> This file stores the CAPI2 log, where Windows records details every time it checks a certificate: building the trust chain, checking revocation lists and reading certificate stores. It is off by default because it gets very noisy. Admins switch it on to troubleshoot certificate errors.
>
> **SOC NOTE**: When enabled, it reveals certificate validation of signed binaries, TLS connections and smart-card logons, useful for spotting rogue root certificates (MITRE T1553.004 Install Root Certificate), untrusted code-signing chains, and contacted CRL/AIA URLs (network IOCs). Microsoft's Windows Event Forwarding baseline enables it and grants Event Log Readers access for intrusion detection. Key IDs: 11, 30, 41, 53, 70, 90.
>

# purpose

Records CryptoAPI events. Learn documents the following: Event ID 11 shows chain building failures; 30 shows policy chain failures (NTAuth, SSL policy); 90 lists all certificates used to build possible chains; 40-43 show stored CRLs and certificates accessed through AIA paths; 50-53 show attempts to retrieve CRLs from the network; Event 41 with **The certificate is revoked** confirms revocation (for example for VPN clients). Enable it by right-clicking **Operational** > **Enable Log**; increase the default 1 MB size to at least 4 MB; save with **Save Events as** (EVTX or XML). The WEF baseline sets it to 100 MB via GPO.
