---
created: 2026-11-21
fullpath: 'C:\Windows\System32\spool\drivers\color'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - print
  - color-management
  - icc
aliases:
  - "color"
  - "Windows COLOR directory"
url:
  - https://learn.microsoft.com/windows-hardware/drivers/print/locating-icc-profiles
  - https://learn.microsoft.com/windows/win32/api/_wcs/
---

**fullpath**:C:\Windows\System32\spool\drivers\color

# description

The Windows COLOR directory, where color profiles used by the Windows Color System (WCS) / ICM are installed. Its path is returned by the GetColorDirectory function; GDI searches it for ICC profiles installed for a printer type. Related APIs include the WCS profile management functions and UpdateICMRegKey.

## simple description

> ### 2026-11-21 Claude said
> This folder holds color profiles (.icc/.icm, plus WCS .cdmp/.camp/.gmmp files) that Windows uses to show and print colors accurately for monitors, printers and scanners. Drivers and display tools install profiles here and Windows associates them with devices.
>
> **SOC NOTE**: Writable by drivers/installers and rarely monitored, so it has been used as a hiding spot for dropped payloads; files here that are not color profiles (e.g. .exe, .dll, .ps1) are suspicious (T1036). Several past vulnerabilities involved malformed ICC profile parsing.
>

# purpose

Holds installed color profiles. When color management is enabled for printing, GDI first asks the driver (DrvQueryColorProfile); otherwise it searches the color directory for profiles installed for the printer type matching resolution, media type and dithering in the DEVMODE, and falls back to the system's default sRGB profile.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
