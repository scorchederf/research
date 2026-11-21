---
created: 2026-11-21
fullpath: 'c:\windows\system32\zipfldr.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - dll
  - shell
aliases:
  - zipfldr.dll
  - Compressed (zipped) Folders
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/2004/ms04-034
  - https://learn.microsoft.com/security-updates/securitybulletins/2002/ms02-054
---

**fullpath**:c:\windows\system32\zipfldr.dll

# description

zipfldr.dll implements the Compressed (zipped) Folders feature of Windows, which lets users create, add files to, and extract files from .zip files as if they were folders in Windows Explorer. It is distinct from NTFS file compression. Its registration can be removed with `regsvr32 /u zipfldr.dll`.

## simple description

> ### 2026-11-21 Claude said
> zipfldr.dll is the Windows shell extension that lets File Explorer open .zip files like normal folders. When you double-click a zip or choose "Extract All" or "Send to > Compressed (zipped) folder", this DLL does the work inside explorer.exe. It is a standard, signed Windows component.
>
> **SOC NOTE**: It can be abused as a LOLBin proxy: `rundll32.exe zipfldr.dll,RouteTheCall <exe>` launches an arbitrary program (MITRE ATT&CK T1218.011). Phishing ZIPs opened through it are also the source of Mark-of-the-Web propagation questions; files extracted via Explorer normally keep MOTW. Hunt for rundll32 command lines referencing zipfldr.dll with RouteTheCall.

# purpose

Provides Compressed (zipped) Folders, storing files and folders in a compressed (.zip) format. Historical vulnerabilities (MS02-054, MS04-034) involved unchecked buffers when processing crafted zip files and incorrect target paths during decompression. As a workaround Microsoft documented unregistering it with `regsvr32 /u zipfldr.dll` (disabling the feature until re-registered with `regsvr32 zipfldr.dll`).
