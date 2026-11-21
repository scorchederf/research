---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows Defender\Scans\mpenginedb.db'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - defender
  - database
aliases:
  - mpenginedb.db
url: []
---

**fullpath**:C:\ProgramData\Microsoft\Windows Defender\Scans\mpenginedb.db

# description

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> mpenginedb.db is a SQLite database used by the Microsoft Defender Antivirus engine, stored in the protected Scans folder under ProgramData. It holds engine state such as file hashes and scan/reputation metadata used to speed up and track scanning. Only SYSTEM and the Defender service can normally write to the Scans folder.
>
> **SOC NOTE**: Forensic value: can contain SHA-1/SHA-256 hashes and paths of files Defender has seen, sometimes after the files were deleted; review alongside Scans\History\Service\DetectionHistory, MPLog files and Defender Operational events 1116/1117. Tampering with or deleting Defender data indicates defense evasion (T1562.001).
>
> _Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
