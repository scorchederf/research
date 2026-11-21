---
created: 2026-11-21
fullpath: 'C:\Windows\System32\tasklist.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - process
aliases:
  - tasklist.exe
  - tasklist
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist
---

**fullpath**:C:\Windows\System32\tasklist.exe

# description

tasklist displays a list of currently running processes on the local computer or on a remote computer. It is a built-in Windows command that replaces the older tlist tool; taskkill is the related command that ends processes by PID or image name.

## simple description

> ### 2026-11-21 Claude said
> tasklist.exe is a built-in Windows command-line tool that lists running processes, similar to Task Manager but in text. It shows the image name, process ID, session and memory use, and can show loaded DLLs and hosted services. It can query remote computers and filter or export the output as CSV.
>
> **SOC NOTE**: Frequently used for discovery (MITRE ATT&CK T1057 Process Discovery, T1518.001 Security Software Discovery), e.g. `tasklist /svc` or `/m` to find AV/EDR or lsass PID before credential dumping. Watch for it spawned by script hosts, Office or web servers; Security 4688 / Sysmon 1 record the command line.
>

# purpose

Lists running processes, with optional verbose, service and module information, output formatting and filters, locally or on a remote computer.

# typical use cases

| usage | description |
| --- | --- |
| `tasklist /v /fi "PID gt 1000" /fo csv` | List all tasks with a process ID greater than 1000 in CSV format. |
| `tasklist /fi "USERNAME ne NT AUTHORITY\SYSTEM" /fi "STATUS eq running"` | List running processes not owned by SYSTEM. |
| `tasklist /v /fi "STATUS eq running"` | Detailed information for all running processes. |
| `tasklist /s srvmain /svc /fi "MODULES eq ntdll*"` | Service information for processes on srvmain that have a DLL beginning with ntdll. |
| `tasklist /s srvmain` | List processes on remote computer srvmain with current credentials. |
| `tasklist /s srvmain /u maindom\hiropln /p p@ssW23` | List processes on srvmain using the Hiropln account. |

# options

| option | description |
| --- | --- |
| `/s <computer>` | Name or IP address of a remote computer (no backslashes). Default is the local computer. |
| `/u <domain>\<username>` | Runs with the specified user's permissions. Only valid with /s. |
| `/p <password>` | Password of the /u account. |
| `/m <module>` | Lists tasks with DLL modules matching the pattern; without a name, shows all modules loaded by each task. |
| `/svc` | Lists all service information for each process without truncation. Valid with /fo table. |
| `/v` | Verbose task information; use with /svc for complete output. |
| `/fo {table \| list \| csv}` | Output format; default is table. |
| `/nh` | Suppresses column headers. Valid with /fo table or csv. |
| `/fi <filter>` | Filters processes to include or exclude. Filters: STATUS, IMAGENAME, PID, SESSION, SESSIONNAME, CPUtime, MEMUSAGE, USERNAME, SERVICES, WINDOWTITLE, MODULES (STATUS and WINDOWTITLE not supported remotely). |
| `/?` | Displays help at the command prompt. |
