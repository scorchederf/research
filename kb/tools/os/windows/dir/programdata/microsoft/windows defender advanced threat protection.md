---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - defender-for-endpoint
aliases:
  - "Windows Defender Advanced Threat Protection"
  - "MDE data folder"
url:
  - https://learn.microsoft.com/defender-endpoint/configure-wdac-script-enforcement-mde
---

**fullpath**: C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection

# description

Protected data folder of Microsoft Defender for Endpoint (MDE) present on onboarded devices. Learn documents its `DataCollection` subfolder, which holds PowerShell scripts signed by the `Microsoft Windows Defender Advanced Threat Protection` publisher. Access requires a SYSTEM context, for example via Sysinternals PsExec.

## simple description

> ### 2026-11-21 Claude said
> This folder is where the Microsoft Defender for Endpoint sensor (Sense service) keeps its working data on an onboarded device: cached configuration, collection scripts, cyber data and temporary files. It is locked down so that even administrators normally cannot browse it without SYSTEM rights. Its existence indicates the machine is, or was, onboarded to MDE.
>
> **SOC NOTE**: Attackers who try to blind EDR may tamper with or delete files here or stop the Sense service (T1562.001 Impair Defenses); tamper protection should block this. Live Response and investigation package files are staged in subfolders, so unexpected files or scripts here deserve review. Offboarding/onboarding state is also visible in HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection.
>

# purpose

Stores Microsoft Defender for Endpoint sensor data on onboarded devices. The folder is protected; a SYSTEM-level shell (for example `PsExec.exe -s cmd.exe`) is required to access it.

# common files found

| file / folder | description |
| --- | --- |
| `DataCollection` | Contains PowerShell scripts signed with the `Microsoft Windows Defender Advanced Threat Protection` publisher; useful as a reference file when creating App Control (WDAC) publisher allow rules. |
