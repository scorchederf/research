---
created: 2026-11-21
fullpath: 'C:\Windows\System32\vssadmin.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - vss
aliases:
  - vssadmin.exe
  - vssadmin
  - VssAdmin
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/vssadmin
  - https://learn.microsoft.com/windows-server/storage/file-server/volume-shadow-copy-service
  - https://learn.microsoft.com/windows-server/administration/windows-commands/vssadmin-delete-shadows
  - https://learn.microsoft.com/windows-server/administration/windows-commands/vssadmin-list-shadows
  - https://learn.microsoft.com/windows-server/administration/windows-commands/vssadmin-list-shadowstorage
  - https://learn.microsoft.com/windows-server/administration/windows-commands/vssadmin-resize-shadowstorage
  - https://learn.microsoft.com/windows-server/administration/windows-commands/vssadmin-list-providers
---

**fullpath**:C:\Windows\System32\vssadmin.exe

# description

vssadmin shows current volume shadow copy backups and all installed shadow copy writers and providers. It is a built-in Volume Shadow Copy Service (VSS) tool available on Windows client and Windows Server; it can only administer shadow copies created by the system software provider. DiskShadow is the related VSS requester on Windows Server.

## simple description

> ### 2026-11-21 Claude said
> vssadmin.exe is the built-in command-line tool for managing Volume Shadow Copies, the point-in-time snapshots Windows uses for System Restore, Previous Versions and backups. Administrators use it to list snapshots, writers and providers, and to delete or resize shadow copy storage. It requires administrative rights for most actions.
>
> **SOC NOTE**: `vssadmin delete shadows /all /quiet` and `vssadmin resize shadowstorage` to a tiny size are classic ransomware pre-encryption steps (MITRE ATT&CK T1490 Inhibit System Recovery). `vssadmin create shadow` is also abused to copy locked files such as NTDS.dit and the SAM/SYSTEM hives (T1003.002/T1003.003). Alert on process creation (Sysmon 1 / Security 4688) with these command lines, and on VSS events in the Application log.
>

# purpose

VssAdmin is used to create, delete, and list information about shadow copies, and to resize the shadow copy storage area (diff area).

# typical use cases

| usage | description |
| --- | --- |
| `vssadmin list shadows` | Lists all existing shadow copies on the computer. |
| `vssadmin list shadowstorage /on=C:` | Lists all shadow copy storage associations located on volume C. |
| `vssadmin list providers` | Lists all registered volume shadow copy providers. |
| `vssadmin delete shadows /for=c: /oldest` | Deletes the oldest shadow copy of volume C. |
| `vssadmin delete shadows /for=d: /all /quiet` | Deletes all client-accessible shadow copies of volume D without progress messages. |
| `vssadmin resize shadowstorage /For=C: /On=D: /MaxSize=900MB` | Resizes shadow storage of volume C on volume D to a 900 MB maximum. |

# options

| option | description |
| --- | --- |
| `delete shadows` | Deletes volume shadow copies (client-accessible type only). Parameters: `/for=<ForVolumeSpec>`, `/oldest`, `/all`, `/shadow=<ShadowID>`, `/quiet`. |
| `list providers` | Lists registered volume shadow copy providers. |
| `list shadows` | Lists existing volume shadow copies. Parameters: `/for=<ForVolumeSpec>`, `/shadow=<ShadowID>`. |
| `list shadowstorage` | Lists volume shadow copy storage associations. Parameters: `/for=<ForVolumeSpec>` or `/on=<OnVolumeSpec>` (not together). |
| `list volumes` | Lists volumes eligible for shadow copies. |
| `list writers` | Lists all subscribed volume shadow copy writers on the system. |
| `resize shadowstorage` | Resizes the maximum size for a shadow copy storage association; may cause shadow copies to disappear. Parameters: `/for=`, `/on=`, `[/maxsize=<MaxSizeSpec>]` (1 MB or greater, KB to EB, `UNBOUNDED` or a percentage). |
| `create shadow` | Creates a new shadow copy. |
