---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft PIX\pixtool.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - pixtool.exe
  - PIX command-line tool
url:
  - https://learn.microsoft.com/windows/pix/gpu-captures/pixtool
  - https://learn.microsoft.com/windows/pix/gpu-captures/export-to-cpp
---

**fullpath**:C:\Program Files\Microsoft PIX\pixtool.exe

# description

pixtool.exe is the command-line tool of PIX on Windows, Microsoft's performance and debugging tool for DirectX 12 games and apps. It installs alongside `WinPix.exe` in the versioned folder `%ProgramFiles%\Microsoft PIX\<version>\` and automates GPU and timing captures without the PIX UI.

## simple description

> ### 2026-11-21 Claude said
> Pixtool is a developer tool for graphics programmers: it launches or attaches to a DirectX 12 game or app and records GPU or timing captures for performance analysis. It can then export event lists and counters to CSV, save screenshots, or export a frame as C++ code. It is normally found only on game or graphics developer machines. Commands can be chained on one command line.
>
> **SOC NOTE**: pixtool can launch arbitrary executables (`launch <exe> --command-line=...`) and attach to running processes, so it could act as a proxy-execution or process-injection helper on developer machines (MITRE ATT&CK T1218-style signed binary proxy execution). Its presence on non-developer endpoints is unusual. Timing captures can record ETW data including file I/O and callstacks.
>

# purpose

Automate common PIX capture workflows: launch or attach to an app, take GPU or timing captures, open `.wpix` captures, export capture data, recapture parts of a GPU capture, upgrade GPU captures, and run playback checks. Global options are parsed first, then commands run left to right in one session, sharing state.

# typical use cases

| usage | description |
| --- | --- |
| `pixtool launch C:\Apps\D3D12HelloTriangle.exe take-capture --open save-capture C:\Captures\triangle.wpix` | Launch an app, take one GPU capture and save it. |
| `pixtool launch C:\Apps\Game.exe --timing take-new-timing-capture C:\Captures\game-timing.wpix --duration=5000` | Take a 5-second timing capture. |
| `pixtool attach 12345 take-new-timing-capture C:\Captures\game-until-exit.wpix --until-exit` | Attach to a running process and capture until it exits. |
| `pixtool open-capture C:\Captures\frame.wpix save-event-list C:\Exports\eventlist.csv --counters=*` | Export the event list with all counters to CSV. |
| `pixtool open-capture C:\Captures\frame.wpix export-to-cpp C:\Exports\FrameProject --force` | Export a captured frame as a C++ project. |

# options

| option | description |
| --- | --- |
| `--help` | Shows general help. |
| `--help <command>` | Shows help for a specific command. |
| `--output=<level>` | Console verbosity: `quiet`, `trace` (default), `engine`, `verbose`. |
| `--log=<level>` | Log-file verbosity: `quiet`, `trace`, `engine`, `verbose` (default), `off`. |
| `--log-file=<filename>` | Log-file path; default `pixtool.log` in the temp folder. |
| `launch <exe> [...]` | Launches an executable for GPU capture (`--command-line`, `--working-directory`, `--setenv`, `--remote`, `--timing`, `--force11on12`, `--captureFromStart`). |
| `launch-app <package> <application> [...]` | Launches a UWP app for GPU capture. |
| `set-gpu-capture-parameters [...]` | Sets parameters for subsequent captures (`--frames`, `--capture-key`, `--winml`, `--remote`). |
| `take-capture [--open] [...]` | Takes a GPU capture of the launched app (`--winml`, `--frames`). |
| `programmatic-capture [--open] [--until-exit]` | Waits for a programmatic capture triggered by the launched app. |
| `save-capture <filename>` | Saves the currently open capture. |
| `save-all-captures <directory>` | Saves all captures taken in this session to a directory. |
| `open-capture <filename> [...]` | Opens a `.wpix` GPU capture (`--remote` and replay options). |
| `list-counters` | Lists all available counters. |
| `recapture-region <outputFilePath> [...]` | Recaptures a global-ID range (`--start`, `--end`) of the open capture. |
| `take-new-timing-capture <filename> [...]` | Takes and saves a timing capture (`--duration`, `--until-exit`, `--circular`, `--etl`, sampling and event options). |
| `attach <targetProcessId>` | Attaches to a running process (`--remote`). |
| `export-to-cpp <directory> [...]` | Exports a captured frame as a C++ project (`--force`, `--use-winpixeventruntime`, `--use-agilitySdk`). |
| `upgrade-gpu-capture <sourceCapturePath> [--dest=<destCapturePath>]` | Upgrades a GPU capture file to the latest format. |
| `save-event-list <filename> [...]` | Saves the event list as CSV (`--counters`, `--counter-groups`, `--queue-name`). |
| `run-debug-layer` | Forces a playback with the debug layer enabled. |
| `save-high-frequency-counters <filename> [...]` | Collects and saves high-frequency counter data as CSV (`--counters`, `--merge`). |
| `save-screenshot <filename>` | Saves the capture's screenshot as PNG. |
| `save-resource <filename> [...]` | Saves a resource from a draw call (`--rtv`, `--depth`, `--global-id`, `--marker`). |
| `begin-recapture` | Begins a capture of pixtool itself. |
| `end-recapture` | Ends a recapture. |
| `recapture-single-playback [...]` | Captures a playback of the open file (`--include-recreation`, `--expand-execute`). |
| `perform-single-playback [...]` | Performs one playback of the open file (`--loop`, `--loop-count`, `--time-cpu`, `--measure-cycles`). |
