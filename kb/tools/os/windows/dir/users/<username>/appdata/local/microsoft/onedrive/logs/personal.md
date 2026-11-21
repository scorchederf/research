---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\OneDrive\logs\Personal'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - OneDrive logs Personal
url:
  - https://learn.microsoft.com/answers/a/12285909
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\OneDrive\logs\Personal

# description

_Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> This folder holds the OneDrive sync client's logs for a user's personal (consumer Microsoft account) OneDrive; work/school accounts log to logs\Business1 etc. Files include SyncEngine-*.odl / .odlgz / .aodl binary logs and *.odlsent files, which record sync activity, uploads, downloads and errors. They are written by OneDrive.exe running as the user.
>
> **SOC NOTE**: Valuable for data-exfiltration investigations (MITRE ATT&CK T1567.002 Exfiltration to Cloud Storage): ODL logs can show file names synced, upload times and account details even after files are deleted. Parse them with community ODL parsers; correlate with the user's personal (non-corporate) account usage on managed devices.
> _Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_ A Microsoft Q&A answer only mentions that admins can open `%localappdata%\Microsoft\OneDrive\logs` to trace sync history.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_
