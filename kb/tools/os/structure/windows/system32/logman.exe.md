---
created: 2026-11-21
fullpath: 'C:\Windows\System32\logman.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-commands
  - etw
aliases:
  - logman.exe
  - logman
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/logman
  - https://learn.microsoft.com/windows-server/administration/windows-commands/logman-create-trace
  - https://learn.microsoft.com/windows-server/administration/windows-commands/logman-delete
  - https://learn.microsoft.com/windows-server/administration/windows-commands/logman-update-trace
---

**fullpath**:C:\Windows\System32\logman.exe

# description

logman creates and manages Event Trace Session and Performance logs and supports many functions of Performance Monitor from the command line. It ships with Windows; subcommands create, query, start/stop, delete, update, import and export data collectors (counter, trace, alert, configuration, API).

## simple description

> ### 2026-11-21 Claude said
> logman.exe is a built-in Windows tool for controlling performance counter logs and ETW (Event Tracing for Windows) trace sessions. Admins use it to start a trace (e.g. network or kernel tracing), collect performance data over time, or list which trace sessions are running. It is the command-line counterpart of Performance Monitor's Data Collector Sets. Output usually lands in .etl or .blg files.
>
> **SOC NOTE**: Attackers use `logman stop <session> -ets` / `logman delete` / `logman update trace ... --p <provider>` to kill or blind ETW sessions such as EventLog-*, Microsoft-Windows-Threat-Intelligence or EDR autologgers (MITRE ATT&CK T1562.002 / T1562.006 Impair Defenses: Indicator Blocking). `logman query -ets` is also used to enumerate security tooling (T1518.001). Alert on logman stop/delete/update with -ets, especially against Defender, Sysmon or EventLog sessions.
>

# purpose

Creates and manages Event Trace Session and Performance logs from the command line. Syntax: `logman [create | query | start | stop | delete | update | import | export | /?] [options]`.

# typical use cases

- Create an event trace collector: `logman create trace trace_log -nb 16 256 -bs 64 -o c:\logfile`.
- Update a collector: `logman update trace trace_log -max 10 -f csv -v mmddhhmm`.
- Delete a collector: `logman delete perf_log`.
- Import a Data Collector Set: `logman import perf_log -s server_1 -xml c:\windows\perf_log.xml`.

# options

| option    | description    |
| --- | --- |
| `create` | Creates a counter, trace, configuration data collector, or API. |
| `query` | Queries data collector properties. |
| `start \| stop` | Starts or stops data collection. |
| `delete` | Deletes an existing data collector. |
| `update` | Updates the properties of an existing data collector. |
| `import \| export` | Imports a data collector set from an XML file or exports one to an XML file. |
| `/?` | Displays context-sensitive help. |

Common subcommand options (logman create trace):

| option    | description    |
| --- | --- |
| `-s <computer name>` | Performs the command on the specified remote computer. |
| `-config <value>` | Specifies the settings file containing command options. |
| `-ets` | Sends commands to Event Trace Sessions directly without saving or scheduling. |
| `[-n] <name>` | Name of the target object. |
| `-f <bin \| bincirc>` | Specifies the log format for the data collector. |
| `-[-]u <user [password]>` | Specifies the user to Run As; `*` prompts for the password. |
| `-m <[start] [stop] ...>` | Changes to manual start or stop instead of a scheduled begin or end time. |
| `-rf <[[hh:]mm:]ss>` | Runs the data collector for the specified period of time. |
| `-b <M/d/yyyy h:mm:ss[AM \| PM]>` | Begins collecting data at the specified time. |
| `-e <M/d/yyyy h:mm:ss[AM \| PM]>` | Ends data collection at the specified time. |
| `-o <path \| dsn!log>` | Specifies the output log file or the DSN and log set name in a SQL database. |
| `-[-]r` | Repeats the data collector daily at the specified begin and end times. |
| `-[-]a` | Appends an existing log file. |
| `-[-]ow` | Overwrites an existing log file. |
| `-[-]v <nnnnnn \| mmddhhmm>` | Attaches file versioning information to the end of the log file name. |
| `-[-]rc <task>` | Runs the command specified each time the log is closed. |
| `-[-]max <value>` | Maximum log file size in MB or maximum number of records for SQL logs. |
| `-[-]cnf <[[hh:]mm:]ss>` | Creates a new file when the time elapses or the maximum size is exceeded. |
| `-y` | Answers yes to all questions without prompting. |
| `-ct <perf \| system \| cycle>` | Specifies the Event Trace Session clock type. |
| `-ln <logger_name>` | Specifies the logger name for Event Trace Sessions. |
| `-ft <[[hh:]mm:]ss>` | Specifies the Event Trace Session flush timer. |
| `-[-]p <provider [flags [level]]>` | Specifies a single Event Trace provider to enable. |
| `-pf <filename>` | Specifies a file listing multiple Event Trace providers, one per line. |
| `-[-]rt` | Runs the Event Trace Session in real-time mode. |
| `-[-]ul` | Runs the Event Trace Session in user mode. |
| `-bs <value>` | Specifies the Event Trace Session buffer size in kb. |
| `-nb <min max>` | Specifies the number of Event Trace Session buffers. |
| `-mode <globalsequence \| localsequence \| pagedmemory>` | Specifies the event trace session logger mode. |
| `/?` | Displays context-sensitive help. |
