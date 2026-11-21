---
created: 2026-11-21
fullpath: 'C:\Program Files\Update Services\LogFiles\SoftwareDistribution.log'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - wsus
  - log
aliases:
  - SoftwareDistribution.log
  - WSUS log
url:
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/log-files
  - https://learn.microsoft.com/troubleshoot/mem/configmgr/update-management/troubleshoot-wsus-import-sync-issues
  - https://learn.microsoft.com/troubleshoot/mem/configmgr/update-management/troubleshoot-software-update-management
  - https://learn.microsoft.com/troubleshoot/mem/configmgr/update-management/troubleshoot-software-update-synchronization
  - https://learn.microsoft.com/windows-server/administration/windows-server-update-services/manage/wsus-and-the-catalog-site
---

**fullpath**:C:\Program Files\Update Services\LogFiles\SoftwareDistribution.log

# description

`SoftwareDistribution.log` is the Windows Server Update Services (WSUS) server log, located in `%ProgramFiles%\Update Services\LogFiles` together with `Change.log`. It records the software updates synchronized from the configured update source to the WSUS database and is used alongside Configuration Manager logs such as `WSyncMgr.log`, `WCM.log` and `WSUSCtrl.log` when troubleshooting software update points.

## simple description

> ### 2026-11-21 Claude said
> This is the main text log of a WSUS server. Every time WSUS synchronizes with Microsoft Update or an upstream server, imports updates from the Microsoft Update Catalog, or starts its service, it writes details and errors here. Administrators read it when update synchronization fails. It only exists on servers with the WSUS role installed, not on normal client PCs.
>
> **SOC NOTE**: WSUS is a high-value target because it pushes code to every managed client; malicious update injection (e.g., WSUSpect-style attacks, MITRE ATT&CK T1195 Supply Chain Compromise / T1072 Software Deployment Tools) or manual imports may leave traces of unexpected imports, sync sources, or TLS/proxy changes here. Correlate with the WSUS Application event log (events 381/382 for sync start) and IIS logs on ports 8530/8531.

# purpose

Records details about the software updates that are synced from the configured update source to the WSUS server database. Learn uses it to confirm manual (event 382) or scheduled (event 381) synchronization starts, to see which SCHANNEL/TLS protocol versions WSUS detected at startup, to find `WebException`/`SoapException` errors when sync or import fails (for example, retired endpoints or missing TLS 1.2), to review activity and errors when importing updates from the Microsoft Update Catalog, and to confirm `WsusUtil.exe reset` State Machine Reset activity.
