---
created: 2026-11-21
fullpath: 'C:\Windows\System32'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
aliases:
  - System32
  - '%SYSTEM32%'
url:
  - https://learn.microsoft.com/windows/win32/winprog64/file-system-redirector
  - https://learn.microsoft.com/windows/deployment/usmt/usmt-recognized-environment-variables
---

**fullpath**:C:\Windows\System32

# description

`%windir%\System32` is the Windows system directory; on 64-bit Windows it is reserved for 64-bit applications. When a 32-bit process accesses it, the WOW64 file system redirector redirects access to `%windir%\SysWOW64` (x86) or `%windir%\SysArm32` (ARM). The `SYSTEM` and `SYSTEM32` environment variables used by USMT refer to `%WINDIR%\system32`.

## simple description

> ### 2026-11-21 Claude said
> System32 is the core Windows folder that holds most operating system programs and libraries, such as cmd.exe, svchost.exe, drivers and configuration hives. On 64-bit Windows it contains the 64-bit files, despite its name, while 32-bit versions live in SysWOW64. Only TrustedInstaller and administrators can normally write here.
>
> **SOC NOTE**: Attackers masquerade malware with System32 file names placed elsewhere, or drop files into System32 to blend in (MITRE ATT&CK T1036.005). Check the full path and signature of any "system" binary: `svchost.exe` running outside System32 is a red flag. DLL search-order hijacking (T1574.001) and LOLBins (certutil, rundll32, mshta) here are common. Monitor new file creation in System32 outside patch windows.

# purpose

Holds 64-bit system files on 64-bit Windows. 32-bit applications can reach the native directory via the `%windir%\Sysnative` alias. Certain subdirectories are exempt from redirection: `catroot`, `catroot2`, `driverstore`, `drivers\etc`, `logfiles` and `spool`.

# common files found

| item | description |
| --- | --- |
| `catroot`, `catroot2` | Subdirectories exempt from WOW64 redirection. |
| `driverstore` | Subdirectory exempt from redirection (redirected on Windows Server 2008, Vista and earlier). |
| `drivers\etc` | Subdirectory exempt from redirection. |
| `logfiles` | Subdirectory exempt from redirection. |
| `spool` | Subdirectory exempt from redirection. |
