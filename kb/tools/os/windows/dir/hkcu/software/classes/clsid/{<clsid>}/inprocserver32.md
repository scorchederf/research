---
created: 2026-11-21
fullpath: 'HKCU\Software\Classes\CLSID\{<CLSID>}\InprocServer32'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - com
  - persistence
aliases:
  - InprocServer32
  - InProcServer32
url:
  - https://learn.microsoft.com/windows/win32/com/inprocserver32
  - https://learn.microsoft.com/windows/win32/com/clsid-key-hklm
  - https://learn.microsoft.com/windows/win32/winprog64/registry-reflection
---

**fullpath**:HKCU\Software\Classes\CLSID\{<CLSID>}\InprocServer32

# description

The InprocServer32 subkey of a CLSID registers a 32-bit (and 64-bit) in-process COM server DLL and the threading model it can run in. Under HKCU\Software\Classes it is the per-user registration of the CLSID key documented for HKLM\SOFTWARE\Classes\CLSID.

## simple description

> ### 2026-11-21 Claude said
> Every COM object in Windows has a CLSID (a GUID), and its InprocServer32 key says which DLL to load when a program creates that object. The default value is the DLL path and ThreadingModel says how it runs. The HKCU copy is per-user and can be written without admin rights. When a program asks for the CLSID, the per-user entry is used before the machine-wide one.
>
> **SOC NOTE**: Classic COM hijacking persistence (MITRE ATT&CK T1546.015): attackers create HKCU\Software\Classes\CLSID\{CLSID}\InprocServer32 pointing to a malicious DLL so that explorer.exe, scheduled tasks or other processes load it. Hunt for HKCU CLSID keys that shadow HKLM entries, DLL paths in user-writable folders (AppData, Temp), and Sysmon Event 12/13 registry writes. Check UsrClass.dat offline.
>

# purpose

Registers an in-process server for a COM class: the (Default) value is the path to the server DLL and ThreadingModel specifies the apartment it can be loaded in. Whenever possible the server is loaded in the same apartment as the client. InprocServer32 CLSIDs are not reflected between 32-bit and 64-bit views, because a 32-bit DLL cannot load in a 64-bit process.

# hive

| property | value |
| --- | --- |
| hive | HKCU |
| scope | per-user |

# values

| value name | type | description |
| --- | --- | --- |
| `(Default)` | REG_SZ | Path to the in-process server DLL. |
| `ThreadingModel` | REG_SZ | `Apartment` (single-threaded apartment), `Both` (STA or MTA), `Free` (multithreaded apartment) or `Neutral` (neutral apartment). If absent, the server loads into the main STA. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Classes\CLSID\{<CLSID>}\InprocServer32"` | List the key's values (replace `<CLSID>` with the class GUID). |
| `reg query "HKCU\Software\Classes\CLSID" /s /f InprocServer32 /k` | Find all per-user InprocServer32 registrations. |
