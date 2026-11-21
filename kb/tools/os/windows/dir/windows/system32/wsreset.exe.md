---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wsreset.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - store
aliases:
  - wsreset.exe
  - Windows Store Reset
url:
  - https://learn.microsoft.com/answers/a/12370339
  - https://learn.microsoft.com/answers/a/12676780
---

**fullpath**:C:\Windows\System32\wsreset.exe

# description

`wsreset.exe` resets the Microsoft Store cache. Microsoft Q&A answers on Learn recommend it as the first step when the Store will not open or downloads hang; a command window appears, closes after 10-30 seconds and the Store launches.

## simple description

> ### 2026-11-21 Claude said
> wsreset.exe clears the Microsoft Store cache without changing account settings or removing apps. Users run it from the Run box when the Store misbehaves. With `-i` it re-provisions the Store app if it is missing. It shows a blank console window and then opens the Store.
>
> **SOC NOTE**: wsreset.exe is auto-elevating, and has been abused for UAC bypass by hijacking `HKCU\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command` (T1548.002). Watch for registry writes to that key followed by wsreset.exe spawning cmd.exe or powershell.exe at high integrity.
>

# purpose

Clears the Microsoft Store cache to fix Store problems such as failure to open or apps stuck on Pending.

# typical use cases

| usage | description |
| --- | --- |
| `wsreset.exe` | Reset the Microsoft Store cache; the Store opens when done. |
| `wsreset.exe -i` | Reset the Store cache (suggested when the Store is missing). |

# options

| option | description |
| --- | --- |
| `-i` | Used in Microsoft Q&A guidance when the Store app is missing. |
