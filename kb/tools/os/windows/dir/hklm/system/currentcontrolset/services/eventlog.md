---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\EventLog'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - event-log
aliases:
  - "EventLog"
  - "Eventlog key"
url:
  - https://learn.microsoft.com/windows/win32/eventlog/eventlog-key
  - https://learn.microsoft.com/windows/win32/eventlog/event-sources
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Services\EventLog

# description

Registry key used by the event logging service; its subkeys are logs (Application, Security, System and custom logs), each containing event sources. It belongs to the legacy Event Logging API; Windows Vista and later use Windows Event Log, and log file paths should be set with wevtutil.exe or EvtSetChannelConfigProperty.

## simple description

> ### 2026-11-21 Claude said
> This is the configuration key for the Windows Event Log service. Each log (Application, System, Security, and custom ones) has a subkey with settings like maximum size, retention and file path, and each application or driver that writes events registers an event source subkey pointing to its message DLL.
>
> **SOC NOTE**: Attackers tamper here to impair logging (T1562.002): shrinking MaxSize, changing File, or editing CustomSD to block reading. Event source subkeys with odd EventMessageFile/CategoryMessageFile DLLs can be used for persistence/DLL loading. Monitor writes to this key and Event ID 1102/104 log clears.
>

# purpose

The event logging service uses the information stored in the Eventlog key. Each log subkey contains information the service uses to locate resources when an application writes to and reads from the event log. Domain controllers also record events in Directory service and File Replication service logs, and DNS servers in DNS server.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SYSTEM |

# values

| value name | type | description |
| --- | --- | --- |
| `AutoBackupLogFiles` | REG_DWORD | Whether a log is automatically saved; default 0 disables auto-backup. Works only if Retention is -1 (0xFFFFFFFF). (per-log value) |
| `CustomSD` | REG_SZ | SDDL restricting access to the log (Clear 0x4, Read 0x1, Write 0x2); SACLs not supported. (per-log value) |
| `DisplayNameFile` | - | Not used. |
| `DisplayNameID` | - | Not used. |
| `File` | REG_SZ / REG_EXPAND_SZ | Fully qualified path of the log file; defaults to %SystemRoot%\system32\winevt\logs\ plus a name based on the key. (per-log value) |
| `MaxSize` | REG_DWORD | Maximum log file size in bytes; multiple of 64K for System, Application, Security; default 1MB. (per-log value) |
| `PrimaryModule` | - | Not used. |
| `Retention` | REG_DWORD | 0 = records always overwritten; nonzero/0xFFFFFFFF = never overwritten and log must be cleared manually. (per-log value) |
| `Sources` | - | Not used. |
| `RestrictGuestAccess` | - | Not used. |
| `Isolation` | REG_SZ | Default access permissions for the log: Application (default), System or Custom. (per-log value) |

# subkeys

| subkey | description |
| --- | --- |
| `Application` | Events logged by applications. |
| `Security` | Logon attempts and resource-use audit events; for system use only. |
| `System` | Events logged by system components such as drivers; device drivers add their sources here. |
| `<CustomLog>` | Custom log created by an application to control size or ACLs. |
| `<Log>\<SourceName>` | Event source (application/driver name) with source-specific info such as the message file; up to 16,384 sources. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\EventLog"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\EventLog\System"` | List the System log settings and its event sources. |
