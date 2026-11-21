---
created: 2026-11-21
fullpath: 'C:\Windows\System32\cscript.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - scripting
aliases:
  - cscript.exe
  - cscript
  - Windows Script Host
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/cscript
---

**fullpath**:C:\Windows\System32\cscript.exe

# description

`cscript` starts a script to run in a command-line environment using Windows Script Host. It is the console counterpart of wscript.exe and runs .wsf, .vbs and .js script files. Windows Server 2028 Preview removes VBScript, so cscript can't run VBScript there (JScript and Windows Script Host remain); Microsoft recommends migrating VBScript automation to PowerShell.

## simple description

> ### 2026-11-21 Claude said
> cscript.exe is the console version of Windows Script Host, the built-in engine that runs VBScript (.vbs) and JScript (.js) files and .wsf script packages. Output goes to the command window instead of pop-up dialogs, so it is used for admin scripts such as slmgr.vbs. It ships in System32 (and SysWOW64) on every Windows version. Microsoft is phasing out VBScript in newer releases.
>
> **SOC NOTE**: cscript is a classic LOLBin for T1059.005 (VBScript) and T1059.007 (JScript); malware droppers from phishing (zipped .js/.vbs) frequently spawn `cscript.exe //B //E:jscript` or `//nologo` from Explorer, Outlook or a temp/Downloads path. Watch Sysmon 1 / 4688 for cscript with scripts in user-writable folders, odd parents (winword.exe, mshta.exe), `/e:` engine overrides on non-script extensions, and child processes like powershell.exe or network connections.
>

# purpose

Runs Windows Script Host scripts from the command line. Script files usually use the .wsf, .vbs or .js extensions; a .wsf file can use multiple scripting engines and perform multiple jobs. Running cscript does not require administrative credentials.

# typical use cases

| usage | description |
| --- | --- |
| `cscript script.vbs` | Run a script in the command-line environment. |
| `cscript //nologo script.vbs` | Run a script without displaying the Windows Script Host banner. |
| `cscript /h:cscript` | Register cscript.exe as the default script host. |
| `cscript script.wsf /job:<identifier>` | Run a specific job in a .wsf script file. |
| `cscript script.vbs /t:60` | Run a script with a maximum run time of 60 seconds. |

# options

| option | description |
| --- | --- |
| `scriptname.extension` | Path and file name of the script file, with optional extension. |
| `/b` | Batch mode; does not display alerts, scripting errors or input prompts. |
| `/d` | Starts the debugger. |
| `/e:<engine>` | Specifies the engine used to run the script. |
| `/h:cscript` | Registers cscript.exe as the default script host. |
| `/h:wscript` | Registers wscript.exe as the default script host (the default). |
| `/i` | Interactive mode, displays alerts, errors and prompts (the default, opposite of `/b`). |
| `/job:<identifier>` | Runs the job identified by *identifier* in a .wsf script file. |
| `/logo` | Displays the Windows Script Host banner before the script runs (the default). |
| `/nologo` | Does not display the Windows Script Host banner. |
| `/s` | Saves the current command-prompt options for the current user. |
| `/t:<seconds>` | Maximum run time in seconds (up to 32,767); default is no limit. |
| `/u` | Uses Unicode for redirected console input and output. |
| `/x` | Starts the script in the debugger. |
| `/?` | Displays available command parameters. |
| `scriptarguments` | Arguments passed to the script; each must be preceded by a slash (/). |
