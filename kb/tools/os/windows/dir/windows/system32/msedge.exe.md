---
created: 2026-11-21
fullpath: 'C:\Windows\System32\msedge.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - msedge.exe
  - Microsoft Edge
url:
  - https://learn.microsoft.com/microsoft-edge/web-platform/devtools-mcp-server
  - https://learn.microsoft.com/deployedge/microsoft-edge-configure-kiosk-mode
  - https://learn.microsoft.com/troubleshoot/microsoft-edge/performance/edge-crashes-fails-to-launch
  - https://learn.microsoft.com/microsoft-edge/webdriver/
---

**fullpath**:C:\Windows\System32\msedge.exe

# description

msedge.exe is the Microsoft Edge browser executable. Microsoft Learn documents its default Windows locations as `%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe` (Stable), the Beta/Dev equivalents and `%LOCALAPPDATA%\Microsoft\Edge SxS\Application\msedge.exe` (Canary); no Learn page lists a copy in C:\Windows\System32.

## simple description

> ### 2026-11-21 Claude said
> msedge.exe is the Chromium-based Microsoft Edge browser. A normal install runs it from Program Files (x86)\Microsoft\Edge\Application (or Program Files on newer installs), with many child msedge.exe processes for tabs, GPU and utilities. Windows does not ship msedge.exe in System32.
>
> **SOC NOTE**: An msedge.exe in C:\Windows\System32 is not a standard location and is a strong masquerading indicator (MITRE ATT&CK T1036.005 Match Legitimate Name or Location). Verify signature, hash and parent process; check for persistence (Run keys, services, scheduled tasks) pointing to it. Edge itself can also be abused for `--headless` downloads or `--remote-debugging-port` cookie theft (T1539).
>

# purpose

Runs Microsoft Edge. _Not documented on Microsoft Learn at 2026/11/21 08:51 UTC_ for the System32 location.

# typical use cases

| usage | description |
| --- | --- |
| `msedge.exe --kiosk www.contoso.com --edge-kiosk-type=fullscreen` | Kiosk mode for digital/interactive signage. |
| `msedge.exe --kiosk www.contoso.com --edge-kiosk-type=public-browsing` | Kiosk mode for public browsing. |
| `msedge.exe --user-data-dir="%TEMP%\edge-test-profile"` | Start with a temporary profile to isolate a corrupted profile. |

# options

| option    | description    |
| --- | --- |
| `--kiosk` | Starts Edge in kiosk mode with the given URL. |
| `--edge-kiosk-type=` | Kiosk type: `fullscreen` (digital/interactive signage) or `public-browsing`. |
| `--no-first-run` | Disables the first-run experience. |
| `--kiosk-idle-timeout-minutes=` | Minutes of inactivity before kiosk mode resets the session by closing the browser (0 turns off; 1-1440). |
| `--user-data-dir=` | Uses the specified user data (profile) folder. |
| `--headless=new` | Runs the browser in headless mode (passed via WebDriver EdgeOptions). |
