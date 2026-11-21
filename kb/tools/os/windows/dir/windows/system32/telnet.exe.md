---
created: 2026-11-21
fullpath: 'C:\Windows\System32\telnet.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - network
aliases:
  - telnet.exe
  - telnet
  - Telnet Client
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/telnet
  - https://learn.microsoft.com/windows-server/administration/windows-commands/telnet-open
  - https://learn.microsoft.com/windows-server/administration/windows-commands/telnet-set
  - https://learn.microsoft.com/windows-server/administration/windows-commands/telnet-send
---

**fullpath**:C:\Windows\System32\telnet.exe

# description

telnet communicates with a computer running the telnet server service. Run without parameters it enters the telnet context (`Microsoft telnet>` prompt), where telnet subcommands such as open, close, display, set, unset, send, status and quit are used. The telnet client is an optional feature that must be installed before use; the server side is administered with `tlntadmn`.

## simple description

> ### 2026-11-21 Claude said
> telnet.exe is the Windows Telnet client, an optional feature that opens a plain-text TCP session to a remote host. It was designed for remote terminal logins but is mostly used today to test whether a TCP port is open. Everything, including passwords, is sent unencrypted. It is not installed by default on modern Windows.
>
> **SOC NOTE**: Telnet use on a modern network is unusual; its presence may indicate someone enabled the TelnetClient feature (`dism /online /Enable-Feature /FeatureName:TelnetClient`) for port scanning or discovery (MITRE ATT&CK T1046) or cleartext remote access (T1021). Outbound TCP 23 or telnet.exe connecting to many ports in sequence is worth investigating. Credentials over telnet can be captured from network traffic.

# purpose

Connects to a remote host by hostname or IP address on TCP port 23 by default, optionally another port, with optional automatic logon, terminal type selection and client-side logging.

# typical use cases

| usage | description |
| --- | --- |
| `telnet telnet.microsoft.com` | Connect to the computer running the telnet Server Service at telnet.microsoft.com. |
| `telnet /f telnetlog.txt telnet.microsoft.com 44` | Connect on TCP port 44 and log the session to telnetlog.txt. |
| `o telnet.microsoft.com` | From the telnet prompt, open a connection to a telnet server. |
| `sen ayt` | From the telnet prompt, send the "Are you there?" command to the server. |

# options

| option | description |
| --- | --- |
| `/a` | Attempts automatic logon; same as /l but uses the currently logged on user's name. |
| `/e <escapechar>` | Specifies the escape character used to enter the telnet client prompt. |
| `/f <filename>` | Specifies the file name used for client side logging. |
| `/l <username>` | Specifies the user name to log on with on the remote computer. |
| `/t {vt100 \| vt52 \| ansi \| vtnt}` | Specifies the terminal type. |
| `<host> [<port>]` | Hostname or IP address of the remote computer and optional TCP port (default 23). |
| `/?` | Displays help at the command prompt. |
