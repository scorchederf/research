---
created: 2026-11-21
fullpath: 'C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_<version_packageid>\wt.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-terminal
aliases:
  - wt.exe
  - wt
  - Windows Terminal
url:
  - https://learn.microsoft.com/windows/terminal/command-line-arguments
---

**fullpath**:C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_<version_packageid>\wt.exe

# description

`wt.exe` is the command-line launcher for Windows Terminal; it can also be invoked through the `wt` app execution alias. Windows Terminal ships as an MSIX/Store package under `C:\Program Files\WindowsApps`, and the alias is exposed via `%LOCALAPPDATA%\Microsoft\WindowsApps`.

## simple description

> ### 2026-11-21 Claude said
> wt.exe starts Windows Terminal, Microsoft's modern tabbed terminal host for Command Prompt, PowerShell, WSL and other shells. It lives inside the protected WindowsApps folder as part of the Store/MSIX package, and users usually launch it through the `wt` alias. It accepts arguments to open tabs, split panes, choose profiles and run a command line. On Windows 11 it is often the default terminal application.
>
> **SOC NOTE**: wt.exe can be used as a proxy to launch other commands (`wt cmd /c ...`, `wt powershell ...`), so the real payload appears as a child of WindowsTerminal.exe/OpenConsole.exe rather than explorer.exe - relevant for parent-child detection logic (MITRE T1202 Indirect Command Execution, T1059). Profiles in the Terminal settings.json can also be modified to run commands at startup (persistence). Check process creation events (4688/Sysmon 1) for the full command line.
>

# purpose

Opens a new Windows Terminal instance or sends commands (new tab, split pane, focus) to an existing window. Syntax is `wt [options] [command ; ]`; with no command, `new-tab` is used. The `windowingBehavior` setting affects whether a new window or tab opens.

# typical use cases

| usage | description |
| --- | --- |
| `wt ping learn.microsoft.com` | Starts Windows Terminal and runs a command in the default shell. |
| `wt -p "Ubuntu-18.04"` | Opens a new terminal instance with the named profile. |
| `wt -w 0 nt` | Opens a new tab with the default profile in the current window. |
| `wt -d d:\` | Opens a terminal with `d:\` as the starting directory. |
| `wt -p "Command Prompt" ; split-pane -p "Windows PowerShell" ; split-pane -H wsl.exe` | Opens one tab with three panes. |
| `wt ; new-tab -p "Ubuntu-18.04" ; focus-tab -t 1` | Opens two tabs and focuses the second. |
| `wt --title tabname --suppressApplicationTitle` | Opens a tab whose title the application can't override. |

# options

| option | description |
| --- | --- |
| `--help, -h, -?, /?` | Displays the help message. |
| `--maximized, -M` | Launches the terminal maximized. |
| `--fullscreen, -F` | Launches the terminal as full screen. |
| `--focus, -f` | Launches the terminal in focus mode; can be combined with maximized. |
| `--pos x,y` | Launches the terminal at the given position; x or y can be omitted to use the settings default. |
| `--size c,r` | Launches the terminal with the specified number of columns and rows. |
| `--window, -w window-id` | Runs the given command in a specific window (integer ID or name; `new`/`-1` = new window, `last`/`0` = most recent window). |
| `new-tab, nt --profile, -p profile-name` | Creates a new tab based on the assigned profile name. |
| `new-tab, nt --startingDirectory, -d starting-directory` | Creates a new tab with the assigned starting directory. |
| `new-tab, nt --title title` | Creates a new tab with the assigned title. |
| `new-tab, nt --tabColor hex-color` | Creates a new tab with the assigned tab color (#RGB or #RRGGBB). |
| `new-tab, nt --suppressApplicationTitle` | Overrides the profile's suppressApplicationTitle setting to true. |
| `new-tab, nt --useApplicationTitle` | Overrides the profile's suppressApplicationTitle setting to false. |
| `new-tab, nt --colorScheme scheme-name` | Overrides the profile's colorScheme with the named scheme. |
| `new-tab, nt --appendCommandLine` | Appends the provided command line to the profile's default command instead of replacing it. |
| `new-tab, nt --inheritEnvironment, !--reloadEnvironment` | Inherits the terminal's own environment variables instead of creating a fresh environment block; default when a commandline is passed. |
| `new-tab, nt commandline` | Creates a new tab running the given executable with optional arguments. |
| `split-pane, sp -H, --horizontal / -V, --vertical` | Creates a new pane split horizontally or vertically. |
| `split-pane, sp --profile, -p profile-name` | Creates a new pane with the assigned profile (default profile if omitted). |
| `split-pane, sp --startingDirectory, -d starting-directory` | Creates a new pane with the assigned starting directory. |
| `split-pane, sp --title` | Creates a new pane with the assigned title. |
| `split-pane, sp --tabColor` | Creates a new pane with the assigned tab color. |
| `split-pane, sp --size, -s size` | Creates a new pane using the given fraction of the parent pane (e.g. `.4`). |
| `split-pane, sp commandline` | Creates a new pane running the given command line. |
| `split-pane, sp --duplicate, -D` | Creates a new pane that duplicates the current pane. |
| `split-pane, sp --suppressApplicationTitle` | Overrides the profile's suppressApplicationTitle setting to true. |
| `split-pane, sp --useApplicationTitle` | Overrides the profile's suppressApplicationTitle setting to false. |
| `split-pane, sp --colorScheme scheme-name` | Overrides the profile's colorScheme with the named scheme. |
| `focus-tab, ft --target, -t tab-index` | Focuses a specific tab by index. |
| `move-focus, mf <direction>` | Moves focus between panes (up, down, left, right, first, previous, nextInOrder, previousInOrder). |
| `move-pane, mp --tab, -t <index>` | Moves the active pane to the given zero-indexed tab. |
| `swap-pane <direction>` | Swaps the active pane with the pane in the given direction. |

