---
created: 2026-11-21
fullpath: 'C:\Windows\SYSVOL\domain\Policies\{<GPO-GUID>}\Machine\Preferences\Groups\Groups.xml'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - group-policy
  - sysvol
aliases:
  - "Groups.xml"
  - "Group Policy Local Users and Groups"
url:
  - https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-preferences
  - https://learn.microsoft.com/defender-for-identity/security-posture-assessments/group-policy
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/information-group-policy-preferences-events
---

**fullpath**: C:\Windows\SYSVOL\domain\Policies\{<GPO-GUID>}\Machine\Preferences\Groups\Groups.xml

# description

Groups.xml is the Group Policy Preferences file for the Local Users and Groups client-side extension in a GPO's computer (Machine) section, stored in SYSVOL. It defines local users and groups to create, modify or delete on target computers.

## simple description

> ### 2026-11-21 Claude said
> This XML file inside a GPO in SYSVOL tells computers which local users and groups to create or change, e.g. adding a domain group to local Administrators or setting a local admin password. Every authenticated domain user can read SYSVOL. Group Policy applies it on the next refresh.
>
> **SOC NOTE**: Older GPP items stored passwords as a cpassword attribute encrypted with a public AES key (MS14-025), trivially decryptable (T1552.006 Group Policy Preferences). Search SYSVOL for cpassword, rotate any exposed passwords, and watch for unexpected changes to Groups.xml that add accounts to local Administrators (T1484.001).
>

# purpose

Holds settings of the Group Policy Local Users and Groups extension (create, modify or delete local users and groups). Defender for Identity flags reversible passwords found in GPO preference items; removing the stored credentials does not invalidate passwords that may already have been obtained, so change exposed passwords. GPP events from source 'Group Policy Local Users and Groups' are written to the Application log.
