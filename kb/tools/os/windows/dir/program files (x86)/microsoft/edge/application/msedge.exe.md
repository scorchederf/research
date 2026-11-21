---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - browser
aliases:
  - msedge.exe
  - Microsoft Edge
url:
  - https://learn.microsoft.com/deployedge/microsoft-edge-configure-kiosk-mode
  - https://learn.microsoft.com/deployedge/edge-learnmore-cmdline-options-proxy-settings
  - https://learn.microsoft.com/microsoft-edge/web-platform/devtools-mcp-server
  - https://learn.microsoft.com/microsoft-edge/webdriver/
  - https://learn.microsoft.com/deployedge/microsoft-edge-policies/commandlineflagsecuritywarningsenabled
---

**fullpath**:C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe

# description

`msedge.exe` is the Microsoft Edge (Chromium-based) browser executable; this path is the default install location of the Stable channel on Windows. Beta and Dev channels install under `Microsoft\Edge Beta` and `Microsoft\Edge Dev`, and Canary under `%LOCALAPPDATA%\Microsoft\Edge SxS\Application`. It can be automated with Microsoft Edge WebDriver and configured through Group Policy (`MSEdge.admx`).

## simple description

> ### 2026-11-21 Claude said
> msedge.exe is the main program of the Microsoft Edge web browser. When Edge runs you see many msedge.exe processes because each tab, extension, GPU and network task runs in its own child process. It accepts Chromium command-line switches that change how the browser behaves (kiosk mode, headless, proxy, profile folder). It also hosts WebView2 content for other applications.
>
> **SOC NOTE**: Watch for msedge.exe launched with `--headless`, `--remote-debugging-port`, `--user-data-dir`, `--load-extension` or `--disable-*` sandbox flags: these are used for cookie/session theft via DevTools, malicious extension loading and hidden browsing (T1185, T1539, T1176). Office or script hosts spawning msedge.exe can indicate phishing payload delivery. Browser artifacts (History, Cookies, Login Data SQLite databases) live under `%LOCALAPPDATA%\Microsoft\Edge\User Data`.
>

# purpose

Runs the Microsoft Edge browser. Learn documents command-line options for kiosk mode, proxy overrides and enabling features, and passing extra arguments through WebDriver `EdgeOptions` (for example `--headless=new`). The `CommandLineFlagSecurityWarningsEnabled` policy controls whether Edge warns when launched with potentially dangerous flags such as `--disable-gpu-sandbox`.

# typical use cases

| usage | description |
| --- | --- |
| `msedge.exe --kiosk www.contoso.com --edge-kiosk-type=fullscreen` | Start kiosk mode for digital/interactive signage. |
| `msedge.exe --kiosk www.contoso.com --edge-kiosk-type=public-browsing` | Start kiosk mode for public browsing. |
| `msedge.exe --kiosk www.contoso.com --edge-kiosk-type=fullscreen --no-first-run` | Kiosk mode without the first-run experience. |
| `msedge.exe --kiosk www.contoso.com --edge-kiosk-type=public-browsing --kiosk-idle-timeout-minutes=1` | Reset the kiosk session after 1 minute idle. |
| `msedge.exe --enable-features=msEdgeAIExplainConsoleError` | Enable an experimental feature flag. |

# options

| option | description |
| --- | --- |
| `--kiosk` | Starts Microsoft Edge in kiosk mode with the given URL. |
| `--edge-kiosk-type=` | Kiosk type: `fullscreen` (digital/interactive signage) or `public-browsing`. |
| `--no-first-run` | Disables the first Microsoft Edge run experience. |
| `--kiosk-idle-timeout-minutes=` | Minutes of inactivity before the kiosk session resets by closing the browser; 0 turns it off, 1-1440 allowed. Defaults: fullscreen 0, public browsing 5. |
| `--enable-features=` | Enables the named feature flags. |
| `--headless=new` | Runs the browser without a visible window (shown via WebDriver `EdgeOptions`). |
| `--disable-gpu-sandbox` | Cited as a potentially dangerous flag that triggers a security warning. |
| proxy options | Command-line options that override system proxy settings, corresponding to the ProxyBypassList, ProxyMode, ProxyPacUrl, ProxyServer and ProxySettings policies. |
