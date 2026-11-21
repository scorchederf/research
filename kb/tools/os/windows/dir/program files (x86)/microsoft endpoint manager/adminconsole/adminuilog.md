---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Endpoint Manager\AdminConsole\AdminUILog'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - AdminUILog
  - Configuration Manager console log folder
url:
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/about-log-files
  - https://learn.microsoft.com/intune/configmgr/core/plan-design/hierarchy/log-files
  - https://learn.microsoft.com/intune/configmgr/core/servers/manage/admin-console-notifications
---

**fullpath**:C:\Program Files (x86)\Microsoft Endpoint Manager\AdminConsole\AdminUILog

# description

AdminUILog is the default log folder of the Configuration Manager (Microsoft Endpoint Manager / ConfigMgr) console on the computer that runs the console. It holds console logs such as SmsAdminUI.log; client, server and management point logs are kept elsewhere (`C:\Windows\CCM\logs`, `C:\Program Files\Microsoft Configuration Manager\Logs`, `C:\SMS_CCM\Logs`).

## simple description

> ### 2026-11-21 Claude said
> This folder holds the log files written by the Configuration Manager admin console, the tool administrators use to manage SCCM/ConfigMgr. Every time someone opens the console, runs CMPivot, or installs a console extension, activity is written here. It exists only on machines where the console is installed, typically admin workstations and site servers. The logs are plain text in CMTrace format.
>
> **SOC NOTE**: ConfigMgr is a high-value target because it can push software and scripts to every managed device (MITRE ATT&CK T1072 Software Deployment Tools). SmsAdminUI.log and CMPivot.log on an admin workstation can show who connected to which site server, when, and which CMPivot queries were run, helping reconstruct attacker use of a compromised admin account. Look for console use from unexpected hosts or at odd hours.
>

# purpose

Default location for Configuration Manager console log files. The console logging level is set in `C:\Program Files (x86)\Microsoft Endpoint Manager\AdminConsole\bin\Microsoft.ConfigurationManagement.exe.config` by changing the `switchValue` of the `SmsAdminUISnapIn` source from `Error` to `Verbose`.

# common files found

| file | description |
| --- | --- |
| `SmsAdminUI.log` | Records Configuration Manager console activity. |
| `ConfigMgrAdminUISetup.log` | Records the installation of the Configuration Manager console. |
| `CMPivot.log` | Records details about each CMPivot task run from the console. |
| `AdminUI.ExtensionInstaller.log` | Records download of extensions from Microsoft and installation/uninstallation of all extensions. |
| `FeatureExtensionInstaller.log` | Records installation and removal of individual extensions when enabled or disabled in the console. |
