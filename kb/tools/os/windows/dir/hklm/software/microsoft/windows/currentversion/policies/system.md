---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - uac
  - policy
aliases:
  - Policies\System
  - User Account Control registry settings
url:
  - https://learn.microsoft.com/windows/security/application-security/application-control/user-account-control/settings-and-configuration
  - https://learn.microsoft.com/troubleshoot/windows-server/windows-security/user-account-control-and-remote-restriction
  - https://learn.microsoft.com/windows/security/identity-protection/access-control/local-accounts
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System

# description

This key holds the User Account Control (UAC) policy settings that correspond to the Security Options in Group Policy, plus `LocalAccountTokenFilterPolicy`, which controls UAC remote restrictions for local accounts.

## simple description

> ### 2026-11-21 Claude said
> This registry key is where Windows stores many system-wide security policies, most importantly User Account Control settings like whether UAC is on and how the elevation prompt behaves. Group Policy security options write here. It also holds other policy values such as logon banner text and shutdown options.
>
> **SOC NOTE**: A prime target for defense evasion: setting `EnableLUA`=0 or `ConsentPromptBehaviorAdmin`=0 disables or silences UAC (T1548.002), and `LocalAccountTokenFilterPolicy`=1 enables pass-the-hash style remote admin with local accounts (T1550.002). Monitor with Sysmon 13 / 4657 registry auditing and compare to baseline.
>

# purpose

Configure UAC behavior and remote token filtering for the machine.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `FilterAdministratorToken` | REG_DWORD | Admin Approval Mode for the built-in Administrator account. 0 (default) disabled, 1 enabled. |
| `EnableUIADesktopToggle` | REG_DWORD | Allow UIAccess apps to prompt for elevation without the secure desktop. 0 (default) disabled. |
| `ConsentPromptBehaviorAdmin` | REG_DWORD | Elevation prompt for admins: 0 elevate without prompting, 1 credentials on secure desktop, 2 consent on secure desktop, 3 credentials, 4 consent, 5 (default) consent for non-Windows binaries. |
| `ConsentPromptBehaviorUser` | REG_DWORD | Elevation prompt for standard users: 0 auto deny, 1 credentials on secure desktop, 3 (default) credentials. |
| `EnableInstallerDetection` | REG_DWORD | Detect app installations and prompt for elevation. 1 enabled (default for home only), 0 disabled. |
| `ValidateAdminCodeSignatures` | REG_DWORD | Only elevate signed and validated executables. 0 (default) disabled. |
| `EnableSecureUIAPaths` | REG_DWORD | Only elevate UIAccess apps installed in secure locations. 1 (default) enabled. |
| `EnableLUA` | REG_DWORD | Run all administrators in Admin Approval Mode. 1 (default) enabled, 0 disabled. |
| `PromptOnSecureDesktop` | REG_DWORD | Switch to the secure desktop when prompting. 1 (default) enabled. |
| `EnableVirtualization` | REG_DWORD | Virtualize file and registry write failures to per-user locations. 1 (default) enabled. |
| `InteractiveLogonFirst` | REG_DWORD | Prioritise network logons over cached logons. 0 (default) disabled. |
| `LocalAccountTokenFilterPolicy` | REG_DWORD | 0 (default) builds a filtered token for remote local-account logons; 1 builds an elevated token (disables UAC remote restrictions). |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"` | List the key's values. |

