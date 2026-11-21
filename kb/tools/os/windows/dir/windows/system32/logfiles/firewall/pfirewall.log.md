---
created: 2026-11-21
fullpath: 'C:\Windows\System32\LogFiles\Firewall\pfirewall.log'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - windows
aliases:
  - "pfirewall.log"
  - "Windows Firewall log"
url:
  - https://learn.microsoft.com/windows/security/operating-system-security/network-security/windows-firewall/configure-logging
  - https://learn.microsoft.com/azure/azure-monitor/vm/data-collection-firewall-logs
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/netsh-advfirewall-firewall-control-firewall-behavior
  - https://learn.microsoft.com/windows/client-management/mdm/firewall-csp
---

**fullpath**:C:\Windows\System32\LogFiles\Firewall\pfirewall.log

# description

`pfirewall.log` is the default Windows Firewall (Windows Defender Firewall with Advanced Security) log file, `%windir%\system32\logfiles\firewall\pfirewall.log`. It is written by the Windows Defender Firewall service (`mpssvc`) and is configured through Group Policy, the Firewall CSP, `netsh advfirewall` or `Set-NetFirewallProfile`.

## simple description

> ### 2026-11-21 Claude said
> This is the text log where Windows Firewall records network connections it dropped or allowed. Logging is off by default and only starts when an administrator enables "Log dropped packets" or "Log successful connections". Each line records a timestamp, action (ALLOW/DROP), protocol, source and destination IPs and ports. The file is size-limited and old entries are overwritten when it fills up.
>
> **SOC NOTE**: Useful for reconstructing lateral movement, scanning (many DROPs from one source), C2 or exfiltration connections when EDR network telemetry is missing. Attackers may disable firewall logging or the firewall itself (`netsh advfirewall set allprofiles state off`, MITRE ATT&CK T1562.004 Impair Defenses: Disable or Modify System Firewall) or clear the log (T1070). The default 4 MB size means older evidence rolls off quickly; collect it early.
>

# purpose

Records packets dropped by Windows Defender Firewall and/or inbound connections it allowed, per profile (Domain, Private, Public). The default maximum size is 4,096 KB; when the limit is reached old entries are deleted to make room for new ones. Microsoft recommends at least 20,480 KB (max 32,767 KB) and separate files per profile (`pfirewall_Domain.log`, `pfirewall_Private.log`, `pfirewall_Public.log`). The `mpssvc` service needs Full Control on the folder; if logging is configured by policy, the `Firewall` folder may need to be created manually. Logs can be forwarded with WEF, to Microsoft Sentinel, or to Azure Monitor.


