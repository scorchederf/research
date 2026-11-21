---
created: 2026-11-21
fullpath: 'c:\windows\system32\shimgvw.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - dll
  - imaging
aliases:
  - 'shimgvw.dll'
  - 'Windows Picture and Fax Viewer'
  - 'Windows Photo Viewer'
url: []
---

**fullpath**: c:\windows\system32\shimgvw.dll

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> shimgvw.dll is the library behind the classic Windows Picture and Fax Viewer (XP) and Windows Photo Viewer (Vista/7 and later, still present on Windows 10/11). It is not a standalone program; it is launched through rundll32 with the ImageView_Fullscreen export to display an image. It also provides image preview/slideshow functions to Explorer.
>
> **SOC NOTE**: LOLBin-style abuse: `rundll32.exe shimgvw.dll,ImageView_Fullscreen <URL>` has been documented as a way to download a file from a remote URL into the INetCache (T1218.011, T1105). Alert on rundll32 command lines with shimgvw.dll and http/https arguments. Historic vulnerabilities in image parsing (e.g., WMF/GDI) were triggered through this viewer.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_


