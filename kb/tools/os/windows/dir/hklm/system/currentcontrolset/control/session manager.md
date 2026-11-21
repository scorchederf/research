---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Session Manager'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - hklm
aliases:
  - Session Manager
  - Session Manager key
url:
  - https://learn.microsoft.com/industry/healthcare/powerscribe-one/client-installation-guide/dvd-image-install-upgrade
  - https://learn.microsoft.com/windows/win32/memory/memory-management-registry-keys
  - https://learn.microsoft.com/windows-hardware/test/wpt/kernel-trace-control-api-reference
  - https://learn.microsoft.com/powershell/dsc/reference/psdscresources/resources/registry/addormodifyvalue?view=dsc-2.0
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/terminal-server-startup-connection-application
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\Session Manager

# description

The `Session Manager` key holds configuration for the Windows Session Manager (SMSS), which the Terminal Server service calls to create new user sessions. It contains values such as `PendingFileRenameOperations` and subkeys such as `Environment` and `Memory Management`. It is part of the SYSTEM hive under the current control set.

## simple description

> ### 2026-11-21 Claude said
> This registry key configures the Session Manager (`smss.exe`), the first user-mode process Windows starts at boot. It controls things like system environment variables, the page file, known DLLs, DOS device names and files that must be renamed or deleted at the next reboot. Windows reads it very early during startup, before most security software runs. Admins rarely change it by hand.
>
> **SOC NOTE**: High-value persistence and tampering location. `BootExecute` (T1547.001 / boot-time autostart) runs native programs before Windows loads; `PendingFileRenameOperations` can replace or delete protected files at reboot; `KnownDLLs` and `SafeDllSearchMode` changes enable DLL hijacking (T1574.001); `AppCertDlls` (T1546.009) loads DLLs into processes that call CreateProcess. `Environment` changes can hijack PATH. Watch Sysmon Event ID 13 and registry auditing (4657) for writes under this key.
>

# purpose

Stores Session Manager settings that Windows applies at boot and session creation. Learn documents it as the location of pending-restart markers (`PendingFileRenameOperations`), the system environment variables (`Environment` subkey) and memory management settings (`Memory Management` subkey).

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `PendingFileRenameOperations` | — | If the value exists, the workstation has a pending restart. |
| `PendingFileRenameOperations2` | — | If the value exists, the workstation has a pending restart. |

# subkeys

| subkey | description |
| --- | --- |
| `Environment` | System environment variables; used as an example key for DSC `Registry` resource value changes. |
| `Memory Management` | Memory settings such as `NonPagedPoolLimit`, `PagedPoolLimit`, `SessionSpaceLimit`, `SystemCacheLimit`, `SystemPtesLimit` (32-bit systems) and `DisablePagingExecutive`. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager"` | List the key's values. |
| `reg query "HKLM\System\CurrentControlSet\Control\Session Manager\Memory Management" -v DisablePagingExecutive` | Query the `DisablePagingExecutive` value used for x64 stackwalking. |
