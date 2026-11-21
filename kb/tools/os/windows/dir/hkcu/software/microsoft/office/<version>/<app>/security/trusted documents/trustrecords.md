---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Office\<version>\<App>\Security\Trusted Documents\TrustRecords'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - office
  - macros
  - trusted-documents
aliases:
  - TrustRecords
  - Trusted Documents
url:
  - https://learn.microsoft.com/microsoft-365-apps/security/internet-macros-blocked
---

**fullpath**:HKCU\Software\Microsoft\Office\<version>\<App>\Security\Trusted Documents\TrustRecords

# description

Per-user Office registry key associated with the Trusted Documents feature of Office applications (Word, Excel, PowerPoint, etc.). When a user selects **Enable Content** on the Trust Bar, the file becomes a Trusted Document and its macros are allowed to run.

## simple description

> ### 2026-11-21 Claude said
> When you click Enable Content (or Enable Editing) on an Office document, Office remembers that decision so it won't ask again. Those remembered documents are recorded under TrustRecords, one value per file path, for each Office app and version. It is stored in the user's own registry hive (NTUSER.DAT).
>
> **SOC NOTE**: High forensic value for phishing investigations: each value name is the full path/URL of a document the user trusted, and its binary data includes a timestamp and a flag showing whether macros were enabled - evidence of MITRE T1204.002 (Malicious File). Collect it from NTUSER.DAT for every Office version and app.
>

# purpose

Learn documents the Trusted Documents behavior: files the user enabled content for are considered trusted, and their macros continue to run even after the default change to block macros in internet files. The key structure itself is _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKCU |
| scope | per-user |
| backing file | `Ntuser.dat` |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Office\<version>\<App>\Security\Trusted Documents\TrustRecords"` | List the key's values. |
