---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Windows\Notifications\wpndatabase.db'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - wpndatabase.db
  - Windows Push Notification database
url:
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\Windows\Notifications\wpndatabase.db

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> wpndatabase.db is a per-user SQLite database used by the Windows Push Notification platform (WPN) to store toast notifications, tile/badge data and push channel registrations for apps. It replaced the older `appdb.dat` in Windows 10 1607 and later. The `Notification` table holds the XML payload of toasts shown in Action Center, along with arrival and expiry times. Related files are `wpndatabase.db-wal` and `-shm`.
>
> **SOC NOTE**: This database is a rich forensic artifact: toast notification payloads can reveal email subjects, chat messages (Teams, Outlook), security alerts, file download notices or web push from browsers, with timestamps, even after the originating app data is gone. Attackers abusing malicious web push subscriptions or phishing via notifications also leave records here. Collect with the `-wal` file and parse with SQLite tools.
>

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_


