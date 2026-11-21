---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Defender Advanced Threat Protection\MsSense.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "MsSense.exe"
  - "MSSense"
  - "Sense"
  - "Defender for Endpoint EDR sensor"
url:
  - https://learn.microsoft.com/defender-endpoint/switch-to-mde-phase-2
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-updates
  - https://learn.microsoft.com/defender-endpoint/configure-proxy-internet
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-endpoint-releases
---

**fullpath**:C:\Program Files\Windows Defender Advanced Threat Protection\MsSense.exe

# description

MsSense.exe is the Microsoft Defender for Endpoint endpoint detection and response (EDR) sensor, the `MSSense` (Sense) service. It ships in-box with Windows 10 1803+/Windows 11/Windows Server 2019+ and is updated for Windows Server 2012 R2/2016 via KB5005292, which places it under `C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Platform\*`. Related processes include SenseCncProxy.exe, SenseIR.exe, SenseCE.exe, SenseSampleUploader.exe, SenseNdr.exe and SenseTVM.exe.

## simple description

> ### 2026-11-21 Claude said
> MsSense.exe is the main Microsoft Defender for Endpoint agent process that collects security telemetry from the device and sends it to the Defender cloud. It runs as a protected service and powers alerts, advanced hunting data and response actions. It is separate from the antivirus engine MsMpEng.exe. If it is stopped or blocked, the device stops reporting to the Defender portal.
>
> **SOC NOTE**: Its presence means MDE telemetry should exist for the host; gaps in telemetry can indicate tampering (MITRE ATT&CK T1562.001 Impair Defenses). Attackers try to block its network traffic (firewall rules, hosts entries, WFP filters such as EDRSilencer) or stop the Sense service. Check Microsoft-Windows-SENSE/Operational events and the device's last-seen time. A copy running from any other path is suspicious.
>

# purpose

Provides the EDR sensor for Defender for Endpoint and generates network communications that must not be blocked; Microsoft lists it as a required EDR exclusion for non-Microsoft security products. The sensor reads static proxy settings (`TelemetryProxyServer`, `PreferStaticProxyForHttpRequest` from version 10.8210.* / 10.8049.*) from `HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection`. Updates for the sensor are delivered through monthly cumulative updates and KB5005292.

# typical use cases

| usage | description |
| --- | --- |
| `reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection" /v PreferStaticProxyForHttpRequest /t REG_DWORD /d 1 /f` | Makes a compatible EDR sensor prefer the static TelemetryProxyServer proxy. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
