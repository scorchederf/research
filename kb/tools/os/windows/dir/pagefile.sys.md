---
created: 2026-11-21
fullpath: 'C:\pagefile.sys'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - memory
  - paging
aliases:
  - pagefile.sys
  - Pagefile.sys
  - paging file
  - page file
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/ram-virtual-memory-pagefile-management
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/cannot-set-page-files-on-partition-larger-than-2-tb
  - https://learn.microsoft.com/biztalk/technical-guides/operating-system-optimizations
---

**fullpath**:C:\pagefile.sys

# description

`Pagefile.sys` is the Windows paging file stored in the root of a partition; when memory used by processes exceeds available RAM, Windows moves 4-KB pages of virtual address space to it. Its location and size are configured in System Properties (Advanced > Performance > Settings) or with `wmic pagefileset`.

## simple description

> ### 2026-11-21 Claude said
> pagefile.sys is Windows' swap file: when RAM fills up, Windows writes less-used memory pages to this hidden file in the root of C:. It lets the system use more memory than is physically installed. It is also needed for writing crash dumps.
>
> **SOC NOTE**: Forensic gold: can contain fragments of process memory, command lines, URLs, credentials and malware strings that were paged out, even after the process ended. Acquire it from disk images (locked while running; use raw-copy tools). Optionally cleared at shutdown via the ClearPageFileAtShutdown policy; attackers rarely touch it but its contents can be searched with strings/YARA.
>

# purpose

Stores paged-out memory so virtual memory can exceed RAM; there can be one per partition. A typical starting size is 1.5 times installed RAM. Removing the paging file from the boot partition prevents Windows from writing a kernel crash dump (MEMORY.DMP); a crash dump requires a paging file of at least physical memory + 1 MB on the boot partition. The `Paging File\% Usage` counter shows how much is used.
