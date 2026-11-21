---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Protect\<SID>'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - dpapi
  - credentials
aliases:
  - Protect\<SID>
  - DPAPI master key folder
url:
  - https://learn.microsoft.com/answers/a/12990340
  - https://learn.microsoft.com/windows-server/security/kerberos/system-key-utility-technical-overview
  - https://learn.microsoft.com/windows/win32/api/dpapi/nf-dpapi-cryptupdateprotectedstate
  - https://learn.microsoft.com/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/dpapi-masterkey-backup-failures
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Protect\<SID>

# description

Per-user folder that stores the user's Data Protection API (DPAPI) master keys, named after the user's SID. DPAPI generates a master key per user that protects other private keys and secrets (EFS, S/MIME, browser and Credential Manager data); the master key is unlocked by the user's sign-in credential and can be backed up to a domain controller.

## simple description

> ### 2026-11-21 Claude said
> This hidden folder contains the user's DPAPI master key files (GUID-named) and a `Preferred` file pointing to the current key. Windows uses these keys to encrypt saved passwords, browser cookies, Wi-Fi keys and Credential Manager entries for that user. The keys themselves are encrypted with a value derived from the user's password. If they are lost or cannot be decrypted, apps lose their saved secrets.
>
> **SOC NOTE**: Prime target for credential theft: with the master key files plus the user's password, NTLM hash, or the domain DPAPI backup key, attackers decrypt browser passwords and credentials offline (MITRE ATT&CK T1555, T1555.003/.004; tools like Mimikatz `dpapi::masterkey`, SharpDPAPI). Watch for non-system processes reading this folder; Crypto-DPAPI events (e.g. 1 master key created, 8198 unprotect failed) help investigations.
>

# purpose

Holds DPAPI master keys that encrypt the user's protected data. Learn Q&A notes that multiple recent key files here can indicate a new master key was created after a credential mismatch; `CryptUpdateProtectedState` migrates master keys after a SID change.

# common files found

| file | description |
| --- | --- |
| `<GUID>` key files | DPAPI master key files; more than one recent file can indicate a newly created master key. |
