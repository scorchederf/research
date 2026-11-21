---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbem'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - wmi
aliases:
  - wbem
  - %WINDIR%\System32\Wbem
url:
  - https://learn.microsoft.com/windows/win32/wmisdk/wmi-architecture
  - https://learn.microsoft.com/windows/win32/wmisdk/mofcomp
  - https://learn.microsoft.com/troubleshoot/windows-server/support-tools/scripts-compile-registered-mof-files
  - https://learn.microsoft.com/windows/win32/wmisdk/wmi-event-messages
---

**fullpath**:C:\Windows\System32\wbem

# description

`%WINDIR%\System32\Wbem` is the home of Windows Management Instrumentation (WMI). It contains WMI provider DLL and MOF files, the WMI command-line tools such as `Winmgmt.exe` and `Mofcomp.exe`, and the WMI repository in the `repository` subfolder.

## simple description

> ### 2026-11-21 Claude said
> WMI lets scripts and tools query and manage almost everything on Windows (processes, services, hardware). This folder holds the WMI engine, its providers and the class definitions (MOF files). The repository subfolder is the database WMI uses to store classes and permanent subscriptions. wmic.exe and WmiPrvSE.exe also live here.
>
> **SOC NOTE**: WMI is heavily abused for execution and lateral movement (T1047) and persistence via event subscriptions (T1546.003) stored in `wbem\repository\OBJECTS.DATA`. Parse the repository for __EventFilter/CommandLineEventConsumer entries. Watch for unexpected .mof files compiled with mofcomp, and WmiPrvSE.exe spawning shells. WMI-Activity/Operational log events 5857-5861 help.
>

# purpose

Contains WMI binaries, provider MOF/DLL files and the WMI repository; provider classes defined in MOF files are compiled into the repository.

# common files found

| file | description |
| --- | --- |
| `Winmgmt.exe` | WMI service command-line tool. |
| `Mofcomp.exe` | MOF compiler that adds classes and instances to the WMI repository. |
| `*.mof` | Managed Object Format files defining provider classes; most MOF files are located here. |
| `Stdprov.dll` | Registry provider DLL that supplies StdRegProv data. |
| `repository\` | The WMI repository; if inconsistent, WMI deletes and rebuilds it from autorecover MOFs. |

