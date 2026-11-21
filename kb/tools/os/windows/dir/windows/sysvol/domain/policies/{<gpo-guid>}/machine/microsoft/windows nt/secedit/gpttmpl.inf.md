---
created: 2026-11-21
fullpath: 'C:\Windows\SYSVOL\domain\Policies\{<GPO-GUID>}\Machine\Microsoft\Windows NT\SecEdit\GptTmpl.inf'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - group-policy
  - sysvol
aliases:
  - "GptTmpl.inf"
  - "GPTTMPL.INF"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/reset-user-rights-in-default-domain-group-policy
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/event-1202-status-0x534-logged
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/domain-controller-not-functioning-correctly
---

**fullpath**: C:\Windows\SYSVOL\domain\Policies\{<GPO-GUID>}\Machine\Microsoft\Windows NT\SecEdit\GptTmpl.inf

# description

GptTmpl.inf is the security template of a GPO's computer section, stored in SYSVOL under Machine\Microsoft\Windows NT\SecEdit. It contains the Security Settings of the GPO (user rights assignments such as SeNetworkLogonRight, account policies, restricted groups, etc.) in security template (.inf) format, as used by secedit.

## simple description

> ### 2026-11-21 Claude said
> This text file holds the security settings of a Group Policy Object, such as who can log on locally or over the network, password policy and restricted groups. Domain computers download and apply it with the security client-side extension. The Default Domain Policy and Default Domain Controllers Policy each have one.
>
> **SOC NOTE**: Modifying it grants privileges domain-wide (T1484.001 Group Policy Modification), e.g. adding an account to SeDebugPrivilege/SeBackupPrivilege or restricted groups. Monitor SYSVOL file changes, Gpt.ini version bumps and Security 5136/5145; review user rights entries (SIDs) for unexpected principals.
>

# purpose

Contains the GPO's security policy. User rights lines take the form `SeNetworkLogonRight = *S-1-5-11,*S-1-5-32-544,*S-1-1-0`. Learn documents editing it (after backup) to reset user rights in the Default Domain Policy ({31B2F340-016D-11D2-945F-00C04FB984F9}) or Default Domain Controllers Policy ({6AC1786C-016F-11D2-945F-00C04fB984F9}), then increasing the version in Gpt.ini and running gpupdate /force; invalid principals cause SceCli event 1202.
