---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - windows
aliases:
  - "Recent"
  - "Recent Items"
  - "FOLDERID_Recent"
  - "CSIDL_RECENT"
  - "My Recent Documents"
url:
  - https://learn.microsoft.com/windows/win32/shell/knownfolderid
  - https://learn.microsoft.com/windows/win32/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs
  - https://learn.microsoft.com/windows/win32/shell/manage
  - https://learn.microsoft.com/windows/win32/shell/csidl
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent

# description

The per-user Recent Items known folder (FOLDERID_Recent {AE50C081-EBD2-438A-8655-8A092E34987A}, CSIDL_RECENT), default path `%APPDATA%\Microsoft\Windows\Recent` (legacy `%USERPROFILE%\Recent`). It holds shortcuts to the user's most recently used documents and is maintained by the Shell through `SHAddToRecentDocs`.

## simple description

> ### 2026-11-21 Claude said
> This folder contains .lnk shortcut files pointing to files and folders the user recently opened. Windows adds them automatically when you open items in Explorer or through common file dialogs. Its AutomaticDestinations and CustomDestinations subfolders store Jump List data. Each shortcut records the target path, and timestamps.
>
> **SOC NOTE**: A top forensic artifact for proving file and folder access (MITRE ATT&CK collection/discovery context): LNK files keep target path, volume serial, MAC times, and sometimes network share or removable-drive details even after the target is deleted. Jump Lists show per-application history. Attackers may clear it (T1070.004 File Deletion), and malicious .lnk files elsewhere are an initial-access vector (T1204.002).
>

# purpose

Contains shortcuts to the user's most recently used documents. Applications should not modify it directly; calling `SHAddToRecentDocs` adds a link, updates the Recent/Frequent lists of the application's Jump List and the Recent Items menu, and can also clear the folder. Executable (.exe) files are filtered out of the list, items represented by an IShellLink are not added, and folders appear only in Explorer's Jump List.

# common files found

| file | description |
| --- | --- |
| `*.lnk` | Shortcuts to recently used documents added by SHAddToRecentDocs. |
