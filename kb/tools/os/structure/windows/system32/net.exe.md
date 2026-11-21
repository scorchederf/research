---
created: 2026-11-21
fullpath: 'C:\Windows\System32\net.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows-commands
aliases:
  - net.exe
  - net
  - Net Commands
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/net-commands-on-operating-systems
  - https://learn.microsoft.com/windows-server/administration/windows-commands/net-user
  - https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands
---

**fullpath**:C:\Windows\System32\net.exe

# description

Net commands perform operations on groups, users, account policies, shares and services in Windows. Subcommands such as `net user` add, modify, delete and display user accounts on the local computer or domain, and `net accounts` sets local password and lockout policy.

## simple description

> ### 2026-11-21 Claude said
> net.exe is the classic Windows networking and account command. It manages users and groups, mapped drives and shares, services, sessions and time sync. Many subcommands work against the domain with `/domain`. It hands much of its work to net1.exe.
>
> **SOC NOTE**: One of the most abused LOLBins: discovery (`net user /domain`, `net group "Domain Admins" /domain`, `net localgroup administrators`, `net view`, `net share`, `net session` - T1087, T1069, T1135, T1049), account creation/persistence (`net user x pw /add`, `net localgroup administrators x /add` - T1136, T1098), lateral movement (`net use \\host\C$`, T1021.002) and stopping services (`net stop`, T1489). Watch 4688 / Sysmon 1 for net.exe and net1.exe plus events 4720, 4728, 4732.
>

# purpose

Command-line administration of accounts, groups, policies, shares, network connections and services.

# typical use cases

- `net user` / `net user <name> /domain` - list or inspect accounts.
- `net user <name> <pw> /add` - create a user.
- `net accounts` - view or set password/lockout policy.
- `net use x: \\server\share` - map a drive.

# options

| option | description |
| --- | --- |
| `ACCOUNTS` | Set local account and password policy (`/FORCELOGOFF`, `/MINPWLEN`, `/MAXPWAGE`, `/MINPWAGE`, `/UNIQUEPW`, `/DOMAIN`); not used on domain controllers. |
| `COMPUTER` | Net subcommand (listed on Learn without further detail). |
| `CONFIG` | Net subcommand (listed on Learn without further detail). |
| `CONTINUE` | Net subcommand (listed on Learn without further detail). |
| `FILE` | Net subcommand (listed on Learn without further detail). |
| `GROUP` | Net subcommand (listed on Learn without further detail). |
| `HELP` | Net subcommand (listed on Learn without further detail). |
| `HELPMSG` | Net subcommand (listed on Learn without further detail). |
| `LOCALGROUP` | Net subcommand (listed on Learn without further detail). |
| `NAME` | Net subcommand (listed on Learn without further detail). |
| `PAUSE` | Net subcommand (listed on Learn without further detail). |
| `PRINT` | Net subcommand (listed on Learn without further detail). |
| `SEND` | Net subcommand (listed on Learn without further detail). |
| `SESSION` | Net subcommand (listed on Learn without further detail). |
| `SHARE` | Net subcommand (listed on Learn without further detail). |
| `START` | Net subcommand (listed on Learn without further detail). |
| `STATISTICS` | Net subcommand (listed on Learn without further detail). |
| `STOP` | Net subcommand (listed on Learn without further detail). |
| `TIME` | Net subcommand (listed on Learn without further detail). |
| `USE` | Connect to a network share, e.g. `net use x: \\server\share`. |
| `USER` | Add, modify, delete or display user accounts on the local computer or domain (`/add`, `/delete`, `/domain`, `/active`, `/times`, `/expires`, ...). |
| `VIEW` | Net subcommand (listed on Learn without further detail). |
