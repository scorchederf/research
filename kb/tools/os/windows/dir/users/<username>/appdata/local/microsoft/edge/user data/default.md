---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\Edge\User Data\Default'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - browser
  - edge
  - forensics
aliases:
  - Default
  - Edge profile path
  - User Data\Default
url:
  - https://learn.microsoft.com/deployedge/edge-learnmore-create-user-directory-vars
  - https://learn.microsoft.com/deployedge/microsoft-edge-policies/userdatadir
  - https://learn.microsoft.com/troubleshoot/microsoft-edge/security/edge-profile-wont-load-locked
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\Edge\User Data\Default

# description

The default Microsoft Edge profile folder for a Windows user. Edge shows this path as **Profile path** on `edge://version`; its parent `User Data` folder can be relocated with the `UserDataDir` policy or the `--user-data-dir` command-line flag.

## simple description

> ### 2026-11-21 Claude said
> This is where Microsoft Edge stores everything for the user's first (default) browser profile: history, bookmarks, cookies, saved passwords, extensions and cache. Additional profiles get folders like `Profile 1`, `Profile 2` next to it. Edge is Chromium-based, so the file layout is the same as Google Chrome's.
>
> **SOC NOTE**: Rich browser-forensics source: `History` (URLs, downloads), `Cookies` (under Network), `Login Data` (DPAPI/app-bound encrypted passwords), `Web Data`, `Bookmarks`, `Extensions`. Infostealers target these files (MITRE T1555.003 Credentials from Web Browsers, T1539 Steal Web Session Cookie); access by non-browser processes is a strong signal. Remote debugging (`--remote-debugging-port`) on the default profile is now blocked, a known cookie-theft technique.
>

# purpose

Holds the profile data for the default Edge profile. Learn notes that you can troubleshoot a broken profile by closing Edge, renaming the `Default` folder (for example to `Default.bak`), letting Edge create a fresh profile and copying individual files such as `Bookmarks` back. The `User Data` folder must be writable by the user.

# common files found

| file | description |
| --- | --- |
| `Bookmarks` | Favorites (bookmarks) of the profile. |
