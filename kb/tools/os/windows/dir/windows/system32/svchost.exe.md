---
created: 2026-11-21
fullpath: 'C:\Windows\System32\svchost.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - svchost.exe
  - Service Host
  - SvcHost
url:
  - https://learn.microsoft.com/windows/application-management/svchost-service-refactoring
  - https://learn.microsoft.com/windows-hardware/drivers/debugger/preparing-to-debug-the-service-application
---

**fullpath**:C:\Windows\System32\svchost.exe

# description

The Service Host (svchost.exe) is a shared-service process that serves as a shell for loading services from DLL files. Services are organized into host groups by matching security requirements (Local Service, Local Service No Network, Local Service Network Restricted, Local System, Local System Network Restricted, Network Service), and each group runs in its own svchost instance; group membership is defined under `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SvcHost`.

## simple description

> ### 2026-11-21 Claude said
> svchost.exe is the generic container Windows uses to run services implemented as DLLs. You'll see dozens of instances, each started by services.exe with `-k <group>` on the command line. Since Windows 10 1703, on machines with more than 3.5 GB RAM, most services get their own svchost process.
>
> **SOC NOTE**: A favorite masquerading name (MITRE ATT&CK T1036.005): legitimate svchost.exe only runs from System32/SysWOW64, is always a child of services.exe (or of svchost for some), and always has `-k`. Malicious services can also register a ServiceDll under an existing group (T1543.003). Check parent, path, command line, user and network connections; Sysmon 1/3 and Event 7045 help.
>

# purpose

Hosts Windows services implemented as DLLs. Starting with Windows 10 version 1703, on Client Desktop SKUs with more than 3.5 GB of RAM, previously grouped services run each in their own SvcHost process for reliability, security, scalability and per-service resource management; services with `SvcHostSplitDisable`=1 under their service key stay grouped. Instance counts typically range from about 17-21 grouped to 67-74 split.

# typical use cases

| usage | description |
| --- | --- |
| `%SystemRoot%\System32\svchost.exe -k LocalServiceNoNetwork` | Example service BINARY_PATH_NAME launching a service in the LocalServiceNoNetwork group. |
| `sc qc ServiceName` | Show which svchost group a service uses before isolating it for debugging. |
| `Get-Process SvcHost \| Group-Object -Property ProcessName` | Count SvcHost instances (Learn sample used to compare grouped vs split memory). |

# options

| option    | description    |
| --- | --- |
| `-k <group>` | Name of the service host group to load, defined as a value/subkey under `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SvcHost`. |
