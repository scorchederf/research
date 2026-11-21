---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - w32time
  - time
aliases:
  - "TimeProviders"
  - "W32Time time providers"
url:
  - https://learn.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings
  - https://learn.microsoft.com/azure/virtual-machines/windows/time-sync
  - https://learn.microsoft.com/windows-server/networking/windows-time-service/windows-server-2016-improvements
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/time-synchronization-not-succeed-non-ntp
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders

# description

The TimeProviders key holds the configuration of the time providers used by the Windows Time service (W32Time), such as the NtpClient and NtpServer providers and, on Azure/Hyper-V guests, VMICTimeProvider. Group Policy settings under Computer Configuration\Administrative Templates\System\Windows Time Service\Time Providers map to these subkeys; the service is managed with `w32tm`.

## simple description

> ### 2026-11-21 Claude said
> W32Time is the Windows service that keeps the clock synchronised, and it does so through pluggable time providers. Each provider (NtpClient, NtpServer, VMICTimeProvider) has a subkey here with an `Enabled` flag and a `DllName` that points to the provider DLL. Domain members sync from domain controllers through NtpClient; NtpServer lets a machine serve time to others.
>
> **SOC NOTE**: A custom time provider DLL registered here is loaded by svchost/W32Time at service start, a known persistence technique (T1547.003 Time Providers); check every `DllName` points to `%windir%\System32\w32time.dll` or a known vendor DLL. Tampering with time sync can also break Kerberos and log correlation.
>

# purpose

Stores per-provider settings for W32Time. Enabling or disabling providers changes where the computer gets time, for example disabling NtpClient and enabling NtpServer on a DC with GPS hardware, or enabling VMICTimeProvider for host-only time sync on Azure VMs. If NtpServer `Enabled` is 1, Windows Time uses symmetric active mode; otherwise it uses client mode.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SYSTEM |

# values

| value name | type | description |
| --- | --- | --- |
| `NtpClient\Enabled` | REG_DWORD | Whether the NtpClient provider is enabled (1 = yes, 0 = no); default 1. |
| `NtpClient\DllName` | REG_SZ | Location of the provider DLL; default `%windir%\System32\W32Time.dll`. |
| `NtpClient\CrossSiteSyncFlags` | REG_DWORD | Whether partners outside the domain can be chosen (0 None, 1 PdcOnly, 2 All); default 2. |
| `NtpClient\SpecialPollInterval` | REG_DWORD | Poll interval in seconds for manual peers when the 0x1 flag is set; default 3,600 on domain members and 604,800 on stand-alone machines. |
| `NtpClient\ResolvePeerBackoffMinutes` | REG_DWORD | Initial wait in minutes before retrying to locate a peer; default 15. |
| `NtpClient\ResolvePeerBackoffMaxTimes` | REG_DWORD | Maximum number of times the wait interval is doubled; default 7. |
| `NtpClient\EventLogFlags` | REG_DWORD | Events logged (0x1 reachability changes, 0x2 large sample skew). |
| `NtpServer\Enabled` | REG_DWORD | Whether the NtpServer provider is enabled; default 0. |
| `NtpServer\DllName` | REG_SZ | Location of the provider DLL; default `%windir%\System32\W32Time.dll`. |
| `NtpServer\RequireSecureTimeSyncRequests` | REG_DWORD | If 1, the DC does not respond to time sync requests using older authentication protocols; default 0. |
| `NtpServer\ChainDisable` | REG_DWORD | Controls whether the RODC chaining mechanism is disabled; default 0. |
| `VMICTimeProvider\Enabled` | REG_DWORD | Set to 1 to enable host-based (VMIC) time sync on Azure VMs. |

# subkeys

| subkey | description |
| --- | --- |
| `NtpClient` | Settings for the NTP client provider. |
| `NtpServer` | Settings for the NTP server provider. |
| `VMICTimeProvider` | Hyper-V/Azure host time provider. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders" /s` | List all time providers and their values. |
| `w32tm /query /configuration` | Show the effective W32Time configuration, including providers. |
| `reg add HKLM\SYSTEM\CurrentControlSet\Services\w32time\TimeProviders\NtpClient /v Enabled /t REG_DWORD /d 0 /f` | Disable the NtpClient provider. |
