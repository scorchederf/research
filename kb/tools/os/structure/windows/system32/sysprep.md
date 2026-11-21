---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Sysprep'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - deployment
aliases:
  - Sysprep
  - System Preparation Tool
url:
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/sysprep-process-overview?view=windows-11
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/sysprep-command-line-options?view=windows-11
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/sysprep--system-preparation--overview?view=windows-11
---

**fullpath**:C:\Windows\System32\Sysprep

# description

Directory containing the System Preparation (Sysprep) tool, present on all Windows installations. Sysprep generalizes a Windows image (removing SID, restore points, event logs and other system-specific data) so it can be captured with DISM and deployed to other computers.

## simple description

> ### 2026-11-21 Claude said
> This folder holds sysprep.exe and its helper files, used by IT to prepare a "golden image" of Windows before cloning it to many PCs or VMs. Running `sysprep /generalize` strips machine-unique data so each deployed copy gets a new SID. The Panther subfolder stores Sysprep logs, and an unattend.xml answer file may be placed here. Normal users never need to touch it.
>
> **SOC NOTE**: Unattend/sysprep.xml answer files left here or in `C:\Windows\Panther` can contain plaintext or base64 local admin passwords (MITRE ATT&CK T1552.001 Credentials In Files) - a well known privilege-escalation check. Historically sysprep.exe was abused for UAC bypass via DLL hijacking (e.g. CRYPTBASE.dll, T1548.002). Unexpected execution of sysprep.exe on a production host is suspicious; review `Sysprep\Panther\setupact.log` for timing.
>

# purpose

Sysprep.exe is the main program that calls other executable files that prepare the Windows installation; it is located in `%WINDIR%\system32\sysprep` on all Windows installations. Syntax: `Sysprep.exe [/oobe | /audit] [/generalize] [/mode:vm] [/reboot | /shutdown | /quit] [/quiet] [/unattend:<answerfile>]`. The Sysprep UI is deprecated; use the command line (and `/quiet` on Server Core).

# common files found

- sysprep.exe - the System Preparation tool.
- Panther\ - log folder for generalize actions (`%WINDIR%\System32\Sysprep\Panther`); setupact.log is the main log file.
