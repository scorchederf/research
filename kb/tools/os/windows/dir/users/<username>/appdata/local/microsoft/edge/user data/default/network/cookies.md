---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Edge\User Data\Default\Network\Cookies'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - edge
  - browser
  - forensics
aliases:
  - Cookies
  - Edge Cookies database
url:
  - https://learn.microsoft.com/answers/a/8046508
  - https://learn.microsoft.com/deployedge/edge-learnmore-create-user-directory-vars
  - https://learn.microsoft.com/deployedge/microsoft-edge-policies/userdatadir
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\Edge\User Data\Default\Network\Cookies

# description

Cookies is the database file where Microsoft Edge stores cookies for the Default profile, located under the user's profile path `C:\Users\<Current-user>\AppData\Local\Microsoft\Edge\User Data\Default` (shown as Profile path on edge://version). The user data directory can be relocated with the UserDataDir policy (`SOFTWARE\Policies\Microsoft\Edge`, REG_SZ) or the `--user-data-dir` command-line flag.

## simple description

> ### 2026-11-21 Claude said
> This file is the cookie jar for the default Microsoft Edge profile. It is an SQLite database holding website cookies, including session and authentication cookies, with cookie values encrypted using a key protected by DPAPI (stored in the Local State file). Edge locks the file while running. Other profiles have their own copy under Profile 1, Profile 2, and so on.
>
> **SOC NOTE**: Infostealers and red-team tools copy this database plus Local State to steal session cookies and bypass MFA (MITRE ATT&CK T1539 Steal Web Session Cookie, T1555.003). Alert on non-Edge processes reading the Cookies file, on Edge launched with `--remote-debugging-port` to dump cookies, and on archive/exfil activity touching User Data. For forensics, it shows visited domains and cookie creation/last-access times.
>

# purpose

Persistent storage of HTTP cookies for the Microsoft Edge Default profile.
