---
created: 2026-11-21
fullpath: 'C:\Windows\System32\drivers'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - drivers
  - kernel
aliases:
  - "drivers"
  - "%SystemRoot%\\System32\\Drivers"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/setup-upgrade-and-drivers/use-recovery-console-replace-driver
  - https://learn.microsoft.com/windows/win32/cimwin32prov/win32-systemdriver
  - https://learn.microsoft.com/windows-hardware/drivers/install/inf-addservice-directive
  - https://learn.microsoft.com/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree
---

**fullpath**:C:\Windows\System32\drivers

# description

`%SystemRoot%\System32\Drivers` is the folder where Windows kernel-mode driver files (.sys) are typically stored. Driver services registered under `HKLM\SYSTEM\CurrentControlSet\Services` point to binaries here through `ImagePath` (for example `\SystemRoot\System32\drivers\afd.sys`).

## simple description

> ### 2026-11-21 Claude said
> This folder contains the kernel-mode drivers that let Windows talk to hardware and implement core features such as file systems, networking and security filters. Each .sys file is loaded into the kernel by a service entry in the registry. It also contains the `etc` subfolder with the hosts, networks, protocol and services files.
>
> **SOC NOTE**: Attackers drop malicious or vulnerable signed drivers here to gain kernel access and kill EDR (T1543.003, T1068 BYOVD) and rootkits hide as .sys files. Check new .sys files against known-vulnerable driver lists, Sysmon event 6 (driver loaded), System event 7045 (service installed), and the `etc\hosts` file for DNS hijacking (T1565.001).
>

# purpose

Stores driver binaries referenced by driver services. INF files install drivers here, and event-log message files for drivers are usually referenced as `%SystemRoot%\System32\drivers\driver.sys`; damaged drivers can be replaced by expanding them from installation media into this folder.

# common files found

| file | description |
| --- | --- |
| afd.sys | Example service binary path given for Win32_SystemDriver PathName (`\SystemRoot\System32\drivers\afd.sys`). |
| *.sys | Kernel-mode driver binaries installed by INF ServiceBinary entries. |
