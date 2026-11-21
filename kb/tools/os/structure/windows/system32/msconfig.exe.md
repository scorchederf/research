---
created: 2026-11-21
fullpath: 'C:\Windows\System32\msconfig.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - troubleshooting
aliases:
  - msconfig.exe
  - msconfig
  - System Configuration utility
  - System Configuration Utility tool
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/performance/system-configuration-utility-troubleshoot-configuration-errors
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/cannot-boot-into-normal-mode
---

**fullpath**:C:\Windows\System32\msconfig.exe

# description

Msconfig.exe is the System Configuration utility, used to troubleshoot configuration errors that might prevent Windows from starting correctly. It's included in Windows and automates routine troubleshooting steps used by Microsoft Customer Support Services. Related tools include Bcdedit.exe and the tools launchable from its Tools tab.

## simple description

> ### 2026-11-21 Claude said
> msconfig.exe (System Configuration) is a built-in Windows GUI tool for controlling how Windows starts. It lets you pick normal, diagnostic, or selective startup, disable services, and change boot options such as Safe Mode. It's mostly used for "clean boot" troubleshooting. It requires administrator rights.
>
> **SOC NOTE**: Attackers or ransomware may force Safe Mode boot (T1562.009) to bypass security tools; msconfig and `bcdedit /set safeboot` are ways to do this. msconfig is also an auto-elevating binary historically abused for UAC bypass (T1548.002). Check BCD safeboot values, Services tab changes, and process creation of msconfig by unexpected users.
>

# purpose

Finds and isolates startup issues by letting you temporarily prevent services and programs from loading during startup, and easily restore the original configuration. It isn't a startup management program. Startup options: Normal startup, Diagnostic startup, and Selective startup (Load system services, Load startup items, Use original boot configuration). Must be run as an administrator.

# typical use cases

- Perform a diagnostic startup to load only basic drivers and services.
- Perform a selective/clean boot and enable services or startup items one at a time to find the cause of an issue (Services and Startup tabs, Disable all).
- Launch diagnostic and advanced tools from the Tools tab, which also shows their paths and switches.
- Remove the /SAFEBOOT option (BOOT.INI tab on older Windows) when a machine keeps booting into safe mode.
- Return to Normal startup after troubleshooting.

# options

| option    | description    |
| --- | --- |
| _Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_ |  |
