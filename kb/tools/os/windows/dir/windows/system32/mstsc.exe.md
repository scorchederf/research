---
created: 2026-11-21
fullpath: 'C:\Windows\System32\mstsc.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - remote-desktop
aliases:
  - mstsc.exe
  - mstsc
  - Remote Desktop Connection
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/mstsc
---

**fullpath**:C:\Windows\System32\mstsc.exe

# description

`mstsc` creates connections to Remote Desktop Session Host servers or other remote computers and edits existing Remote Desktop Connection (.rdp) configuration files. It is the built-in Windows Remote Desktop Connection client. Each user has a hidden Default.rdp file in the Documents folder.

## simple description

> ### 2026-11-21 Claude said
> mstsc.exe is the Windows Remote Desktop Connection client that opens an RDP session to another computer. Users and admins use it to log on to servers or desktops remotely, optionally through an RD Gateway. It can also open or edit saved .rdp files and shadow other users' sessions.
>
> **SOC NOTE**: mstsc usage is key evidence of lateral movement (T1021.001 Remote Desktop Protocol). Artifacts on the source host include `HKCU\Software\Microsoft\Terminal Server Client\Default` and `\Servers` (MRU of targets), Default.rdp, the RDP bitmap cache, Jump Lists and Prefetch; the destination logs 4624 logon type 10 and TerminalServices events 1149/21/25. Attackers also abuse `/shadow /noConsentPrompt` to spy on sessions, and malicious .rdp attachments (rogue RDP) can redirect drives to attacker servers.
>

# purpose

Connects to remote computers via Remote Desktop, sets window size and monitor layout, uses an RD Gateway, connects to an administration session, and supports credential-protecting modes (Restricted Admin and Remote Credential Guard) and session shadowing.

# typical use cases

| usage | description |
| --- | --- |
| `mstsc /f` | Connect to a session in full-screen mode. |
| `mstsc /v:computer1 /fullscreen` | Connect to computer1 full-screen using the equivalent `/fullscreen` parameter. |
| `mstsc /v:computer1 /span` | Span a session across horizontally aligned monitors of the same resolution. |
| `mstsc /v:computer1 /w:1920 /h:1080` | Connect with a specified window width and height. |
| `mstsc /edit filename.rdp` | Open filename.rdp for editing. |

# options

| option | description |
| --- | --- |
| `<connectionfile>` | Name of an .rdp file for the connection. |
| `/v:<server>[:<port>]` | Remote computer and optional port to connect to. |
| `/g:<gateway>` | RD Gateway server to use; only read when the endpoint is given with `/v`. |
| `/admin` | Connects to a session for administering the server. |
| `/f[ullscreen]` | Starts in full-screen mode; `/f` and `/fullscreen` are equivalent. |
| `/w:<width>` | Width of the Remote Desktop window. |
| `/h:<height>` | Height of the Remote Desktop window. |
| `/public` | Public mode; passwords and bitmaps are not cached. |
| `/span` | Matches the local virtual desktop size and spans the session across horizontally aligned monitors of equal resolution. |
| `/multimon` | Makes the session monitor layout identical to the client-side configuration. |
| `/l` | Enumerates local monitors and their IDs (for the `selectedmonitors` RDP setting). |
| `/edit <connectionfile>` | Opens the specified .rdp file for editing. |
| `/restrictedAdmin` | Does not send credentials to the remote PC; implies `/admin`. |
| `/remoteGuard` | Does not send credentials to the remote PC and redirects authentication requests back to your device. |
| `/prompt` | Prompts for credentials when connecting. |
| `/shadow:<sessionID>` | ID of the session to shadow. |
| `/control` | Allows control of the session when shadowing. |
| `/noConsentPrompt` | Allows shadowing without user consent. |
| `/?` | Shows the Remote Desktop Connection Usage dialog box. |
