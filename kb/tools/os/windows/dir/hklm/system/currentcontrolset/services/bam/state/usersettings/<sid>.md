---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID>'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - bam UserSettings
  - Background Activity Moderator
url:
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID>

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This key belongs to the Background Activity Moderator (BAM), a Windows 10/11 kernel driver service that manages background activity of applications. Under `UserSettings`, each user SID has a subkey whose values are full paths of executables that user ran, each with a binary timestamp of last execution. Windows uses it to throttle background apps; it was introduced in Windows 10 1709. Entries age out after roughly a week.
>
> **SOC NOTE**: BAM is a valuable execution-evidence artifact for forensics (supports detection of MITRE ATT&CK T1204/T1059 activity): each value is a device path to an executable (e.g. `\Device\HarddiskVolume3\Users\x\Downloads\tool.exe`) with a FILETIME of last run, attributed to a specific SID. It survives deletion of the executable. Parse it from a live system or offline `SYSTEM` hive (RegRipper `bam` plugin, Registry Explorer); short retention means collect early.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKEY_LOCAL_MACHINE (SYSTEM) |
| scope | machine-wide (subkeys per user SID) |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID>"` | List the key's values. |
