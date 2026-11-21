---
created: 2026-11-21
fullpath: 'C:\Windows\ccmsetup\Logs'
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
  - "Logs"
  - "ccmsetup logs"
url:
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/log-files
  - https://learn.microsoft.com/intune/configmgr/core/clients/deploy/about-client-installation-properties
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files
---

**fullpath**:C:\Windows\ccmsetup\Logs

# description

This folder holds the logs written by ccmsetup.exe when it installs, upgrades, repairs or removes the Configuration Manager (SCCM/MECM) client. ccmsetup uses `%Windir%\Ccmsetup` as its system folder; once installed, the client writes its operational logs to `C:\Windows\CCM\Logs`.

## simple description

> ### 2026-11-21 Claude said
> When the Configuration Manager agent is installed on a Windows machine, the installer ccmsetup.exe records everything it does in this folder. The main file is ccmsetup.log, which shows download sources, command-line properties, errors and exit codes. Admins check it first when a client fails to install or upgrade.
>
> **SOC NOTE**: Shows when and from which management point/site the SCCM agent was pushed, which is useful when attackers abuse SCCM for lateral movement or deployment (T1072 Software Deployment Tools) or when client push credentials are targeted. Unexpected reinstall/uninstall entries can indicate tampering.
>

# purpose

Stores client installation logs for Configuration Manager. Log level, size and history are controlled by client.msi properties such as `CCMLOGLEVEL`, `CCMLOGMAXSIZE` and `CCMLOGMAXHISTORY`.

# common files found

| file | description |
| --- | --- |
| ccmsetup.log | Records ccmsetup.exe tasks for client setup, client upgrade, and client removal; used to troubleshoot client installation problems. |
| ccmsetup-ccmeval.log | Records ccmsetup.exe tasks for client status and remediation. |
| client.msi.log | Records setup tasks done by client.msi; used to troubleshoot client installation or removal problems. |
