---
created: 2026-11-21
fullpath: 'C:\Windows\System32\LogFiles\WMI'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - etw
  - autologger
  - logs
aliases:
  - LogFiles\WMI
  - AutoLogger log folder
url:
  - https://learn.microsoft.com/windows/win32/etw/configuring-and-starting-an-autologger-session
---

**fullpath**:C:\Windows\System32\LogFiles\WMI

# description

Default output folder for Event Tracing for Windows (ETW) AutoLogger sessions. If an AutoLogger session in `HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\<session>` does not specify `FileName`, events are written to `%SystemRoot%\System32\LogFiles\WMI\<sessionname>.etl`.

## simple description

> ### 2026-11-21 Claude said
> Windows and drivers can start trace sessions very early at boot (AutoLoggers) and those traces land here as `.etl` files. It also contains the `RtBackup` folder for real-time sessions. Files are binary ETW traces that can be converted with tools such as `tracerpt`. Most content is diagnostic data from Windows components.
>
> **SOC NOTE**: Contains boot-time ETW traces that can reveal activity (network, Defender, diagnostics) useful in forensics. Attackers may disable or tamper with AutoLogger sessions (for example setting `Start`=0 for EventLog-related or Defender sessions) to blind telemetry (MITRE ATT&CK T1562.006 Indicator Blocking).
>

# purpose

Stores `.etl` output of AutoLogger sessions. With `FileMax` set, files rotate as `<sessionname>.etl.NNNN` (up to 16 instances).

# common files found

| file | description |
| --- | --- |
| `<sessionname>.etl` | Default AutoLogger session log file. |
| `<sessionname>.etl.NNNN` | Numbered instance when `FileMax` is used. |
