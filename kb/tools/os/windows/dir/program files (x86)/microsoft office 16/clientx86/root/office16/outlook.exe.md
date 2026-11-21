---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Outlook.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - outlook
  - office
aliases:
  - Outlook.exe
  - classic Outlook for Windows
url:
  - https://learn.microsoft.com/answers/a/12199181
  - https://learn.microsoft.com/answers/a/12287738
  - https://learn.microsoft.com/microsoft-365-apps/outlook/administration/architecture-changes-new-outlook
---

**fullpath**:C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Outlook.exe

# description

Executable of classic Outlook for Windows from Microsoft Office / Microsoft 365 Apps (Click-to-Run, under `root\Office16`). New Outlook for Windows is a different app (`olk.exe`). Learn Q&A answers show it being started with switches such as `/safe` and `/resetnavpane` for troubleshooting.

## simple description

> ### 2026-11-21 Claude said
> Outlook.exe is the classic desktop email, calendar and contacts client from Microsoft Office. It connects to Exchange/Microsoft 365, IMAP or POP mailboxes and caches mail in OST/PST files. This particular path is a 32-bit Click-to-Run install layout. Command-line switches let users start it in safe mode or reset parts of the UI.
>
> **SOC NOTE**: Outlook is a frequent initial access vector: child processes of Outlook.exe (cmd, powershell, wscript, mshta) indicate a malicious attachment or link (MITRE ATT&CK T1566.001/.002). Outlook home-page, rules and forms abuse provide persistence (T1137). Also watch for Outlook launched by unusual parents or via COM for email collection/exfiltration.
>

# purpose

Runs the classic Outlook client. Safe mode starts without add-ins for troubleshooting.

# typical use cases

| usage | description |
| --- | --- |
| `outlook.exe /safe` | Start classic Outlook in Safe mode. |
| `outlook.exe /resetnavpane` | Reset the navigation pane when Outlook cannot start correctly. |

# options

| option | description |
| --- | --- |
| `/safe` | Starts Outlook in Safe mode. |
| `/resetnavpane` | Resets the navigation pane. |
