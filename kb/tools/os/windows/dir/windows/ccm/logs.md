---
created: 2026-11-21
fullpath: 'C:\Windows\CCM\Logs'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Logs
  - CCM Logs
  - Configuration Manager client logs
url:
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/log-files
---

**fullpath**:C:\Windows\CCM\Logs

# description

The default log folder for the Microsoft Configuration Manager (ConfigMgr/MECM) client. Client components write operational information here, one log per process. Other default locations are the site server (`C:\Program Files\Microsoft Configuration Manager\Logs`) and management point (`C:\SMS_CCM\Logs`).

## simple description

> ### 2026-11-21 Claude said
> This folder holds the log files for the Microsoft Configuration Manager client (also called SCCM, MECM or ConfigMgr), the agent many organisations use to deploy software, updates, scripts and settings to their computers. Each client component writes its own `.log` file here, for example `CcmExec.log` for the main service, `AppEnforce.log` for application installs and `execmgr.log` for package/program runs. Admins read these with the CMTrace tool to troubleshoot deployments. Logs roll over to a `.lo_` file when they reach their size limit.
>
> **SOC NOTE**: These logs show exactly what Configuration Manager executed on a host, with command lines and timestamps, which helps you tell legitimate admin deployments apart from attacker activity. Attackers who compromise SCCM can push malware or scripts to many machines at once (MITRE ATT&CK T1072, software deployment tools), and this folder is where that shows up on each endpoint. Check `AppEnforce.log`, `execmgr.log` and `smsts.log` around the time of suspicious activity, and remember older history may already be overwritten.
>

# purpose

- Logs use `.log`; when a log reaches its maximum size it is copied to `.lo_` and the `.log` continues (some components instead keep date-stamped history).
- Verbosity, size and history can be configured during client install (CCMENABLELOGGING, CCMDEBUGLOGGING, CCMLOGLEVEL, CCMLOGMAXHISTORY, CCMLOGMAXSIZE), via Configuration Manager Service Manager, or in the registry.
- After a task sequence completes, `smsts.log` is in this folder (during it, in `Logs\smstslog\smsts.log`).

# common files found

- `CcmExec.log` - client and SMS Agent Host service activity
- `CcmMessaging.log` - client/management point communication
- `CcmEval.log` / `CcmEvalTask.log` - client health evaluation
- `CAS.log` - Content Access service / package cache
- `CIAgent.log` - compliance, software updates and app remediation
- `PolicyEvaluator.log` - policy evaluation
- `ScanAgent.log`, `RebootCoordinator.log`, `DeltaDownload.log` - software updates
- `ccmsetup.log`, `client.msi.log`, `CcmRepair.log` - client install/repair
- `smsts.log` - task sequences
- `BitLockerManagementHandler.log`, `ATPHandler.log` - BitLocker / Defender ATP onboarding

Full list: the Configuration Manager *Log file reference*.
