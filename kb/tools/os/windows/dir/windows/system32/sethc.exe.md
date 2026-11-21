---
created: 2026-11-21
fullpath: 'C:\Windows\System32\sethc.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - accessibility
aliases:
  - sethc.exe
  - StickyKeys
url:
  - https://learn.microsoft.com/windows/win32/winauto/built-in-accessibility-features
  - https://learn.microsoft.com/windows/win32/api/winuser/ns-winuser-stickykeys
---

**fullpath**:C:\Windows\System32\sethc.exe

# description

sethc.exe is the Windows StickyKeys accessibility component. Learn documents the StickyKeys feature: when on, a user can press a modifier key (SHIFT, CTRL, ALT) and then another key in sequence instead of simultaneously, and the feature's hot key is pressing SHIFT five times. Applications control it via `SystemParametersInfo` with `SPI_GETSTICKYKEYS`/`SPI_SETSTICKYKEYS` and the `STICKYKEYS` structure.

## simple description

> ### 2026-11-21 Claude said
> sethc.exe is the program that pops up when you press Shift five times, asking whether to turn on Sticky Keys. Sticky Keys helps people who cannot hold several keys at once. Because the shortcut works on the logon screen, sethc.exe can run before anyone signs in.
>
> **SOC NOTE**: Classic backdoor: replacing sethc.exe with cmd.exe, or setting an Image File Execution Options Debugger for sethc.exe, gives a SYSTEM shell at the logon/RDP screen by pressing Shift five times (MITRE ATT&CK T1546.008 Accessibility Features). Check the file hash/signature and size against the original, IFEO registry keys, and sethc.exe spawning cmd.exe/powershell.exe from winlogon.
>

# purpose

Provides the StickyKeys hot key behaviour. The `SKF_HOTKEYACTIVE` flag lets the user turn StickyKeys on and off by pressing SHIFT five times; `SKF_CONFIRMHOTKEY` shows a confirmation dialog when activated by the hot key; `SKF_HOTKEYSOUND` plays a siren sound when toggled.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
