---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - jumplist
  - forensics
aliases:
  - AutomaticDestinations
  - Jump Lists
url:
  - https://learn.microsoft.com/windows/win32/shell/taskbar-extensions
  - https://learn.microsoft.com/windows/win32/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs
  - https://learn.microsoft.com/answers/a/1989869
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations

# description

Per-user folder holding the Windows-managed ("automatic") Jump List data for the Recent and Frequent categories of taskbar/Start Jump Lists. Entries are populated via SHAddToRecentDocs, which the Shell calls automatically when files are opened through Explorer or the common file dialog. Deleting its files clears recent items for all applications.

## simple description

> ### 2026-11-21 Claude said
> This folder stores the Jump Lists Windows keeps for each program: the recent and frequent files you see when you right-click a taskbar icon. Each file is named after an AppID hash and ends in .automaticDestinations-ms. Windows updates them automatically as you open files.
>
> **SOC NOTE**: Key forensic artifact for file and folder access (evidence of execution/opening): each file is an OLE compound file with embedded LNK data showing target paths, timestamps, volume serials and network shares, and it survives target deletion. Clearing this folder suggests anti-forensics (T1070.004). Parse with JLECmd.
>

# purpose

Stores automatic destination lists (Recent/Frequent) that back each application's Jump List; apps can remove entries via IApplicationDestinations.

# common files found

- `<AppID hash>.automaticDestinations-ms` - one per application Jump List
