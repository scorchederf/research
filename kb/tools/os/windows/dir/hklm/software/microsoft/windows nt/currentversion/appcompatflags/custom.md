---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - appcompat
aliases:
  - Custom
  - AppCompatFlags\Custom
url:
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom

# description

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

## simple description

> ### 2026-11-21 Claude said
> This key maps executable names to custom application compatibility (shim) databases installed on the machine. When a custom .sdb file is installed (normally with `sdbinst.exe`), Windows creates a subkey named after the target executable here, with a value pointing to the database GUID; the database itself is registered under the sibling `InstalledSDB` key. When that program starts, the shim engine loads the matching fixes. Legitimate use is fixing old line-of-business apps.
>
> **SOC NOTE**: Custom shim databases are a known persistence and code-injection technique (MITRE ATT&CK T1546.011 Application Shimming), for example using the InjectDll or RedirectEXE shims. Any unexpected subkey here, especially one paired with an `InstalledSDB` entry and an .sdb file in `C:\Windows\AppPatch\Custom`, should be investigated. Watch for `sdbinst.exe` process creation and registry writes to this key in Sysmon (Event IDs 1, 12, 13).
>
> _Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# hive

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# values

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom"` | List the key's values. |
