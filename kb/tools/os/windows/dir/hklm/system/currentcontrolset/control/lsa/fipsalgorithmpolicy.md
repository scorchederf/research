---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Lsa\FipsAlgorithmPolicy'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - cryptography
  - fips
aliases:
  - "FipsAlgorithmPolicy"
  - "FIPSAlgorithmPolicy"
url:
  - https://learn.microsoft.com/azure/governance/policy/samples/guest-configuration-baseline-windows
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-cryptography
  - https://learn.microsoft.com/windows/security/security-foundations/certification/fips-140-validation
  - https://learn.microsoft.com/troubleshoot/windows-client/windows-security/bitlocker-recovery-password-not-fips-compliant
---

**fullpath**: HKLM\SYSTEM\CurrentControlSet\Control\Lsa\FipsAlgorithmPolicy

# description

Registry key holding the legacy Windows FIPS policy, set by the Group Policy security option 'System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing' or the MDM Cryptography/AllowFipsAlgorithmPolicy setting. Since the April 2024 updates, the cryptographic modules run FIPS self-tests automatically, so the policy is mainly needed for BitLocker PIN key derivation.

## simple description

> ### 2026-11-21 Claude said
> This key turns FIPS mode on or off in Windows. When Enabled is 1, Windows and apps that honor it restrict themselves to FIPS-approved algorithms. It is mostly used in government or regulated environments. Turning it on can break some apps (e.g. BitLocker recovery passwords, SharePoint).
>
> **SOC NOTE**: Changing FIPS mode is rarely malicious but can be used to weaken (disable) or disrupt (enable) crypto-dependent services; monitor changes via Sysmon 13 / Security 4657 and compare to baselines (CIS/STIG expect Enabled=1 in some profiles). Useful context when RDP, BitLocker or TLS issues appear suddenly.
>

# purpose

Controls whether the system uses FIPS-compliant algorithms for encryption, hashing and signing. With the policy enabled, BitLocker cannot create or use recovery passwords (non-FIPS key derivation) and uses PBKDF2 for PIN protectors.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

| value name | type | description |
| --- | --- | --- |
| `Enabled` | REG_DWORD | 1 = use FIPS-compliant algorithms for encryption, hashing and signing (security baseline expected value); 0 = disabled. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\FipsAlgorithmPolicy"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\FipsAlgorithmPolicy" /v Enabled` | Show whether the FIPS policy is enabled. |
