---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Crypto'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - cryptography
aliases:
  - "Crypto"
  - "%APPDATA%\Microsoft\Crypto"
url:
  - https://learn.microsoft.com/windows/win32/seccng/key-storage-and-retrieval
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Crypto

# description

%APPDATA%\Microsoft\Crypto is where the CryptoAPI legacy CSPs and CNG store a user's private keys. Legacy keys live under RSA or DSS subfolders named after the user SID; CNG user keys live in the Keys subfolder.

## simple description

> ### 2026-11-21 Claude said
> This hidden folder in a user's roaming profile stores that user's private cryptographic keys, such as keys for personal certificates (EFS, client auth, S/MIME). The key files are themselves protected with DPAPI. Normal users never interact with it directly.
>
> **SOC NOTE**: Target for certificate/private-key theft (MITRE ATT&CK T1552.004 Private Keys, T1649) using tools like Mimikatz `crypto::` or SharpDPAPI together with the DPAPI master keys in `%APPDATA%\Microsoft\Protect`. Executables or scripts stored here are a known malware hiding place and are not legitimate.
>

# purpose

Stores user private keys. CryptoAPI places the key container file in a directory named for the user's SID; CNG does not, which helps when moving users between domains. Keys migrated with USMT remain accessible only via CryptoAPI.

# common files found

| file | description |
| --- | --- |
| `RSA\<User SID>\` | Legacy CryptoAPI RSA user private keys. |
| `DSS\<User SID>\` | Legacy CryptoAPI DSS user private keys. |
| `Keys\` | CNG user private keys (no .key extension). |
