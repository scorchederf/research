---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObjectDelayLoad'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - explorer
  - persistence
aliases:
  - ShellServiceObjectDelayLoad
  - SSODL
url: []
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObjectDelayLoad

# description

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> This registry key lists COM objects that Windows Explorer loads automatically when it starts, called shell service objects. Each value is a name with a CLSID as data, and Explorer creates that COM object in its own process at logon. It was used by older Windows components such as tray helpers. On modern Windows it is usually empty or holds very few entries.
>
> **SOC NOTE**: Classic autostart persistence point (MITRE T1547 Boot or Logon Autostart Execution / T1546.015 COM hijacking): adding a value pointing to a malicious CLSID whose InprocServer32 DLL then loads into explorer.exe for every user at logon. Listed in Sysinternals Autoruns under Explorer. Review any value here and resolve its CLSID under HKCR\CLSID to the DLL path and signer.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SOFTWARE` |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObjectDelayLoad"` | List the key's values. |
