---
created: 2026-11-21
fullpath: 'C:\Windows\System32\rasautou.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "rasautou.exe"
  - "RAS AutoDial"
url:
  - https://learn.microsoft.com/windows/win32/rras/ras-autodial
  - https://learn.microsoft.com/windows/win32/rras/autodial-mapping-database
---

**fullpath**:C:\Windows\System32\rasautou.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

Microsoft Learn does not document rasautou.exe by name. It documents the related Remote Access Service (RAS) AutoDial feature and the AutoDial mapping database that the RAS Auto Connection Manager uses.

## simple description

> ### 2026-11-21 Claude said
> rasautou.exe is the Remote Access Dialer helper that Windows uses for the RAS AutoDial feature, prompting or dialing a VPN/dial-up connection when a network address cannot be reached. It is launched by the Remote Access Auto Connection Manager service. On modern systems it is rarely used. It accepts command-line switches to load a DLL and call a function.
>
> **SOC NOTE**: rasautou.exe is a known LOLBin: `rasautou -d <dll> -p <export>` loads an arbitrary DLL and calls an exported function, giving signed-binary proxy execution (MITRE ATT&CK T1218). Any execution with `-d`/`-p` arguments, or from a parent such as Office or a script host, should be treated as suspicious.
>

# purpose

Learn describes RAS AutoDial: when an attempt to connect to a network address fails, the system checks the AutoDial database for a matching Winsock or share name and can dial the stored or default connection. The AutoDial mapping database maps IP addresses, host names and NetBIOS names to RAS phone-book entries and can be managed with `RasSetAutodialAddress`, `RasGetAutodialAddress` and `RasEnumAutodialAddresses`.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
