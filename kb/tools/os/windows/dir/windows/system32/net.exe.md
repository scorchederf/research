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
  - https://learn.microsoft.com/windows-server/administration/server-core/server-core-administer
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/add-special-groups-to-built-in-groups
  - https://learn.microsoft.com/powershell/scripting/samples/performing-networking-tasks
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/problems-administrative-shares-missing
  - https://learn.microsoft.com/windows-server/administration/windows-commands/net-print
  - https://learn.microsoft.com/sysinternals/downloads/psfile
  - https://learn.microsoft.com/windows/win32/wmisdk/starting-and-stopping-the-wmi-service
  - https://learn.microsoft.com/sql/database-engine/configure-windows/start-stop-pause-resume-restart-sql-server-services
  - https://learn.microsoft.com/biztalk/core/how-to-start-stop-pause-resume-or-restart-biztalk-server-services
  - https://learn.microsoft.com/windows/win32/com/error-handling-strategies
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

| usage | description |
| --- | --- |
| `net user` / `net user <name> /domain` | list or inspect accounts. |
| `net user <name> <pw> /add` | create a user. |
| `net accounts` | view or set password/lockout policy. |
| `net use x: \\server\share` | map a drive. |
| `net localgroup Administrators /add <domain>\<username>` | Add a user to the local Administrators group. |
| `net share` | List shares, including ADMIN$, C$ and IPC$. |
| `net start <ServiceName>` / `net stop <ServiceName>` | Start or stop a service. |
| `net helpmsg 1355` | Decode a Windows error number. |

# options

| option | description |
| --- | --- |
| `ACCOUNTS` | Set local account and password policy (`/FORCELOGOFF`, `/MINPWLEN`, `/MAXPWAGE`, `/MINPWAGE`, `/UNIQUEPW`, `/DOMAIN`); not used on domain controllers. |
| `COMPUTER` | _Not documented on Microsoft Learn at 2026/11/21 06:28 UTC_ |
| `CONFIG` | _Not documented on Microsoft Learn at 2026/11/21 06:28 UTC_ |
| `CONTINUE` | Resumes a paused service: `net continue <ServiceName>`. |
| `FILE` | Shows files on this system that other computers have opened. Long path names are truncated and it can't show remote systems. |
| `GROUP` | _Not documented on Microsoft Learn at 2026/11/21 06:28 UTC_ |
| `HELP` | _Not documented on Microsoft Learn at 2026/11/21 06:28 UTC_ |
| `HELPMSG` | Shows the text for a system or network error code: `net helpmsg <decimal_code>` (e.g. `net helpmsg 1355` returns "The specified domain did not exist"). |
| `LOCALGROUP` | Lists local groups (`net localgroup`), creates one (`net localgroup <name> /add`), or adds/removes members (`net localgroup Administrators /add <domain>\<user>`, `/delete`). Can add special groups such as `"nt authority\authenticated users"`. |
| `NAME` | _Not documented on Microsoft Learn at 2026/11/21 06:28 UTC_ |
| `PAUSE` | Pauses a running service: `net pause <ServiceName>`. |
| `PRINT` | Deprecated. Displays a printer queue or print job, or controls a job (`/hold`, `/release`, `/delete`): `net print \\<computer>\<share>` or `net print \\<computer> <jobnumber>`. |
| `SEND` | _Not documented on Microsoft Learn at 2026/11/21 06:28 UTC_ |
| `SESSION` | _Not documented on Microsoft Learn at 2026/11/21 06:28 UTC_ |
| `SHARE` | Lists shares, including administrative shares (ADMIN$, C$, IPC$), or creates one, e.g. `net share tempshare=C:\temp /users:25 /remark:"..."`. |
| `START` | Starts a service: `net start <ServiceName>` (e.g. `net start winmgmt`); service startup options can be appended using `/` instead of `-`. |
| `STATISTICS` | _Not documented on Microsoft Learn at 2026/11/21 06:28 UTC_ |
| `STOP` | Stops a service: `net stop <ServiceName>`; services that depend on it also stop. |
| `TIME` | _Not documented on Microsoft Learn at 2026/11/21 06:28 UTC_ |
| `USE` | Connect to a network share, e.g. `net use x: \\server\share`. |
| `USER` | Add, modify, delete or display user accounts on the local computer or domain (`/add`, `/delete`, `/domain`, `/active`, `/times`, `/expires`, ...). |
| `VIEW` | Used to view a computer's resources remotely (mentioned on Learn alongside `net use`; no syntax documented). |
