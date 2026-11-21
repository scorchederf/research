---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4MSI and Script.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - evtx
  - applocker
  - app-control
aliases:
  - Microsoft-Windows-AppLocker%4MSI and Script.evtx
  - AppLocker - MSI and Script
url:
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/applocker/using-event-viewer-with-applocker
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/applocker/plan-for-applocker-policy-management
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/operations/event-id-explanations
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4MSI and Script.evtx

# description

This is the backing file of the **AppLocker - MSI and Script** event log (Applications and Services Logs\Microsoft\Windows\AppLocker). It contains events for files affected by the Windows Installer and script rule collections (.msi, .msp, .ps1, .bat, .cmd, .vbs, .js), and App Control for Business also logs MSI, script, packaged app and COM object events here.

## simple description

> ### 2026-11-21 Claude said
> This .evtx file is the Windows event log where AppLocker and App Control record decisions about installers and scripts. Each time a script or MSI is allowed, audited or blocked, an event is written with the file path, user and rule. It is viewed in Event Viewer under Applications and Services Logs > Microsoft > Windows > AppLocker > MSI and Script.
>
> **SOC NOTE**: High-value for detecting script-based execution (T1059) and blocked attacker tooling: 8006/8021 show what would have been blocked in audit mode, 8007/8022 and 8029 show blocks, and 8028/8038 show script host checks with signature info. Clearing or missing data here can indicate log tampering (T1070.001). Forward it to the SIEM; Sentinel event sets include 8005-8007.
>

# purpose

Records AppLocker and App Control events for scripts and MSI files. Not included on Windows Server Core.

| event id | description |
| --- | --- |
| 8005 | Script or .msi file was allowed to run. |
| 8006 | Audit only: script or .msi would have been blocked if enforced. |
| 8007 | Script or MSI was prevented from running (Enforce rules). |
| 8008 | AppLocker component not available on this SKU. |
| 8020 | File was allowed to run (Windows 8 / Server 2012+). |
| 8021 | Allowed but would have been prevented if enforced (Windows 8 / Server 2012+). |
| 8022 | File was prevented from running (Windows 8 / Server 2012+). |
| 8028 | App Control audit: script host queried a file that would fail policy if enforced. |
| 8029 | App Control enforcement equivalent of 8028. |
| 8036 | COM object was blocked. |
| 8037 | Script passed the App Control policy. |
| 8038 | Signing information correlated with 8028/8029. |
| 8039 | Packaged app allowed in audit mode but would be blocked. |
| 8040 | Packaged app prevented from installing or running. |

