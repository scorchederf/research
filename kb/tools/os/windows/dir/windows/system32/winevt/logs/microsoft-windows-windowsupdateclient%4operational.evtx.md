---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-WindowsUpdateClient%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - evtx
  - event-log
  - windows-update
aliases:
  - "Microsoft-Windows-WindowsUpdateClient%4Operational.evtx"
  - "WindowsUpdateClient Operational"
url: []
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-WindowsUpdateClient%4Operational.evtx

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This file stores the Operational channel of the WindowsUpdateClient provider, which records Windows Update activity: scans, downloads, installation start/success/failure and required restarts. It is viewable in Event Viewer under Applications and Services Logs > Microsoft > Windows > WindowsUpdateClient > Operational. Common IDs include 19 (installation successful), 20 (installation failure), 43 (installation started) and 44 (download started).
>
> **SOC NOTE**: Helps establish patch level and timing for vulnerability-exploitation timelines, and shows whether updates (including Defender signature updates) were blocked or failed, which may indicate tampering (T1562.001). Gaps or clearing of this log alongside update failures are worth investigating.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
