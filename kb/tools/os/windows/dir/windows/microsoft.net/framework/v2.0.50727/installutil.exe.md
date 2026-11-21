---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v2.0.50727\InstallUtil.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - installer
aliases:
  - InstallUtil.exe
  - Installutil.exe
  - Installer tool
url:
  - https://learn.microsoft.com/dotnet/framework/tools/installutil-exe-installer-tool
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v2.0.50727\InstallUtil.exe

# description

Installutil.exe (Installer tool) is a .NET Framework command-line utility that installs and uninstalls server resources by executing the installer components in specified assemblies, working with the System.Configuration.Install namespace. It ships with the .NET Framework (this copy is the 32-bit v2.0.50727 runtime) and is installed with Visual Studio, available from the Developer Command Prompt.

## simple description

> ### 2026-11-21 Claude said
> InstallUtil.exe is a .NET Framework helper that runs the "installer" classes inside a .NET assembly, typically to register a Windows service, event log source or performance counters. Developers and admins run it with an assembly path to install, or with /u to uninstall. This copy belongs to the old .NET 2.0/3.5 runtime in the 32-bit Framework folder. It is signed by Microsoft and present on most Windows systems.
>
> **SOC NOTE**: A well-known LOLBin (MITRE ATT&CK T1218.004 System Binary Proxy Execution: InstallUtil). Attackers use `InstallUtil.exe /logfile= /LogToConsole=false /U payload.dll` to run code in an Uninstall() method, bypassing application allowlisting. Watch for it launched by Office, scripts or from user-writable paths, assemblies outside Program Files, network connections from InstallUtil, and .InstallLog/.InstallState files next to unusual assemblies.
>

# purpose

Detects and executes installer components in .NET assemblies to create resources such as message queues, event logs and performance counters when an application is deployed, and to remove them on uninstall. It uses reflection to find Installer types with RunInstallerAttribute set to true and calls their Install or Uninstall method; installation is transactional (one failure rolls back all), uninstall is not. Without options it writes InstallUtil.InstallLog, assemblyname.InstallLog and assemblyname.InstallState into the assembly's directory. It cannot install delay-signed assemblies or C++ Windows services.

# typical use cases

| usage | description |
| --- | --- |
| `installutil /?` | Displays command syntax and options. |
| `installutil /? myAssembly.exe` | Also displays options supported by the installer components in the assembly. |
| `installutil myAssembly.exe` | Executes the installer components in the assembly. |
| `installutil /AssemblyName "myAssembly, Culture=neutral, PublicKeyToken=0038abc9deabfle5, Version=4.0.0.0"` | Executes installers in an assembly specified by strong name. |
| `installutil /u myAssembly.exe` | Executes the uninstaller components in the assembly. |
| `installutil /u myAssembly1.exe myAssembly2.exe` | Uninstalls two assemblies (position of /u does not matter). |
| `installutil /LogFile=myLog.InstallLog myAssembly.exe` | Writes progress information to myLog.InstallLog. |
| `installutil /LogFile= /email=admin@mycompany.com myAssembly.exe` | Passes a custom installer option and suppresses the log file. |

# options

| option | description |
| --- | --- |
| `assembly` | File name of the assembly whose installer components are executed; omit when using /AssemblyName. |
| `/h[elp]` or `/?` | Displays command syntax and options for the tool. |
| `/help assembly` or `/? assembly` | Also displays additional options recognized by individual installers in the assembly (from Installer.HelpText). |
| `/AssemblyName "assemblyName,Version=...,Culture=...,PublicKeyToken=..."` | Specifies the fully qualified strong name of an assembly registered in the global assembly cache. |
| `/InstallStateDir=[directoryName]` | Directory of the .InstallState file used to uninstall the assembly; default is the assembly's directory. |
| `/LogFile=[filename]` | Log file for installation progress; default assemblyname.InstallLog; if filename is omitted no log is generated. |
| `/LogToConsole={true\|false}` | If true, displays output to the console; false (default) suppresses it. |
| `/ShowCallStack` | Outputs the call stack to the log file if an exception occurs during installation. |
| `/u[ninstall]` | Uninstalls the specified assemblies; applies to all assemblies regardless of position. |
