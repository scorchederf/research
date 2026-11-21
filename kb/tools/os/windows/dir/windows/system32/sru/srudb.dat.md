---
created: 2026-11-21
fullpath: 'C:\Windows\System32\sru\SRUDB.dat'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - srum
  - forensics
aliases:
  - SRUDB.dat
  - SRUM database
  - System Resource Usage Monitor database
url: []
---

**fullpath**:C:\Windows\System32\sru\SRUDB.dat

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> SRUDB.dat is the database of the System Resource Usage Monitor (SRUM), which Windows uses to track per-app resource usage for the Task Manager App history and Settings data/battery usage pages. It is an ESE (Jet Blue) database written by the Diagnostic Policy Service (svchost) roughly hourly, keeping about 30-60 days of data. It is locked while Windows runs.
>
> **SOC NOTE**: Excellent forensic artifact: records per-application network bytes sent/received, per-interface connectivity (including Wi-Fi profiles), CPU time, energy use and push notifications, tied to user SIDs, even for deleted programs. Useful for spotting exfiltration (large bytes sent by an unexpected process) and execution evidence. Parse with SrumECmd or srum-dump using the SOFTWARE hive. Attackers may delete it to cover tracks.
>
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_


