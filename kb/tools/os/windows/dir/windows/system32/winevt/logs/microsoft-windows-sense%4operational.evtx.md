---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-SENSE%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - evtx
  - defender-for-endpoint
aliases:
  - Microsoft-Windows-SENSE%4Operational.evtx
  - Microsoft-Windows-SENSE/Operational
  - SENSE
url:
  - https://learn.microsoft.com/defender-endpoint/event-error-codes
  - https://learn.microsoft.com/defender-endpoint/troubleshoot-onboarding
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-SENSE%4Operational.evtx

# description

Event log file for the **Microsoft-Windows-SENSE/Operational** channel, written by the Microsoft Defender for Endpoint service. SENSE is the internal name of the behavioral sensor that powers Defender for Endpoint. Viewable in Event Viewer under Applications and Services Logs > Microsoft > Windows > SENSE > Operational.

## simple description

> ### 2026-11-21 Claude said
> This log records the health of the Microsoft Defender for Endpoint sensor on a device: when it starts and stops, when it connects to the cloud, onboarding/offboarding, and errors. It does not contain detections themselves, which go to the Defender portal. Admins use it to troubleshoot devices not showing up in the portal.
>
> **SOC NOTE**: Gaps or service-stop/offboarding events (e.g. ID 2 shutdown, 3 failed to start, 5 failed to connect) can indicate EDR tampering or blinding (T1562.001). Unexpected offboarding or connectivity failures during an incident timeline are worth checking against Defender tamper-protection alerts.
>

# purpose

Records Defender for Endpoint service events for troubleshooting onboarding and connectivity.

| event ID | description |
| --- | --- |
| 1 | Defender for Endpoint service started (startup, shutdown, onboarding). |
| 2 | Service shutdown (device shut down or offboarded). |
| 3 | Service failed to start. |
| 4 | Service contacted the server at the given URL. |
| 5 | Service failed to connect to the server; check proxy/Internet connectivity. |
| 6 | Service isn't onboarded and no onboarding parameters were found. |
| 7 | Service failed to read onboarding parameters. |
| 9 | Service failed to change its start type. |
| 99 | Error while communicating with server. |
| 100 | SenseCE executable failed to start. |
| 102 / 103 | SenseNdr (Network Detection and Response) executable started / ended. |
| 106 / 107 | Service failed to start due to MsSense DLL module issue. |

