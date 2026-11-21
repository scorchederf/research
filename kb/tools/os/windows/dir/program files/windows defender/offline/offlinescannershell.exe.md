---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Defender\Offline\OfflineScannerShell.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - defender
  - lolbin
aliases:
  - OfflineScannerShell.exe
  - Microsoft Defender Offline
url:
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-offline
---

**fullpath**:C:\Program Files\Windows Defender\Offline\OfflineScannerShell.exe

# description

OfflineScannerShell.exe belongs to Microsoft Defender Offline, the scanner that reboots a device into a trusted environment (via WinRE) to detect rootkits and MBR malware. Learn documents starting the offline scan from Windows Security, `Start-MpWDOScan` or WMI `MSFT_MpWDOScan`, and that the process starts from `C:\ProgramData\Microsoft\Windows Defender\Offline Scanner`. Related: MpCmdRun.exe, MsMpEng.exe.

## simple description

> ### 2026-11-21 Claude said
> OfflineScannerShell.exe is a part of Microsoft Defender that runs the offline scan. When a user chooses "Microsoft Defender Offline scan", Windows prepares the scanner, restarts, scans outside the normal OS and boots back. It is a normal component of Windows Defender. It is not run directly by users.
>
> **SOC NOTE**: LOLBAS: when run from a folder containing an attacker-supplied `mpclient.dll`, OfflineScannerShell.exe loads it (DLL search-order hijack, T1574.001), giving signed-binary execution. Alert on copies of OfflineScannerShell.exe outside its install folder or loading mpclient.dll from non-Defender paths. Event 2030/5007 in Windows Defender/Operational records offline scan scheduling.
>

# purpose

Run a Microsoft Defender Offline scan; requires Defender as primary AV, local admin rights and enabled WinRE.

# typical use cases

| usage | description |
| --- | --- |
| `Start-MpWDOScan` | Start a Defender Offline scan (reboots the device). |
| `wmic /namespace:\\root\Microsoft\Windows\Defender path MSFT_MpWDOScan call Start` | Trigger an offline scan through WMI. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
