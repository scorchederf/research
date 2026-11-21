---
created: 2026-11-21
fullpath: 'C:\Windows\System32\cmdkey.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - exe
  - credentials
aliases:
  - "cmdkey.exe"
  - "cmdkey"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey
---

**fullpath**:C:\Windows\System32\cmdkey.exe

# description

cmdkey is a built-in Windows command that creates, lists and deletes stored user names and passwords (credentials) in Credential Manager. It ships with Windows; related tools are the Credential Manager control panel and VaultCmd.exe.

## simple description

> ### 2026-11-21 Claude said
> cmdkey.exe is the command-line front end to Windows Credential Manager. Admins use it to save credentials for a server so connections (like RDP or file shares) don't prompt, list what is saved, or delete entries.
>
> **SOC NOTE**: `cmdkey /list` is common attacker reconnaissance for saved credentials (T1555.004) before lateral movement with `runas /savecred` or RDP; `cmdkey /add` can stage creds for RDP (T1021.001). Alert on cmdkey execution by unusual parents and correlate with 5379 (Credential Manager read) events.
>

# purpose

Creates, lists and deletes stored user names and passwords or credentials.

# typical use cases

| usage | description |
| --- | --- |
| `cmdkey /list` | Display all stored user names and credentials. |
| `cmdkey /add:server01 /user:mikedan /pass:Kleo` | Store a user name and password for accessing Server01. |
| `cmdkey /add:server01 /user:mikedan` | Store a user name and prompt for the password when Server01 is accessed. |
| `cmdkey /delete /ras` | Delete the credential stored by remote access. |
| `cmdkey /delete:server01` | Delete the credential stored for Server01. |

# options

| option | description |
| --- | --- |
| `/add:<targetname>` | Adds a user name and password to the list for the computer or domain name targetname. |
| `/generic:<targetname>` | Adds generic credentials to the list for targetname. |
| `/smartcard` | Retrieves the credential from a smart card; prompts to choose if more than one is found. |
| `/user:<username>` | User or account name to store; requested if not supplied. |
| `/pass:<password>` | Password to store; requested if not supplied; not displayed after storage. |
| `/delete:{<targetname> \| /ras}` | Deletes the entry for targetname, or the stored remote access entry with /ras. |
| `/list:<targetname>` | Displays stored user names and credentials; all if no targetname. |
| `/?` | Displays help at the command prompt. |
