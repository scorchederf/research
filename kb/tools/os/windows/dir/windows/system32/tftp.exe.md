---
created: 2026-11-21
fullpath: 'C:\Windows\System32\tftp.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - network
  - file-transfer
  - lolbin
aliases:
  - 'tftp.exe'
  - 'tftp'
  - 'TFTP client'
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/tftp
---

**fullpath**:C:\Windows\System32\tftp.exe

# description

`tftp.exe` is the Windows Trivial File Transfer Protocol client, used to transfer files to and from a remote computer running a TFTP service or daemon. It is an optional Windows feature (TFTP Client) documented in the Windows Commands reference; Microsoft no longer ships a TFTP server service.

## simple description

> ### 2026-11-21 Claude said
> TFTP is a very simple file-copy protocol over UDP port 69 with no username, password or encryption. The Windows tftp.exe client can download (get) or upload (put) a file to a TFTP server. It is mainly used with network gear and PXE boot, and is not installed by default on modern Windows.
>
> **SOC NOTE**: Rare on normal endpoints, so its presence or execution is suspicious. Used for ingress tool transfer (T1105) and exfiltration over an unencrypted non-C2 protocol (T1048.003). Look for process creation (4688 / Sysmon 1) of tftp.exe with `get`/`put`, outbound UDP/69 in firewall/NetFlow/Sysmon 3, and enablement of the TFTP optional feature (e.g. `dism /enable-feature /featurename:TFTP`).
>

# purpose

Transfers files to and from a remote computer, typically one running UNIX, that runs the TFTP service. Typically used by embedded devices or systems that retrieve firmware, configuration information, or a system image during the boot process. Learn warns that the protocol has no authentication or encryption, installing the client is not recommended for Internet-connected systems, and a TFTP server is no longer provided by Microsoft for security reasons.

# typical use cases

| usage | description |
| --- | --- |
| `tftp -i Host1 get boot.img` | Copy the file *boot.img* from the remote computer *Host1* in binary mode. |

# options

| option | description |
| --- | --- |
| `-i` | Binary image (octet) transfer mode; use for binary files. Without it, the file is transferred in ASCII mode (default), converting EOL characters. |
| `<host>` | The local or remote computer. |
| `get` | Transfers the remote file *destination* to the local file *source*. |
| `put` | Transfers the local file *source* to the remote file *destination*; files must be writable on the remote computer because TFTP has no authentication. |
| `<source>` | The file to transfer. |
| `<destination>` | Where to transfer the file. |
