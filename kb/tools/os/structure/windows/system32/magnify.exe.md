---
created: 2026-11-21
fullpath: 'C:\Windows\System32\magnify.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - magnify.exe
  - Magnifier
url:
  - https://learn.microsoft.com/windows/configuration/windows-backup/catalog
  - https://learn.microsoft.com/windows/win32/winauto/magapi/entry-magapi-sdk
  - https://learn.microsoft.com/windows-insider/release-notes/beta/preview-build-26220-9836
---

**fullpath**:C:\Windows\System32\magnify.exe

# description

Magnifier is the Windows accessibility tool configured under **Settings > Accessibility > Magnifier**, with settings such as zoom level, zoom increment, view (docked, full screen, lens), invert colors and starting before or after sign-in. Learn documents the related Magnification API (Magnification.dll) for building assistive magnifier applications; the executable itself is not documented.

## simple description

> ### 2026-11-21 Claude said
> Magnify.exe is Windows Magnifier, an Ease of Access tool that zooms part or all of the screen for people with low vision. It starts with Windows key + Plus (+) and can run in full screen, lens or docked mode. It can be configured to start before sign-in, from the logon screen. It is a signed Microsoft binary in System32.
>
> **SOC NOTE**: Like sethc.exe and utilman.exe, magnify.exe is an accessibility binary reachable from the logon screen, so attackers replace it or set an Image File Execution Options `Debugger` value on it to get a SYSTEM shell without logging in (MITRE ATT&CK T1546.008 Accessibility Features). Check file hash/signature of magnify.exe, `HKLM\...\Image File Execution Options\magnify.exe` and magnify.exe spawning cmd.exe or running as SYSTEM via winlogon.
>

# purpose

Magnify screen content for low-vision users, with settings for zoom level and increment, view mode, following mouse/keyboard focus/text cursor, invert colors and starting before or after sign-in.

# typical use cases

- Toggle Magnifier with Windows key + Plus (+); zoom with Windows key + Plus/Minus or Ctrl + Alt + mouse wheel.
- Configure per-display zoom and view locking in **Accessibility > Magnifier**.

# options

| option    | description    |
| --- | --- |
| | _Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_ |
