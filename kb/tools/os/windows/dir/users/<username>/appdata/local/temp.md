---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Temp'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - temp
  - user-profile
aliases:
  - Temp
  - %TEMP%
  - %TMP%
url:
  - https://learn.microsoft.com/windows/deployment/usmt/usmt-recognized-environment-variables
  - https://learn.microsoft.com/windows/win32/api/fileapi/nf-fileapi-gettemppatha
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/new-temporaryfile
---

**fullpath**:C:\Users\<username>\AppData\Local\Temp

# description

`%USERPROFILE%\AppData\Local\Temp` is the typical path of the per-user temporary folder referenced by the `TEMP` and `TMP` environment variables. Windows APIs such as `GetTempPath`/`GetTempPath2`, .NET `Path.GetTempPath()` and PowerShell `New-TemporaryFile` resolve to it when those variables point there.

## simple description

> ### 2026-11-21 Claude said
> This is the user's personal scratch folder where Windows and applications drop temporary files such as installers, extracted archives and caches. Every user has their own copy under their profile. Programs find it through the TEMP and TMP environment variables. Contents are usually safe to delete when no program is using them.
>
> **SOC NOTE**: One of the most common malware staging locations (MITRE T1105 Ingress Tool Transfer, T1204 User Execution) because any user can write and execute there; email attachments opened from Outlook or archive tools are often extracted here. Look for executables, scripts, DLLs and LNK files launched from `%TEMP%`, and correlate with Sysmon Event ID 1/11 and Defender alerts. Timestamps of dropped files help build an execution timeline.
>

# purpose

Designated directory for temporary files for the current user. `GetTempPath` checks `TMP`, then `TEMP`, then `USERPROFILE`, then the Windows directory and returns the first path found; it does not verify the path exists or is accessible. `New-TemporaryFile` creates empty `tmp<NNNN>.tmp` files in this folder.

# common files found

| file | description |
| --- | --- |
| `tmp<NNNN>.tmp` | Empty temporary file created by `New-TemporaryFile`, where `<NNNN>` is a random hexadecimal number. |
