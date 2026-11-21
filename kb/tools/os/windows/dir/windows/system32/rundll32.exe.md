---
created: 2026-11-21
fullpath: 'C:\Windows\System32\rundll32.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lolbin
aliases:
  - rundll32.exe
  - rundll32
  - Rundll32
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/rundll32
  - https://learn.microsoft.com/windows-hardware/drivers/install/runonce-registry-key
---

**fullpath**:C:\Windows\System32\rundll32.exe

# description

`rundll32.exe` loads and runs 32-bit DLLs. It has no configurable settings; help comes from the specific DLL being run, and it can only call functions explicitly written to be called by Rundll32. Used e.g. by `printui.dll,PrintUIEntry` and in RunOnce entries of driver packages.

## simple description

> ### 2026-11-21 Claude said
> rundll32 is a Windows helper that runs a function exported from a DLL, using the syntax rundll32 DllName,EntryPoint arguments. Windows itself uses it constantly for Control Panel items, printer UI and shell features. Because it is so common, it blends in. The 64-bit version lives in System32 and the 32-bit one in SysWOW64.
>
> **SOC NOTE**: One of the most abused LOLBins (MITRE T1218.011): running malicious DLLs, javascript: URLs via mshtml, comsvcs.dll MiniDump of LSASS (T1003.001), and Cobalt Strike default spawn-to process. Flag rundll32 with no arguments, loading DLLs from user-writable paths, unusual export names/ordinals, or making network connections.
>

# purpose

Runs an exported function from a DLL.

# typical use cases

| usage | description |
| --- | --- |
| `rundll32 printui.dll,PrintUIEntry` | Displays the printer user interface. |
| `Rundll32[.exe] DllName,EntryPoint[Arguments]` | Format used in RunOnce entries; DllName is the full DLL path, EntryPoint the export, exactly one space before Arguments. |

# options

| option | description |
| --- | --- |
| `<DLLname>` | The DLL (and entry point) to run, e.g. `printui.dll,PrintUIEntry`. |
| `printui.dll,PrintUIEntry` | Displays the printer user interface. |
