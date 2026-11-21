---
created: 2026-11-21
fullpath: 'C:\$Recycle.Bin\<SID>'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - recycle-bin
  - forensics
aliases:
  - "<SID>"
  - "$Recycle.Bin"
  - "Recycle Bin"
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/2000/ms00-007
  - https://learn.microsoft.com/troubleshoot/windows-client/shell-experience/recycle-bin-corrupted
  - https://learn.microsoft.com/windows/win32/shell/datascenarios
---

**fullpath**:C:\$Recycle.Bin\<SID>

# description

Each user's Recycle Bin on a volume maps to a folder whose name is based on the owner's SID; the folder is created the first time the user deletes a file and the owner is given sole permissions to it. The Recycle Bin is a Windows Shell virtual folder that holds files that are no longer needed until it is emptied.

## simple description

> ### 2026-11-21 Claude said
> When a user deletes a file in Explorer, Windows moves it into `C:\$Recycle.Bin\<their SID>` instead of erasing it, so it can be restored. Each deleted item produces two files: `$I<random>.<ext>` (metadata: original path, size and deletion time) and `$R<random>.<ext>` (the actual content). Every volume has its own `$Recycle.Bin` folder with one SID subfolder per user who has deleted something there. The folder is hidden and system-protected.
>
> **SOC NOTE**: Very high forensic value: `$I` files prove a user deleted a specific file and when (T1070.004 File Deletion), and `$R` files let you recover it; map the SID to a user via the ProfileList key. Malware sometimes hides payloads in the Recycle Bin because users rarely look there, so executables running from `$Recycle.Bin` are suspicious.
>

# purpose

Stores files deleted by the user identified by the SID so they can later be recovered and returned to the file system until the Recycle Bin is emptied. If the `$Recycle.bin` folder is corrupted, Windows reports that the Recycle Bin on the drive is corrupted; the fix is `RD <Drive>$Recycle.bin /s /q` from an elevated prompt and a restart.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
