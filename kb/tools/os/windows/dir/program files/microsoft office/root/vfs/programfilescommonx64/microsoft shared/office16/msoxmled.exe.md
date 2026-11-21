---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Office\root\vfs\ProgramFilesCommonX64\Microsoft Shared\Office16\msoxmled.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - microsoft-office
aliases:
  - "msoxmled.exe"
  - "Microsoft Office XML Editor"
url: []
---

**fullpath**: C:\Program Files\Microsoft Office\root\vfs\ProgramFilesCommonX64\Microsoft Shared\Office16\msoxmled.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> msoxmled.exe is the "Microsoft Office XML Editor" helper shipped with Microsoft 365 Apps / Office 2016+. It is registered as the handler for .xml files that carry an Office `mso-application` processing instruction and opens them in the right Office app (Word, Excel, InfoPath, etc.). The `root\vfs\ProgramFilesCommonX64` part of the path is the Click-to-Run virtual file system that maps to `C:\Program Files\Common Files`.
>
> **SOC NOTE**: Because it launches Office applications to open XML documents, msoxmled.exe can appear as the parent of WINWORD/EXCEL when a user opens a malicious Office-XML (Flat OPC / WordprocessingML) attachment - a common phishing vector (T1566.001, T1204.002). Unexpected child processes under that chain, or msoxmled.exe running from a non-Office path, deserve investigation.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_
