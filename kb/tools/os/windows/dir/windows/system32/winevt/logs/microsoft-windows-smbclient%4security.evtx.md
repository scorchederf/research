---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-SmbClient%4Security.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - smb
aliases:
  - Microsoft-Windows-SmbClient%4Security.evtx
  - Microsoft-Windows-SmbClient/Security
url:
  - https://learn.microsoft.com/windows-server/storage/file-server/enable-insecure-guest-logons-smb2-and-smb3
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-SmbClient%4Security.evtx

# description

The event log file behind the Microsoft-Windows-SmbClient/Security channel (source Microsoft-Windows-SMBClient), viewed in Event Viewer under Applications and Services Logs\Microsoft\Windows\SMBClient\Security. Learn documents it for auditing insecure guest logons in SMB2 and SMB3.

## simple description

> ### 2026-11-21 Claude said
> This .evtx file holds security-related events from the Windows SMB client, the component that connects to file shares. It records authentication problems, signing/encryption issues and guest logon behaviour when this machine talks to SMB servers. The "%4" in the name stands for "/" in the channel name.
>
> **SOC NOTE**: Useful for lateral movement and NTLM relay/rogue-server investigations (T1021.002): events show which servers the host tried to reach and failed authentication against. 31017/31022 reveal insecure guest logons; 31018 flags AllowInsecureGuestAuth being enabled, a weakening of SMB security.
>

# purpose

Records SMB client security events, including:

| event ID | description |
| --- | --- |
| 31017 | RejectedInsecureGuestAuth: rejected an insecure guest logon. |
| 31018 | InsecureGuestAuthEnabled: an administrator has enabled AllowInsecureGuestAuth. |
| 31022 | AllowedInsecureGuestAuth: allowed an insecure guest logon. |
