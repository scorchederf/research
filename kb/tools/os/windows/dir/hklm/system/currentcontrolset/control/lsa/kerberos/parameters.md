---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - kerberos
aliases:
  - "Kerberos\\Parameters"
  - "Kerberos protocol registry entries"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/kerberos-protocol-registry-kdc-configuration-keys
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/enable-kerberos-event-logging
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/kerberos-authentication-problems-if-user-belongs-to-groups
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/group-policy-add-maxtokensize-registry-entry
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-kerberos
---

**fullpath**: HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters

# description

Registry key holding client-side configuration for the Windows Kerberos v5 authentication package (time skew, logging, KDC timeouts, token size, encryption and caching behaviour). The key may not exist by default and must be created before adding entries. KDC-side settings live separately under `HKLM\SYSTEM\CurrentControlSet\Services\Kdc`; some values (such as MaxTokenSize) can also be set by Group Policy (System > Kerberos, Kerberos.admx) or the Policy CSP.

## simple description

> ### 2026-11-21 Claude said
> Kerberos is the main way Windows computers in a domain prove who they are. This key lets administrators tweak how the Kerberos client on a machine behaves: how much clock difference is tolerated, how big tickets may be, whether verbose Kerberos events are logged, and which encryption to prefer. Most values are absent by default, meaning Windows uses built-in defaults.
>
> **SOC NOTE**: `AllowTgtSessionKey=1` lets user-mode tools export TGT session keys (used by tools like Rubeus/Mimikatz to dump usable tickets - T1558 / T1550.003 Pass the Ticket); it is off by default and blocked by Credential Guard. Forcing `DefaultEncryptionType=23` (RC4) weakens tickets and aids Kerberoasting/overpass-the-hash. `LogLevel=1` produces verbose Kerberos System events, helpful during investigations. Monitor changes to this key (Sysmon 13, 4657).
>

# purpose

Used to tune and troubleshoot Kerberos authentication. Learn recommends removing any added entries after troubleshooting. Typical documented uses are raising `MaxTokenSize` for users in many groups (computers must restart) and enabling `LogLevel` to log Kerberos events to the System log (takes effect immediately).

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `SkewTime` | REG_DWORD | Maximum permitted time difference between client and server/KDC. Default 5 minutes. |
| `LogLevel` | REG_DWORD | Non-zero logs all Kerberos-related events to the System event log. Default 0. |
| `MaxPacketSize` | REG_DWORD | Maximum UDP packet size before TCP is used. Default 1465 bytes; 0 (never UDP) on Windows Vista and later. |
| `StartupTime` | REG_DWORD | Time Windows waits for the KDC to start. Default 120 seconds. |
| `KdcWaitTime` | REG_DWORD | Time Windows waits for a KDC response. Default 10 seconds. |
| `KdcBackoffTime` | REG_DWORD | Time between successive KDC calls after a failure. Default 10 seconds. |
| `KdcSendRetries` | REG_DWORD | Number of attempts to contact a KDC. Default 3. |
| `DefaultEncryptionType` | REG_DWORD | Default pre-authentication encryption type: 18 AES256 (default), 17 AES128, 23 RC4 HMAC. Not applicable from Windows Server 2025 / Windows 11 24H2. |
| `FarKdcTimeout` | REG_DWORD | Time-out to invalidate an other-site DC in the DC cache. Default 10 minutes. |
| `NearKdcTimeout` | REG_DWORD | Time-out to invalidate a same-site DC in the DC cache. Default 30 minutes. |
| `StronglyEncryptDatagram` | REG_DWORD | Use 128-bit encryption for datagram packets. Default 0; 1 from Windows Server 2025 / Windows 11 24H2. |
| `MaxReferralCount` | REG_DWORD | Number of KDC referrals pursued before giving up. Default 6. |
| `MaxTokenSize` | REG_DWORD | Maximum Kerberos token size. Default 12000, 48000 from Windows 8 / Server 2012; keep at or below 48000 (max 65535). |
| `SpnCacheTimeout` | REG_DWORD | Lifetime used to purge negative SPN cache entries and scavenge the cache at 350 entries. Default 15 minutes. |
| `S4UCacheTimeout` | REG_DWORD | Lifetime of S4U negative cache entries. Default 15 minutes. |
| `S4UTicketLifetime` | REG_DWORD | Lifetime of tickets obtained by S4U proxy requests. Default 15 minutes. |
| `RetryPdc` | REG_DWORD | Non-zero makes the client contact the PDC for AS_REQ after a password expiration error. Default 0. |
| `RequestOptions` | REG_DWORD | Extra KDC options sent in TGS_REQ (any RFC 1510 value). |
| `ClientIpAddresses` | REG_DWORD | Non-zero adds client IP addresses to AS_REQ so tickets carry the Caddr field. Default 0. |
| `TgtRenewalTime` | REG_DWORD | Time before expiry at which Kerberos tries to renew a TGT. Default 600 seconds. |
| `AllowTgtSessionKey` | REG_DWORD | Non-zero exports session keys with initial or cross-realm TGT authentication. Default 0 for security; cannot be enabled with Credential Guard. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters"` | List the key's values. |
| `reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters" /v LogLevel /t REG_DWORD /d 1` | Enable Kerberos event logging to the System log (remove when done). |
| `reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters" /v MaxTokenSize /t REG_DWORD /d 48000` | Set the recommended maximum token size (restart required). |
