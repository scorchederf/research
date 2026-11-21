---
created: 2026-11-21
fullpath: 'C:\Windows\WinSxS'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - component-store
  - servicing
aliases:
  - 'WinSxS'
  - 'Windows Component Store'
  - 'side-by-side'
url:
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/manage-the-component-store?view=windows-11
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/determine-the-actual-size-of-the-winsxs-folder?view=windows-11
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder?view=windows-11
  - https://learn.microsoft.com/windows/deployment/update/forward-reverse-differentials
---

**fullpath**:C:\Windows\WinSxS

# description

`C:\Windows\WinSxS` is the Windows Component Store, which holds the components that make up Windows plus side-by-side assemblies. It is managed by servicing (Windows Update, DISM, Server Manager) and is cleaned up by DISM `/StartComponentCleanup` and Disk Cleanup.

## simple description

> ### 2026-11-21 Claude said
> WinSxS is where Windows keeps every version of its system components so it can install updates, turn features on/off, roll back updates and repair corrupted files. Many files here are hard-linked into System32, so it looks larger in Explorer than it really is. You should never delete it manually.
>
> **SOC NOTE**: A trove of signed Microsoft binaries, including older vulnerable versions, which attackers can copy or side-load (DLL side-loading with WinSxS assemblies, T1574.002) or use to find LOLBins outside monitored System32 paths. Execution of binaries directly from WinSxS by non-servicing processes is unusual and worth alerting on. Also a source for comparing known-good file versions during forensics.
>

# purpose

The component store supports customization and updating of Windows: installing new component versions through Windows Update, enabling/disabling features, adding roles, moving between editions, recovery from corruption or boot failures, uninstalling problematic updates and running programs using side-by-side assemblies. Files are often hard linked to locations elsewhere in Windows. Deleting files from WinSxS or the whole folder might severely damage the system.

# common files found

| item | description |
| --- | --- |
| Component files (hydrated/full files) | Files for each component version, many hard linked into other Windows folders. |
| `f` subfolders | Forward differentials staged for updates. |
| `r` subfolders | Reverse differentials used to return to the base version. |
| `n` subfolders | Null compressed files. |
| Component manifests | Used by corruption repair to detect missing files and get hashes. |

