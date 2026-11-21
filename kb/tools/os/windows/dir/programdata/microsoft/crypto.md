---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Crypto'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - cryptography
  - private-keys
aliases:
  - 'Crypto'
  - '%ALLUSERSPROFILE%\Application Data\Microsoft\Crypto'
url:
  - https://learn.microsoft.com/windows/win32/seccng/key-storage-and-retrieval
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/default-permissions-machinekeys-folders
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/troubleshoot-extension-certificates-issues-windows-vm
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/event-id-troubleshoot-vm-rdp-connecton
  - https://learn.microsoft.com/answers/a/8069162
---

**fullpath**:C:\ProgramData\Microsoft\Crypto

# description

Machine-wide private key store used by the legacy CryptoAPI CSPs and CNG key storage providers (`%ALLUSERSPROFILE%\Application Data\Microsoft\Crypto`). It is a system folder common to all Windows installations.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the private keys behind machine certificates (for example the RDP, IIS/TLS and service certificates) and keys belonging to SYSTEM, LocalService and NetworkService. The public certificates live in the certificate store; the matching private key files live here, protected by DPAPI. Wrong permissions here break TLS, RDP and certificate enrollment.
>
> **SOC NOTE**: Credential access target (T1552.004 Private Keys, T1649): with SYSTEM/admin rights attackers export machine private keys (Mimikatz `crypto::`, certificate theft) to impersonate servers or decrypt traffic. Monitor unusual reads of MachineKeys/SystemKeys and ACL changes. Corrupt/missing keys cause RDP event 1057/1058 and Schannel 36870 errors.
>

# purpose

Stores private keys for machine and service accounts. Legacy CryptoAPI CSPs use `Crypto\RSA\` and `Crypto\DSS\` with subfolders `S-1-5-18` (local system), `S-1-5-19` (local service), `S-1-5-20` (network service) and `MachineKeys` (shared private); CNG uses `Crypto\SystemKeys` (local system) and `Crypto\Keys` (shared private). Legacy key files have the .key extension; CNG key files don't. Default MachineKeys permissions are Administrators (Full Control, this folder only) and Everyone (special, this folder only).

# common files found

| item | description |
| --- | --- |
| `RSA\MachineKeys` | Shared machine private keys (legacy RSA CSP), e.g. RDP self-signed and IIS certificate keys. |
| `RSA\S-1-5-18` | Local system private keys (legacy RSA CSP). |
| `RSA\S-1-5-19` / `RSA\S-1-5-20` | Local service / network service private keys. |
| `DSS\MachineKeys`, `DSS\S-1-5-18` ... | Equivalent DSS CSP key folders. |
| `SystemKeys` | CNG local system private keys. |
| `Keys` | CNG shared private keys. |

