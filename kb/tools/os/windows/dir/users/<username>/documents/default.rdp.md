---
created: 2026-11-21
fullpath: 'C:\Users\<username>\Documents\Default.rdp'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - rdp
  - remote-desktop
aliases:
  - 'Default.rdp'
  - 'Remote Desktop connection file'
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/mstsc
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/remote-desktop-protocol-settings
---

**fullpath**: C:\Users\<username>\Documents\Default.rdp

# description

Hidden per-user Remote Desktop Connection settings file. Each user has a hidden Default.rdp in the Documents folder; it is created on the client when RDP is used to connect to a remote computer and stores the connection settings configured in Remote Desktop Connection (mstsc.exe) Options.

## simple description

> ### 2026-11-21 Claude said
> Default.rdp is a small hidden text file that Remote Desktop Connection (mstsc) writes in the user's Documents folder. It remembers the last connection settings: the computer name, screen size, colour depth, and which local resources were shared. Every time the user connects, the file is updated. It does not normally contain the password.
>
> **SOC NOTE**: Forensic artifact for lateral movement (T1021.001): the `full address:s:` and `username:s:` lines show the last RDP target and account used from this host, and the file's modified time approximates the last outbound RDP session. Compare with HKCU\Software\Microsoft\Terminal Server Client\Default (MRU) and Servers keys, and RDP bitmap cache. Malicious .rdp files are also used in phishing (redirecting drives/clipboard).
>

# purpose

Stores the user's default Remote Desktop Connection settings (display, address, compression and other options) that mstsc.exe loads and saves.

# settings

| setting | description |
| --- | --- |
| `desktopwidth:i` | Desktop width selected on the Display tab. |
| `desktopheight:i` | Desktop height selected on the Display tab. |
| `session bpp:i` | Color depth selected on the Display tab. |
| `winposstr:s` | Window position (string form of the WINDOWPOS structure). |
| `auto connect:i` | Not used by desktop computers or Windows CE clients. |
| `full address:s` | The computer you connect to (Computer box on the General tab). |
| `compression:i` | Whether data is compressed when transmitted to the client. |
