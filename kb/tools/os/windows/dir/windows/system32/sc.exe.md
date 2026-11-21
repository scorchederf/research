---
created: 2026-11-21
fullpath: 'C:\Windows\System32\sc.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - services
aliases:
  - sc.exe
  - Service Control
url:
  - https://learn.microsoft.com/windows/win32/services/configuring-a-service-using-sc
  - https://learn.microsoft.com/windows/win32/services/controlling-a-service-using-sc
  - https://learn.microsoft.com/windows-server/administration/windows-commands/sc-create
  - https://learn.microsoft.com/windows-server/administration/windows-commands/sc-config
  - https://learn.microsoft.com/dotnet/core/extensions/windows-service
---

**fullpath**:C:\Windows\System32\sc.exe

# description

Sc.exe is a command-line utility that queries or modifies the database of installed services and controls services; its commands correspond to the functions provided by the Service Control Manager (SCM). It is included with Windows and documented in the Windows SDK and Windows Commands reference (`sc.exe create`, `sc.exe config`, `sc.exe delete`, `sc.exe query`).

## simple description

> ### 2026-11-21 Claude said
> sc.exe is the built-in command-line tool for managing Windows services. It can create, delete, start, stop, query and reconfigure services on the local machine or on a remote one. Admins and installers use it routinely. In PowerShell you must type `sc.exe`, because `sc` is an alias for Set-Content.
>
> **SOC NOTE**: Attackers use sc.exe to create or modify services for persistence and privilege escalation (`sc create`, `sc config binpath=`; MITRE ATT&CK T1543.003), to run payloads remotely (`sc \\host create ...`, T1569.002, T1021), and to stop or disable security tools (`sc stop`, `sc config start= disabled`, T1489/T1562.001). Correlate with System Event ID 7045 (service installed), 7040 (start type changed) and Security 4697.
>

# purpose

Query, configure and control services through the Service Control Manager, locally or on a remote server.

# typical use cases

| usage | description |
| --- | --- |
| `sc.exe create NewService binpath= c:\windows\system32\NewServ.exe type= share start= auto depend= +TDI NetBIOS` | Create and register a new service with a shared process, auto start and a dependency. |
| `sc.exe \\myserver create NewService binpath= c:\windows\system32\NewServ.exe` | Create a service on a remote server. |
| `sc.exe config NewService binpath= c:\windows\system32\NewServ.exe` | Change the binary path of an existing service. |
| `sc.exe failure ".NET Joke Service" reset= 0 actions= restart/60000/restart/60000/run/1000` | Configure service recovery actions. |
| `sc qfailure ".NET Joke Service"` | Query the current recovery configuration. |
| `sc pause` | Show the syntax for a specific command (here, pause). |

# options

| option | description |
| --- | --- |
| `<servername>` | Remote server in UNC format (for example `\\myserver`); omit to run locally. |
| `<command>` | Configuration commands: boot, config, create, delete, description, EnumDepend, failure, failureflag, GetDisplayName, GetKeyName, Lock, qc, qdescription, qfailure, qfailureflag, qprivs, qsidtype, query, queryex, privs, QueryLock, sdset, sdshow, showsid, sidtype. Control commands: continue, control, interrogate, pause, start, stop. |
| `<servicename>` | Name of the service as specified when it was installed (returned by getkeyname). |
| `type= {own \| share \| kernel \| filesys \| rec \| adapt \| interact type= {own \| share}}` | Service type (create/config); `adapt` is config only, and `interact` must be combined with own or share. |
| `start= {boot \| system \| auto \| demand \| disabled \| delayed-auto}` | Start type; `demand` is the default for create. |
| `error= {normal \| severe \| critical \| ignore}` | Severity if the service fails to start at boot; `normal` is the default. |
| `binpath= <binarypathname>` | Path to the service binary; required for create. |
| `group= <loadordergroup>` | Load order group, listed under HKLM\System\CurrentControlSet\Control\ServiceGroupOrder. |
| `tag= {yes \| no}` | Whether to obtain a TagID from CreateService; boot-start and system-start drivers only. |
| `depend= <dependencies>` | Services or groups that must start first, separated by `/`. |
| `obj= {<accountname> \| <objectname>}` | Account the service runs as, or driver object name; default LocalSystem. |
| `displayname= <displayname>` | Friendly name shown in UI programs. |
| `password= <password>` | Password, required when an account other than LocalSystem is used. |
| `/?` | Displays help at the command prompt. |
