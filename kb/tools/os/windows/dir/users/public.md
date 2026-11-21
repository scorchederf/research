---
created: 2026-11-21
fullpath: 'C:\Users\Public'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - profile
aliases:
  - "Public"
  - "Public profile"
url:
  - https://learn.microsoft.com/windows/configuration/wcd/wcd-folders
  - https://learn.microsoft.com/windows/win32/shell/profiles-directory
---

**fullpath**:C:\Users\Public

# description

C:\Users\Public is the public profile folder inside the profiles directory (C:\Users). It is shared by all users of the computer; Windows Configuration Designer can add files to its public documents folder through the PublicDocuments setting.

## simple description

> ### 2026-11-21 Claude said
> The Public folder is a shared profile that every local user can read and write. It contains Public Desktop, Public Documents, Public Downloads and similar folders. Items in Public Desktop show on every user's desktop.
>
> **SOC NOTE**: Because any user can write here without admin rights, attackers frequently stage tools, payloads and exfil archives in C:\Users\Public (MITRE ATT&CK T1074.001 Local Data Staging). Executables, scripts or DLLs created here, and processes started from it, are worth alerting on.
>

# purpose

Provides a location for files shared between all users of the computer, alongside the per-user, Default and ProgramData/All Users profile directories.

# common files found

| file | description |
| --- | --- |
| `Documents` | Public profile documents folder; target of the Windows Configuration Designer PublicDocuments setting. |
