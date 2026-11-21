---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wsl.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - wsl
  - lolbin
aliases:
  - wsl.exe
  - wsl
  - Windows Subsystem for Linux
url:
  - https://learn.microsoft.com/windows/wsl/basic-commands
  - https://learn.microsoft.com/windows/wsl/install
  - https://learn.microsoft.com/windows/wsl/setup/environment
---

**fullpath**:C:\Windows\System32\wsl.exe

# description

`wsl.exe` is the command-line tool for the Windows Subsystem for Linux (WSL), used to install, manage and run Linux distributions on Windows. It replaces the deprecated `wslconfig.exe`, `bash` and `lxrun` commands. From inside a Linux distribution it must be called as `wsl.exe`.

## simple description

> ### 2026-11-21 Claude said
> wsl.exe lets you run Linux distributions (like Ubuntu) directly on Windows. Running it opens a Linux shell, and `wsl <command>` runs a single Linux command from PowerShell or CMD. It also manages installs, imports/exports, versions and disk mounts for WSL.
>
> **SOC NOTE**: WSL is a known defense-evasion and execution vector (MITRE ATT&CK T1202 Indirect Command Execution, T1059.004): Linux binaries and shells run outside many Windows EDR/AMSI hooks, and `wsl --import` can load attacker-supplied distributions. Watch for wsl.exe/wslhost.exe spawned by unusual parents, `wsl -e`/`--exec` with network tools, `--user root`, new distributions under user profiles, and `--mount` of disks. Linux-side history (e.g. `.bash_history` inside ext4.vhdx) is a forensic source.
>

# purpose

Installs WSL and Linux distributions, lists, starts, stops, imports, exports and unregisters distributions, sets WSL 1/2 versions and defaults, updates WSL, and mounts physical or virtual disks into WSL 2. Run with no arguments it opens the default distribution in the current command line; `wsl [command]` runs a Linux command without entering a shell.

# typical use cases

| usage | description |
| --- | --- |
| `wsl --install` | Install WSL and the default Ubuntu distribution. |
| `wsl --install -d <DistroName>` | Install a specific distribution. |
| `wsl --list --online` | List distributions available online (`wsl -l -o`). |
| `wsl -l -v` | List installed distributions with state and WSL version. |
| `wsl ls -la` | Run a Linux command from PowerShell/CMD. |
| `wsl --distribution <Distribution Name> --user <User Name>` | Run a specific distribution as a specific user. |
| `wsl --export <Distribution Name> <FileName>` | Export a distribution snapshot to a tar file. |
| `wsl --import <Distribution Name> <InstallLocation> <FileName>` | Import a tar file as a new distribution. |
| `wsl --shutdown` | Terminate all distributions and the WSL 2 VM. |
| `ipconfig.exe \| wsl grep IPv4 \| wsl cut -d: -f2` | Mix Windows and Linux tools in a pipeline. |

# options

| option | description |
| --- | --- |
| `--install` | Install WSL and the default Ubuntu distribution, or `--install <Distribution Name>` for another distribution. |
| `--install --distribution` | Specify the Linux distribution to install. |
| `--install --no-launch` | Install the distribution but do not launch it automatically. |
| `--install --web-download` | Install from an online source rather than the Microsoft Store. |
| `--install --location` | Folder to install the WSL distribution to. |
| `--install --inbox` | (WSL not installed) Install WSL using the Windows component instead of the Microsoft Store. |
| `--install --enable-wsl1` | (WSL not installed) Enable WSL 1 by also enabling the "Windows Subsystem for Linux" optional component. |
| `--install --no-distribution` | (WSL not installed) Do not install a distribution. |
| `--list --online` | List distributions available through the online store; also `-l -o`. |
| `--list --verbose` | List installed distributions with state and WSL version; also `-l -v`. Additional: `--all`, `--running`, `--quiet`. |
| `--set-version <distribution name> <versionNumber>` | Set a distribution to WSL 1 or 2. |
| `--set-default-version <Version>` | Default WSL version (1 or 2) for new installs. |
| `--set-default <Distribution Name>` | Set the default distribution. |
| `~` | Start in the user's home directory. |
| `--distribution <Distribution Name>` | Run a specific distribution. |
| `--user <Username>` | Run as a specified user that exists in the distribution. |
| `--update` | Update WSL to the latest version; `--web-download` downloads from GitHub instead of the Store. |
| `--status` | Show default distribution type, default distribution and kernel version. |
| `--version` | Show version information about WSL and its components. |
| `--help` | List options and commands. |
| `--shutdown` | Immediately terminate all running distributions and the WSL 2 utility VM. |
| `--terminate <Distribution Name>` | Stop the specified distribution. |
| `--export <Distribution Name> <FileName>` | Export a distribution snapshot (tar by default; `--vhd` for .vhdx, WSL 2 only). |
| `--import <Distribution Name> <InstallLocation> <FileName>` | Import a tar file as a new distribution; `--vhd` for .vhdx, `--version <1/2>` for the WSL version. |
| `--import-in-place <Distribution Name> <FileName>` | Import a .vhdx (ext4) as a new distribution. |
| `--unregister <DistributionName>` | Unregister a distribution; all its data is permanently lost. |
| `--mount <DiskPath>` | Attach and mount a physical disk in all WSL 2 distributions. Options: `--vhd`, `--name`, `--bare`, `--type <Filesystem>` (`-t`), `--partition <Partition Number>`, `--options <MountOptions>` (`-o`). |
| `--unmount <DiskPath>` | Unmount a disk; with no path, unmount and detach all mounted disks. |
