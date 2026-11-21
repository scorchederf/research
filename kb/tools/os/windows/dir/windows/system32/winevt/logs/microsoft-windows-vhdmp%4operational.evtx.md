---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-VHDMP%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
aliases:
  - Microsoft-Windows-VHDMP%4Operational.evtx
  - Microsoft-Windows-VHDMP/Operational
  - VHDMP log
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/virtualization/fail-to-manage-vhd-file
  - https://learn.microsoft.com/windows/win32/vstor/about-vhd
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-VHDMP%4Operational.evtx

# description

This file stores the Microsoft-Windows-VHDMP/Operational event log, written by the VHD miniport driver `Vhdmp.sys`, the kernel-mode VHD parser and dependency property provider. Related VHD components are `VirtDisk.dll` (user-mode VHD management APIs), `VDrvRoot.sys` (root virtual drive enumerator) and `FsDepends.sys` (nested volume dependency management).

## simple description

> ### 2026-11-21 Claude said
> This event log records activity of the Windows virtual hard disk driver, which handles mounting and unmounting VHD, VHDX and ISO files. Each time a user double-clicks an ISO or VHD, or Hyper-V attaches a virtual disk, events can be written here. It is also useful for troubleshooting virtual disks that fail to attach.
>
> **SOC NOTE**: Attackers deliver payloads inside ISO/IMG/VHD(X) containers to bypass Mark-of-the-Web (MITRE ATT&CK T1553.005, T1204.002). Mount events here (commonly Event ID 1 surfaced/ 2 removed, with the file path) give evidence that a user opened such a container, including its full path and time, even after the file is deleted. Correlate with Explorer/Downloads activity and process creation from the new drive letter.
>

# purpose

The VHDMP log is used when troubleshooting virtual disk problems. For example, when a tool such as Hyper-V Manager, Storage Manager or Diskpart reports "A Virtual Disk Provider for the specified file was not found", the VHDMP log can contain **Event ID 3**: "Failed to surface VHD <path>. Error Status: 0xC0000061". This is caused by a timing issue with FSDepends.sys and VHDMP.sys when certain backup programs are installed; the workaround is setting `HKLM\SYSTEM\CurrentControlSet\Services\FsDepends` `Start` to 0 (Boot).
