---
created: 2026-11-21
fullpath: 'C:\Windows\debug'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - logs
  - netlogon
  - domain-join
aliases:
  - debug
  - %windir%\debug
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/active-directory-domain-join-troubleshooting-guidance
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/domain-join-log-analysis
  - https://learn.microsoft.com/troubleshoot/windows-client/windows-security/enable-debug-logging-netlogon-service
  - https://learn.microsoft.com/windows/win32/api/lmjoin/nf-lmjoin-netcreateprovisioningpackage
---

**fullpath**:C:\Windows\debug

# description

`%windir%\debug` is the Windows folder that holds diagnostic logs for domain join, offline domain join provisioning and the Netlogon service, notably `Netsetup.log` and `netlogon.log`.

## simple description

> ### 2026-11-21 Claude said
> C:\Windows\debug is where Windows writes troubleshooting logs for joining a computer to a domain and for the Netlogon service, which handles domain authentication. Netsetup.log is on by default; netlogon.log fills up only when verbose Netlogon logging is enabled. Admins read these files when domain joins or DC discovery fail.
>
> **SOC NOTE**: netsetup.log records domain join/unjoin events with timestamps, account and DC names - useful to timeline a rogue machine join or offline domain join (djoin). netlogon.log (when enabled) shows authentication and secure-channel activity, e.g. useful when investigating Zerologon (CVE-2020-1472). The folder is writable only by admins, but check for unexpected executables placed there.
>

# purpose

Default location of the domain join log (enabled by default, no need to enable explicitly), of provisioning operations performed by admins (non-admin provisioning logs go to `%USERPROFILE%\Debug`), and of Netlogon debug output after `Nltest /DBFlag:0x2080FFFF` or the "Specify log file debug output level" policy.

# common files found

| file | description |
| --- | --- |
| `Netsetup.log` | Domain join and offline domain join provisioning activity; enabled by default. |
| `netlogon.log` | Netlogon service debug log when verbose Netlogon logging is enabled. |
