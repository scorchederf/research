---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft SQL Server\90\Shared\SQLDumper.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - sql-server
aliases:
  - SQLDumper.exe
  - Sqldumper.exe
url:
  - https://learn.microsoft.com/troubleshoot/sql/tools/use-sqldumper-generate-dump-file
---

**fullpath**:C:\Program Files\Microsoft SQL Server\90\Shared\SQLDumper.exe

# description

Sqldumper.exe is a SQL Server utility that generates memory dump files of the SQL Server process (or any Windows application) for troubleshooting exceptions, asserts and non-yielding schedulers. It is installed in `Program Files\Microsoft SQL Server\<number>\Shared`, where 90 corresponds to SQL Server 2005, and requires Dbghelp.dll in the same folder. SQL Server and the SQL Server cluster resource DLL invoke it automatically; DBCC STACKDUMP is a related method.

## simple description

> ### 2026-11-21 Claude said
> SQLDumper.exe is a Microsoft-signed helper shipped with SQL Server that writes a memory dump of a process for crash analysis. SQL Server calls it automatically when it hits a serious error, and admins can run it manually with a process ID. The 90 folder is the SQL Server 2005 copy. Dumps are written as SQLDmpr<xxxx>.mdmp files.
>
> **SOC NOTE**: It is a known LOLBin: `sqldumper.exe <lsass PID> 0 0x0110` (or 0x01100) dumps LSASS memory for credential theft (MITRE ATT&CK T1003.001). Alert when the target PID is lsass or when it runs outside SQL Server context; look for unexpected .mdmp files and Sysmon 10 (process access to lsass).
>

# purpose

Generates full, mini, or filtered dump files of a process. By default it writes to the current/install folder (SQL-triggered dumps go to the instance MSSQL\LOG directory). It must be run by an administrator or the SQL Server service account; dumping freezes the target process and may trigger cluster failover.

# typical use cases

| usage | description |
| --- | --- |
| `Sqldumper.exe <ProcessID> 0 0x01100` | Generate a full dump file. |
| `Sqldumper.exe <ProcessID> 0 0x0120` | Generate a mini-dump file. |
| `Sqldumper.exe <ProcessID> 0 0x0128` | Mini-dump including indirectly referenced memory (recommended; SQL Server default). |
| `Sqldumper.exe <ProcessID> 0 0x8100` | Generate a filtered dump file. |
| `Sqldumper.exe ProcessID 0 0x0128 0 <MdumpPath>` | Write the dump to a custom existing folder (no UNC paths). |
| `Sqldumper.exe <ProcessID> 0 0x8100 0 d:\temp -zdmp` | Capture a compressed memory dump. |

# options

| option | description |
| --- | --- |
| `<ProcessID>` | Process identifier of the application to dump. |
| `0x01100` | Dump flag: full dump. |
| `0x0120` | Dump flag: mini-dump. |
| `0x0128` | Dump flag: mini-dump with indirectly referenced memory. |
| `0x8100` | Dump flag: filtered dump. |
| `<MdumpPath>` | Output directory; must already exist. Default is the current folder. |
| `-zdmp` | Captures a compressed memory dump (multithreaded parallel compression). |
