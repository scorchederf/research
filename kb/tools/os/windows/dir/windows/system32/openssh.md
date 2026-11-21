---
created: 2026-11-21
fullpath: 'C:\Windows\System32\OpenSSH'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - openssh
  - ssh
  - remote-access
aliases:
  - OpenSSH
  - OpenSSH for Windows
url:
  - https://learn.microsoft.com/windows-server/administration/openssh/openssh-overview
  - https://learn.microsoft.com/windows-server/administration/openssh/openssh-server-configuration
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/upgrade-in-box-openssh-to-latest-openssh-release
---

**fullpath**:C:\Windows\System32\OpenSSH

# description

In-box install folder of OpenSSH for Windows, available as a feature on demand since Windows 10 build 1809 and Windows Server 2019 (installed but not enabled on Windows Server 2025). Configuration lives separately in `%programdata%\ssh`. It is managed with `Add-WindowsCapability` / `Remove-WindowsCapability` (`OpenSSH.Client~~~~0.0.1.0`, `OpenSSH.Server~~~~0.0.1.0`).

## simple description

> ### 2026-11-21 Claude said
> This folder holds Microsoft's built-in OpenSSH client and server: ssh.exe, scp.exe, sftp.exe, ssh-keygen and, if the server feature is installed, sshd.exe. It lets admins connect to and from Windows over SSH like on Linux. Server settings and host keys are in C:\ProgramData\ssh, user keys in %USERPROFILE%\.ssh.
>
> **SOC NOTE**: ssh.exe is abused for tunneling/port forwarding and exfiltration (T1572, T1021.004), and attackers enable sshd for persistent remote access, adding keys to administrators_authorized_keys (T1098.004). Watch for new sshd service installs, firewall rules for port 22, and logs in Applications and Services Logs > OpenSSH > Operational.
>

# purpose

Contains the OpenSSH commands built into Windows. sshd reads `%programdata%\ssh\sshd_config` by default; the client reads `%userprofile%\.ssh\config` then `%programdata%\ssh\ssh_config`. Host keys are stored under `C:\ProgramData\ssh`. When upgrading from GitHub releases, multiple OpenSSH folders (typically in System32) can cause path conflicts.

# common files found

| file | description |
| --- | --- |
| `ssh.exe` | SSH client component. |
| `sshd.exe` | SSH server component (OpenSSH SSH Server service). |
| `ssh-keygen.exe` | Generates, manages and converts authentication keys. |
| `ssh-agent.exe` | Stores private keys used for public key authentication. |
| `ssh-add.exe` | Adds private keys to the list allowed by the server. |
| `ssh-keyscan.exe` | Collects public SSH host keys from hosts. |
| `sftp.exe` | Secure File Transfer Protocol over SSH. |
| `scp.exe` | File copy utility over SSH. |
