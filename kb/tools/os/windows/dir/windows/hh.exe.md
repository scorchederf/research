---
created: 2026-11-21
fullpath: 'C:\Windows\hh.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - html-help
  - lolbin
aliases:
  - "hh.exe"
  - "Microsoft HTML Help Executable"
url: []
---

**fullpath**:C:\Windows\hh.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> hh.exe is the Microsoft HTML Help executable that opens compiled help files (.chm). Double-clicking a .chm file runs hh.exe, which renders the HTML content using the Internet Explorer engine. It also supports `hh.exe -decompile <folder> <file.chm>` to extract the HTML contents of a help file.
>
> **SOC NOTE**: Malicious .chm files are a common phishing payload: embedded HTML/script or ActiveX shortcut objects make hh.exe execute commands (T1218.001 Compiled HTML File). hh.exe spawning cmd.exe, powershell.exe, mshta.exe or making network connections is highly suspicious; also check the Zone.Identifier of the .chm and the hh.exe command line.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
