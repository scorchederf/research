---
created: 2026-11-21
fullpath: 'C:\Windows\System32\OpenSSH\scp.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - openssh
  - file-transfer
aliases:
  - 'scp.exe'
  - 'scp'
  - 'OpenSSH scp'
url:
  - https://learn.microsoft.com/windows-server/administration/openssh/openssh-overview
  - https://learn.microsoft.com/windows-server/administration/openssh/openssh_keymanagement
  - https://learn.microsoft.com/azure/virtual-machines/copy-files-to-vm-using-scp
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/factoryos/connect-using-ssh?view=windows-11
  - https://learn.microsoft.com/windows/terminal/tutorials/ssh
---

**fullpath**: C:\Windows\System32\OpenSSH\scp.exe

# description

`scp` is the OpenSSH file copy utility that runs over SSH, part of OpenSSH for Windows (a feature on demand since Windows 10 1809 / Windows Server 2019) installed in `C:\Windows\System32\OpenSSH`. Related tools: ssh, sshd, sftp, ssh-keygen, ssh-agent, ssh-add, ssh-keyscan.

## simple description

> ### 2026-11-21 Claude said
> scp securely copies files between this computer and a remote SSH server, encrypting the transfer. It uses SSH for login (password or key) so the same accounts and keys as ssh apply. It is part of the optional OpenSSH Client feature built into modern Windows.
>
> **SOC NOTE**: Signed in-box binary usable for exfiltration or tool transfer over port 22 (MITRE T1048 Exfiltration Over Alternative Protocol, T1105 Ingress Tool Transfer, T1021.004). Watch for scp.exe to external hosts, `-o StrictHostKeyChecking=no`, or use by service accounts; the client leaves known_hosts entries in %USERPROFILE%\.ssh.
>

# purpose

Copies files to and from remote systems over SSH; also used to copy public keys to a server during initial key-based authentication setup.

# typical use cases

| usage | description |
| --- | --- |
| `scp file azureuser@azurehost:directory/targetfile` | Upload a file to a remote host. |
| `scp azureuser@azurehost:directory/file targetfile` | Download a file from a remote host. |

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
