---
created: 2026-11-21
fullpath: 'C:\Windows\PSEXESVC.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - sysinternals
  - psexec
  - remote-execution
aliases:
  - PSEXESVC.exe
  - PSEXESVC
  - PsExec
url:
  - https://learn.microsoft.com/sysinternals/downloads/psexec
  - https://learn.microsoft.com/sysinternals/downloads/pstools
---

**fullpath**:C:\Windows\PSEXESVC.exe

# description

PSEXESVC.exe is the remote service component of Sysinternals PsExec, part of the PsTools suite. PsExec runs it on the target system to execute processes remotely without manually installing client software; the remote service name can be changed with PsExec `-r`.

## simple description

> ### 2026-11-21 Claude said
> When someone runs PsExec against a computer, PsExec copies PSEXESVC.exe into C:\Windows on that computer and creates a temporary service to run the requested command. The service is normally removed afterwards. Finding this file means the machine was the target of PsExec. Administrators also use it legitimately for remote administration.
>
> **SOC NOTE**: Strong lateral movement indicator (MITRE ATT&CK T1569.002, T1021.002): look for System Event 7045 service install PSEXESVC, Security 4697, 5145 ADMIN$ share writes, named pipes \PSEXESVC-*, and HKLM\SYSTEM\CurrentControlSet\Services\PSEXESVC. Renamed services (`-r`) and Impacket psexec use other names. Defender ASR rule "Block process creations originating from PSExec and WMI commands" covers it.
>

# purpose

Executes processes on remote systems for PsExec, with full interactivity for console applications. The process runs in the context of the specified account, the caller account (without network access when impersonating), or the System account with `-s`. Password and command are encrypted in transit.

# typical use cases

| usage | description |
| --- | --- |
| `psexec -i \\marklap cmd` | Launch an interactive command prompt on \\marklap. |
| `psexec -i \\marklap ipconfig /all` | Run IpConfig remotely and show the output locally. |
| `psexec -i \\marklap -c test.exe` | Copy test.exe to the remote system and run it interactively. |
| `psexec -i -d -s c:\windows\regedit.exe` | Run Regedit as System to view the SAM and SECURITY keys. |
| `psexec -accepteula -nobanner -s powershell.exe -NoLogo -NoProfile -File C:\path\script-name.ps1` | Run a PowerShell script as Local System. |

# options

| option | description |
| --- | --- |
| `-a` | Comma-separated processors on which the application can run (1 is the lowest CPU). |
| `-c` | Copy the executable to the remote system for execution. |
| `-d` | Do not wait for the process to terminate (non-interactive). |
| `-e` | Do not load the account profile. |
| `-f` | Copy the program even if it already exists on the remote system. |
| `-i` | Interact with the desktop of the specified session (console session if none). |
| `-h` | Run with the account elevated token on Vista or higher. |
| `-l` | Run as limited user (Low Integrity on Vista). |
| `-n` | Timeout in seconds connecting to remote computers. |
| `-p` | Password for the user name; prompted if omitted. |
| `-r` | Name of the remote service to create or interact with. |
| `-s` | Run the remote process in the System account. |
| `-u` | User name for login to the remote computer. |
| `-v` | Copy only if newer or a higher version than the remote copy. |
| `-w` | Working directory of the process on the remote computer. |
| `-x` | Display the UI on the Winlogon secure desktop (local system only). |
| `-priority` | -low, -belownormal, -abovenormal, -high or -realtime; -background for low memory and I/O priority. |
| `computer` | Remote computer(s); `\\*` runs on all computers in the current domain. |
| `@file` | Run the command on each computer listed in the file. |
| `cmd` | Name of the application to execute. |
| `arguments` | Arguments to pass (file paths must be absolute on the target). |
| `-accepteula` | Suppress the license dialog. |
| `-nobanner` | Suppress the startup banner and copyright message. |
