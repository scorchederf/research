---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Outlook'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - outlook
  - office
  - email
aliases:
  - Outlook data folder
  - %localappdata%\Microsoft\Outlook
url:
  - https://learn.microsoft.com/microsoft-365-apps/outlook/configuration/cached-exchange-mode
  - https://learn.microsoft.com/troubleshoot/outlook/data-files/errors-have-been-detected-in-.ost-file
  - https://learn.microsoft.com/troubleshoot/outlook/synchronization/synchronization-issues-occur-in-outlook-owa
  - https://learn.microsoft.com/troubleshoot/outlook/data-files/cannot-change-the-location-of-ost-file
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\Outlook

# description

Default per-user folder where classic Outlook (Microsoft 365 Apps / Outlook 2016 and later) stores its offline Outlook Data File (`.ost`) used by Cached Exchange Mode. Offline Address Book files default to the `Offline Address Books` subfolder. The location can be overridden with the `Default location for OST files` Group Policy or the `ForceOSTPath` registry value.

## simple description

> ### 2026-11-21 Claude said
> This is where classic Outlook keeps a local cached copy of a user's mailbox, in a file ending in `.ost`. It lets Outlook work offline and syncs with Exchange/Microsoft 365 in the background. The folder is hidden by default and lives in each user's profile. Deleting the `.ost` just makes Outlook re-download the mailbox.
>
> **SOC NOTE**: OST/PST files contain full mailbox contents, so they are high-value targets for data theft (MITRE ATT&CK T1114.001 Local Email Collection). Look for unusual processes reading or copying `*.ost`/`*.pst` files, or archiving this folder. Forensically, the OST can be parsed to recover mail, including deleted items, from the endpoint.
>

# purpose

Holds the local mailbox cache for Cached Exchange Mode. When the user is offline, Outlook works from the `.ost` copy and the Offline Address Book; when online, they are periodically updated from Exchange. If an `.ost` already exists, Outlook appends a number to new file names (for example `Outlook0.ost`).

# common files found

| file | description |
| --- | --- |
| `*.ost` (e.g. `user@org.com.ost`, `Outlook.ost`) | Offline Outlook Data File holding the cached mailbox. |
| `Offline Address Books\` | Default location for Offline Address Book files. |
