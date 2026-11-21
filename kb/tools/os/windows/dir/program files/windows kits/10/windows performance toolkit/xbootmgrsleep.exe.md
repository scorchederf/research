---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - xbootmgrsleep.exe
url:
---

**fullpath**:C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> xbootmgrsleep.exe is a helper binary shipped with the Windows Performance Toolkit in the Windows ADK. It is used alongside xbootmgr.exe, the legacy command-line tool that captures ETW traces across boot, shutdown, standby and hibernate transitions. The helper handles putting the machine to sleep/hibernate and resuming during those trace scenarios. Modern guidance uses WPR's on/off scenarios instead.
>
> **SOC NOTE**: Rarely seen outside developer or OEM performance-testing machines; presence is benign if the ADK is installed. It can force sleep/hibernate transitions, so unexpected execution from a non-ADK path or by a non-admin user deserves a look. Check path and signer to rule out masquerading (T1036).
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
