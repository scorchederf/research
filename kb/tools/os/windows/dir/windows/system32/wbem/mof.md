---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbem\MOF'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - wmi
aliases:
  - "wbem\\MOF"
  - "MOF self-install directory"
url:
  - https://learn.microsoft.com/windows/win32/wmisdk/mofcomp
  - https://learn.microsoft.com/windows/win32/wmisdk/pragma-autorecover
  - https://learn.microsoft.com/troubleshoot/windows-server/support-tools/scripts-compile-registered-mof-files
---

**fullpath**: C:\Windows\System32\wbem\MOF

# description

Subfolder of the WMI directory `%Windir%\System32\wbem`, where most Managed Object Format (MOF) files and the MOF compiler (Mofcomp.exe) live. Microsoft Learn documents MOF files, mofcomp and the autorecover list (`HKLM\SOFTWARE\Microsoft\Wbem\CIMOM\Autorecover MOFs`), but does not document this `MOF` subfolder itself.

## simple description

> ### 2026-11-21 Claude said
> This is the WMI "MOF self-install" folder. On older Windows versions (XP / Server 2003 era) the WMI service watched this folder and automatically compiled any .mof file dropped into it, then moved it to a "good" or "bad" subfolder with a log. On Vista and later the auto-compile behaviour was removed by default, so the folder is usually empty or holds legacy items.
>
> **SOC NOTE**: Historically abused for code execution and persistence by dropping a MOF that registers a WMI event subscription (e.g. Stuxnet, Metasploit's MOF technique) - T1546.003. On modern systems, look instead for `mofcomp.exe` executions with unusual MOF files and for subscriptions in root\subscription. Any recent .mof files appearing here are suspicious.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_
