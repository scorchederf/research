---
created: 2026-11-21
fullpath: 'C:\Windows\System32\SearchIndexer.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - search
aliases:
  - "SearchIndexer.exe"
  - "Windows Search Indexer"
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/shell-experience/windows-search-performance-issues
  - https://learn.microsoft.com/windows/win32/search/-search-indexing-process-overview
  - https://learn.microsoft.com/windows/win32/search/-search-3x-wds-overview
---

**fullpath**:C:\Windows\System32\SearchIndexer.exe

# description

SearchIndexer.exe is the Windows Search indexer process (Windows Search service, WSearch). It runs as a Windows service in the LocalSystem account and maintains a single shared index; related host processes are the search protocol host and filter host.

## simple description

> ### 2026-11-21 Claude said
> SearchIndexer.exe is the background process that builds the Windows Search index so file, email and Start menu searches are fast. It runs as the Windows Search (WSearch) service under SYSTEM. It slows down or pauses when the PC is busy or on battery.
>
> **SOC NOTE**: Normally a child of services.exe running as SYSTEM from System32; any other path or parent is suspicious masquerading (MITRE ATT&CK T1036). The index database `%ProgramData%\Microsoft\Search\Data\Applications\Windows\Windows.edb` is a forensic artifact that can reveal file names and even content of deleted files.
>

# purpose

Indexes properties and content of files and data stores in three stages (queue URLs, crawl URLs, update the index) under the gatherer. It throttles or pauses on high CPU, high I/O, low memory, low battery or low disk space. Task Manager can confirm the searchindexer.exe process is running when the indexer is not reporting status.

# typical use cases

| usage | description |
| --- | --- |
| `Sc config wsearch start=disabled` | Disables the Windows Search service before defragmenting the index. |
| `Net stop wsearch` | Stops the Windows Search service. |
| `EsentUtl.exe /d %AllUsersProfile%\Microsoft\Search\Data\Applications\Windows\Windows.edb` | Defragments the index database to reclaim space. |
| `Sc config wsearch start=delayed-auto` | Restores delayed automatic start. |
| `Net start wsearch` | Starts the Windows Search service. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
