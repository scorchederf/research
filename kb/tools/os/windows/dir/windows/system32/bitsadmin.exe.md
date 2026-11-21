---
created: 2026-11-21
fullpath: 'C:\Windows\System32\bitsadmin.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lolbin
aliases:
  - bitsadmin.exe
  - bitsadmin
  - BITSAdmin tool
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin
  - https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin-examples
  - https://learn.microsoft.com/windows/win32/bits/bitsadmin-tool
  - https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin-transfer
  - https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin-list
  - https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin-monitor
  - https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin-reset
  - https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin-addfile
---

**fullpath**:C:\Windows\System32\bitsadmin.exe

# description

BITSAdmin is a built-in Windows command-line tool that creates download or upload jobs for the Background Intelligent Transfer Service (BITS) and monitors their progress. Many of its switches map to methods in the BITS interfaces. Accessing another user's jobs needs administrator privileges, and jobs created elevated must be managed from an elevated window.

## simple description

> ### 2026-11-21 Claude said
> `bitsadmin.exe` controls BITS, the Windows service that downloads files in the background (it is what Windows Update has traditionally used). With it you can create a "job", add a URL and a local file name, and let Windows download it, even across reboots and network drops. Microsoft considers it deprecated in favour of the PowerShell BITS cmdlets, but it still ships with Windows.
>
> **SOC NOTE**: Classic LOLBin: attackers use `bitsadmin /transfer` to download payloads (T1105) and `/setnotifycmdline` to run a program when a job finishes, which gives persistence that survives reboots (T1197 BITS Jobs). Look for bitsadmin process creation (4688 / Sysmon 1) with URLs, the `Microsoft-Windows-Bits-Client/Operational` log (Event IDs 3, 59, 60), and the BITS job database (`qmgr.db` / `qmgr*.dat` under `%ALLUSERSPROFILE%\Microsoft\Network\Downloader`).
>

# purpose

Create, configure, run and monitor BITS download and upload jobs from the command line; list or cancel jobs for the current user or all users; and manage the BITS cache and peer caching.

# typical use cases

| usage | description |
| --- | --- |
| `bitsadmin /transfer myDownloadJob /download /priority normal https://downloadsrv/10mb.zip c:\\10mb.zip` | Create a job, add the file, activate it and complete it, showing progress until done. |
| `bitsadmin /create myDownloadJob` | Create a download job; returns the job GUID. |
| `bitsadmin /addfile myDownloadJob https://downloadsrv/10mb.zip c:\\10mb.zip` | Add a file to the job. |
| `bitsadmin /resume myDownloadJob` | Activate the (suspended) new job in the transfer queue. |
| `bitsadmin /info myDownloadJob /verbose` | Show the job state and files/bytes transferred. |
| `bitsadmin /list /verbose` | List all of the current user's BITS jobs with details. |
| `bitsadmin /monitor /refresh 60` | Monitor the current user's jobs, refreshing every 60 seconds. |
| `bitsadmin /reset` | Cancel all jobs in the queue owned by the current user. |

# options

Learn lists 110 switches on the bitsadmin page, each with its own reference page. The table below covers the switches whose reference content was retrieved for this note; the full list is on the bitsadmin page linked in `url`.

| option | description |
| --- | --- |
| `/addfile <job> <remoteURL> <localname>` | Adds a file to the job; `localname` must be an absolute path. |
| `/create` | Creates a job and returns its GUID. |
| `/info <job> [/verbose]` | Returns the job state and the number of files and bytes transferred; `/verbose` gives full details. |
| `/list [/allusers] [/verbose]` | Lists transfer jobs owned by the current user; `/allusers` needs administrator privileges. |
| `/monitor [/allusers] [/refresh <seconds>]` | Monitors jobs in the transfer queue; default refresh is five seconds. |
| `/reset [/allusers]` | Cancels all jobs owned by the current user; jobs created by Local System can't be reset this way. |
| `/resume <job>` | Activates a job in the transfer queue (new jobs start suspended). |
| `/transfer <name> [/DOWNLOAD\|/UPLOAD] [/priority FOREGROUND\|HIGH\|NORMAL\|LOW] [/ACLflags o\|g\|d\|s] [/DYNAMIC] <remotefilename> <localfilename>` | Transfers one or more files; creates a NORMAL priority download job by default and completes or cancels it. `/DYNAMIC` uses BITS_JOB_PROPERTY_DYNAMIC_CONTENT. |
| `/?` or `/help` | Lists the switches. |
