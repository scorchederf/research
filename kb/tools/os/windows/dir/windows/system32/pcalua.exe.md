---
created: 2026-11-21
fullpath: 'C:\Windows\System32\pcalua.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - pcalua.exe
  - Program Compatibility Assistant
url:
  - https://learn.microsoft.com/windows/compatibility/pca-scenarios-for-windows-8
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-pca
---

**fullpath**:C:\Windows\System32\pcalua.exe

# description

pcalua.exe is the Program Compatibility Assistant (PCA) launcher binary. Learn documents the Program Compatibility Assistant feature, which tracks desktop apps for known compatibility issues and offers fixes, but does not document pcalua.exe or its command line. PCA depends on the Diagnostic Policy Service and the Program Compatibility Assistant Service.

## simple description

> ### 2026-11-21 Claude said
> Pcalua.exe is a Windows helper that starts programs under the Program Compatibility Assistant, the feature that watches older apps for compatibility problems and offers to rerun them with compatibility settings. Windows uses it, for example, when launching installers or apps that may need compatibility fixes. It is a legitimate Microsoft-signed file in System32. Its common command line is `pcalua.exe -a <program>`.
>
> **SOC NOTE**: pcalua.exe is a known LOLBin: `pcalua.exe -a malware.exe` (or a DLL / remote UNC path) launches a payload with pcalua as the parent, which can bypass simple parent-process or application allowlist rules (MITRE ATT&CK T1202 Indirect Command Execution). Hunt for pcalua.exe with `-a` pointing to user-writable or network paths. PCA also leaves execution artifacts (e.g. `C:\Windows\appcompat\pca\PcaAppLaunchDic.txt` on Windows 11) useful for forensics.
>

# purpose

Program Compatibility Assistant helps end users run desktop apps designed for earlier Windows versions: it tracks apps when they run, detects symptoms of known compatibility issues, and offers or silently applies compatibility modes (for example PINDLL). It also shows hard/soft block messages for apps with known issues. Administrators can turn off PCA through policy (`DisablePcaUIPolicy`, "Turn off Program Compatibility Assistant").

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
