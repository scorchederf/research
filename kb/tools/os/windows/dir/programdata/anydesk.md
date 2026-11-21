---
created: 2026-11-21
fullpath: 'C:\ProgramData\AnyDesk'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - third-party
  - remote-access
aliases:
  - "AnyDesk"
url:
  []
---

**fullpath**:C:\ProgramData\AnyDesk

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This folder is created by AnyDesk, a third-party remote desktop application, when it is installed as a service. It holds machine-wide configuration such as `system.conf` and `service.conf` and the service trace log `ad_svc.trace`. Per-user settings and `ad.trace` usually live under `%AppData%\AnyDesk` instead.
>
> **SOC NOTE**: AnyDesk is a common Remote Monitoring and Management tool abused by ransomware operators and tech-support scammers for persistence and hands-on-keyboard access (MITRE ATT&CK T1219 Remote Access Software). `ad_svc.trace` records incoming session IDs, client IDs and source IPs, `connection_trace.txt` lists accepted connections, and `system.conf` may contain an unattended-access password hash; unexpected presence of this folder on a server is a strong lead.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
