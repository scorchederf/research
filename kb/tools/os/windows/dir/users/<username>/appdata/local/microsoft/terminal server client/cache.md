---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Terminal Server Client\Cache'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - rdp
  - forensics
aliases:
  - Terminal Server Client Cache
  - RDP bitmap cache
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/remote-desktop-protocol-settings
  - https://learn.microsoft.com/windows-server/administration/performance-tuning/role/remote-desktop/session-hosts
  - https://learn.microsoft.com/windows/win32/termserv/imstscadvancedsettings-bitmapperistence
  - https://learn.microsoft.com/windows/win32/termserv/imsrdpclientadvancedsettings-bitmapvirtualcache32bppsize
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\Terminal Server Client\Cache

# description

This per-user folder is where the Remote Desktop Connection client keeps its persistent bitmap cache. Learn documents the related settings: `bitmapcachepersistenable:i` in .rdp files (the **Bitmap caching** check box) and the RDP ActiveX control properties `BitmapPeristence` and `BitmapVirtualCache*Size`, which set the size of the persistent bitmap cache files. The folder path itself is not described on Learn.

## simple description

> ### 2026-11-21 Claude said
> When you use Remote Desktop (`mstsc.exe`), the client saves small image tiles of the remote screen in this folder so it doesn't have to download them again. The files are named like `bcache24.bmc` and `Cache0000.bin`. Each user who has used RDP from this machine has their own copy.
>
> **SOC NOTE**: Valuable for lateral movement investigations (T1021.001): tools like `bmc-tools` rebuild the cached tiles into images that can show what an attacker saw and did on the remote host (consoles, commands, file names). File timestamps show when RDP was used from this host. Combine with `HKCU\Software\Microsoft\Terminal Server Client\Servers` and Event ID 1024/1102 in `Microsoft-Windows-TerminalServices-RDPClient/Operational`.
>

# purpose

Stores bitmaps rendered in RDP sessions on the client so they can be reused, which Learn says gives a significant bandwidth improvement and should always be enabled unless there are other security considerations. Persistent caching requires additional disk space.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
