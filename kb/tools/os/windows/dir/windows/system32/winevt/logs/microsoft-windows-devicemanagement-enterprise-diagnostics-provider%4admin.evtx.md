---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%4Admin.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - evtx
  - event-log
  - mdm
  - intune
aliases:
  - "Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%4Admin.evtx"
  - "DeviceManagement-Enterprise-Diagnostics-Provider Admin"
  - "MDM event log"
url:
  - https://learn.microsoft.com/troubleshoot/mem/intune/device-protection/troubleshoot-bitlocker-policies
  - https://learn.microsoft.com/windows/client-management/mdm-collect-logs
  - https://learn.microsoft.com/windows/client-management/mdm-diagnose-enrollment
  - https://learn.microsoft.com/troubleshoot/mem/intune/device-management/remotewipe-fails-sending-dowipe-command
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%4Admin.evtx

# description

File-system backing store of the Admin channel of the Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider event log, the main Mobile Device Management (MDM) event log in Windows. It records the OMA-DM agent's processing of MDM (for example Intune) policies and CSP settings, including successes and failures. Related logs are the Debug and Operational channels of the same provider and the MDM diagnostic report produced by mdmdiagnosticstool.exe.

## simple description

> ### 2026-11-21 Claude said
> This is the Windows MDM 'Admin' event log. Whenever Intune or another MDM pushes policies, enrolls the device or runs remote commands (wipe, lock), the MDM client writes the result here. Event ID 75 means automatic MDM enrollment succeeded, 76 means it failed, and 400/404 show CSP command failures.
>
> **SOC NOTE**: Useful for timelining device enrollment and policy changes (BitLocker, Defender, firewall CSPs), confirming a remote wipe/lock attempt, or spotting an unexpected enrollment into a rogue MDM tenant. Clearing or missing records alongside policy changes is suspicious (T1070.001).
>

# purpose

Learn identifies this file as the file-system location of the DeviceManagement-Enterprise-Diagnostics-Provider Admin log (Event Viewer path: Applications and Services Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin). It shows success and failures processing Intune policies, errors in CSP settings in OMA-URI format (e.g. ./Device/Vendor/MSFT/BitLocker/RequireDeviceEncryption), autoenrollment results (event ID 75 success, 76 failure) and CSP command failures such as event ID 400 for RemoteWipe. The Admin channel logs by default; a Debug channel can be enabled for more detail, and the channel can be collected remotely via the DiagnosticLog CSP as `Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%2FAdmin`.
