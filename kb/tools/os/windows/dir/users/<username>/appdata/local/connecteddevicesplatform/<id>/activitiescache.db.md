---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\ConnectedDevicesPlatform\<id>\ActivitiesCache.db'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - timeline
  - activity-history
  - forensics
aliases:
  - ActivitiesCache.db
  - Windows Timeline database
url: []
---

**fullpath**:C:\Users\<username>\AppData\Local\ConnectedDevicesPlatform\<id>\ActivitiesCache.db

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> ActivitiesCache.db is a SQLite database where Windows 10 stores the user's activity history for the Timeline feature: apps opened, files and websites used, and how long they were in focus. Each account gets its own folder under ConnectedDevicesPlatform, named by an ID (L.<username> for local accounts or an account ID). Timeline was removed in Windows 11, so the file is mostly found on Windows 10.
>
> **SOC NOTE**: Rich user-activity artifact (program execution, file opening, focus time, clipboard sync on some builds) with start/end timestamps - excellent evidence of execution (MITRE T1204) and data access even after files are deleted. Parse the `Activity` and `ActivityOperation` tables with tools like WxTCmd; copy alongside `-wal`/`-shm` files to avoid losing recent records.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_


