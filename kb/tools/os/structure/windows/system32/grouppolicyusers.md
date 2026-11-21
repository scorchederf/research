---
created: 2026-11-21
fullpath: 'C:\Windows\System32\GroupPolicyUsers'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - group-policy
aliases:
  - GroupPolicyUsers
url: []
---

**fullpath**:C:\Windows\System32\GroupPolicyUsers

# description

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> GroupPolicyUsers is a hidden folder that holds Multiple Local Group Policy Objects (MLGPO) for specific local users or groups. Each subfolder is named with a user or group SID and contains a `User\Registry.pol` and possibly scripts, like `System32\GroupPolicy`. It lets an admin apply different local policies to, for example, Administrators versus non-Administrators on a standalone machine. It is managed through the Local Group Policy Editor snap-in.
>
> **SOC NOTE**: Attackers with admin rights can plant per-user local policy here (logon scripts under `<SID>\User\Scripts`, Registry.pol settings) for persistence or defense evasion (T1484.001, T1037). Unexpected SID folders or recently modified Registry.pol / scripts.ini files are worth reviewing; parse Registry.pol to see what was applied.
>
> _Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_
