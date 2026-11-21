---
created: 2026-11-21
fullpath: 'c:\windows\system32\iscsicpl.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - iscsi
  - storage
aliases:
  - iscsicpl.exe
  - iSCSI Initiator
  - iSCSI Initiator Properties
  - Microsoft.iSCSIInitiator
url:
  - https://learn.microsoft.com/windows/win32/shell/controlpanel-canonical-names
  - https://learn.microsoft.com/troubleshoot/windows-server/backup-and-storage/iscsi-storage-connectivity-troubleshooting
  - https://learn.microsoft.com/troubleshoot/windows-server/backup-and-storage/iscsi-initiator-not-login-to-favorite-targets
---

**fullpath**:c:\windows\system32\iscsicpl.exe

# description

iscsicpl.exe opens the Microsoft iSCSI Initiator Properties dialog, the Control Panel item (canonical name Microsoft.iSCSIInitiator, module iscsicpl.dll) used to connect Windows to iSCSI storage targets. Related tools are the iSCSI and Storage PowerShell modules (for example Connect-IscsiTarget).

## simple description

> ### 2026-11-21 Claude said
> iscsicpl.exe is the launcher for the iSCSI Initiator settings window. iSCSI lets a computer use disks on a remote storage array over the network as if they were local. Administrators use the window to discover targets, connect to them and keep them as Favorite Targets that reconnect at boot. It is mainly seen on servers and clusters.
>
> **SOC NOTE**: Has been abused for UAC bypass via DLL search-order hijacking (it auto-elevates and loads iscsiexe.dll; MITRE ATT&CK T1548.002 / T1574.001). Investigate iscsicpl.exe launched from unusual parent processes or a DLL named iscsiexe.dll outside System32. New iSCSI targets can also indicate data staging to attacker-controlled storage.
>

# purpose

Configures the Microsoft iSCSI Initiator: Discovery (target portals, refresh, remove), Favorite Targets (persistent connections), Targets, and the Configuration tab where the Initiator Name (IQN) is set. Changing the Initiator Name does not update existing Favorite Target entries, so they should be removed and recreated.

# typical use cases

| usage | description |
| --- | --- |
| `iscsicpl.exe` | Open iSCSI Initiator Properties to discover, connect, or manage Favorite Targets. |
| `control /name Microsoft.iSCSIInitiator` | Open the same Control Panel item by its canonical name. |

# options

_Not documented on Microsoft Learn at 2026/11/21 18:50 UTC_
