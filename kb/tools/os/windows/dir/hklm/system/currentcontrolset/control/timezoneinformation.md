---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
aliases:
  - TimeZoneInformation
url:
  - https://learn.microsoft.com/windows/apps/develop/settings/settings-common
  - https://learn.microsoft.com/windows/win32/api/timezoneapi/ns-timezoneapi-time_zone_information
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation

# description

Registry key holding the currently set time zone for the system, documented in the Windows settings reference under Date and Time. Definitions of each available time zone are stored separately under `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones`; the related automatic time zone toggle is `HKLM\SYSTEM\CurrentControlSet\Services\tzautoupdate`.

## simple description

> ### 2026-11-21 Claude said
> This key stores which time zone the computer is set to, plus the bias (offset from UTC) and daylight saving details Windows uses to convert UTC to local time. It changes when someone sets the time zone in Settings or with tzutil. Every Windows machine has it.
>
> **SOC NOTE**: Essential for forensic timelines: read TimeZoneKeyName and ActiveTimeBias from the SYSTEM hive to normalise local timestamps to UTC. Time zone or time changes (Security 4616, System Kernel-General 1/22) can indicate anti-forensic activity (T1070.006).
>

# purpose

Holds the currently configured system time zone.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `timeZone` | REG_SZ | The currently set time zone for the system, as a string. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation"` | List the key's values. |
