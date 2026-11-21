---
created: 2026-11-21
fullpath: 'C:\Windows\ccmcache'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - configmgr
  - sccm
aliases:
  - ccmcache
  - Configuration Manager client cache
url:
  - https://learn.microsoft.com/intune/configmgr/core/clients/manage/configure-client-cache
  - https://learn.microsoft.com/intune/configmgr/core/clients/deploy/about-client-installation-properties
  - https://learn.microsoft.com/troubleshoot/mem/configmgr/content-management/configure-peer-cache
---

**fullpath**:C:\Windows\ccmcache

# description

`%windir%\ccmcache` is the default content cache folder of the Microsoft Configuration Manager (SCCM/MECM) client. It stores temporary files used when clients install applications, programs and software updates; default size is 5120 MB.

## simple description

> ### 2026-11-21 Claude said
> When an SCCM/ConfigMgr-managed PC installs software or updates pushed by IT, it first downloads the installer files into this folder, in numbered subfolders. The client manages the folder itself and cleans old content. It only exists on machines with the Configuration Manager client installed.
>
> **SOC NOTE**: Shows what software was deployed to a host and when (folder timestamps), useful for timeline building. Because content runs as SYSTEM, attackers who compromise ConfigMgr can push malicious packages (MITRE T1072 Software Deployment Tools); suspicious scripts/binaries in ccmcache subfolders warrant checking the deployment in DataTransferService.log, ContentTransferManager.log and CAS.log.
>

# purpose

Holds downloaded deployment content. Location and size can be set at install with CCMSetup properties `SMSCACHEDIR`, `SMSCACHEFLAGS` and `DISABLECACHEOPT`, during client push, in Client Settings, or on the **Cache** tab of the Configuration Manager control panel. Don't encrypt the folder and don't manually delete files with Explorer or the command line; use **Delete Files** in the control panel. Peer cache downloads also land here (for example `C:\windows\ccmcache\1`).

# common files found

| file | description |
| --- | --- |
| `<n>\` (numbered subfolders) | Content of a single deployment downloaded by the client, for example `C:\windows\ccmcache\1`. |
