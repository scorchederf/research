---
created: 2026-11-21
fullpath: 'C:\Windows\SoftwareDistribution'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - windows-update
aliases:
  - SoftwareDistribution
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/installing-updates-features-roles/additional-resources-for-windows-update
  - https://learn.microsoft.com/troubleshoot/windows-client/installing-updates-features-roles/troubleshoot-windows-update-error-0x80240439
  - https://learn.microsoft.com/troubleshoot/windows-client/installing-updates-features-roles/troubleshoot-windows-update-error-0x80070005
---

**fullpath**:C:\Windows\SoftwareDistribution

# description

`%windir%\SoftwareDistribution` is the Windows Update agent's working folder, holding its state files, data store and downloaded updates. Resetting Windows Update components involves stopping the BITS, Windows Update (wuauserv) and Cryptographic services and renaming this folder (or its `DataStore` and `Download` subfolders) along with `%windir%\System32\catroot2`.

## simple description

> ### 2026-11-21 Claude said
> SoftwareDistribution is where Windows Update keeps its database of update history and the update files it downloads before installing them. It is safe to clear when the update services are stopped; Windows rebuilds it. The `DataStore\DataStore.edb` file holds update history, and `Download` holds cached payloads.
>
> **SOC NOTE**: DataStore.edb is a forensic source for update and patch history (useful to confirm patch level at time of compromise). Attackers sometimes stage files in `Download` to blend in with update payloads, and wiping or renaming the folder can hide update tampering. Abuse of BITS and wuauserv-related binaries (MITRE ATT&CK T1197) may leave traces nearby.

# purpose

Stores Windows Update agent state. Corrupted state files in this folder can cause errors such as 0x80240439 (WU_E_NOT_INITIALIZED). Its default permissions can be reset with icacls when troubleshooting error 0x80070005.

# common files found

| item | description |
| --- | --- |
| `DataStore` | Windows Update agent data store; renamed to DataStore.bak when resetting Windows Update components. |
| `Download` | Downloaded update files; renamed to Download.bak when resetting Windows Update components. |
