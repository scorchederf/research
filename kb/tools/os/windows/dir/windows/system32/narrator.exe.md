---
created: 2026-11-21
fullpath: 'C:\Windows\System32\narrator.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - accessibility
aliases:
  - narrator.exe
  - Narrator
url:
  - https://learn.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-embedded-keyboardfilterservice-windowsenter
  - https://learn.microsoft.com/exchange/accessibility/get-started-using-screen-reader
  - https://learn.microsoft.com/windows/configuration/windows-backup/catalog
  - https://learn.microsoft.com/windows-insider/archive/new-in-rs5
---

**fullpath**:C:\Windows\System32\narrator.exe

# description

Narrator is the screen reader built into Windows. It reads aloud text and UI elements and lets users control the device with a keyboard, controller or touch gestures; it is configured under Settings > Accessibility > Narrator.

## simple description

> ### 2026-11-21 Claude said
> Narrator is the Windows built-in screen reader that speaks what is on the screen for people who are blind or have low vision. It can be started with Windows logo key + Ctrl + Enter and also from the sign-in screen. It runs as `narrator.exe` in the user's session. Seeing it start once by accident is common and harmless.
>
> **SOC NOTE**: Like other accessibility binaries (sethc.exe, utilman.exe), narrator.exe can be replaced or hijacked via an IFEO `Debugger` value to get a SYSTEM shell at the logon screen (MITRE T1546.008 Accessibility Features). Narrator has also been abused for DLL hijacking (MSTTSLocEnUS.dll in System32\Speech\Engines). Check file hash/signature and look for `Image File Execution Options\narrator.exe` registry keys, and Narrator spawned by winlogon/utilman followed by a cmd.exe child.
>

# purpose

Turns Narrator on or off. Learn documents the keyboard shortcuts used to start it: **Windows logo key + Enter** on a PC (Windows 10 and earlier), **Windows logo button + Volume Up** on a tablet, and **Windows logo key + Ctrl + Enter** on current versions. The Windows logo key + Enter combination can be blocked with the Keyboard Filter `WindowsEnter` setting. Features include Scan Mode (**Caps lock + Spacebar**), a standard keyboard layout, Narrator QuickStart and a commands list (**Caps + F1**).

# typical use cases

| usage | description |
| --- | --- |
| `narrator.exe` | Start Narrator. |
| `Windows logo key + Ctrl + Enter` | Turn Narrator on or off with the keyboard. |
| `Caps lock + Spacebar` | Toggle Narrator Scan Mode. |
| `Caps + F1` | Show the Narrator commands list. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
