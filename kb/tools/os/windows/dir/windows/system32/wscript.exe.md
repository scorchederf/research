---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wscript.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - scripting
aliases:
  - wscript.exe
  - wscript
  - Windows Script Host
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/wscript
  - https://learn.microsoft.com/windows/win32/com/using-com-objects-in-windows-script-host
---

**fullpath**:C:\Windows\System32\wscript.exe

# description

`wscript.exe` is the Windows-based host of Windows Script Host (WSH), which runs scripts from the Windows desktop; its console counterpart is `cscript.exe`. WSH ships with Windows and includes the VBScript and JScript scripting engines. Windows Server 2025 includes VBScript as a preinstalled Feature on Demand, and Windows Server 2028 Preview removes VBScript (WSH and JScript remain).

## simple description

> ### 2026-11-21 Claude said
> wscript.exe is the built-in Windows program that runs script files such as .vbs, .js and .wsf when you double-click them. It is the "windowed" version of Windows Script Host, so any output shows up in pop-up message boxes instead of a console. Administrators use it for logon scripts and small automation tasks. Because it is signed by Microsoft and present on every Windows system, it is a common way to launch script code.
>
> **SOC NOTE**: wscript.exe is heavily abused for initial access and execution (MITRE ATT&CK T1059.005 Visual Basic, T1059.007 JavaScript), typically launched by Outlook, a browser, explorer.exe opening a .js/.vbs from a ZIP, or a scheduled task/Run key for persistence. Red flags: parent is an Office app or email client, scripts in %TEMP%/Downloads/AppData, use of `/e:` with odd extensions, `/b` batch mode, and child processes like powershell.exe, cmd.exe, mshta.exe or rundll32.exe. Check Sysmon Event ID 1 / Security 4688 command lines, Prefetch (WSCRIPT.EXE-*.pf), and AMSI script content in Defender telemetry.
>

# purpose

Windows Script Host provides an environment in which users can execute scripts in various languages that use various object models to perform tasks. WScript.exe runs scripts from the Windows desktop (for example when a script file is double-clicked), while CScript.exe runs scripts from the command prompt. If no script or arguments are given, wscript.exe displays the **Windows Script Host Settings** dialog box to set global scripting properties. Script files usually use the .wsf, .vbs or .js extensions; a .wsf file can use multiple scripting engines and perform multiple jobs.

# typical use cases

| usage | description |
| --- | --- |
| `wscript script.vbs` | Run a script with the Windows-based script host. |
| `wscript /b script.vbs` | Run in batch mode without alerts, scripting errors or input prompts. |
| `wscript /e:vbscript test.admin` | Run a script with a nonstandard extension by specifying the engine. |
| `wscript /t:60 script.vbs` | Stop the script if it runs longer than 60 seconds. |
| `wscript /h:cscript` | Register cscript.exe as the default script host. |
| `wscript` | With no arguments, open the Windows Script Host Settings dialog box. |

# options

| option | description |
| --- | --- |
| `scriptname` | Specifies the path and file name of the script file. |
| `/b` | Batch mode; doesn't display alerts, scripting errors, or input prompts. Opposite of `/i`. |
| `/d` | Starts the debugger. |
| `/e` | Specifies the engine used to run the script, allowing scripts with custom file name extensions. |
| `/h:cscript` | Registers cscript.exe as the default script host for running scripts. |
| `/h:wscript` | Registers wscript.exe as the default script host. This is the default when `/h` is omitted. |
| `/i` | Interactive mode, which displays alerts, scripting errors, and input prompts. The default. |
| `/job:<identifier>` | Runs the job identified by *identifier* in a .wsf script file. |
| `/logo` | Displays the Windows Script Host banner before the script runs. The default. |
| `/nologo` | Doesn't display the Windows Script Host banner. |
| `/s` | Saves the current command prompt options for the current user. |
| `/t:<number>` | Maximum time in seconds the script can run (up to 32,767). Default is no time limit. |
| `/x` | Starts the script in the debugger. |
| `ScriptArguments` | Arguments passed to the script; each must be preceded with a slash (/). |
| `/?` | Displays Help at the command prompt. |
