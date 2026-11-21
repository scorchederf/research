---
created: 2026-11-21
fullpath: 'C:\Windows\System32\pcwrun.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "pcwrun.exe"
  - "Program Compatibility Troubleshooter Wizard"
url: []
---

**fullpath**:C:\Windows\System32\pcwrun.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> pcwrun.exe is the Program Compatibility Troubleshooter Wizard launcher, used to start the compatibility troubleshooter for a specific program. It takes the path of a program as an argument and starts the MSDT-based compatibility diagnostic. It is Microsoft-signed and lives in System32.
>
> **SOC NOTE**: A known LOLBin: `pcwrun.exe <path>` launches the target executable as a child of pcwrun/msdt, which can be used for proxy execution and parent-process evasion (MITRE ATT&CK T1218, T1202 Indirect Command Execution). It was also referenced in Follina-style (CVE-2022-30190) MSDT abuse. Investigate any pcwrun.exe launching non-installer programs or running from scripts.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
