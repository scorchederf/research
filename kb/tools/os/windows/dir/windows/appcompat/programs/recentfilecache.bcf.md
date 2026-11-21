---
created: 2026-11-21
fullpath: 'C:\Windows\AppCompat\Programs\RecentFileCache.bcf'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - appcompat
  - forensics
aliases:
  - "RecentFileCache.bcf"
url: []
---

**fullpath**: C:\Windows\AppCompat\Programs\RecentFileCache.bcf

# description

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

## simple description

> ### 2026-11-21 Claude said
> RecentFileCache.bcf is a small Application Compatibility cache file found on Windows 7 and Windows Server 2008 R2. It records the full paths of executables recently run on the system, written by the Application Experience (AeLookupSvc/ProgramDataUpdater) components. On Windows 8 and later it was replaced by Amcache.hve in the same folder. It holds only paths, not timestamps for each entry.
>
> **SOC NOTE**: Useful evidence of execution on Windows 7 systems, especially for programs run from removable media, temp or user folders that no longer exist (T1204 User Execution investigations). Entries are cleared/rolled over when the ProgramDataUpdater task runs, so it reflects recent activity only. Parse with tools such as RecentFileCacheParser and correlate with Prefetch, ShimCache and Amcache.
>
> _Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_
