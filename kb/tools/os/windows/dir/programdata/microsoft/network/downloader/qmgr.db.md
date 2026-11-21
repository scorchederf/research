---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Network\Downloader\qmgr.db'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - windows
aliases:
  - "qmgr.db"
  - "BITS job database"
url: []
---

**fullpath**:C:\ProgramData\Microsoft\Network\Downloader\qmgr.db

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> qmgr.db is the database where the Background Intelligent Transfer Service (BITS) stores its queue of transfer jobs on Windows 10 and later (older systems used qmgr0.dat/qmgr1.dat). It records each job's name, URLs, local file paths, owner, state and notification command line. The BITS service keeps it locked while running.
>
> **SOC NOTE**: BITS jobs are a persistence and download technique (MITRE ATT&CK T1197 BITS Jobs): attackers use `bitsadmin` or PowerShell to download payloads and set a notify command line that runs when the job completes. Parsing qmgr.db (e.g. with BitsParser) can reveal past and present jobs, URLs and commands, even deleted ones. Correlate with Microsoft-Windows-Bits-Client/Operational events 3, 59, 60.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_


