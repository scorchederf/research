---
created: 2026-11-21
fullpath: 'C:\Windows\System32\systeminfo.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-commands
aliases:
  - systeminfo.exe
  - systeminfo
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo
  - https://learn.microsoft.com/windows/client-management/client-tools/windows-version-search
---

**fullpath**:C:\Windows\System32\systeminfo.exe

# description

systeminfo is a built-in Windows command that displays detailed configuration information about a computer and its operating system, including OS configuration, security information, product ID, and hardware properties (RAM, disk space, network cards). It ships with Windows and can query the local or a remote computer. Related tools include msinfo32 (System Information GUI).

## simple description

> ### 2026-11-21 Claude said
> systeminfo.exe is a built-in Windows command-line tool that prints a summary of the computer: OS name and version, build, install date, last boot time, domain, hotfixes (KBs), memory and network adapters. Administrators use it for quick inventory and troubleshooting. It can also query remote machines with credentials. Output can be formatted as a table, list or CSV.
>
> **SOC NOTE**: A classic discovery command (MITRE ATT&CK T1082 System Information Discovery) run by attackers and malware right after initial access to learn OS version, patch level (hotfix list for exploit selection) and domain membership. Hunt for systeminfo spawned by unusual parents (Office apps, script hosts, web server processes) or in bursts with whoami/ipconfig/net. Remote use with `/s /u /p` may expose plaintext credentials in process command-line logs (Event ID 4688 / Sysmon 1).
>

# purpose

Displays detailed configuration information about a computer and its operating system, including operating system configuration, security information, product ID, and hardware properties (such as RAM, disk space, and network cards).

# typical use cases

- View the configuration of the local or a remote computer (`systeminfo /s srvmain`).
- Remotely query a domain computer with alternate credentials and list output (`systeminfo /s srvmain2 /u maindom\hiropln /p p@ssW23 /fo list`).
- Determine the Windows version: `systeminfo | findstr /B /C:"OS Name" /B /C:"OS Version"`.

# options

| option    | description    |
| --- | --- |
| `/s <computer>` | Specifies the name or IP address of a remote computer (do not use backslashes). The default is the local computer. |
| `/u <domain>\<username>` | Runs the command with the account permissions of the specified user account; defaults to the currently logged-on user. |
| `/p <password>` | Specifies the password of the user account specified in `/u`. |
| `/fo <format>` | Specifies the output format: `TABLE`, `LIST`, or `CSV`. |
| `/nh` | Suppresses column headers in the output. Valid when `/fo` is TABLE or CSV. |
| `/?` | Displays help at the command prompt. |
