---
created: 2026-11-21
fullpath: 'C:\Windows\System32\services.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - scm
  - services
aliases:
  - services.exe
  - Service Control Manager
  - SCM
url:
  - https://learn.microsoft.com/windows/win32/services/service-control-manager
  - https://learn.microsoft.com/windows/win32/services/service-startup
  - https://learn.microsoft.com/windows/win32/services/about-services
---

**fullpath**:C:\Windows\System32\services.exe

# description

Process hosting the Service Control Manager (SCM), started at system boot. The SCM is an RPC server that maintains the database of installed services and driver services, starts them at boot or on demand, tracks their status and sends control requests; service control programs such as `sc` talk to it.

## simple description

> ### 2026-11-21 Claude said
> services.exe is a core Windows process that starts and manages all Windows services. It is launched by wininit.exe at boot and runs as SYSTEM, and it is the parent of every svchost.exe and other service process. There should be exactly one instance, running from System32. It has no user-facing command line.
>
> **SOC NOTE**: Attackers create or modify services for persistence and privilege escalation (MITRE ATT&CK T1543.003) and for remote execution like PsExec (T1569.002); these appear as service processes whose parent is services.exe and System event 7045/Security 4697. A services.exe outside System32, more than one instance, or a parent other than wininit.exe indicates masquerading (T1036).
>

# purpose

Maintains the services database, starts auto-start and demand-start services and driver services, enumerates services, maintains their status, transmits control requests and locks/unlocks the service database. If a service does not update its status within 80 seconds plus its wait hint, the SCM logs an event and stops it.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:47 UTC_
