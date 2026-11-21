---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - safe-mode
  - boot
aliases:
  - "SafeBoot"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/not-boot-in-normal-mode-driver-issue
  - https://learn.microsoft.com/windows-hardware/drivers/taef/te-service
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/cannot-boot-into-normal-mode
  - https://learn.microsoft.com/windows-hardware/drivers/kernel/determining-whether-the-operating-system-is-running-in-safe-mode
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot

# description

The SafeBoot key lists the drivers and services that Windows loads when it starts in Safe Mode. Its `Minimal` subkey covers pure Safe Mode and its `Network` subkey covers Safe Mode with Networking; Safe Mode itself is selected with the `safeboot` BCD option (bcdedit or msconfig).

## simple description

> ### 2026-11-21 Claude said
> Safe Mode starts Windows with only a minimal set of drivers and services, and this key is the allow-list that decides which ones are loaded. Each allowed driver or service has a subkey under `Minimal` or `Network` whose default value is its type (for example `Service` or `Driver`). Anything not listed here will not start in Safe Mode, which is why Safe Mode is used to troubleshoot bad drivers. An `AlternateShell` value defines the shell used for Safe Mode with Command Prompt.
>
> **SOC NOTE**: Ransomware (e.g., REvil, Snatch, BlackMatter) reboots victims into Safe Mode with `bcdedit /set {current} safeboot minimal` so that EDR/AV does not load, and adds its own service under `SafeBoot\Minimal` or `Network` so it still runs (T1562.009 Safe Mode Boot). Removal of security product entries from these subkeys is also a red flag. Monitor registry writes here (Sysmon 12/13) and bcdedit safeboot changes.
>

# purpose

Controls which drivers and services are allowed to start in Safe Mode. Adding a subkey named after a service under `Minimal` (pure Safe Mode) or `Network` (Safe Mode with Networking) with a default value of `Service` lets that service start in Safe Mode; otherwise starting it fails with error 1084 (This service cannot be started in Safe Mode). Drivers can detect Safe Mode through the kernel `InitSafeBootMode` variable (1 = SAFEBOOT_MINIMAL, 2 = SAFEBOOT_NETWORK, 3 = SAFEBOOT_DSREPAIR).

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SYSTEM |

# values

| value name | type | description |
| --- | --- | --- |
| (Default) of each service subkey | REG_SZ | Set to `Service` to allow the named service to start in Safe Mode. |

# subkeys

| subkey | description |
| --- | --- |
| `Minimal` | Drivers and services allowed in pure Safe Mode. |
| `Network` | Drivers and services allowed in Safe Mode with networking. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal" /s` | List every driver and service allowed in Safe Mode. |
| `bcdedit /deletevalue {default} safeboot` | Remove the safeboot flag so the machine boots in normal mode. |
