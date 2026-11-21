---
created: 2026-11-21
fullpath: 'C:\WINDOWS\System32\Netsh.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Netsh.exe
  - netsh
  - Network shell
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/netsh
  - https://learn.microsoft.com/windows-server/administration/windows-commands/netsh-show
---

**fullpath**:C:\WINDOWS\System32\Netsh.exe

# description

Network shell (netsh) is a command-line utility to configure and monitor Windows networking components. It is extended by helper DLLs that each provide a context (for example dhcpclient, interface, advfirewall), and can run locally or against a remote computer.

## simple description

> ### 2026-11-21 Claude said
> netsh lets you view and change almost any network setting from the command line: IP addresses, DNS, firewall rules, Wi-Fi profiles, port proxies and more. It can run interactively (typing netsh opens its own prompt) or run single commands and scripts. Most changes need an elevated prompt.
>
> **SOC NOTE**: Heavily abused: `netsh advfirewall` to open ports or disable the firewall (T1562.004), `interface portproxy` for pivoting (T1090), `wlan show profile key=clear` to dump Wi-Fi passwords (T1555), `add helper` for DLL persistence (T1546.007), and `trace start` for packet capture. Check for unexpected helper DLLs (HKLM\SOFTWARE\Microsoft\NetSh) and portproxy entries.
>

# purpose

Configure and monitor networking components through contexts provided by helper DLLs.

# typical use cases

| usage | description |
| --- | --- |
| `netsh interface ipv4 set address "NetLAN1" static <IP_Address> <Subnet_Mask> <Gateway>` | Set a static IPv4 address, mask and gateway for an interface without changing context. |
| `netsh show alias` | List aliases defined in the environment. |
| `netsh show helper` | List the DLL helper files in use. |

# options

| option    | description    |
| --- | --- |
| `-a` | Return to the netsh shell after running an alias file. |
| `-c` | Enter the specified netsh context. |
| `-r` | Run on a remote computer (name, FQDN or IP); requires Remote Registry on the target. |
| `-u` | Run under a specific user account (`DomainName\Username`). |
| `-p` | Password for the user account; `*` prompts securely. |
| `Command` | The netsh command to run. |
| `-f` | Exit netsh after running the commands in the specified script file. |
