---
created: 2026-11-21
fullpath: 'C:\Windows\System32\cmstp.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - connection-manager
aliases:
  - cmstp.exe
  - Connection Manager Profile Installer
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp
---

**fullpath**:C:\Windows\System32\cmstp.exe

# description

cmstp installs or removes a Connection Manager service profile; used without optional parameters, it installs a service profile with default settings appropriate to the operating system and the user's permissions. It is a built-in Windows command documented in the Windows Commands reference and is typically invoked by a Connection Manager profile installation package (`<serviceprofilefilename>.exe`) together with an .inf configuration file.

## simple description

> ### 2026-11-21 Claude said
> cmstp.exe installs Connection Manager profiles, which are pre-packaged VPN or dial-up connection settings described by an .inf file. It is a signed Microsoft binary present on every Windows system. Legitimate use is rare outside old VPN deployments.
>
> **SOC NOTE**: Attackers abuse cmstp.exe with a malicious .inf (`cmstp.exe /ni /s c:\temp\evil.inf`) to run commands or register a remote .sct and to bypass UAC through the CMSTPLUA COM interface (MITRE ATT&CK T1218.003 CMSTP, T1548.002). Hunt for cmstp.exe launching child processes, loading .inf files from user-writable paths, or making network connections; Sysmon Event ID 1/3/12/13 around cmstp are high value.
>

# purpose

Install or uninstall Connection Manager service profiles from an .inf configuration file.

# typical use cases

| usage | description |
| --- | --- |
| `fiction.exe /c:cmstp.exe fiction.inf /nf` | Install the fiction service profile without any support files. |
| `fiction.exe /c:cmstp.exe fiction.inf /s /su` | Silently install the fiction service profile for a single user. |
| `fiction.exe /c:cmstp.exe fiction.inf /s /u` | Silently uninstall the fiction service profile. |

# options

| option | description |
| --- | --- |
| `<serviceprofilefilename>.exe` | Installation package that contains the profile to install. Required for Syntax 1, not valid for Syntax 2. |
| `/q:a` | Installs the profile without prompting the user; the success verification message still appears. Required for Syntax 1, not valid for Syntax 2. |
| `[drive:][path] <serviceprofilefilename>.inf` | Required. Configuration file that determines how the profile is installed; `[drive:][path]` is not valid for Syntax 1. |
| `/nf` | Specifies that the support files should not be installed. |
| `/s` | Installs or uninstalls the service profile silently; the only parameter that can be combined with `/u`. |
| `/u` | Uninstalls the service profile. |
| `/?` | Displays help at the command prompt. |
