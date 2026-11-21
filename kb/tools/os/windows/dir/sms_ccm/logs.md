---
created: 2026-11-21
fullpath: 'C:\SMS_CCM\Logs'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - configmgr
  - logs
aliases:
  - Logs
  - SMS_CCM\Logs
  - Management point log folder
url:
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/log-files
---

**fullpath**:C:\SMS_CCM\Logs

# description

C:\SMS_CCM\Logs is the default log file location for a Configuration Manager management point. Configuration Manager (current branch) client and site server components record process information in individual log files. Other default locations are C:\Windows\CCM\logs (client) and C:\Program Files\Microsoft Configuration Manager\Logs (server).

## simple description

> ### 2026-11-21 Claude said
> This folder holds text log files written by a Microsoft Configuration Manager (SCCM/MECM) management point, the site role that clients talk to for policy and content locations. Each component writes its own .log file, and older data rolls over into .lo_ files. Admins read these logs with CMTrace to troubleshoot client communication.
>
> **SOC NOTE**: SCCM is a high-value target (lateral movement, software deployment abuse, NAA credential theft; MITRE ATT&CK T1072). MP logs (e.g. MP_Location, MP_Policy, MP_GetPolicy) can show which clients requested policy and from where, helping detect rogue client registrations or relay attacks against the MP. Preserve these logs early since they roll over quickly.
>

# purpose

Stores operational log files for the Configuration Manager management point. Processes write to a `.log` file until it reaches its maximum size, then copy it to `.lo_` and continue. Logging for client and management point is configured under `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\CCM\Logging\@Global` (LogLevel, LogMaxHistory, LogMaxSize; default size 250,000 bytes) and debug logging under `...\CCM\Logging\DebugLogging`.

# common files found

- `*.log` - current component log files.
- `*.lo_` - previous (rolled-over) log file history.
- Management point logs listed in the Log file reference under "Management point" (e.g. CcmExec-related and MP_* logs).
- CertificateMaintenance.log - maintains certificates for AD DS and management points.
