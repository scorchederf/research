---
created: 2026-11-21
fullpath: 'c:\windows\system32\ieadvpack.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - dll
  - internet-explorer
  - setup
aliases:
  - "ieadvpack.dll"
  - "IE Advanced INF Package"
url: []
---

**fullpath**:c:\windows\system32\ieadvpack.dll

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> ieadvpack.dll is an Internet Explorer-era helper library that provides 'Advanced INF' setup functions, essentially the IE-branded copy of advpack.dll. It exposes exports such as LaunchINFSection, LaunchINFSectionEx and RegisterOCX that run sections of an INF file or register components. Legitimate installers and IE components call it through rundll32.exe. It ships with Windows in System32 (and SysWOW64).
>
> **SOC NOTE**: Classic LOLBin (MITRE ATT&CK T1218.011 Rundll32). Attackers run `rundll32.exe ieadvpack.dll,LaunchINFSection <file>.inf,DefaultInstall_SingleUser,1,` or `RegisterOCX <payload>` to execute code or scriptlets via a signed Microsoft DLL and bypass application control. Hunt for rundll32 command lines referencing ieadvpack/advpack with LaunchINFSection, RegisterOCX or INF paths in user-writable folders (Sysmon EID 1 / Security 4688).
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
