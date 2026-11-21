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

Where the Configuration Manager client keeps its log files. Each client component writes its own `.log` file here. These logs are the main source for troubleshooting the client.

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
