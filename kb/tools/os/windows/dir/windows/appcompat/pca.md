---
created: 2026-11-21
fullpath: 'C:\Windows\AppCompat\pca'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - appcompat
  - forensics
aliases:
  - "pca"
  - "Program Compatibility Assistant"
url:
  - https://learn.microsoft.com/windows/win32/w8cookbook/pca-scenarios-for-windows-8
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-appcompat
---

**fullpath**:C:\Windows\AppCompat\pca

# description

Folder used by the Program Compatibility Assistant (PCA), the Windows feature that tracks apps run by users and offers compatibility fixes. Learn documents PCA and its policy controls but not this folder's contents.

## simple description

> ### 2026-11-21 Claude said
> This folder is used by the Program Compatibility Assistant, which watches programs you run and suggests compatibility fixes.
> On Windows 11 22H2+ it contains text files such as PcaAppLaunchDic.txt and PcaGeneralDb0.txt that record executables launched and their times.
> The PCA service (PcaSvc) writes them.
>
> **SOC NOTE**: Valuable execution evidence (Windows 11 22H2+): PcaAppLaunchDic.txt lists full paths and last-execution timestamps of programs run from Explorer, even if the binary is deleted; useful alongside Prefetch/Amcache for T1204 user execution and malware launch timelines.
>

# purpose

Supports the Program Compatibility Assistant. PCA tracks apps, detects symptoms of known compatibility issues and recommends fixes. The PCA requires the Diagnostic Policy Service and Program Compatibility Assistant Service to be running and can be turned off with the 'Turn off Program Compatibility Assistant' policy.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
