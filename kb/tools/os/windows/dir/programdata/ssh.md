---
created: 2026-11-21
fullpath: 'C:\ProgramData\ssh'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - openssh
  - ssh
aliases:
  - ssh
  - %programdata%\ssh
url:
  - https://learn.microsoft.com/windows-server/administration/openssh/openssh-server-configuration
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/enable-openssh-verbose-logging
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/troubleshoot-sftp-issues-using-openssh
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/upgrade-in-box-openssh-to-latest-openssh-release
---

**fullpath**:C:\ProgramData\ssh

# description

`%programdata%\ssh` is the system-wide configuration and data folder for OpenSSH for Windows (in-box since Windows Server 2019 and Windows 10 1809). It holds the server configuration `sshd_config`, the system-wide client configuration `ssh_config`, host keys, `administrators_authorized_keys` and the `logs` folder.

## simple description

> ### 2026-11-21 Claude said
> This folder stores the settings and keys for the built-in OpenSSH server and client on Windows. sshd_config controls who can log in and how; the host key files identify the server; administrators_authorized_keys lists public keys allowed to log in as an administrator. When file logging is enabled, logs go to the logs subfolder.
>
> **SOC NOTE**: Key persistence location: adding a key to `administrators_authorized_keys` or loosening `sshd_config` (e.g. PasswordAuthentication, AllowUsers) grants backdoor remote access (MITRE T1098.004 SSH Authorized Keys, T1021.004). Stolen host private keys enable server impersonation. Monitor file changes here, the sshd service install, and OpenSSH/Operational event logs.
>

# purpose

Default configuration location read by sshd at service start (changes require a service restart; generated with defaults if missing) and by the ssh client as the system-wide config after `-F` and `%userprofile%\.ssh\config`. Should be backed up before upgrading in-box OpenSSH.

# common files found

| file | description |
| --- | --- |
| `sshd_config` | OpenSSH Server configuration file. |
| `ssh_config` | System-wide OpenSSH client configuration. |
| `administrators_authorized_keys` | Public keys allowed for administrator accounts. |
| `logs` | Folder for sshd/SFTP log files when `SyslogFacility LOCAL0` is set. |
