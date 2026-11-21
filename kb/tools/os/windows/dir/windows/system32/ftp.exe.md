---
created: 2026-11-21
fullpath: 'C:\Windows\System32\ftp.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - network
  - ftp
aliases:
  - ftp.exe
  - ftp
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/ftp
---

**fullpath**:C:\Windows\System32\ftp.exe

# description

`ftp` transfers files to and from a computer running an FTP server service, interactively or in batch mode using ASCII text script files. It is a built-in Windows command available when TCP/IP is installed; subcommands such as `open`, `get`, `put`, `user` and `type` are documented separately.

## simple description

> ### 2026-11-21 Claude said
> ftp.exe is the built-in Windows command-line FTP client. It connects to an FTP server to upload and download files, either by typing commands interactively or by reading them from a script file with `-s:`. FTP sends credentials and data unencrypted, so it is rarely used legitimately in modern environments.
>
> **SOC NOTE**: A LOLBin: `ftp -s:script.txt` can run local commands via `!` and exfiltrate data (MITRE T1048.003, T1105, T1202). Any ftp.exe execution on a workstation, especially with `-s:` or spawned from scripts/Office, deserves a look; check outbound TCP 21 connections and the script file contents.
>

# purpose

Transfers files to/from an FTP server; parameters are case-sensitive; with `-s:` commands run automatically after start (UTF-8 required on Windows 8/Server 2012+).

# typical use cases

| usage | description |
| --- | --- |
| `ftp <host>` | Connects to an FTP server interactively. |
| `ftp -s:<filename> <host>` | Runs ftp commands from a text file after connecting. |
| `ftp -A <host>` | Logs on as anonymous. |
| `ftp -n -s:<filename>` | Suppresses auto-login and runs a command script. |
| `open ftp.microsoft.com 755` | (Interactive) connects to a server on TCP port 755. |
| `get test.txt test1.txt` | (Interactive) downloads a remote file under a new name. |
| `put program.exe` | (Interactive) uploads a local file. |

# options

| option | description |
| --- | --- |
| `-v` | Suppresses display of remote server responses. |
| `-d` | Enables debugging, showing all commands passed between client and server. |
| `-i` | Disables interactive prompting during multiple file transfers. |
| `-n` | Suppresses auto-login upon initial connection. |
| `-g` | Disables file name globbing (wildcards `*` and `?`). |
| `-s:<filename>` | Text file with ftp commands that run automatically after start; no spaces allowed. |
| `-a` | Any local interface can be used when binding the data connection. |
| `-A` | Logs on as anonymous. |
| `-x:<sendbuffer>` | Overrides the default SO_SNDBUF size of 8192. |
| `-r:<recvbuffer>` | Overrides the default SO_RCVBUF size of 8192. |
| `-b:<asyncbuffers>` | Overrides the default async buffer count of 3. |
| `-w:<windowsize>` | Transfer buffer size; default 65535 bytes. |
| `<host>` | Computer name, IP or IPv6 address of the server; must be last. |
| `-?` | Displays help at the command prompt. |

