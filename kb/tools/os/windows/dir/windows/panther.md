---
created: 2026-11-21
fullpath: 'C:\Windows\Panther'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - windows
aliases:
  - "Panther"
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/setup-upgrade-and-drivers/windows-setup-log-file-locations
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/deployment-troubleshooting-and-log-files
  - https://learn.microsoft.com/windows/deployment/upgrade/log-files
  - https://learn.microsoft.com/azure/azure-local/manage/collect-log-files-arc-enabled-vms
---

**fullpath**:C:\Windows\Panther

# description

`%windir%\Panther` is the Windows Setup log folder. It contains logs written during the online configuration (first boot), OOBE, LogonUI and OEM first-run phases and after an upgrade. Related setup logs are in `$Windows.~BT\Sources\Panther` (down-level/WinPE) and `%windir%\inf` (setupapi logs).

## simple description

> ### 2026-11-21 Claude said
> Panther is where Windows Setup writes its logs when Windows is installed or upgraded. The most important are setupact.log (all actions) and setuperr.log (errors). It may also contain unattend files used for automated installs. Admins use it to troubleshoot failed installs and upgrades.
>
> **SOC NOTE**: Unattend.xml or autounattend copies here (and `Panther\Unattend`) can contain plaintext or base64 local administrator passwords used during deployment (MITRE ATT&CK T1552.001 Credentials In Files); attackers and pentesters routinely check it. Setup logs also give OS install/upgrade timestamps useful for timelines.
>

# purpose

Holds Windows Setup log files. During online configuration it stores setupact.log, setuperr.log, miglog.xml (migrated user directory structure including SIDs), PostGatherPnPList.log and PreGatherPnPList.log. The `UnattendGC` subfolder holds the OOBE setupact.log; `cbs_unattend.log` records unattended-setup servicing failures; `SetupComplete.log` records custom scripts run at the end of setup.

# common files found

| file | description |
| --- | --- |
| `setupact.log` | Primary log for setup actions and most installation errors. |
| `setuperr.log` | High-level list of setup errors. |
| `miglog.xml` | User directory structure migrated during installation, including SIDs. |
| `PreGatherPnPList.log` | Initial capture of devices during the downlevel phase. |
| `PostGatherPnPList.log` | Capture of devices after the online configuration phase. |
| `cbs_unattend.log` | Unattended-setup servicing failures. |
| `SetupComplete.log` | Custom scripts run during or after Windows Setup. |
| `UnattendGC\setupact.log` | Actions during the OOBE phase. |
