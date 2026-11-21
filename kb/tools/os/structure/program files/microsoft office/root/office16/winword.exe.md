---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Office\root\Office16\winword.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - office
  - executable
  - word
aliases:
  - winword.exe
  - Microsoft Word
url:
  - https://learn.microsoft.com/office/vba/word/concepts/miscellaneous/modifying-a-word-command
  - https://learn.microsoft.com/office/dev/add-ins/word/word-add-ins-troubleshooting
---

**fullpath**:C:\Program Files\Microsoft Office\root\Office16\winword.exe

# description

winword.exe is the Microsoft Word application executable in a Click-to-Run Microsoft 365 / Office 2016+ installation (the `root\Office16` folder). Word bases new blank documents on the Normal.dotm global template and can be extended with VBA macros and Office add-ins.

## simple description

> ### 2026-11-21 Claude said
> winword.exe is Microsoft Word, the word-processing program in Microsoft Office / Microsoft 365. The `root\Office16` path is used by Click-to-Run installs of Office 2016, 2019, 2021 and Microsoft 365. It opens .docx, .doc, .rtf, .dotm and other document types and can run VBA macros. Command-line switches such as `/safe`, `/n`, `/m`, `/t` and `/a` control how it starts.
>
> **SOC NOTE**: Word is a top initial-access vector (MITRE ATT&CK T1566.001 Spearphishing Attachment, T1204.002 Malicious File). Alert on winword.exe spawning cmd.exe, powershell.exe, wscript/cscript, mshta, rundll32 or regsvr32, and on outbound network connections or template injection (T1221 remote .dotm). Macro persistence via Normal.dotm (T1137.001) and Office Trusted Locations/registry are worth checking. Useful artifacts: Office MRU/TrustRecords registry keys, `%APPDATA%\Microsoft\Office\Recent`, and the OAlerts event log.
>

# purpose

Runs Microsoft Word. Built-in Word commands (e.g. FileSave) can be replaced by macros of the same name, and new documents are created from the Normal template (Normal.dotm), which Word recreates automatically if renamed or moved.

# typical use cases

- Create and edit documents based on Normal.dotm.
- Override built-in commands with VBA macros stored in a template or Normal.dotm.
- Troubleshoot add-ins/compatibility mode by resetting Normal.dotm.

# options

| option    | description    |
| --- | --- |
| _Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_ |  |
