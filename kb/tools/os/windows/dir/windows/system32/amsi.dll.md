---
created: 2026-11-21
fullpath: 'C:\Windows\System32\amsi.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - dll
  - security
aliases:
  - "amsi.dll"
  - "Antimalware Scan Interface"
  - "AMSI"
url:
  - https://learn.microsoft.com/windows/win32/amsi/antimalware-scan-interface-portal
  - https://learn.microsoft.com/windows/win32/amsi/antimalware-scan-interface-functions
  - https://learn.microsoft.com/windows/win32/api/amsi/nf-amsi-amsiscanbuffer
  - https://learn.microsoft.com/defender-endpoint/amsi-on-mdav
---

**fullpath**: C:\Windows\System32\amsi.dll

# description

Amsi.dll implements the Windows Antimalware Scan Interface (AMSI), a vendor-agnostic interface that lets applications and services send content (buffers, strings, streams, URLs) to whatever antimalware product is installed for scanning. It exports functions such as `AmsiInitialize`, `AmsiOpenSession`, `AmsiScanBuffer`, `AmsiScanString`, `AmsiNotifyOperation`, `AmsiCloseSession` and `AmsiUninitialize` (header amsi.h, library Amsi.lib) and is available on Windows 10 / Windows Server 2016 and later. Microsoft Defender Antivirus uses it to detect fileless and script-based attacks.

## simple description

> ### 2026-11-21 Claude said
> amsi.dll is the bridge between script engines and your antivirus. Right before PowerShell, VBScript/JScript, Office macros or .NET run code, they hand the (already de-obfuscated) content to amsi.dll, which passes it to the registered AV provider (e.g. Defender's MpOav.dll) for a verdict. This lets AV catch malware that never touches disk. It is loaded into many processes, including powershell.exe.
>
> **SOC NOTE**: "AMSI bypass" is a standard attacker step (T1562.001 Impair Defenses): patching AmsiScanBuffer in memory, setting amsiInitFailed via reflection, or planting a fake amsi.dll next to a copied powershell.exe for DLL hijacking (T1574.001). Hunt for strings like `AmsiUtils`/`amsiInitFailed` in 4104 script-block logs, amsi.dll loaded from paths other than System32/SysWOW64 (Sysmon 7), and Defender AMSI detections (event 1116 with AMSI source).
>

# purpose

Provides the AMSI API for two audiences: application developers who want to request scans from inside their apps, and antimalware vendors who implement providers (IAntimalwareProvider). AMSI supports file, memory/stream scanning and URL/IP reputation checks, and sessions so that fragments of a payload can be correlated. Windows components integrated with AMSI include UAC (EXE, COM, MSI and ActiveX installation elevation), PowerShell (scripts, interactive use, dynamic code evaluation), Windows Script Host (wscript.exe/cscript.exe), JavaScript and VBScript, Office VBA macros, .NET Framework 4.8+ assembly scanning and WMI; Microsoft 365 Apps also cover JavaScript, VBA and XLM, and Exchange and SharePoint Server integrate with it. From Windows 10 version 1903, provider DLLs that are not Authenticode-signed may not be loaded. In Defender, AMSI is enabled by turning on script scanning.
