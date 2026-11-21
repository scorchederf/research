---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-NTLM%4Operational.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - event-log
  - ntlm
  - authentication
aliases:
  - Microsoft-Windows-NTLM%4Operational.evtx
  - Microsoft-Windows-NTLM/Operational
  - NTLM Operational log
url:
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-localpoliciessecurityoptions
  - https://learn.microsoft.com/defender-for-identity/deploy/configure-windows-event-collection
  - https://learn.microsoft.com/windows-server/security/kerberos/ntlm-overview
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-NTLM%4Operational.evtx

# description

Event log file backing the **Applications and Services Logs/Microsoft/Windows/NTLM/Operational** channel. NTLM audit and block events produced by the "Network security: Restrict NTLM" policies are recorded here.

## simple description

> ### 2026-11-21 Claude said
> This is the event log where Windows records NTLM authentication auditing and blocking, but only once the Restrict NTLM audit policies are turned on. Admins use it to find which applications and servers still use the old NTLM protocol before disabling it. The %4 in the file name stands for the slash in the channel name.
>
> **SOC NOTE**: Useful for detecting NTLM relay/pass-the-hash and NTLM usage (MITRE T1550.002, T1557.001): events 8001 (outgoing), 8002/8003 (incoming/blocked) and 8004 (DC pass-through, used by Defender for Identity) show client, user, target server and process. Requires audit policies to be enabled first - empty logs usually mean auditing is off, not that NTLM isn't used.
>

# purpose

Stores audit events for outgoing NTLM traffic ("Audit all"), incoming NTLM traffic ("Enable auditing for domain/all accounts"), domain NTLM audit, and block events when "Deny all" settings are configured. Defender for Identity parses event 8004 on domain controllers to enrich NTLM authentication activities.


