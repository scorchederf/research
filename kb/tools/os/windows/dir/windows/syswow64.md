---
created: 2026-11-21
fullpath: 'C:\Windows\SysWOW64'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - SysWOW64
  - '%windir%\SysWOW64'
url:
  - https://learn.microsoft.com/windows/win32/winprog64/file-system-redirector
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/compatibility-limitations-32-bit-programs-64-bit-system
  - https://learn.microsoft.com/windows/win32/api/wow64apiset/nf-wow64apiset-wow64disablewow64fsredirection
---

**fullpath**:C:\Windows\SysWOW64

# description

SysWOW64 is the 32-bit system directory on 64-bit (x64) Windows. The WOW64 file system redirector transparently redirects 32-bit x86 processes that access %windir%\System32 to %windir%\SysWOW64 (32-bit ARM processes go to SysArm32); 64-bit applications get its name with `GetSystemWow64Directory2` / `GetSystemWow64Directory`.

## simple description

> ### 2026-11-21 Claude said
> Despite the name, SysWOW64 holds the 32-bit versions of Windows system files (cmd.exe, rundll32.exe, DLLs) on 64-bit Windows, while System32 holds the 64-bit ones. When a 32-bit program asks for System32, Windows silently sends it to SysWOW64. 32-bit programs can reach the real System32 via the `Sysnative` alias.
>
> **SOC NOTE**: Processes running from SysWOW64 (e.g. 32-bit rundll32.exe, powershell.exe) are common with 32-bit malware and Cobalt Strike-style spawn-to defaults; an unexpected 32-bit LOLBin is worth a look. Malware also drops files here to blend in (T1036.005). Compare hashes against known-good and check signature for any non-Microsoft file.
>

# purpose

Stores 32-bit system binaries for WOW64. Accesses to %windir%\System32, %windir%\lastgood\system32 and %windir%\regedit.exe by 32-bit x86 processes are redirected to SysWOW64 equivalents, except exempt subdirectories (catroot, catroot2, driverstore, drivers\etc, logfiles, spool). If the access triggers a UAC prompt, redirection does not occur. A 32-bit command prompt can be started with `%windir%\SysWoW64\cmd.exe`; redirection can be controlled with `Wow64DisableWow64FsRedirection` / `Wow64RevertWow64FsRedirection`.

# common files found

| file | description |
| --- | --- |
| `cmd.exe` | 32-bit command prompt (`%windir%\SysWoW64\cmd.exe`). |
| `regedit.exe` | 32-bit Registry Editor that 32-bit callers of `%windir%\regedit.exe` are redirected to. |
| `vbscript.dll`, `jscript.dll` | 32-bit scripting engine DLLs (referenced in security bulletin workarounds). |
