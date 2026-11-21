---
created: 2026-11-21
fullpath: 'C:\Windows\System32\manage-bde.wsf'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - bitlocker
  - script
aliases:
  - manage-bde.wsf
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/manage-bde
  - https://learn.microsoft.com/windows/security/operating-system-security/data-protection/bitlocker/operations-guide
---

**fullpath**:C:\Windows\System32\manage-bde.wsf

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> manage-bde.wsf is the original Windows Script File version of the BitLocker command-line management tool, shipped with Windows Vista and Windows Server 2008 and run through `cscript.exe`. It was later replaced by the native `manage-bde.exe`, which Microsoft Learn documents as the BitLocker Configuration Tool. It lets an administrator turn BitLocker on or off, manage key protectors and check encryption status from the command line. On modern systems it is usually absent or kept only for legacy compatibility.
>
> **SOC NOTE**: Any BitLocker CLI use can be abused by ransomware actors to encrypt volumes with attacker-held protectors (MITRE ATT&CK T1486 Data Encrypted for Impact) or to remove/disable protectors and read recovery keys. Look for `cscript.exe` launching `manage-bde.wsf` (process creation events 4688 / Sysmon 1) and BitLocker-API events in `Microsoft-Windows-BitLocker/BitLocker Management`.
>
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
