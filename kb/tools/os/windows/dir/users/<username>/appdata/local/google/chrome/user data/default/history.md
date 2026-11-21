---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\History'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - browser
  - chrome
  - forensics
aliases:
  - History
  - Chrome History database
url:
  - https://learn.microsoft.com/deployedge/microsoft-edge-policies/importhistory
  - https://learn.microsoft.com/deployedge/microsoft-edge-policies/autoimportatfirstrun
---

**fullpath**:C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\History

# description

SQLite database of the default Google Chrome profile that stores browsing history. Learn does not describe the file itself; it documents only that Microsoft Edge can import browsing history from Google Chrome, controlled by the `ImportHistory` and `AutoImportAtFirstRun` policies.

## simple description

> ### 2026-11-21 Claude said
> This file is Google Chrome's browsing history for the user's default profile. It is an SQLite database with tables such as `urls`, `visits` and `downloads`, recording which sites were visited, when, and which files were downloaded. Chrome locks the file while running, so investigators copy it first. Times are stored as microseconds since 1601-01-01 UTC.
>
> **SOC NOTE**: Core web-activity artifact: phishing click-through, malware download source URLs (`downloads` table with `tab_url`/`referrer`), C2 web panels, and data exfiltration sites. Infostealers also exfiltrate it (MITRE T1217 Browser Information Discovery). Parse with tools like Hindsight or DB Browser for SQLite and correlate downloads with Zone.Identifier ADS and MOTW on the saved files.
>

# purpose

Stores Chrome browsing history. From the Learn side, Microsoft Edge can read Chrome browsing history during import: with `ImportHistory` enabled the Browsing history box is preselected; disabled prevents import; and `AutoImportAtFirstRun` = `FromGoogleChrome` (2) silently imports browsing history and other data at first run.
