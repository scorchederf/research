---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-AAD%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - entra-id
aliases:
  - "Microsoft-Windows-AAD%4Operational.evtx"
  - "AAD Operational"
  - "Microsoft-Windows-AAD/Operational"
url:
  - https://learn.microsoft.com/entra/identity/devices/troubleshoot-primary-refresh-token
  - https://learn.microsoft.com/entra/identity/devices/troubleshoot-hybrid-join-windows-current
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-AAD%4Operational.evtx

# description

File backing the `Microsoft-Windows-AAD/Operational` channel (Applications and Services Logs > Microsoft > Windows > AAD > Operational), written by the Microsoft Entra Cloud Authentication Provider (CloudAP) plug-in. It is used with the AAD Analytic log to troubleshoot Primary Refresh Token (PRT) and Entra join issues.

## simple description

> ### 2026-11-21 Claude said
> This log records errors from Windows' Microsoft Entra ID (Azure AD) sign-in component on joined or hybrid-joined devices.
> It shows problems getting or renewing the Primary Refresh Token, the token used for single sign-on to cloud resources.
> The '%4' in the name is how Windows encodes the '/' in the channel name.
>
> **SOC NOTE**: Useful in token-theft and device-identity investigations (T1528, T1550.001, PRT abuse): error spikes, unexpected token acquisition failures, or AADSTS codes (events 1081/1088) can show tampering or blocked sign-ins. Correlate with Entra sign-in logs.
>

# purpose

In the CloudAP plug-in, Error events are written to the Operational log and information events to the Analytic log. Events between 1006 (start of PRT acquisition) and 1007 (end) belong to one PRT flow; events 1081 and 1088 contain server error codes from the Entra authentication service and the WS-Trust endpoint respectively.
