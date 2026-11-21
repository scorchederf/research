---
created: 2026-11-21
fullpath: 'C:\Windows\AppCompat\Programs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - appcompat
aliases:
  - Programs
  - AppCompat\Programs
url:
---

**fullpath**:C:\Windows\AppCompat\Programs

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This folder is used by the Windows application compatibility and inventory components. On Windows 8 and later it contains Amcache.hve, a registry-format file recording programs, drivers and executables that ran or were installed, plus related install/inventory text files. On Windows 7 it held RecentFileCache.bcf instead.
>
> **SOC NOTE**: Amcache.hve is a key forensic artifact for evidence of execution/presence: it records full paths, SHA-1 hashes, timestamps and publisher info for executables, often surviving deletion of the malware itself. Parse it with tools like AmcacheParser or RegRipper; attacker tampering or deletion of this folder is itself suspicious (MITRE ATT&CK T1070.004).
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
