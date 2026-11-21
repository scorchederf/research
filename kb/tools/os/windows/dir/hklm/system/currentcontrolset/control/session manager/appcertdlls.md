---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCertDlls'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - persistence
aliases:
  - "AppCertDlls"
url: []
---

**fullpath**: HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCertDlls

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> AppCertDlls is a registry key under Session Manager where each value points to a DLL. Windows loads every DLL listed here into any process that calls process-creation APIs such as CreateProcess, CreateProcessAsUser or WinExec. It was intended for application certification/whitelisting hooks, but almost no legitimate software uses it today. On a normal system the key is usually absent or empty.
>
> **SOC NOTE**: Classic persistence and privilege-escalation location (MITRE ATT&CK T1546.009 Event Triggered Execution: AppCert DLLs). Any value here should be treated as suspicious; check the DLL path, signature and creation time. Monitor with Sysmon event 12/13 and Security 4657, and look for the DLL being loaded into many processes (Sysmon 7). Autoruns shows entries on its AppInit tab.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCertDlls"` | List the key's values. |
