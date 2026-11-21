---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Group Policy\History'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - group-policy
aliases:
  - "Group Policy History"
url:
  []
---

**fullpath**:C:\ProgramData\Microsoft\Group Policy\History

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This folder is the local Group Policy cache of computer-side GPOs that the client has downloaded. It contains subfolders named after GPO GUIDs holding copies of policy files such as `Registry.pol`, `GptTmpl.inf` and Group Policy Preferences XML files. Windows uses it to remember which policies were applied previously.
>
> **SOC NOTE**: Useful forensically to see which GPOs and settings reached a host even after the GPO is removed from the domain. Cached Group Policy Preferences XML (Groups.xml, ScheduledTasks.xml, Services.xml) may contain `cpassword` values decryptable with the published AES key (MITRE ATT&CK T1552.006). Attackers who abuse GPOs to deploy tasks or ransomware also leave traces here.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
