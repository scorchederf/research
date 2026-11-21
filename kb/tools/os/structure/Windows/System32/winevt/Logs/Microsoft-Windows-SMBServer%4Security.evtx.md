---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-SMBServer%4Security.evtx'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Microsoft-Windows-SMBServer%4Security.evtx
  - Microsoft-Windows-SmbServer/Security
url:
  - https://learn.microsoft.com/windows-server/storage/file-server/enable-insecure-guest-logons-smb2-and-smb3
---

**fullpath**:C:\Windows\System32\winevt\Logs\Microsoft-Windows-SMBServer%4Security.evtx

# description

The file behind the `Microsoft-Windows-SmbServer/Security` event log, written by the Microsoft-Windows-SMBServer provider. Learn documents it only in the context of insecure guest logons; there is no dedicated page for the log.

## simple description

> ### 2026-11-21 Claude said
> This file is the event log where the Windows SMB server records security-related events. SMB is the protocol used for Windows file shares and many remote admin tasks. The log captures things like guest (unauthenticated) logons, failed authentication or access problems, and clients connecting without required security features such as SMB encryption or signing. In Event Viewer it's under Applications and Services Logs > Microsoft > Windows > SMBServer > Security.
>
> **SOC NOTE**: SMB is central to lateral movement (MITRE ATT&CK T1021.002), so this log can show suspicious share access, guest logons (event 3023) and clients that don't support signing or encryption, which may indicate old or non-Windows tooling. Correlate it with Security log logon events (4624/4625) and share access events (5140/5145) for the full picture of who touched which shares.
>

# purpose

- Event ID 3023 (Task Category: InsecureGuestLogon, Keywords: Authentication): "The SMB client was logged on as Guest account."
- Related client-side events (31017, 31018, 31022) are in `Microsoft-Windows-SmbClient/Security`.
