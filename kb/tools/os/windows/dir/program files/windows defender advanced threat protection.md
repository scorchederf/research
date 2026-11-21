---
created: 2026-11-21
fullpath: 'C:\Program Files\Windows Defender Advanced Threat Protection'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Windows Defender Advanced Threat Protection
  - Microsoft Defender for Endpoint
  - Sense
url:
  - https://learn.microsoft.com/defender-endpoint/switch-to-mde-phase-2
  - https://learn.microsoft.com/defender-endpoint/standard-device-connectivity-urls-commercial
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-endpoint-releases
  - https://learn.microsoft.com/defender-endpoint/application-deployment-via-mecm
---

**fullpath**:C:\Program Files\Windows Defender Advanced Threat Protection

# description

Installation folder of the Microsoft Defender for Endpoint (formerly Windows Defender ATP) EDR sensor, built into Windows 10 1703+/Windows 11 and Windows Server 2019+. It contains the Sense service executables (`MsSense.exe` and helpers); Microsoft Defender Antivirus lives separately under `C:\Program Files\Windows Defender`.

## simple description

> ### 2026-11-21 Claude said
> This is where the Microsoft Defender for Endpoint sensor (called "Sense") lives. Sense is the EDR component that records process, file, network and registry activity and sends it to the Microsoft Defender portal for detection and investigation. It runs as the Sense service and is present on onboarded Windows clients and servers. The antivirus engine is a different component in a different folder.
>
> **SOC NOTE**: Attackers try to blind EDR by stopping the Sense service, tampering with or deleting files here, blocking its network traffic (e.g. via firewall rules or WFP, as in EDRSilencer), or abusing exclusions (MITRE ATT&CK T1562.001 Impair Defenses). Watch for Tamper Protection alerts, Sense service stop events (System log 7036/7040), and processes other than Microsoft-signed ones writing here. The `HKLM\SYSTEM\CurrentControlSet\Services\Sense` key shows the sensor service is installed (not that the device is onboarded).
>

# purpose

Holds the Defender for Endpoint EDR client processes, which generate network communications to the Defender cloud service and must be added to exclusion lists of other security products during migration. Microsoft also lists `HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\*` as the registry path and `C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\DataCollection` as the data collection folder.

# common files found

| file | description |
| --- | --- |
| `MsSense.exe` | Defender for Endpoint EDR sensor (Sense) main process; release notes track `MsSense.exe` versions. |
| `SenseCncProxy.exe` | EDR client process that requires network connectivity. |
| `SenseSampleUploader.exe` | EDR client process that requires network connectivity. |
| `SenseIR.exe` | EDR client process that requires network connectivity. |
| `SenseCM.exe` | EDR client process that requires network connectivity. |
| `SenseNdr.exe` | EDR client process that requires network connectivity. |
| `Classification\SenseCE.exe` | EDR client process that requires network connectivity. |
| `SenseTVM.exe` | EDR client process that requires network connectivity. |
| `SenseTracer.exe` | EDR client process that requires network connectivity. |
| `SenseDlpProcessor.exe` | EDR client process that requires network connectivity. |
