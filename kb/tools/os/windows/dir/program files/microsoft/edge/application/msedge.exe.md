---
created: 2026-11-21
fullpath: 'c:\Program Files\Microsoft\Edge\Application\msedge.exe'
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

**fullpath**:c:\Program Files\Microsoft\Edge\Application\msedge.exe

# description

msedge.exe is the Microsoft Edge browser executable. Microsoft Learn documents its default Windows locations as `%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe` (Stable), the Beta/Dev equivalents and `%LOCALAPPDATA%\Microsoft\Edge SxS\Application\msedge.exe` (Canary); Learn pages also show the per-channel `initial_preferences` file is deployed next to msedge.exe, and the process can be inspected in Task Manager / Event Viewer (Application Error events for msedge.exe).

## simple description

> ### 2026-11-21 Claude said
> msedge.exe is the Chromium-based Microsoft Edge browser. A normal install runs it from Program Files (x86)\Microsoft\Edge\Application (or Program Files on newer installs), with many child msedge.exe processes for tabs, GPU and utilities. This path (64-bit Program Files) is used by newer system-wide Edge installs; older installs use Program Files (x86).
>
> **SOC NOTE**: Legitimate but frequently abused: attackers launch Edge with `--headless`, `--remote-debugging-port` (cookie/session theft, MITRE ATT&CK T1539/T1185) or `--load-extension` for malicious extensions (T1176). Profile data (cookies, Login Data, History) under `%LOCALAPPDATA%\Microsoft\Edge\User Data` is a key forensic artifact. Check the parent process and command line of msedge.exe started by scripts or Office.
>

# purpose

Runs Microsoft Edge (Stable channel). Learn documents the Stable default as `%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe` and notes paths may vary by configuration, version or policy; this 64-bit Program Files location is not specifically documented. Ending all `msedge.exe` tasks, turning off graphics acceleration, starting with a temporary profile and repairing Edge are the documented troubleshooting steps when it fails to start.

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
