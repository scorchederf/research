---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wevtutil.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - eventlog
aliases:
  - wevtutil.exe
  - wevtutil
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/wevtutil
---

**fullpath**:C:\Windows\System32\wevtutil.exe

# description

`wevtutil` is a built-in Windows command that retrieves information about event logs and publishers. It can also install and uninstall event manifests, run queries, and export, archive and clear logs. It is part of Windows (Windows Commands) and complements Event Viewer and `wecutil`.

## simple description

> ### 2026-11-21 Claude said
> wevtutil is the command-line tool for Windows Event Logs. Admins use it to list logs, query events, export logs to .evtx files and change log settings. It can also clear logs completely. Because it ships with Windows, it is present on every system.
>
> **SOC NOTE**: `wevtutil cl <log>` is a classic anti-forensics command used to clear logs (MITRE ATT&CK T1070.001 Clear Windows Event Logs); clearing the Security log produces event 1102 and clearing other logs produces System event 104. Also watch for `wevtutil sl ... /e:false` disabling logs (T1562.002) and `qe`/`epl` used to collect logs for reconnaissance or exfiltration.
>

# purpose

Enumerate logs and publishers, display and modify log configuration, install/uninstall event manifests, read events with XPath or structured queries, display log status, export, archive and clear logs, locally or on a remote computer.

# typical use cases

| usage | description |
| --- | --- |
| `wevtutil el` | List the names of all logs. |
| `wevtutil gl System /f:xml` | Display configuration information about the System log in XML format. |
| `wevtutil sl /c:config.xml` | Use a configuration file to set event log attributes. |
| `wevtutil gp Microsoft-Windows-Eventlog /ge:true` | Display information about the Microsoft-Windows-Eventlog publisher, including event metadata. |
| `wevtutil im myManifest.xml` | Install publishers and logs from a manifest file. |
| `wevtutil um myManifest.xml` | Uninstall publishers and logs from a manifest file. |
| `wevtutil qe Application /c:3 /rd:true /f:text` | Display the three most recent events from the Application log in text format. |
| `wevtutil gli Application` | Display the status of the Application log. |
| `wevtutil epl System C:\backup\system0506.evtx` | Export events from the System log to a file. |
| `wevtutil cl Application /bu:C:\admin\backups\a10306.evtx` | Clear the Application log after saving events to a backup file. |
| `wevtutil archive-log "C:\backup\Application.evtx" /locale:en-us` | Archive an .evtx file in a self-contained format with locale metadata. |

# options

| option | description |
| --- | --- |
| `{el \| enum-logs}` | Displays the names of all logs. |
| `{gl \| get-log} <Logname> [/f:<Format>]` | Displays configuration information for the specified log (enabled state, maximum size, file path). |
| `{sl \| set-log} <Logname> [...]` | Modifies the configuration of the specified log. |
| `{ep \| enum-publishers}` | Displays the event publishers on the local computer. |
| `{gp \| get-publisher} <Publishername>` | Displays configuration information for the specified event publisher. |
| `{im \| install-manifest} <Manifest>` | Installs event publishers and logs from a manifest; `/rf`, `/mf`, `/pf` set resource, message and parameter file paths. |
| `{um \| uninstall-manifest} <Manifest>` | Uninstalls all publishers and logs from a manifest. |
| `{qe \| query-events} <Path>` | Reads events from a log, a log file, or using a structured query. |
| `{gli \| get-loginfo} <Logname> [/lf:<Logfile>]` | Displays status information about an event log or log file. |
| `{epl \| export-log} <Path> <Exportfile>` | Exports events from a log, log file or structured query to a file. |
| `{al \| archive-log} <Logpath> [/l:<Locale>]` | Archives the specified log file in a self-contained format with a locale subdirectory. |
| `{cl \| clear-log} <Logname> [/bu:<Backup>]` | Clears events from the specified log; `/bu` backs up the cleared events. |
| `/f:<Format>` | Output in XML or Text format (default Text). |
| `/e:<Enabled>` | Enables or disables a log (set-log). |
| `/i:<Isolation>` | Sets log isolation mode: system, application or custom. |
| `/lfn:<Logpath>` | Defines the log file name (full path). |
| `/rt:<Retention>` | Sets log retention mode; true keeps existing events and discards new ones when full. |
| `/ab:<Auto>` | Sets the auto-backup policy; requires `/rt:true`. |
| `/ms:<MaxSize>` | Sets maximum log size in bytes (minimum 1048576, multiples of 64KB). |
| `/l:<Level>` | Level filter of the log (logs with a dedicated session only). |
| `/k:<Keywords>` | Keywords filter of the log (logs with a dedicated session only). |
| `/ca:<Channel>` | Sets the log access permission as an SDDL security descriptor. |
| `/c:<Config>` | Reads log properties from a configuration file (set-log). |
| `/ge:<Metadata>` | Gets metadata for events the publisher can raise. |
| `/gm:<Message>` | Displays the actual message instead of the numeric message ID. |
| `/lf:<Logfile>` | Treat the path as a log file rather than a log name. |
| `/sq:<Structquery>` | Treat the path as a file containing a structured query. |
| `/q:<Query>` | XPath query to filter events read or exported (not with `/sq`). |
| `/bm:<Bookmark>` | Path to a bookmark file from a previous query. |
| `/sbm:<Savebm>` | Path to save a bookmark of this query (.xml). |
| `/rd:<Direction>` | If true, most recent events are returned first. |
| `/l:<Locale>` | Locale used to print event text (with `/f` text output). |
| `/c:<Count>` | Maximum number of events to read. |
| `/e:<Element>` | Root element to include when displaying events in XML. |
| `/ow:<Overwrite>` | Overwrite an existing export file without confirmation. |
| `/bu:<Backup>` | File (.evtx) where cleared events are stored. |
| `/r:<Remote>` | Run the command on a remote computer (not supported by `im`/`um`). |
| `/u:<Username>` | User for the remote computer (with `/r`). |
| `/p:<Password>` | Password for the user (with `/u`); `*` prompts. |
| `/a:<Auth>` | Authentication type: Default, Negotiate (default), Kerberos or NTLM. |
| `/uni:<Unicode>` | Displays output in Unicode. |
