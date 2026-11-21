---
created: 2026-11-21
fullpath: 'C:\Windows\System32\bash.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - wsl
  - lolbin
aliases:
  - "bash.exe"
  - "Bash on Windows"
url:
  - https://learn.microsoft.com/windows/wsl/troubleshooting
  - https://learn.microsoft.com/windows/wsl/release-notes
  - https://learn.microsoft.com/windows/wsl/faq
---

**fullpath**:C:\Windows\System32\bash.exe

# description

`bash.exe` is the original Windows Subsystem for Linux launcher in `System32`, used on early Windows 10 builds (Anniversary/Creators Update) to run Linux commands. It has been replaced by `wsl.exe`.

## simple description

> ### 2026-11-21 Claude said
> bash.exe starts a Linux shell inside the Windows Subsystem for Linux (WSL) from a Windows command prompt.
> On modern Windows it is a legacy launcher kept for compatibility; wsl.exe is the current tool.
> It only works if WSL and a Linux distribution are installed.
>
> **SOC NOTE**: LOLBin (T1202 Indirect Command Execution): `bash.exe -c "<cmd>"` runs commands inside WSL, where Windows EDR has less visibility, and Linux tools can reach /mnt/c. Unexpected bash.exe on servers or non-developer hosts is suspicious.
>

# purpose

Runs Linux commands from Windows on early WSL versions. Commands passed into `bash -c` are forwarded to the WSL process without modification; file paths must be in WSL format. Console lifetime is tied to bash.exe lifetime.

# typical use cases

| usage | description |
| --- | --- |
| `bash -c "ls -la"` | Runs a Linux command in WSL from Windows (early Windows versions). |
| `bash -c "ls -la /proc/cpuinfo"` | Runs a command using a WSL-format path. |
| `bash -c "ls -la \"/mnt/c/Program Files\""` | Lists a Windows folder via /mnt/c, escaping quotes. |
| `bash.exe -c "su -"` | Runs a command as root on early versions (use `wsl -u root` on supported versions). |

# options

| option | description |
| --- | --- |
| `-c` | Passes the command string to the WSL process without modification. |
