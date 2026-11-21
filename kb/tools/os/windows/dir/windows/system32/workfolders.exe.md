---
created: 2026-11-21
fullpath: 'C:\Windows\System32\WorkFolders.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - workfolders
  - sync
aliases:
  - WorkFolders.exe
  - Work Folders
url:
  - https://learn.microsoft.com/windows-server/storage/work-folders/work-folders-overview
  - https://learn.microsoft.com/windows-server/storage/work-folders/deploy-work-folders-adfs-step5
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-workfoldersclient
---

**fullpath**:C:\Windows\System32\WorkFolders.exe

# description

Client component of Work Folders, a feature introduced with Windows Server 2012 R2 that lets information workers sync work files between their devices and a file server sync share. The client is configured through the Work Folders Control Panel item or Group Policy (WorkFolders-Client.admx).

## simple description

> ### 2026-11-21 Claude said
> WorkFolders.exe is the Windows client for Work Folders, a corporate file sync feature similar to a self-hosted OneDrive. Users set it up from Control Panel by entering their work email or the Work Folders URL, and files then sync between the PC and the company file server. By default files live in %USERPROFILE%\Work Folders. It is rarely used on home machines.
>
> **SOC NOTE**: Known LOLBin: WorkFolders.exe launches control.exe from the current working directory, so a planted control.exe in a user-writable folder can be executed via a signed binary (T1218 System Binary Proxy Execution). Investigate WorkFolders.exe started from unusual directories or spawning unexpected children. Sync shares can also be a data-exfiltration path.
>

# purpose

Syncs work files between the user's devices and the Work Folders server. Setup asks for an email address or Work Folders URL, authenticates (Windows Integrated Authentication on the corporate network, AD FS OAuth otherwise), shows security policies, then syncs. Policies can force automatic setup (`AutoProvision` under `Software\Policies\Microsoft\Windows\WorkFolders`), set the URL and local path, and on-demand file access.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 18:47 UTC_
