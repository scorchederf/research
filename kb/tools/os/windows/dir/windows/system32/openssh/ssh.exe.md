---
created: 2026-11-21
fullpath: 'c:\windows\system32\OpenSSH\ssh.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - remote-access
aliases:
  - ssh.exe
  - ssh
  - OpenSSH Client
url:
  - https://learn.microsoft.com/windows-server/administration/openssh/openssh-overview
  - https://learn.microsoft.com/windows-server/administration/openssh/openssh_install_firstuse
  - https://learn.microsoft.com/windows-server/administration/openssh/openssh-server-configuration
---

**fullpath**:c:\windows\system32\OpenSSH\ssh.exe

# description

`ssh.exe` is the SSH client component of OpenSSH for Windows, available as a Feature on Demand (`OpenSSH.Client~~~~0.0.1.0`) since Windows 10 build 1809 and Windows Server 2019. Microsoft services this in-box version through Windows Update and maintains a fork at PowerShell/openssh-portable. Related tools in the same folder are `sshd`, `ssh-keygen`, `ssh-agent`, `ssh-add`, `ssh-keyscan`, `sftp` and `scp`.

## simple description

> ### 2026-11-21 Claude said
> ssh.exe is the built-in OpenSSH client in Windows that opens encrypted remote shell sessions to other machines over the SSH protocol, normally on TCP port 22. Admins use it to manage Linux servers, network devices or Windows hosts running sshd. It can also forward ports, creating encrypted tunnels. It reads settings from the user's `.ssh\config` and stores trusted host keys in `.ssh\known_hosts`.
>
> **SOC NOTE**: Because it is a signed, preinstalled binary, attackers use ssh.exe for lateral movement (T1021.004), tunnelling and port forwarding to bypass firewalls (T1572, T1090 with `-R`/`-L`/`-D`), and exfiltration via scp/sftp (T1048). Investigate unusual parents (Office, wscript, rundll32), outbound connections to internet IPs on 22/443, `-R` reverse tunnels, and artifacts in `%USERPROFILE%\.ssh\known_hosts`, `config` and private keys; check Sysmon Event IDs 1 and 3 and the OpenSSH/Operational event log.
>

# purpose

SSH is based on a client-server architecture: `ssh` runs on the user's local system and connects to `sshd` on the system being managed remotely, encrypting all traffic to prevent eavesdropping and connection hijacking. On first connection the user confirms the server's key fingerprint, which adds the server to the known SSH hosts list. The client reads configuration from a file passed with `-F`, then `%userprofile%\.ssh\config`, then the system-wide `%programdata%\ssh\ssh_config`. Microsoft Learn does not duplicate the open-source OpenSSH option documentation, which is on OpenSSH.com.

# typical use cases

| usage | description |
| --- | --- |
| `ssh domain\username@servername` | Connect to an OpenSSH server as a domain user. |
| `Get-WindowsCapability -Online \| Where-Object Name -like 'OpenSSH*'` | Check whether the OpenSSH client and server are installed. |
| `Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0` | Install the OpenSSH client. |

# options

| option | description |
| --- | --- |
| `-F` | Uses the specified configuration file (with an entry name from that file) instead of the user and system-wide configuration files. |
