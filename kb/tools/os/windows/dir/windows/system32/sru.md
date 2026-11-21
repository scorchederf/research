---
created: 2026-11-21
fullpath: 'C:\Windows\System32\sru'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - srum
  - forensics
aliases:
  - sru
  - SRUM folder
url:
  - https://learn.microsoft.com/answers/a/12208163
---

**fullpath**:C:\Windows\System32\sru

# description

Folder containing `SRUDB.dat`, used by the System Resource Usage Monitor (SRUM). Microsoft Learn only references it in a Q&A answer about `SRU.CHK` errors, where deleting `SRUDB.dat` and restarting is suggested as troubleshooting.

## simple description

> ### 2026-11-21 Claude said
> The sru folder holds the System Resource Usage Monitor database (`SRUDB.dat`, an ESE database) and its logs. Windows records per-app network bytes, CPU time, energy use and push notifications roughly every hour and keeps about 30 to 60 days of history. Task Manager's App history and Settings data-usage pages read from it.
>
> **SOC NOTE**: Excellent forensic artifact: shows which executables ran and how much data each sent/received, per user SID, even after the program was deleted. Useful to detect exfiltration (MITRE ATT&CK T1041/T1048) and execution of tools. Parse with SrumECmd or similar; the database is locked while running so collect via VSS or offline copy.
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# common files found

| file | description |
| --- | --- |
| `SRUDB.dat` | SRUM database file referenced in Microsoft Learn Q&A. |
| `SRU.CHK` | Checkpoint file mentioned in the same Q&A. |
