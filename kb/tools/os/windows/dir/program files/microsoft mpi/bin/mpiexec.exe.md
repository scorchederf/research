---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft MPI\Bin\mpiexec.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - hpc
  - mpi
aliases:
  - 'mpiexec.exe'
  - 'mpiexec'
  - 'MS-MPI'
url:
  - https://learn.microsoft.com/powershell/high-performance-computing/mpiexec?view=hpc19-ps
  - https://learn.microsoft.com/message-passing-interface/microsoft-mpi-release-notes
  - https://learn.microsoft.com/powershell/high-performance-computing/understanding-parallel-computing-jobs?view=hpc19-ps
---

**fullpath**: C:\Program Files\Microsoft MPI\Bin\mpiexec.exe

# description

Launcher for Microsoft MPI (MS-MPI), Microsoft's Message Passing Interface implementation for Windows used standalone or with Microsoft HPC Pack. It starts one or more MPI applications across cores and cluster nodes, working with the smpd.exe service on each node and the optional MS-MPI Launch Service. Related tools: clusrun, mpicsync, etl2clog, etl2otf.

## simple description

> ### 2026-11-21 Claude said
> mpiexec starts parallel programs that use MPI, running many copies (ranks) of an application on the local machine or across multiple cluster nodes. You tell it how many processes, which hosts, and which program to run. It is installed by the Microsoft MPI redistributable, often pulled in by scientific or engineering software.
>
> **SOC NOTE**: Can execute arbitrary programs locally or on remote hosts (`/hosts`, `/machinefile`) and accepts clear-text passwords via `/pwd`, which may appear in command-line logs (T1552 credentials in command lines). Signed Microsoft binary that can serve as proxy execution / lateral execution (T1218, T1021). Investigate mpiexec on hosts that aren't HPC nodes or with unusual child processes.
>

# purpose

Starts one or more MPI applications on the local computer or an HPC cluster, controlling process placement, affinity, environment and tracing.

# typical use cases

| usage | description |
| --- | --- |
| `mpiexec application1` | Run application1 on all local cores. |
| `mpiexec /np 1 master : subordinate` | Run one master process and subordinates on the remaining cores. |
| `mpiexec /gmachinefile myhosts.txt /np 1 master : subordinate` | Run across hosts listed in a file. |
| `mpiexec /trace (pt2pt,coll,interconn) /tracemax 20480 /np 2 application1` | Trace MPI calls with a 20 GB trace limit. |
| `mpiexec /machinefile myhosts.txt /env MPICH_CONNECTIVITY_TABLE 1 application1` | Print a connectivity table. |
| `mpiexec -hosts 2 host1 1 host2 2 -wdir C:\MpiTests -pwd <password> -savecreds mpiapp.exe` | Launch via the Launch Service and store credentials on the hosts. |

# options

| option | description |
| --- | --- |
| `/genv <env_var_name> <env_var_value>` | Sets an environment variable for applications in all sections; /env overrides it per section. |
| `/gpath <path1>[;<path2>...]` | Search paths on the target node for applications in all sections. |
| `/gwdir <working_dir>` | Working directory for all sections (alias /gdir). |
| `/ghost <host_name>` | Starts applications in all sections on the specified node. |
| `/gmachinefile <file_name>` | Reads the list of nodes (and optional core counts) for all sections from a file. |
| `/configfile <file_name>` | Reads the remaining command-line sections from a file. |
| `/np {<num>\|*}` | Number of processes for the section; * uses all available cores (alias /n). |
| `/machinefile <file_name>` | Reads the list of nodes for this section from a file. |
| `/host <host_name>` | Starts this section's application on the specified node. |
| `/hosts <num> <host1> [num1] ...` | Number of nodes and list of node names with optional process counts. |
| `/cores <num>` | Number of cores to use on each node (alias /c). |
| `/affinity` | Sets each process's affinity mask to a single core; use only with exclusive nodes. |
| `/affinity_layout <algorithm>[:<target>]` | Distribution algorithm (0 Disabled, 1 Spread, 2 Sequential, 3 Balanced) and target (L logical core, P physical core, N NUMA node). |
| `/wdir <working_dir>` | Working directory for this section (alias /dir). |
| `/env <env_var_name> <env_var_value>` | Sets an environment variable for this section. |
| `/genvlist <env_var1>[,<env_var2>...]` | Passes values of the listed environment variables to started processes. |
| `/exitcodes` | Prints exit codes of started processes at the end of the run. |
| `/priority {0\|1\|2\|3\|4}` | Process priority: 0 Idle, 1 Below normal, 2 Normal (default), 3 Above normal, 4 High. |
| `/port <port>` | Port on which smpd.exe listens (alias /p). |
| `/path <path1>[;<path2>...]` | Search paths for this section's application. |
| `/timeout <seconds>` | Time before the job times out. |
| `/job <string>` | Associates the MPI job with an HPC Job Scheduler job. |
| `/lines` | Prefixes each output line with the rank of the process (alias /l). |
| `/trace [(<filter1>,<filter2>...)]` | Traces MS-MPI events, optionally filtered (alias /t); deprecated as of HPC Pack 2008 R2 SP3. |
| `/tracefile <file_name>` | Trace log file name (alias /tf); deprecated. |
| `/tracemax <max_size>` | Maximum trace file size in MB, default 10240 (alias /tm); deprecated. |
| `/debug [{0\|1\|2\|3}]` | Prints debugging information to standard error (alias /d). |
| `/logfile <log_file_name>` | Log file name including path. |
| `<sectionN_parameters>` | Per-section parameters: /env, /path, /wdir, /host, /hosts, /machinefile, /np. |
| `<applicationN> [<applicationN_parameters>]` | MPI application(s) to start; multiple sections are colon-separated. |
| `/pwd <string>` | Authenticates the user with the provided password; only with MS-MPI Launch Service. |
| `/saveCreds` | Tells the Launch Service to save credentials; only valid with /pwd. |
| `/unicode` | Switches mpiexec output to a Unicode stream. |
| `/?` | Help for common parameters (alias /help). |
| `/??` | Help for all parameters and examples (alias /help2). |
| `/???` | Help for environment variables (alias /help3). |
