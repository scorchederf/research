---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Security-Mitigations%4KernelMode.evtx'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Microsoft-Windows-Security-Mitigations%4KernelMode.evtx
  - Microsoft-Windows-Security-Mitigations/KernelMode
url:
  - https://learn.microsoft.com/defender-endpoint/exploit-protection
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-Security-Mitigations%4KernelMode.evtx

# description

Event log file for the Security-Mitigations provider's KernelMode channel. Microsoft Learn documents Security-Mitigations events (IDs 1-24) created when exploit protection blocks or audits an app, but does not document this specific KernelMode log file.

## simple description

> ### 2026-11-21 Claude said
> This .evtx file stores the "Microsoft-Windows-Security-Mitigations/KernelMode" event log, viewable in Event Viewer under Applications and Services Logs > Microsoft > Windows > Security-Mitigations. It records events when Windows exploit-protection mitigations (Exploit Protection / former EMET features such as ACG, CIG, blocking remote or low-integrity images, disabling win32k calls) audit or block something enforced from the kernel side. The `%4` in the name stands for the `/` in the channel name. A companion UserMode log holds user-mode mitigation events.
>
> **SOC NOTE**: Block/audit events here (e.g. code integrity guard 11/12, block remote/low-integrity images 5-8, ACG 1/2) can reveal exploitation attempts or injection of unsigned DLLs into protected processes (MITRE ATT&CK T1203, T1055). Correlate the process name in the event with process creation logs. Attackers clearing logs (T1070.001) can remove this evidence.
>

# purpose

Stores kernel-mode Security-Mitigations events. Learn documents the Security-Mitigations event IDs: 1/2 ACG audit/enforce, 3/4 child process audit/block, 5/6 low integrity images, 7/8 remote images, 9/10 win32k system calls, 11/12 code integrity guard, 13-16 EAF/EAF+, 17/18 IAF, 19-24 ROP StackPivot/CallerCheck/SimExec audit/enforce.
