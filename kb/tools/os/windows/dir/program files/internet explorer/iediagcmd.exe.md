---
created: 2026-11-21
fullpath: 'C:\Program Files\Internet Explorer\iediagcmd.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - internet-explorer
aliases:
  - iediagcmd.exe
  - IEDiagCMD
url:
  - https://learn.microsoft.com/answers/a/8192702
---

**fullpath**:C:\Program Files\Internet Explorer\iediagcmd.exe

# description

IEDiagCMD.exe is part of a suite of Microsoft tools that help users and IT professionals diagnose and troubleshoot Internet Explorer issues. It ships with Internet Explorer (copies also appear under WinSxS ie-setup-support component folders), alongside ie4uinit.exe, the Internet Explorer per-user initialization binary.

## simple description

> ### 2026-11-21 Claude said
> iediagcmd.exe is the Internet Explorer diagnostics command-line tool. It gathers network, proxy and browser configuration details to help troubleshoot IE problems, and it runs other system utilities (such as ipconfig, netsh and route) to collect that data. It is legitimate and signed by Microsoft. Most users never run it directly.
>
> **SOC NOTE**: iediagcmd.exe is a documented LOLBin: because it launches helper tools like ipconfig.exe and netsh.exe by name, attackers can set a modified working directory or path and have it execute a planted binary (MITRE ATT&CK T1218 System Binary Proxy Execution, T1574 hijack execution flow). Alert on iediagcmd.exe spawning processes outside System32 or being run on systems where IE is retired.
>

# purpose

Collect diagnostic information to troubleshoot Internet Explorer problems.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
