---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\wsb.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-sandbox
  - cli
aliases:
  - wsb.exe
  - wsb
  - Windows Sandbox command line interface
url:
  - https://learn.microsoft.com/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli
  - https://learn.microsoft.com/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-faq
  - https://learn.microsoft.com/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions
---

**fullpath**:C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\wsb.exe

# description

`wsb.exe` is the Windows Sandbox command line interface, available starting with Windows 11, version 24H2 with the Store-updated Windows Sandbox app. It creates, lists, connects to, executes commands in, shares folders with and stops sandboxes; the WindowsApps path is its app execution alias.

## simple description

> ### 2026-11-21 Claude said
> wsb.exe lets you control Windows Sandbox, a throwaway lightweight Windows virtual machine, from the command line. You can start a sandbox, run programs inside it, share host folders into it and stop it. Everything inside is deleted when the sandbox closes. It lives in WindowsApps because it ships with the Microsoft Store version of the Sandbox app.
>
> **SOC NOTE**: Sandbox activity leaves little evidence on the host because the guest is discarded (relevant to MITRE T1564.006 Run Virtual Instance). Watch for `wsb exec ... -r System`, `wsb share` with `--allow-write` to host folders, and networking-enabled configs that could be used to stage or exfiltrate data. wsb.exe on endpoints where Sandbox isn't expected is worth review.
>

# purpose

Scripting and automation of Windows Sandbox: creating sandboxes with custom configuration, running commands in the guest, sharing host folders, opening a remote session and stopping sessions. `wsb --version` also tells you whether the newer Sandbox version is installed.

# typical use cases

| usage | description |
| --- | --- |
| `wsb start` | Creates a Windows Sandbox environment with default settings and returns its ID. |
| `wsb start --config "<Configuration><Networking>Disabled</Networking></Configuration>"` | Creates a sandbox with a custom configuration. |
| `wsb list` | Lists running sandbox sessions for the current user with ID, status and uptime. |
| `wsb exec --id 12345678-1234-1234-1234-1234567890AB -c app.exe -r System` | Runs a command in the sandbox as System. |
| `wsb share --id 12345678-1234-1234-1234-1234567890AB -f C:\host\folder -s C:\sandbox\folder --allow-write` | Shares a host folder into the sandbox with write access. |
| `wsb connect --id 12345678-1234-1234-1234-1234567890AB` | Opens a remote desktop session to the sandbox. |
| `wsb ip --id 12345678-1234-1234-1234-1234567890AB` | Shows the sandbox IP address. |
| `wsb stop --id 12345678-1234-1234-1234-1234567890AB` | Stops the sandbox and releases its resources. |

# options

| option | description |
| --- | --- |
| `--raw` | Common parameter: formats all output as JSON. |
| `-?`, `-h`, `--help` | Common parameter: shows help and usage information. |
| `start` | Creates and launches a new sandbox; returns the sandbox ID. |
| `start --id <id>` | ID of the Windows Sandbox environment. |
| `start --c`, `--config <config>` | Formatted string with settings used to create the sandbox. |
| `list` | Displays running Windows Sandbox sessions for the current user. |
| `exec` | Executes a command in the sandbox and returns the exit code; no process I/O is returned. |
| `exec --id <id>` | (Required) ID of the sandbox. |
| `exec -c`, `--command <command>` | (Required) Command to execute in the sandbox. |
| `exec -r`, `--run-as <ExistingLogin\|System>` | (Required) User context: System, or the active user session (fails if none). |
| `exec -d`, `--working-directory <directory>` | Directory to run the command in. |
| `stop --id <id>` | Stops a running sandbox and closes its window. |
| `share` | Shares a host folder with the sandbox. |
| `share --id <id>` | (Required) ID of the sandbox. |
| `share -f`, `--host-path <host-path>` | (Required) Host folder to share. |
| `share -s`, `--sandbox-path <sandbox-path>` | (Required) Folder path inside the sandbox (existing or new). |
| `share -w`, `--allow-write` | Allows the sandbox to write to the shared folder. |
| `connect --id <id>` | Starts a remote desktop session in the sandbox. |
| `ip --id <id>` | Displays the IP address of the sandbox. |
| `--version` | Shows the version; if `wsb` is unavailable, the older Sandbox is installed. |
