---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - firewall
aliases:
  - "FirewallPolicy"
  - "Windows Firewall local policy store"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/disable-stealth-mode
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/enable-disable-firewall-rule-guest-os
---

**fullpath**: HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy

# description

Registry key holding the local Windows Defender Firewall configuration: per-profile settings (DomainProfile, PublicProfile, StandardProfile) and the local firewall rules (FirewallRules). Group Policy settings are stored separately under `HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall`. Rules are normally managed with `netsh advfirewall`, the NetSecurity PowerShell cmdlets or the Windows Defender Firewall with Advanced Security console.

## simple description

> ### 2026-11-21 Claude said
> This is where Windows keeps the local firewall settings and rules. Each profile (domain, private/standard, public) has its own subkey with options like whether the firewall is enabled, and every firewall rule is stored as one pipe-delimited string under FirewallRules. Tools like netsh and Set-NetFirewallRule write here behind the scenes. Because it is in the SYSTEM hive, it can even be edited offline.
>
> **SOC NOTE**: Attackers disable the firewall (EnableFirewall=0) or add allow rules (e.g. for RDP 3389 or a C2 binary) here - T1562.004 Impair Defenses: Disable or Modify System Firewall. Watch Security events 4946-4950 and the Microsoft-Windows-Windows Firewall With Advanced Security/Firewall log (2004/2005/2006/2097), plus Sysmon 13 on this key. In forensics, FirewallRules shows rules added by malware or remote-access tools.
>

# purpose

Stores the local firewall profile settings and firewall rules. Learn documents editing it to disable stealth mode (adding `DisableStealthMode` to a profile subkey) and to enable or disable a rule offline by changing `Active=TRUE`/`Active=FALSE` inside a rule string, for example on an Azure VM whose disk is attached to a recovery VM.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# subkeys

| subkey | description |
| --- | --- |
| `DomainProfile` | Domain profile settings; can hold `DisableStealthMode` (REG_DWORD, 0 = stealth mode enabled (default), 1 = disabled). |
| `PublicProfile` | Public profile settings; can hold `DisableStealthMode`. |
| `StandardProfile` | Standard (private) profile settings; can hold `DisableStealthMode`. |
| `FirewallRules` | One string value per rule, e.g. `RemoteDesktop-UserMode-In-TCP` = `v2.22\|Action=Allow\|Active=TRUE\|Dir=In\|Protocol=6\|...\|LPort=3389\|...`. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\FirewallRules"` | List all local firewall rule strings. |
| `netsh advfirewall firewall set rule dir=in name="Remote Desktop - User Mode (TCP-In)" new enable=yes` | Enable a rule the supported way instead of editing the registry. |
