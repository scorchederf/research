---
created: 2026-11-21
fullpath: 'C:\Windows\Logs\DISM\dism.log'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - log
  - dism
aliases:
  - dism.log
  - DISM.log
url:
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/deployment-image-servicing-and-management--dism--best-practices
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/dism-global-options-for-command-line-syntax
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/deployment-troubleshooting-and-log-files
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/dism/disminitialize-function
---

**fullpath**:C:\Windows\Logs\DISM\dism.log

# description

`dism.log` is the default verbose log of Deployment Image Servicing and Management (DISM), at `%WINDIR%\Logs\Dism\dism.log`. It is the primary log for all online and offline DISM servicing actions and points to `CBS.log` (`%windir%\Logs\CBS`) and `Sessions.xml` (`%windir%\servicing\sessions`) for more detail. The DISM API (`DismInitialize`) also writes here when no log path is given.

## simple description

> ### 2026-11-21 Claude said
> dism.log is the text log written by DISM, the Windows tool used to repair, update and add features or packages to Windows images. Every DISM run (for example `DISM /Online /Cleanup-Image /RestoreHealth`) records its steps and errors here. When the file gets large it is archived to dism.log.bak and a new log is started. Admins read it to troubleshoot failed repairs or feature installs.
>
> **SOC NOTE**: The log records timestamps, the command line, and packages/features/drivers added or removed - useful to confirm when features like SMBv1, Telnet, Hyper-V or Windows Defender components were enabled or disabled (possible T1562.001 Impair Defenses) or when drivers were injected into an offline image. Because it is rolled to a single .bak, history is limited; collect it early. Attackers may use `/LogPath` to redirect logging elsewhere.
>

# purpose

Records history of DISM operations to help troubleshoot. Location can be changed with `/LogPath` and detail with `/LogLevel`. The file is automatically archived with `.bak` appended, and each archive overwrites the previous `.bak`. In Windows PE the default directory is the RAMDISK scratch space. On failure, review DISM.log first, then Sessions.xml, then CBS.log.


