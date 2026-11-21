---
created: 2026-11-21
fullpath: 'c:\windows\system32\eudcedit.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - eudcedit.exe
  - Private Character Editor
  - EUDC editor
url:
  - https://learn.microsoft.com/windows/win32/intl/character-sets-and-fonts
  - https://learn.microsoft.com/windows/win32/intl/end-user-defined-characters
  - https://learn.microsoft.com/windows/win32/intl/eudc
---

**fullpath**:c:\windows\system32\eudcedit.exe

# description

eudcedit.exe is the Windows EUDC editor (Private Character Editor). Learn describes end-user-defined characters (EUDC) in double-byte character sets and private use area (PUA) characters in Unicode, which users create with an EUDC editor and which are associated with fonts through the HKEY_CURRENT_USER\EUDC registry key.

## simple description

> ### 2026-11-21 Claude said
> Private Character Editor lets users draw their own characters (glyphs) and assign them to reserved code points, mainly for East Asian names or symbols missing from standard fonts. The characters are saved into EUDC font files (.tte) and linked via the registry. It is a GUI tool built into Windows. Most users never run it.
>
> **SOC NOTE**: Rarely used, so execution on corporate endpoints is unusual. It has appeared in UAC-bypass/LOLBin research because it auto-elevates and its file dialogs can spawn processes (T1548.002). Treat child processes of eudcedit.exe (cmd, powershell) as suspicious.
>

# purpose

Create and edit end-user-defined characters (EUDC) and Unicode private use area (PUA) characters by adding glyphs to a font at chosen code values. The system default EUDC font is set by the SystemDefaultEUDCFont value under the EUDC key.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
