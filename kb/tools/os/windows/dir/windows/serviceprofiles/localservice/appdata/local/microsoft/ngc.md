---
created: 2026-11-21
fullpath: 'C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - windows-hello
  - credentials
aliases:
  - Ngc
  - NGC folder
url:
  - https://learn.microsoft.com/answers/a/12891158
  - https://learn.microsoft.com/answers/a/12586548
  - https://learn.microsoft.com/troubleshoot/windows-client/user-profiles-and-logon/event-id-300-windows-hello-successfully-created-in-windows-10
---

**fullpath**:C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc

# description

The Ngc folder is a hidden, protected folder in the LocalService profile that holds Windows Hello / Windows Hello for Business (NGC, "Next Generation Credentials") PIN and key container data. Microsoft Q&A answers on Learn describe deleting its contents (after taking ownership) to reset a corrupted PIN; registration of the NGC key is logged as Event ID 300 in the User Device Registration log.

## simple description

> ### 2026-11-21 Claude said
> Ngc stands for "Next Generation Credentials", the internal name for Windows Hello. This folder stores the per-user protector and key metadata that make PIN, face and fingerprint sign-in work; the actual private keys are usually protected by the TPM. It is owned by the LocalService account and normal users and administrators cannot open it without taking ownership. Deleting its contents resets every user's Windows Hello PIN on the device.
>
> **SOC NOTE**: Offline extraction of Ngc together with DPAPI system/user keys can enable PIN or credential attacks when keys are software-protected (no TPM) - tools such as WINHELLO2hashcat target it. Unexpected ownership/ACL changes or deletion of this folder can indicate tampering or a "reset PIN" step during an intrusion. Related artifacts: User Device Registration log (Event ID 300/358) and the msDS-KeyCredentialLink attribute in AD (Shadow Credentials, T1556).
>

# purpose

Stores the Windows Hello PIN / NGC credential state. When the folder is corrupted the PIN option becomes unavailable; the documented community fix is to take ownership of the folder, delete its contents and restart, after which a new PIN can be set up (existing PINs are removed).

# common files found

_Not documented on Microsoft Learn at 2026/11/21 18:51 UTC_
