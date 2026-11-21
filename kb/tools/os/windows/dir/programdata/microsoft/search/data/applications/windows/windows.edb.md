---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - windows-search
  - ese-database
aliases:
  - Windows.edb
  - Windows.db
  - Windows Search index database
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/shell-experience/windows-search-performance-issues
  - https://learn.microsoft.com/troubleshoot/windows-client/shell-experience/larger-windowsdotedb-file
  - https://learn.microsoft.com/windows/win32/search/-search-3x-wds-overview
  - https://learn.microsoft.com/windows/win32/extensible-storage-engine/extensible-storage-engine-files
---

**fullpath**:C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb

# description

`Windows.edb` is the Windows Search index database, an Extensible Storage Engine (ESE) database maintained by the Windows Search service (WSearch) running as LocalSystem. On Windows 11 the index is `Windows.db` in the same folder. It is managed through Indexing Options and can be defragmented offline with `EsentUtl.exe /d`.

## simple description

> ### 2026-11-21 Claude said
> Windows.edb is the database behind Windows Search. The indexer service reads files, emails (such as Outlook PSTs) and their properties and stores the extracted text and metadata here so searches are fast. It can grow to many gigabytes. Windows 11 replaced it with a SQLite-based Windows.db.
>
> **SOC NOTE**: High forensic value: it can retain file names, paths, timestamps, and even content snippets of documents and emails, sometimes for files that have since been deleted. Parse with tools such as ESEDatabaseView, SIDR or WinSearchDBAnalyzer (copy it offline first, it is locked by the service). Attackers may stop WSearch or delete the index to hide traces.
>

# purpose

Stores the search catalog: since Windows 8 both properties and persistent indexes are kept in Windows.edb (Windows 7 kept persistent indexes in separate *.ci files), and the full contents of files are indexed regardless of size, so the file grows with indexed content such as PST files. Use the **Size on disk** property to check its real size because of sparse ESE/NTFS compression. Reduce it by indexing less content and rebuilding the index, or defragment offline: `sc config wsearch start=disabled`, `net stop wsearch`, `EsentUtl.exe /d %AllUsersProfile%\Microsoft\Search\Data\Applications\Windows\Windows.edb`, `sc config wsearch start=delayed-auto`, `net start wsearch`.
