---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - sysmon
aliases:
  - Microsoft-Windows-Sysmon%4Operational.evtx
  - Microsoft-Windows-Sysmon/Operational
  - Sysmon Operational log
url:
  - https://learn.microsoft.com/sysinternals/downloads/sysmon
  - https://learn.microsoft.com/windows/security/operating-system-security/sysmon/read-tune-sysmon-events
  - https://learn.microsoft.com/windows/security/operating-system-security/sysmon/sysmon-events
  - https://learn.microsoft.com/windows/security/operating-system-security/sysmon/overview
  - https://learn.microsoft.com/windows-server/administration/windows-commands/sysmon
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx

# description

The event log file backing the `Applications and Services Logs/Microsoft/Windows/Sysmon/Operational` channel, where System Monitor (Sysmon) writes its events on Windows Vista and later. Sysmon is available as the Sysinternals download and, from 2026, as a built-in optional feature of Windows 11 and Windows Server 2025; events are viewed in Event Viewer or collected by Windows Event Collection or SIEM agents.

## simple description

> ### 2026-11-21 Claude said
> This .evtx file is where Sysmon stores everything it records: process starts with full command lines and hashes, network connections, driver and DLL loads, registry changes, file creations, DNS queries and more. The "%4" in the name is how Windows encodes the "/" in the channel name "Microsoft-Windows-Sysmon/Operational". You read it in Event Viewer or with tools like wevtutil or Get-WinEvent. It only exists once Sysmon is installed or enabled.
>
> **SOC NOTE**: One of the most valuable host logs for investigations (process tree via ProcessGuid, Event ID 1 process create, 3 network, 7 image load, 8 CreateRemoteThread, 10 process access e.g. LSASS dumping, 11 file create, 12-14 registry, 22 DNS, 23/26 file delete, 25 process tampering). Attackers target it for defense evasion: clearing the log (System Event ID 104), uninstalling Sysmon (Event ID 4/16 config/state changes), or unloading the driver (T1562.002/T1070.001). Collect the file in triage and check its size/retention, since default max size is small.
>

# purpose

Stores Sysmon events, which record process creations with full command lines and hashes, network connections, driver and image loads, file creation time changes, raw disk access, registry, DNS, clipboard, file delete and process tampering events, among others. Event timestamps are in UTC. Events are structured records (event ID, process and parent information, command line, file paths, network addresses, hashes and identifiers) meant to be correlated into timelines for detecting malicious or anomalous activity.
