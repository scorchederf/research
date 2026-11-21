---
created: 2026-11-21
fullpath: 'C:\Windows\System32\xwizard.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
aliases:
  - xwizard.exe
  - Extensible Wizards Host Process
url:
---

**fullpath**:C:\Windows\System32\xwizard.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

## simple description

> ### 2026-11-21 Claude said
> xwizard.exe is the Extensible Wizards Host Process, a built-in Windows program that hosts wizard-style setup dialogs implemented as COM objects. It can be told to run a specific wizard by its CLSID, for example with `xwizard RunWizard {GUID}`. Normal users rarely see it start directly.
>
> **SOC NOTE**: xwizard.exe is a known LOLBin: `xwizard RunWizard {CLSID}` loads any registered COM object, so attackers register a malicious InprocServer32 DLL under HKCU\Software\Classes\CLSID and get it executed by a signed binary (MITRE ATT&CK T1218, T1546.015 COM hijacking). It can also be copied to a writable folder to side-load a fake xwizards.dll (T1574.002). Alert on xwizard.exe with RunWizard arguments, running outside System32, or loading DLLs from user paths.
> _Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
