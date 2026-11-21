---
created: 2026-11-21
fullpath: 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - powershell.exe
  - Windows PowerShell
  - PowerShell 5.1
url:
  - https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_powershell_exe?view=powershell-5.1
  - https://learn.microsoft.com/windows-server/administration/windows-commands/powershell
  - https://learn.microsoft.com/powershell/scripting/whats-new/differences-from-windows-powershell?view=powershell-7.6
---

**fullpath**:C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

# description

powershell.exe is the command-line interface for Windows PowerShell 5.1, a task-based shell and scripting language built on the .NET Framework for Windows administration. It starts a PowerShell session and accepts parameters to customise it. PowerShell 7 uses a different executable, `pwsh.exe`, documented in about_Pwsh.

## simple description

> ### 2026-11-21 Claude said
> This is Windows PowerShell 5.1, the command shell and scripting language built into Windows. Admins use it to automate almost anything: managing users, services, the registry, remote machines and Microsoft cloud services. You can use it interactively, or start it to run a single command or script and exit. PowerShell 7 is a separate, newer program (`pwsh.exe`) that installs alongside it.
>
> **SOC NOTE**: PowerShell is one of the most abused tools in Windows attacks (MITRE ATT&CK T1059.001), used for downloading payloads, running code in memory and lateral movement. Red flags in command lines include `-EncodedCommand`/`-enc` (Base64 commands, T1027), `-WindowStyle Hidden`, `-NoProfile`, `-ExecutionPolicy Bypass`, `IEX`/`Invoke-Expression` and `DownloadString`/`Invoke-WebRequest`. Check Script Block Logging (event 4104 in `Microsoft-Windows-PowerShell/Operational`), the PSReadLine `ConsoleHost_history.txt` file, and watch for attempts to downgrade with `-Version 2` to evade logging.
>

# purpose

- Start an interactive Windows PowerShell session from a Command Prompt.
- Run a single command (`-Command`) or a script file (`-File`) non-interactively.
- Pass complex commands safely with `-EncodedCommand`.
- Control session settings such as execution policy, profile loading and apartment state.

# typical use cases

| usage | description |
| --- | --- |
| `PowerShell -Command "Get-EventLog -LogName Security"` | Run a command. |
| `PowerShell -Command {Get-EventLog -LogName Security}` | Run a script block. |
| `PowerShell.exe -NoProfile` | Start without profiles. |
| `PowerShell.exe -ExecutionPolicy Restricted` | Session-only execution policy. |
| — | Encoded command: build a UTF-16LE Base64 string and run `powershell.exe -EncodedCommand $encodedCommand`. |

# options

| option    | description    |
| --- | --- |
| `-PSConsoleFile <FilePath>` | Loads the specified PowerShell console file (create one with Export-Console). |
| `-Version <PowerShell Version>` | Starts the specified version of PowerShell. Valid values are 2.0 and 3.0; the version must be installed. |
| `-NoLogo` | Hides the copyright banner at startup. |
| `-NoExit` | Doesn't exit after running startup commands. |
| `-Sta` | Starts PowerShell using a single-threaded apartment (default from 3.0). |
| `-Mta` | Starts PowerShell using a multi-threaded apartment (introduced in 3.0). |
| `-NoProfile` | Doesn't load the PowerShell profile. |
| `-NonInteractive` | Creates a session that shouldn't need user input; interactive features (e.g. Read-Host) cause terminating errors instead of hanging. |
| `-InputFormat {Text | XML}` | Format of data sent to PowerShell: Text strings or serialized CLIXML. |
| `-OutputFormat {Text | XML}` | How output is formatted: Text strings or serialized CLIXML. |
| `-WindowStyle <style>` | Window style for the session: Normal, Minimized, Maximized or Hidden. |
| `-EncodedArguments <Base64EncodedArguments>` | Base64-encoded (UTF-16LE) command arguments, for complex nested quoting. |
| `-EncodedCommand <Base64EncodedCommand>` | Base64-encoded (UTF-16LE) version of a command, for commands with complex quotes or braces. |
| `-ConfigurationName <string>` | Configuration endpoint to run PowerShell in, including remoting or custom endpoints. |
| `-File - | <filePath> <args>` | Runs a script (dot-sourced) with optional parameters, or reads commands from standard input with `-`. Must be the last parameter. |
| `-ExecutionPolicy <ExecutionPolicy>` | Sets the execution policy for the current session (stored in $Env:PSExecutionPolicyPreference); doesn't change the registry setting. |
| `-Command - | <script-block> | <string>` | Runs commands from a script block, a string, or standard input (`-`). From cmd.exe the value is always a string. |
| `-Help, -?, /?` | Displays help for powershell.exe. |
