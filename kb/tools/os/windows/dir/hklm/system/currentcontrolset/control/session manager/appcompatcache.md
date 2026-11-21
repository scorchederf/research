---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - appcompat
aliases:
  - AppCompatCache
  - ShimCache
url:
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache

# description

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

## simple description

> ### 2026-11-21 Claude said
> AppCompatCache, often called the ShimCache, is a registry key that the Windows Application Compatibility subsystem uses to track executables it has evaluated for compatibility shims. Its `AppCompatCache` binary value holds a list of file paths with metadata such as the last-modified timestamp of each file. The cache is kept in memory and written to the registry when the system shuts down or reboots. It helps Windows decide quickly whether a program needs a compatibility fix.
>
> **SOC NOTE**: ShimCache is a key forensic artifact for proving that a file existed on a host (and on older Windows versions, that it likely ran), even after the binary was deleted. Parse it from the offline SYSTEM hive with tools such as AppCompatCacheParser. Entries are ordered most-recent first, but the timestamp is the file's modification time, not the execution time. Recent entries are lost if the host is powered off hard without a clean shutdown. Relevant to MITRE ATT&CK T1070.004 (deleted tools still show up) and T1036 (masquerading paths).
>
> _Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# hive

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# values

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache"` | List the key's values. |
