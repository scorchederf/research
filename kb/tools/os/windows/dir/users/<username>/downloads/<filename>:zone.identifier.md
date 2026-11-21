---
created: 2026-11-21
fullpath: 'C:\Users\<username>\Downloads\<filename>:Zone.Identifier'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - ntfs-ads
  - mark-of-the-web
aliases:
  - "Zone.Identifier"
  - "Mark of the Web"
  - "MOTW"
url:
  - https://learn.microsoft.com/openspecs/windows_protocols/ms-fscc/6e3f7352-d11c-4d76-8c39-2516a9df36e8
  - https://learn.microsoft.com/microsoft-365-apps/security/internet-macros-blocked
---

**fullpath**: C:\Users\<username>\Downloads\<filename>:Zone.Identifier

# description

NTFS alternate data stream named `Zone.Identifier` attached to a downloaded file, which stores the URL security zone the file came from - known as Mark of the Web (MotW). Its fully qualified form is `<filename>:Zone.Identifier:$DATA`, and it is a simple text stream with a `[ZoneTransfer]` section containing `ZoneId`. Office uses it to decide whether to block macros, and PowerShell's `Unblock-File` (or the **Unblock** checkbox in file Properties) removes it.

## simple description

> ### 2026-11-21 Claude said
> When you download a file with a browser, email client or many other apps, Windows attaches a hidden "sidecar" stream to the file called Zone.Identifier. It records that the file came from the Internet (ZoneId=3) and, on modern Windows, often the referrer and download URL (ReferrerUrl, HostUrl). SmartScreen, Office Protected View and macro blocking read it to warn the user. It does not change the file's size or content and is lost if the file is copied to a non-NTFS volume.
>
> **SOC NOTE**: Excellent forensic artifact: HostUrl/ReferrerUrl reveal where a malicious file was downloaded from. Attackers evade MotW (T1553.005 Subvert Trust Controls: Mark-of-the-Web Bypass) by delivering payloads in ISO/VHD/7z containers, or strip it with Unblock-File / `Remove-Item -Stream Zone.Identifier`. Sysmon event 15 (FileCreateStreamHash) logs the stream creation and its contents.
>

# purpose

Records the security zone of a file's source. By default MotW is added only to files from the **Internet** or **Restricted sites** zones. ZoneId values map to zones as follows: 0 = My Computer, 1 = Local intranet, 2 = Trusted sites, 3 = Internet, 4 = Restricted sites. For example, VBA macros in a file with ZoneId 3 are blocked by default in Office, while ZoneId 2 is not blocked. The ZoneId can be viewed with `notepad <filename>:Zone.Identifier`.
