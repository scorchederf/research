---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-PrintService%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - eventlog
  - printing
aliases:
  - "Microsoft-Windows-PrintService%4Operational.evtx"
  - "Microsoft-Windows-PrintService/Operational"
url: []
---

**fullpath**: C:\Windows\System32\winevt\Logs\Microsoft-Windows-PrintService%4Operational.evtx

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This file stores the PrintService Operational log, which is disabled by default. When enabled, it records print jobs (event 307 shows document name, user, printer and pages), printer and driver changes, and spooler activity. Admins enable it to audit printing.
>
> **SOC NOTE**: Event 307 provides print-job auditing for data exfiltration via printing; events 316/808/811 help detect PrintNightmare-style driver installs (CVE-2021-34527, T1068/T1547.012 Print Processors). Enable the channel in advance; it's empty otherwise.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
