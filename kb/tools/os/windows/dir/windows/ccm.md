---
created: 2026-11-21
fullpath: 'C:\Windows\CCM'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - configmgr
aliases:
  - CCM
  - %WinDir%\CCM
  - Configuration Manager client folder
url:
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/log-files
  - https://learn.microsoft.com/intune/configmgr/core/clients/deploy/about-client-installation-properties
---

**fullpath**:C:\Windows\CCM

# description

`%WinDir%\CCM` is the default installation folder of the Microsoft Configuration Manager (ConfigMgr/SCCM) client, set by the client.msi `CCMINSTALLDIR` property. Its `Logs` subfolder holds the client log files. Related tools include ccmsetup.exe and the CcmExec (SMS Agent Host) service.

## simple description

> ### 2026-11-21 Claude said
> This folder exists on machines managed by Microsoft Configuration Manager (SCCM/MECM). It holds the management agent's program files and, most usefully, its log files in C:\Windows\CCM\Logs. These logs record software deployments, inventory, updates, scripts and task sequences pushed to the machine.
>
> **SOC NOTE**: The CCM logs are a high-value forensic source: AppEnforce.log, execmgr.log, Scripts.log and CcmExec.log show what software/scripts were run by ConfigMgr, which attackers who compromise a site server abuse for mass deployment (MITRE ATT&CK T1072 Software Deployment Tools). Also check `CCM\Logs\smsts.log` for task sequences, and note that the folder can reveal management point and site information useful for an attacker's reconnaissance.
>

# purpose

Holds the Configuration Manager client installation. By default, client files are installed to `%WinDir%\CCM`; client log files are in `C:\Windows\CCM\logs`, and after a task sequence completes `smsts.log` is in `C:\Windows\CCM\Logs` (in `C:\Windows\CCM\Logs\smstslog\smsts.log` while running after client install). Log level, size and history are controlled by the `CCMLOGLEVEL`, `CCMLOGMAXSIZE` and `CCMLOGMAXHISTORY` setup properties.

# common files found

| file | description |
| --- | --- |
| `Logs\CcmExec.log` | Activities of the client and the SMS Agent Host service. |
| `Logs\CcmMessaging.log` | Communication between the client and management points. |
| `Logs\CAS.log` | Content Access service; maintains the local package cache. |
| `Logs\CcmEval.log` | Client status evaluation activities. |
| `Logs\CIAgent.log` | Remediation and compliance for compliance settings, software updates and application management. |
| `Logs\ccmsetup.log` | ccmsetup.exe tasks for client setup, upgrade and removal. |
| `Logs\smsts.log` | Task sequence log after the task sequence completes. |
| `Logs\StatusAgent.log` | Status messages created by client components. |
