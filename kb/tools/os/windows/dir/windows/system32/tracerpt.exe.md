---
created: 2026-11-21
fullpath: 'C:\Windows\System32\tracerpt.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - etw
  - windows-commands
aliases:
  - 'tracerpt.exe'
  - 'tracerpt'
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/tracerpt_1
---

**fullpath**: C:\Windows\System32\tracerpt.exe

# description

Built-in Windows command that parses Event Trace Logs (.etl), Performance Monitor log files and real-time Event Trace providers, and generates dump files, report files and report schemas. It complements logman/Performance Monitor for ETW analysis and can output CSV, EVTX or XML.

## simple description

> ### 2026-11-21 Claude said
> tracerpt converts Event Tracing for Windows (ETW) trace files into readable reports or dumps (XML, CSV, EVTX). It can also read live ETW sessions such as the NT Kernel Logger. Admins use it to analyse performance and diagnostic traces.
>
> **SOC NOTE**: Useful for responders to convert .etl artifacts (e.g., netsh trace, WMI/AutoLogger traces) to CSV/XML for analysis. Low abuse history, but reading the NT Kernel Logger or other sessions (-rt) can expose process/network activity; execution by non-admins or on servers without a diagnostic reason is unusual (T1082-style discovery).
>

# purpose

Parses ETW logs, performance logs and real-time ETW sessions to produce dump, report and summary files.

# typical use cases

| usage | description |
| --- | --- |
| `tracerpt logfile1.etl logfile2.etl -o logdump.xml -of XML` | Report on two logs and dump to logdump.xml in XML. |
| `tracerpt logfile.etl -o logdmp.xml -of XML -lr -summary logdmp.txt -report logrpt.xml` | Dump, summary and report with best-effort schema matching. |
| `tracerpt logfile1.etl logfile2.etl -o -report` | Dump and report with default file names. |
| `tracerpt logfile.etl counterfile.blg -report logrpt.xml -df schema.xml` | Combine ETL and performance log into a report and schema file. |
| `tracerpt -rt NT Kernel Logger -o logfile.csv -of CSV` | Read the real-time NT Kernel Logger session to CSV. |

# options

| option | description |
| --- | --- |
| `-config <filename>` | Specifies which settings file to load, which includes your command options. |
| `-y` | Answer yes to all questions without prompting. |
| `-f <XML \| HTML>` | Specifies the report file format. |
| `-of <CSV \| EVTX \| XML>` | Specifies the dump file format. Default is XML. |
| `-df <filename>` | Create a Microsoft-specific counting/reporting schema file. |
| `-int <filename>` | Dump the interpreted event structure to the specified file. |
| `-rts` | Add the report raw timestamp in the event trace header; only with -o, not with -report or -summary. |
| `-tmf <filename>` | Trace Message Format definition file to use. |
| `-tp <value>` | TMF file search path; multiple paths separated by semicolons. |
| `-i <value>` | Provider image path; matching PDB located on the Symbol Server. |
| `-pdb <value>` | Symbol server path; multiple paths separated by semicolons. |
| `-gmt` | Convert WPP payload timestamps to Greenwich Mean Time. |
| `-rl <value>` | System Report Level from 1 to 5. Default is 1. |
| `-summary [filename]` | Create a summary report text file (default summary.txt). |
| `-o [filename]` | Create a text output file (default dumpfile.xml). |
| `-report [filename]` | Create a text output report file (default workload.xml). |
| `-lr` | Be less restrictive; best efforts for events that don't match the events schema. |
| `-export [filename]` | Create an Event Schema export file (default schema.man). |
| `[-l] <value [value [...]]>` | Event Trace log file(s) to process. |
| `-rt <session_name [session_name [...]]>` | Real-time Event Trace Session data sources. |
| `-?` | Displays help. |
