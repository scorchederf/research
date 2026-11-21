---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Security.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - security
aliases:
  - Security.evtx
  - Security log
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/application-management/move-event-viewer-log-files
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-eventlog
  - https://learn.microsoft.com/windows/win32/eventlog/eventlog-key
---

**fullpath**:C:\Windows\System32\winevt\Logs\Security.evtx

# description

File backing the Windows Security event log, stored by default in `%SystemRoot%\System32\winevt\Logs`. The Security log contains events such as valid and invalid logon attempts and resource use (create, open, delete files); administrators control which events are recorded. Its location can be changed with the `Control the location of the log file` policy (`Software\Policies\Microsoft\Windows\EventLog\Security`) or the `File` value under `HKLM\SYSTEM\CurrentControlSet\Services\Eventlog\Security`.

## simple description

> ### 2026-11-21 Claude said
> Security.evtx is the main audit log of Windows. It records logons and logoffs, privilege use, account changes, process creation (if enabled) and object access according to the audit policy. Only administrators can read it. It is one of the first files collected in any investigation.
>
> **SOC NOTE**: Core forensic artifact: 4624/4625 logons, 4672 special privileges, 4688 process creation, 4720/4732 account and group changes, 4698 scheduled task created, 1102 log cleared (MITRE ATT&CK T1070.001). Gaps in record IDs or a small file size can indicate tampering.
>

# purpose

Stores Security events (auditing). Can be moved or resized via policy or the Eventlog registry key.
