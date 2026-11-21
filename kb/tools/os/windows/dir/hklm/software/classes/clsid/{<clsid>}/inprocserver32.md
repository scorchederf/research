---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Classes\CLSID\{<CLSID>}\InprocServer32'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - com
aliases:
  - "InprocServer32"
  - "InProcServer32"
url:
  - https://learn.microsoft.com/windows/win32/com/inprocserver32
  - https://learn.microsoft.com/windows/win32/com/clsid-key-hklm
  - https://learn.microsoft.com/windows/win32/com/in-process-server-threading-issues
---

**fullpath**: HKLM\SOFTWARE\Classes\CLSID\{<CLSID>}\InprocServer32

# description

COM registry key that registers a 32-bit in-process server (DLL) for a class identified by `{CLSID}` and specifies the threading model of the apartment it can run in. It is one of the subkeys of the CLSID key, alongside LocalServer32, InprocHandler32, AppID and others. The same data is visible through the merged view `HKCR\CLSID\{CLSID}\InprocServer32`.

## simple description

> ### 2026-11-21 Claude said
> Every COM object in Windows has a GUID called a CLSID. When a program asks Windows to create that object, COM looks up this key to find which DLL implements it and loads that DLL into the program. The default value is the DLL path and ThreadingModel says how the DLL handles threads. This location is machine-wide; a per-user copy under HKCU overrides it.
>
> **SOC NOTE**: COM hijacking (T1546.015) replaces or shadows the DLL path here (or in HKCU\Software\Classes\CLSID, which takes precedence) so a trusted process loads attacker code - persistence and sometimes elevation. Also used for AMSI/ETW provider tampering. Hunt for InprocServer32 defaults pointing to user-writable paths (AppData, Temp, ProgramData) or unsigned DLLs, and monitor Sysmon 12/13 on CLSID keys.
>

# purpose

Tells COM where the in-process server DLL for a class lives and which apartment threading model it supports. If `ThreadingModel` is absent, the server is loaded into the main single-threaded apartment (first STA initialised in the process); otherwise it is loaded in the client's apartment when compatible, or in a host STA/MTA or neutral apartment as required. Every object provided by the same in-process server must use the same value.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `(Default)` | REG_SZ | Path to the in-process server DLL. |
| `ThreadingModel` | REG_SZ | `Apartment` (single-threaded apartment), `Both` (STA or MTA), `Free` (multithreaded apartment) or `Neutral` (neutral apartment). |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Classes\CLSID\{<CLSID>}\InprocServer32"` | List the DLL path and ThreadingModel for one CLSID. |
| `reg query "HKCR\CLSID\{<CLSID>}\InprocServer32"` | Query the merged HKCR view (per-user registration overrides machine). |
