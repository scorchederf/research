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

An event log for security-related events from the Windows SMB server. Learn's example is event 3023, logged when an SMB client is logged on as the Guest account.

# purpose

- Event ID 3023 (Task Category: InsecureGuestLogon, Keywords: Authentication): "The SMB client was logged on as Guest account."
- Related client-side events (31017, 31018, 31022) are in `Microsoft-Windows-SmbClient/Security`.
