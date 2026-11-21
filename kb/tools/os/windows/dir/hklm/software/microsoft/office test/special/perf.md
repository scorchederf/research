---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Office test\Special\Perf'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - office
  - persistence
aliases:
  - Perf
  - Office test
url: []
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Office test\Special\Perf

# description

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> This is an undocumented Office registry key that was apparently meant for internal Microsoft testing. If its default value points to a DLL, Office applications (Word, Excel, etc.) load that DLL every time they start. It does not exist on normal systems. Legitimate software essentially never uses it.
>
> **SOC NOTE**: Known persistence technique "Office Test" (MITRE T1137.002), used by APT28/Sofacy. Any existence of this key (HKLM or HKCU) is highly suspicious; the default value names the malicious DLL. Monitor registry creation (Sysmon 12/13) and Office processes loading unexpected DLLs (Sysmon 7).
> _Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# hive

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# values

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Office test\Special\Perf"` | List the key's values. |
