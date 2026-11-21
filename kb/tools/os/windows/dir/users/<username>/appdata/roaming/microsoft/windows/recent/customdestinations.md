---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - jump-lists
aliases:
  - "CustomDestinations"
  - "Custom Jump Lists"
url:
  - https://learn.microsoft.com/windows/win32/api/shobjidl_core/nn-shobjidl_core-icustomdestinationlist
  - https://learn.microsoft.com/windows/win32/shell/taskbar-extensions
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations

# description

Learn documents custom Jump Lists, built by applications through the ICustomDestinationList interface (CLSID_DestinationList) for display on the taskbar. It does not document this folder path.

## simple description

> ### 2026-11-21 Claude said
> This folder stores the custom Jump Lists that applications build for their taskbar and Start menu icons. Each file is named with an AppID hash and the extension `.customDestinations-ms`. Browsers and Office apps commonly create them.
>
> **SOC NOTE**: Jump list files record recently or frequently opened items per application, even after the original file is deleted, and are a staple of user-activity forensics (parse with JLECmd). They show files, remote hosts (e.g. mstsc) and URLs a user accessed; companion automatic lists are in the AutomaticDestinations folder.
>

# purpose

Applications use ICustomDestinationList to define custom categories and tasks in place of or in addition to the Recent and Frequent categories; the application must honor items the user removed.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
