---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Temp\.net\devtunnel\devtunnel.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - tunneling
aliases:
  - devtunnel.exe
  - devtunnel
  - Dev tunnels CLI
url:
  - https://learn.microsoft.com/azure/developer/dev-tunnels/cli-commands
  - https://learn.microsoft.com/azure/developer/dev-tunnels/get-started
---

**fullpath**:C:\Users\<username>\AppData\Local\Temp\.net\devtunnel\devtunnel.exe

# description

`devtunnel.exe` is the Microsoft dev tunnels command-line tool (in public preview) for creating, hosting and managing dev tunnels, which expose a local server to the internet with access control. It can be installed with winget (`Microsoft.devtunnel`), downloaded directly, or used through Visual Studio. This path under `%TEMP%\.net\` is where a single-file .NET app extracts itself; Learn does not document this specific location.

## simple description

> ### 2026-11-21 Claude said
> Dev tunnels let a developer share a web server running on their PC (for example `localhost:3000`) through a public Microsoft URL like `https://xyz-3000.usw2.devtunnels.ms`. `devtunnel.exe` is the command-line tool that signs in and keeps that tunnel open. The `Temp\.net\devtunnel` folder is where the self-contained .NET executable unpacks its files when it runs.
>
> **SOC NOTE**: Abused for command-and-control and exfiltration through a trusted Microsoft domain (T1572 Protocol Tunneling, T1090 Proxy, T1219). Watch for `devtunnel host` with `--allow-anonymous`, connections to `*.devtunnels.ms` / `global.rel.tunnels.api.visualstudio.com` from non-developer hosts, and devtunnel run from Temp or Downloads. Tunnels to RDP/SMB ports are a strong red flag.
>

# purpose

Host a local port through a dev tunnel, connect to tunnels, and manage tunnels, ports, access and user login.

# typical use cases

| usage | description |
| --- | --- |
| `devtunnel user login` | Log in with a Microsoft Entra ID or Microsoft account. |
| `devtunnel user login -g -d` | Log in with a GitHub account using device code login. |
| `devtunnel host -p 3000` | Host a temporary dev tunnel for a server listening on port 3000. |
| `devtunnel host -p 3000 --allow-anonymous` | Host a temporary tunnel and enable anonymous client access. |
| `devtunnel host -p 8443 --protocol https` | Host a tunnel for an HTTPS server on port 8443. |
| `devtunnel host -p 8000 --expiration 2d` | Host a temporary tunnel with a custom expiration (1h to 30d). |
| `devtunnel connect TUNNELID` | Forward connections from a local port on the client to the tunnel port. |
| `devtunnel create -a` | Create a persistent dev tunnel that allows anonymous access. |
| `devtunnel port create -p 3000 --protocol http` | Add a port to a tunnel. |
| `devtunnel clusters --ping` | List service clusters sorted by measured latency. |
| `devtunnel echo http --port 8080 --interface 127.0.0.1` | Start a local HTTP diagnostic echo server on port 8080. |

# options

| option | description |
| --- | --- |
| `-v, --verbose` | Enable verbose output (global option). |
| `-?, -h, --help` | Show help and usage information (global option). |
| `user login` | Log in with a Microsoft or GitHub account (`-g` GitHub, `-d` device code). |
| `user logout` | Clear the cached token. |
| `user show` | Show current login status. |
| `host` | Host a dev tunnel; creates a temporary tunnel if no ID is given. |
| `connect` | Connect to a dev tunnel and forward ports to the client. |
| `create` | Create a persistent dev tunnel. |
| `list` | List dev tunnels. |
| `show` | Show dev tunnel details. |
| `update` | Update dev tunnel properties. |
| `delete` | Delete a dev tunnel. |
| `delete-all` | Delete all dev tunnels. |
| `port create` | Create a dev tunnel port. |
| `port list` | List dev tunnel ports. |
| `port show` | Show dev tunnel port details. |
| `port update` | Update dev tunnel port properties. |
| `port delete` | Delete a dev tunnel port. |
| `clusters` | List available service clusters by location. |
| `echo` | Run a diagnostic echo server on a local port. |
| `ping` | Send diagnostic messages to a remote echo server. |
