---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4EXE and DLL.evtx'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Microsoft-Windows-AppLocker%4EXE and DLL.evtx
  - AppLocker - EXE and DLL
  - EXE and DLL
url:
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/applocker/using-event-viewer-with-applocker
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/applocker/plan-for-applocker-policy-management
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/operations/event-id-explanations
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4EXE and DLL.evtx

# description

The on-disk event log file behind the **AppLocker - EXE and DLL** log under Applications and Services Logs\Microsoft\Windows\AppLocker. It contains events for all files affected by the executable and DLL rule collections (.exe, .com, .dll and .ocx). Related logs are **MSI and Script** and **Packaged app-Deployment / Packaged app-Execution**; events are viewed with Event Viewer (eventvwr.msc).

## simple description

> ### 2026-11-21 Claude said
> This file stores the AppLocker events for programs and DLLs. Each time an executable or DLL is evaluated against AppLocker rules, Windows records whether it was allowed, would have been blocked (audit mode), or was blocked. Entries include the file path, user, and the rule that matched. It is a normal .evtx file that can be opened in Event Viewer or parsed with log tools.
>
> **SOC NOTE**: Key IDs: 8002 allowed, 8003 audit-would-block, 8004 blocked. 8003/8004 from user-writable paths (AppData, Temp, Downloads) often indicate malware or LOLBin abuse and attempts to bypass application control (T1218, T1574 DLL side-loading). Even in audit mode it gives a near-complete execution history with full paths and user SID. Clearing or disabling the log is T1070.001.
>

# purpose

Records which files AppLocker allowed or blocked. Each event includes which file is affected and its path, whether it was allowed or blocked, the rule type (path, file hash, or publisher), the rule name and the SID of the user or group in the rule. Microsoft notes the log is very verbose and suggests collecting only Error events if forwarding to a service such as Log Analytics.

| event ID | level | description |
| --- | --- | --- |
| 8000 | Error | AppID policy conversion failed; the policy wasn't applied correctly. |
| 8001 | Information | The AppLocker policy was applied successfully to this computer. |
| 8002 | Information | An AppLocker rule allowed the .exe or .dll file. With PolicyName = MANAGEDINSTALLER it marks a managed installer process. |
| 8003 | Warning | Audit only: the file would have been blocked if rules were enforced. |
| 8004 | Error | AppLocker blocked the named EXE or DLL file (Enforce rules mode). |
