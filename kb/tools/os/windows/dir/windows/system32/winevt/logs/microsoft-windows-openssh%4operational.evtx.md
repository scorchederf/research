---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-OpenSSH%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - evtx
  - openssh
aliases:
  - "Microsoft-Windows-OpenSSH%4Operational.evtx"
  - "OpenSSH/Operational"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/upgrade-in-box-openssh-to-latest-openssh-release
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/enable-openssh-verbose-logging
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/error-1053-1067-7034-after-update-openssh-doesnt-start
  - https://learn.microsoft.com/answers/a/12217128
---

**fullpath**: C:\Windows\System32\winevt\Logs\Microsoft-Windows-OpenSSH%4Operational.evtx

# description

Event log file backing the `OpenSSH/Operational` channel, shown in Event Viewer under **Applications and Services Logs** > **OpenSSH** > **Operational**. It is written by OpenSSH for Windows (the in-box `sshd` OpenSSH SSH Server and related components). Related logs can instead be written to `%ProgramData%\ssh\logs` when configured.

## simple description

> ### 2026-11-21 Claude said
> This file stores the events written by the built-in OpenSSH server and agent on Windows. It records things like successful and failed SSH logons, disconnects and service errors. Administrators read it in Event Viewer or with Get-WinEvent. It only gets meaningful content when the OpenSSH Server feature is installed and in use.
>
> **SOC NOTE**: Key source for detecting SSH brute force, lateral movement and remote access over SSH (T1021.004 Remote Services: SSH, T1110 Brute Force). Events such as "Accepted password/publickey for <user> from <ip>" and "Failed password" give user, source IP and port. Clearing the log (T1070.001) or switching sshd_config to SyslogFacility LOCAL0 to divert logs is suspicious. Raising LogLevel to VERBOSE adds key fingerprints.
>

# purpose

By default the OpenSSH Server service sends its logs to Windows Event Viewer, into this channel. Learn recommends checking it for errors after installing or upgrading OpenSSH and when troubleshooting. Setting `SyslogFacility LOCAL0` in `%ProgramData%\ssh\sshd_config` writes log files to `%ProgramData%\ssh\logs` instead; `LogLevel VERBOSE` increases detail. The legacy `Get-EventLog` cmdlet cannot read this channel; use `Get-WinEvent -LogName "OpenSSH/Operational"`.
