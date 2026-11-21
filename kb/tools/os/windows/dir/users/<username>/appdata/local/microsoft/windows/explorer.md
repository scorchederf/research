---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Windows\Explorer'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - user-profile
aliases:
  - Explorer
url:
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\Windows\Explorer

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This per-user folder holds File Explorer's cache databases, mainly thumbcache_*.db (thumbnail images) and iconcache_*.db (icon images). Windows uses them to display thumbnails and icons quickly. Deleting them is safe; Windows rebuilds them.
>
> **SOC NOTE**: Thumbcache databases can retain thumbnails of images and documents that the user viewed even after the originals are deleted or were on removable/network drives, making them useful evidence of file knowledge (parse with Thumbcache Viewer). Clearing these caches can indicate anti-forensics (MITRE ATT&CK T1070.004).
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
