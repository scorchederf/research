---
created: 2026-11-21
fullpath: 'HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - shellbags
  - forensics
aliases:
  - BagMRU
  - ShellBags
url: []
---

**fullpath**:HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU

# description

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> BagMRU is part of ShellBags, registry data where Windows Explorer remembers folders a user has browsed and how each folder was displayed. Each numbered subkey represents a folder in a tree, and the binary values store shell item IDs that encode the folder names. The data lives in the user's `UsrClass.dat` hive. Entries remain even after the folder is deleted or the drive is removed.
>
> **SOC NOTE**: Classic forensic artifact proving a user browsed a folder (including on removable drives, network shares and ZIPs) with timestamps, even for deleted folders; useful for data staging/exfiltration and lateral movement investigations (MITRE ATT&CK T1083 File and Directory Discovery). Parse with ShellBags Explorer/SBECmd. Attackers may clear it as anti-forensics (T1070).
>
> _Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# hive

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# values

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU"` | List the key's values. |
