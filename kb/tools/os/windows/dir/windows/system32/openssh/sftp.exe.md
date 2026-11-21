---
created: 2026-11-21
fullpath: 'C:\Windows\System32\OpenSSH\sftp.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - openssh
  - file-transfer
aliases:
  - 'sftp.exe'
  - 'sftp'
  - 'OpenSSH SFTP client'
url:
  - https://learn.microsoft.com/windows-server/administration/openssh/openssh-overview
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/factoryos/connect-using-ssh?view=windows-11
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/troubleshoot-sftp-issues-using-openssh
---

**fullpath**:C:\Windows\System32\OpenSSH\sftp.exe

# description

`sftp.exe` is the OpenSSH for Windows Secure File Transfer Protocol client, available as a Feature on Demand since Windows 10 build 1809 and Windows Server 2019 alongside `ssh`, `scp`, `ssh-keygen`, `ssh-agent`, `ssh-add`, `ssh-keyscan` and `sshd`. Microsoft maintains a fork of OpenSSH on GitHub; full option documentation is on OpenSSH.com.

## simple description

> ### 2026-11-21 Claude said
> Sftp is an interactive or scripted file-transfer client that runs over SSH (TCP 22), so traffic is encrypted and authenticated by password or keys. On Windows it is part of the built-in OpenSSH client. Users can get/put files and browse remote directories.
>
> **SOC NOTE**: Encrypted exfiltration and tool transfer channel (T1048.002 / T1105) that blends in with admin traffic; batch mode (`-b`) enables unattended transfers. Look for sftp.exe on hosts where admins don't normally use it, connections to external IPs on 22/2222, use of new keys in `%USERPROFILE%\.ssh`, and known_hosts entries for unexpected hosts.
>

# purpose

Per Learn, `sftp` provides the Secure File Transfer Protocol and runs over SSH; it is included in Windows and can be run from a command prompt. Learn shows the usage synopsis `sftp [-46aCfpqrv] [-B buffer_size] [-b batchfile] [-c cipher] [-D sftp_server_path] [-F ssh_config] [-i identity_file] [-l limit] [-o ssh_option] [-P port] [-R num_requests] [-S program] [-s subsystem | sftp_server] destination`, but does not describe the individual options.

# typical use cases

| usage | description |
| --- | --- |
| `sftp contoso4.contosouser@contoso4.blob.core.windows.net` | Connect to an SFTP endpoint (Azure Blob Storage example) as the given user. |
| `sftp -i ~/.ssh/<your_private_key> -P 2705 <username>@sftp.linkedin.com` | Connect with a specific private key on a non-default port. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
