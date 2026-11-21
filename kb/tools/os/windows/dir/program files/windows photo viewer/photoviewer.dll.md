---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Photo Viewer\PhotoViewer.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - dll
  - lolbin
aliases:
  - PhotoViewer.dll
  - Windows Photo Viewer
url:
  - https://learn.microsoft.com/windows/win32/wic/-wic-rawguidelines-intro-vista
---

**fullpath**:C:\Program Files\Windows Photo Viewer\PhotoViewer.dll

# description

PhotoViewer.dll implements Windows Photo Viewer, the classic image viewer from Windows 7. Learn mentions Windows 7 Photo Viewer only as an application that uses the Windows Imaging Component (WIC) and so supports RAW image formats when the matching codecs are installed; the DLL itself is not documented.

## simple description

> ### 2026-11-21 Claude said
> This DLL is the legacy Windows Photo Viewer. It has no .exe of its own: it is started through `rundll32.exe` with the `ImageView_Fullscreen` export. On Windows 10/11 it is still present but not registered as the default viewer; the Photos app replaced it.
>
> **SOC NOTE**: Normal invocation looks like `rundll32.exe "C:\Program Files\Windows Photo Viewer\PhotoViewer.dll", ImageView_Fullscreen <image>`. Because it is reached via rundll32 (MITRE T1218.011), unusual arguments, a non-image path, or a PhotoViewer.dll outside this folder deserve scrutiny. Registry changes re-enabling Photo Viewer file associations are typically benign tweaks.
>

# purpose

Provides the Windows Photo Viewer image viewing functionality, which uses WIC for decoding, including RAW formats through installed WIC codecs.
