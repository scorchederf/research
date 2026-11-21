---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\dam\State\UserSettings\<SID>'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - hklm
  - forensics
aliases:
  - dam UserSettings
  - Desktop Activity Moderator
url:
  - https://learn.microsoft.com/windows/win32/w8cookbook/desktop-activity-moderator
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/bug-check-0x1eb--dam-watchdog-timeout
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services\dam\State\UserSettings\<SID>

# description

This key belongs to the `dam` service, the Desktop Activity Moderator (DAM). DAM is a kernel-mode driver, introduced in Windows 8, that is loaded at boot on systems that support connected (modern) standby and suspends or throttles desktop app processes while the system is in that state. The `UserSettings\<SID>` subkey itself is not described on Learn.

## simple description

> ### 2026-11-21 Claude said
> The Desktop Activity Moderator is a Windows driver that pauses desktop programs when a laptop or tablet goes into modern standby, to save battery. Under this key it keeps one subkey per user SID. Each subkey holds values named after full executable paths with a binary value that includes a last-run timestamp. It is very similar to the BAM (Background Activity Moderator) key.
>
> **SOC NOTE**: Execution artifact (like BAM): value names list executable paths a user ran, with a FILETIME of last execution, which helps prove program execution (T1204 / T1059 investigations) and attribute it to a SID. Mostly present on devices with modern standby. Parse it from the SYSTEM hive with RegRipper (`bam` plugin) or Registry Explorer.
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\dam\State\UserSettings\<SID>"` | List the key's values. |
