---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Print\Environments\Windows x64\Print Processors'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - print-spooler
  - persistence
aliases:
  - Print Processors
url:
  - https://learn.microsoft.com/windows/win32/printdocs/print-processor
  - https://learn.microsoft.com/windows/win32/printdocs/addprintprocessor
  - https://learn.microsoft.com/windows/win32/printdocs/getprintprocessordirectory
  - https://learn.microsoft.com/windows-hardware/drivers/print/introduction-to-print-processors
  - https://learn.microsoft.com/windows-hardware/drivers/print/printer-inf-file-entries
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\Print\Environments\Windows x64\Print Processors

# description

Registry location where the print spooler tracks the print processors installed for the `Windows x64` environment. Print processors are user-mode DLL plug-ins of the Windows print spooler that convert spooled job data for the print monitor; they are installed with `AddPrintProcessor` and enumerated with `EnumPrintProcessors`.

## simple description

> ### 2026-11-21 Claude said
> Each subkey here is a print processor registered for 64-bit Windows, such as the built-in `winprint`. The subkey's `Driver` value names a DLL in `C:\Windows\System32\spool\prtprocs\x64`. The Print Spooler service (spoolsv.exe, running as SYSTEM) loads these DLLs when it starts. Normally only `winprint` and vendor printer processors appear.
>
> **SOC NOTE**: Persistence/privilege escalation via print processors (MITRE T1547.012, used by Earth Lusca/PipeMon). A new subkey with an unknown DLL means code runs as SYSTEM inside spoolsv.exe at every boot. Check DLL signatures in the prtprocs folder and registry change events (Sysmon 12/13).
>

# purpose

Holds the print processors available to the spooler for the x64 environment. The spooler calls the print processor when a job is ready to print; it reads the spool file, converts the data (e.g. EMF, RAW, TEXT to RAW) and handles pause, resume and cancel requests. `AddPrintProcessor` installs a processor DLL (which must be in the system print-processor directory, `%Windir%\System32\Spool\Prtprocs\%Environment%`) and adds its name to the list of supported print processors. If a printer INF doesn't specify `PrintProcessor`, the default WinPrint processor is used.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# subkeys

| subkey | description |
| --- | --- |
| `winprint` | Default print processor (WinPrint) used when a printer INF does not specify one. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Print\Environments\Windows x64\Print Processors"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Print\Environments\Windows x64\Print Processors" /s` | List all print processor subkeys and their values. |
