---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Enrollments'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - mdm
  - intune
aliases:
  - "Enrollments"
  - "MDM enrollments"
url:
  - https://learn.microsoft.com/windows/client-management/mdm-diagnose-enrollment
  - https://learn.microsoft.com/windows/client-management/mobile-device-enrollment
  - https://learn.microsoft.com/answers/a/12210560
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Enrollments

# description

The Enrollments key stores enrollment information for MDM solutions (such as Microsoft Intune) and related device enrollment features like Microsoft Entra ID join. Entries are added when a device enrolls and are normally removed when it unenrolls; MDM enrollment can be disabled with the `HKLM\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\MDM\DisableRegistration` policy.

## simple description

> ### 2026-11-21 Claude said
> This key records each management enrollment of the device, one GUID subkey per enrollment. Values inside describe the provider (e.g., MS DM Server for Intune), the enrolled UPN, the enrollment type and the server URLs. Some subkeys exist by default on any Windows install and do not by themselves mean the PC is company-managed.
>
> **SOC NOTE**: Shows whether and when a device was enrolled in MDM and to which tenant/user, useful in insider or BYOD investigations. Attackers abusing rogue MDM enrollment for persistence or policy push will leave a new GUID subkey here; stale entries can also break auto-enrollment.
>

# purpose

Holds per-enrollment data for MDM. Outdated entries can remain after unenrollment and cause Group Policy auto-enrollment to fail with error 2149056522 (Task Scheduler event ID 7016); the fix is to remove the stale enrollment subkey manually, typically the one with the most entries. Device ownership is managed in Settings > Accounts > Access work or school.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SOFTWARE |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# subkeys

| subkey | description |
| --- | --- |
| `<enrollment GUID>` | One subkey per MDM enrollment containing the enrollment information; normally removed when the device is unenrolled. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Enrollments"` | List the key's values and enrollment subkeys. |
| `reg query "HKLM\SOFTWARE\Microsoft\Enrollments" /s` | Dump all enrollment data recursively. |
