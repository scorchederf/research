---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - uac
aliases:
  - "LocalAccountTokenFilterPolicy"
  - "UAC remote restrictions"
  - "Apply UAC restrictions to local accounts on network logons"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/user-account-control-and-remote-restriction
  - https://learn.microsoft.com/windows/security/identity-protection/access-control/local-accounts
  - https://learn.microsoft.com/windows/win32/wmisdk/user-account-control-and-wmi
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_remote_troubleshooting?view=powershell-7.6
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/disable-user-account-control
  - https://learn.microsoft.com/windows-server/storage/storage-migration-service/known-issues
---

**fullpath**: HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy

# description

DWORD registry value under the UAC policy key that controls User Account Control remote restrictions for local administrator accounts on network logons. At the default `0`, a local account that signs in remotely (e.g. NET USE, WinRM, WMI) gets a filtered standard-user token; at `1` it gets a full elevated token. It can be enforced via Group Policy Preferences or the Security Compliance Toolkit setting "Apply UAC restrictions to local accounts on network logons" (MS Security Guide / SCM: Pass the Hash Mitigations).

## simple description

> ### 2026-11-21 Claude said
> By default, when someone connects to a Windows machine over the network using a local admin account (not a domain account), Windows strips their admin rights. This value turns that protection off when set to 1, so remote local admins get full rights - for example to use C$/ADMIN$ shares, PsExec, WMI or WinRM. Admins sometimes set it in workgroups to make remote management work.
>
> **SOC NOTE**: Setting LocalAccountTokenFilterPolicy=1 is a common attacker step to enable pass-the-hash and lateral movement with local admin hashes (T1550.002, T1021.002) and appears as T1112 Modify Registry / T1562 impair defenses. Alert on changes to this value (Sysmon 13, Security 4657) and on `reg add ... LocalAccountTokenFilterPolicy /d 1` command lines. Pair with LAPS and denying network logon to local admins.
>

# purpose

Controls whether remote UAC token filtering applies to local accounts. With filtering on, local accounts that sign in by network logon can't access administrative shares such as C$ or ADMIN$ or perform remote administration; also, administrators from other domains connect with standard-user tokens. Microsoft recommends keeping it at 0 to mitigate pass-the-hash risk; disabling it removes the restriction for all users of the affected computer. Storage Migration Service temporarily enables it during cutover, and a GPO forcing 0 can make cutover hang.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `LocalAccountTokenFilterPolicy` | REG_DWORD | `0` (default) builds a filtered token - administrator credentials are removed, remote UAC filtering enabled. `1` builds an elevated token - remote UAC restrictions disabled. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v LocalAccountTokenFilterPolicy` | Show the current value. |
| `New-ItemProperty -Name LocalAccountTokenFilterPolicy -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -PropertyType DWord -Value 1` | Disable UAC remote restrictions (documented for cross-domain PowerShell remoting; weakens security). |
| `gpupdate /force /target:computer` | Apply a GPO that enforces the value 0 on workstations. |
