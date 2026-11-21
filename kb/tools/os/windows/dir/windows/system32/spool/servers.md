---
created: 2026-11-21
fullpath: 'C:\Windows\System32\spool\SERVERS'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - SERVERS
  - spool\SERVERS
url:
---

**fullpath**:C:\Windows\System32\spool\SERVERS

# description

_Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> The SERVERS folder is a subfolder of the Print Spooler directory (C:\Windows\System32\spool), next to PRINTERS, drivers and prtprocs. It is used by the spooler for print-server related data and is normally empty on most machines. It is created by Windows and owned by SYSTEM.
>
> **SOC NOTE**: The spool tree is a frequent target for print-spooler exploits (PrintNightmare CVE-2021-34527, T1068/T1547.012 Print Processors) that drop DLLs under spool\drivers or spool\prtprocs; unexpected files anywhere under spool, including SERVERS, deserve review. Spoolsv.exe writing DLLs and Event 808/316 in PrintService logs are useful indicators.
> _Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_
