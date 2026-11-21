---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Configuration Manager\Logs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - configmgr
  - sccm
  - logs
aliases:
  - 'Logs'
  - 'Configuration Manager site server logs'
url:
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/log-files
---

**fullpath**: C:\Program Files\Microsoft Configuration Manager\Logs

# description

Default log folder on a Microsoft Configuration Manager (ConfigMgr/SCCM) site server. Other defaults are `C:\Windows\CCM\logs` (client), `C:\SMS_CCM\Logs` (management point) and the console's AdminUILog folder. Logging is configured under `HKLM\SOFTWARE\Microsoft\SMS\Tracing`.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the log files written by the Configuration Manager site server components - the server that pushes software, updates and OS deployments to managed PCs. Each component (e.g., SMS Provider, software update sync, distribution manager) writes its own .log file. Admins view them with CMTrace to troubleshoot.
>
> **SOC NOTE**: ConfigMgr is a high-value target: attackers with admin rights can deploy applications/scripts to every client (T1072 Software Deployment Tools). SMSProv.log records WMI/SMS Provider access (who did what from the console), and hman/distmgr/objreplmgr show deployment activity. Preserve these logs when investigating suspicious deployments, CMPivot/script runs or NAA credential abuse.
>

# purpose

Stores site server component logs used to troubleshoot Configuration Manager site operations.

# common files found

| file | description |
| --- | --- |
| `hman.log` | Site configuration changes and publishing of site information to AD DS; message forwarding. |
| `SMSProv.log` | WMI provider (SMS Provider) access to the site database. |
| `objreplmgr.log` | Replication of software update notification files; processing of policy and assignment. |
| `ruleengine.log` | Automatic deployment rules processing. |
| `WCM.log` | Software update point configuration and WSUS connections. |
| `wsyncmgr.log` | Software updates sync process. |
| `PolicyPV.log` | Policy generation of all policies. |
| `Sitecomp.log` | Site component / service connection point installation. |
| `CloudMgr.log` | Cloud management gateway deployment and status. |
| `bgbmgr.log` | Client notification tasks and online/task status files. |
| `wolmgr.log` | Wake On LAN procedures. |
