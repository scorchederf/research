---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - services
  - drivers
  - persistence
aliases:
  - Services
  - Services registry tree
  - SCM database
  - ServicesActive database
url:
  - https://learn.microsoft.com/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree
  - https://learn.microsoft.com/windows/win32/services/database-of-installed-services
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services

# description

Registry tree that stores information about each service and driver on the system; it is the Service Control Manager's database of installed services (also called the ServicesActive or SCM database). Each service has a subkey named after the service, created via `CreateService` or an INF AddService directive.

## simple description

> ### 2026-11-21 Claude said
> This key lists every Windows service and driver: each subkey (for example Spooler or WinDefend) defines what binary runs, when it starts, which account it runs as and how errors are handled. The Service Control Manager reads it at boot to decide what to load. Tools like sc.exe and services.msc read and write it. Changes generally take effect on the next service start or reboot.
>
> **SOC NOTE**: Classic persistence and privilege-escalation location: new services (T1543.003, Event 7045 / 4697), modified ImagePath or ServiceDll, weak key ACLs, Start=4 to disable security tools (T1562.001), and malicious drivers (Type 1). Check ImagePath for paths in temp/user folders, unquoted paths, and Parameters\ServiceDll for svchost services. Compare against baselines/Autoruns.
>

# purpose

Contains a subkey per installed service and driver service with: service type, start type, error control level, fully qualified executable path (.exe for services, .sys for drivers), dependency/load-order information, optional account name, and for drivers an optional driver object name. The PnP manager passes a driver's key path as RegistryPath to DriverEntry. Microsoft advises using SCM functions rather than editing the database directly.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | `%SystemRoot%\System32\config\SYSTEM` (System, System.alt, System.log, System.sav) |

# values

Values below are found under each `Services\<ServiceName>` subkey.

| value name | type | description |
| --- | --- | --- |
| `Start` | REG_DWORD | When the service starts: 0x0 Boot, 0x1 System, 0x2 Automatic, 0x3 Demand, 0x4 Disabled. |
| `Type` | REG_DWORD | Service type: 0x1 kernel driver, 0x2 file system driver, 0x10 Win32 own process, 0x20 Win32 share process. |
| `ErrorControl` | REG_DWORD | Severity if start fails: 0x0 Ignore, 0x1 Normal, 0x2 Severe (restart with last-known-good), 0x3 Critical. |
| `ImagePath` | REG_EXPAND_SZ | Path to the service binary, from the INF ServiceBinary entry. |
| `DisplayName` | REG_SZ | Friendly name of the service. |
| `Description` | REG_SZ | Description of the service. |

# subkeys

| subkey | description |
| --- | --- |
| `<ServiceName>` | One key per installed service or driver, named as passed to `CreateService`. |
| `<ServiceName>\Parameters` | Driver/service-specific data, added via INF AddReg directives. |
| `<ServiceName>\Performance` | Optional performance monitoring info: performance DLL name and exported function names. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services"` | List the key's subkeys (installed services and drivers). |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName>"` | Show Start, Type, ImagePath and other values of one service. |
