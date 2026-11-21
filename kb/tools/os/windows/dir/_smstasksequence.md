---
created: 2026-11-21
fullpath: 'C:\_SMSTaskSequence'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - configmgr
aliases:
  - _SMSTaskSequence
url: []
---

**fullpath**:C:\_SMSTaskSequence

# description

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

## simple description

> ### 2026-11-21 Claude said
> C:\_SMSTaskSequence is a temporary working folder created by Configuration Manager (SCCM/MECM) during an operating system deployment task sequence. It holds the task sequence environment, downloaded packages and logs while the deployment runs, and is normally removed when the task sequence finishes. A leftover folder usually means a failed or interrupted deployment.
>
> **SOC NOTE**: The folder can contain TSEnv.dat and policy files that may expose task sequence variables, including network access or domain join account credentials (MITRE ATT&CK T1552.001 Credentials In Files). Leftover copies are a known target for SCCM credential harvesting; treat unexpected access to it as suspicious and clean up after failed deployments.
> _Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
